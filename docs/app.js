(() => {
  "use strict";

  const state = {
    papers: [],
    categories: [],
    activeCategoryCodes: new Set(),
    query: "",
    sort: "date-desc",
    semanticOn: false,
    semanticReady: false,
    semanticVectors: null, // { model, urls, vectors }
    lastSemanticScores: null, // Map(url -> score)
  };

  let fuse = null;

  const els = {
    searchBox: document.getElementById("search-box"),
    semanticToggle: document.getElementById("semantic-toggle"),
    semanticStatus: document.getElementById("semantic-status"),
    sortSelect: document.getElementById("sort-select"),
    categoryFilters: document.getElementById("category-filters"),
    clearFilters: document.getElementById("clear-filters"),
    resultCount: document.getElementById("result-count"),
    paperList: document.getElementById("paper-list"),
    emptyState: document.getElementById("empty-state"),
    paperCount: document.getElementById("paper-count"),
  };

  async function init() {
    const [papers, categories] = await Promise.all([
      fetch("data/papers.json").then((r) => r.json()),
      fetch("data/categories.json").then((r) => r.json()),
    ]);

    state.papers = papers;
    state.categories = categories;

    els.paperCount.textContent = `${papers.length} papers.`;

    fuse = new Fuse(papers, {
      keys: [
        { name: "title", weight: 0.7 },
        { name: "authors", weight: 0.3 },
      ],
      threshold: 0.32,
      ignoreLocation: true,
    });

    renderCategoryChips();
    bindEvents();
    render();
  }

  function renderCategoryChips() {
    els.categoryFilters.innerHTML = "";
    for (const cat of state.categories) {
      const chip = document.createElement("button");
      chip.type = "button";
      chip.className = "chip";
      chip.textContent = cat.name;
      chip.dataset.code = cat.code;
      chip.addEventListener("click", () => {
        if (state.activeCategoryCodes.has(cat.code)) {
          state.activeCategoryCodes.delete(cat.code);
        } else {
          state.activeCategoryCodes.add(cat.code);
        }
        chip.classList.toggle("active");
        els.clearFilters.hidden = state.activeCategoryCodes.size === 0;
        render();
      });
      els.categoryFilters.appendChild(chip);
    }
  }

  function bindEvents() {
    let debounceTimer;
    els.searchBox.addEventListener("input", () => {
      clearTimeout(debounceTimer);
      debounceTimer = setTimeout(() => {
        state.query = els.searchBox.value.trim();
        if (state.semanticOn && state.query) {
          runSemanticSearch(state.query);
        } else {
          render();
        }
      }, 150);
    });

    els.sortSelect.addEventListener("change", () => {
      state.sort = els.sortSelect.value;
      render();
    });

    els.clearFilters.addEventListener("click", () => {
      state.activeCategoryCodes.clear();
      els.categoryFilters
        .querySelectorAll(".chip.active")
        .forEach((c) => c.classList.remove("active"));
      els.clearFilters.hidden = true;
      render();
    });

    els.semanticToggle.addEventListener("change", async (e) => {
      state.semanticOn = e.target.checked;
      if (state.semanticOn) {
        await enableSemanticSearch();
        if (state.query) runSemanticSearch(state.query);
      } else {
        state.lastSemanticScores = null;
        render();
      }
    });
  }

  // --- Semantic search (lazy-loaded, only when the user opts in) ---

  let embedderPromise = null;

  async function enableSemanticSearch() {
    els.semanticStatus.textContent = "loading model...";
    try {
      const [{ pipeline }, vectorData] = await Promise.all([
        import("https://cdn.jsdelivr.net/npm/@xenova/transformers@2.17.2"),
        state.semanticVectors
          ? Promise.resolve(state.semanticVectors)
          : fetch("data/embeddings.json").then((r) => {
              if (!r.ok) throw new Error("no precomputed embeddings available");
              return r.json();
            }),
      ]);

      state.semanticVectors = vectorData;

      if (!embedderPromise) {
        embedderPromise = pipeline("feature-extraction", "Xenova/all-MiniLM-L6-v2");
      }
      await embedderPromise;

      state.semanticReady = true;
      els.semanticStatus.textContent = "ready";
      setTimeout(() => (els.semanticStatus.textContent = ""), 1500);
    } catch (err) {
      console.warn("Semantic search unavailable:", err);
      els.semanticStatus.textContent = "unavailable (using lexical search)";
      state.semanticOn = false;
      els.semanticToggle.checked = false;
    }
  }

  function cosineSim(a, b) {
    let dot = 0;
    for (let i = 0; i < a.length; i++) dot += a[i] * b[i];
    return dot; // vectors are pre-normalized, so dot product == cosine similarity
  }

  async function runSemanticSearch(query) {
    if (!state.semanticReady || !state.semanticVectors) {
      render();
      return;
    }
    els.semanticStatus.textContent = "searching...";
    const embedder = await embedderPromise;
    const output = await embedder(query, { pooling: "mean", normalize: true });
    const queryVec = Array.from(output.data);

    const { urls, vectors } = state.semanticVectors;
    const scores = new Map();
    for (let i = 0; i < urls.length; i++) {
      scores.set(urls[i], cosineSim(queryVec, vectors[i]));
    }
    state.lastSemanticScores = scores;
    els.semanticStatus.textContent = "";
    state.sort = "relevance";
    els.sortSelect.value = "relevance";
    render();
  }

  // --- Rendering ---

  function getFilteredPapers() {
    let results = state.papers;

    if (state.query) {
      if (state.semanticOn && state.lastSemanticScores) {
        results = state.papers
          .map((p) => ({ paper: p, score: state.lastSemanticScores.get(p.url) ?? -1 }))
          .filter((r) => r.score > 0.2)
          .sort((a, b) => b.score - a.score)
          .map((r) => r.paper);
      } else {
        results = fuse.search(state.query).map((r) => r.item);
      }
    }

    if (state.activeCategoryCodes.size > 0) {
      results = results.filter((p) =>
        p.categories.some((c) => state.activeCategoryCodes.has(c.code))
      );
    }

    return results;
  }

  function sortPapers(papers) {
    const arr = [...papers];
    if (state.sort === "date-desc") {
      arr.sort((a, b) => (a.date < b.date ? 1 : -1));
    } else if (state.sort === "date-asc") {
      arr.sort((a, b) => (a.date > b.date ? 1 : -1));
    }
    // "relevance" keeps the order search already produced
    return arr;
  }

  function render() {
    const filtered = getFilteredPapers();
    const isRelevanceSort = state.sort === "relevance" && state.query;
    const papers = isRelevanceSort ? filtered : sortPapers(filtered);

    els.resultCount.textContent = state.query
      ? `${papers.length} result(s) for "${state.query}"`
      : `Showing all ${papers.length} papers`;

    els.emptyState.hidden = papers.length !== 0;
    els.paperList.innerHTML = "";

    const frag = document.createDocumentFragment();
    for (const paper of papers.slice(0, 300)) {
      frag.appendChild(renderPaperItem(paper));
    }
    els.paperList.appendChild(frag);
  }

  function renderPaperItem(paper) {
    const li = document.createElement("li");
    li.className = "paper-item";

    const title = document.createElement("div");
    title.className = "paper-title";
    const a = document.createElement("a");
    a.href = paper.url;
    a.target = "_blank";
    a.rel = "noopener noreferrer";
    a.textContent = paper.title;
    title.appendChild(a);

    const meta = document.createElement("div");
    meta.className = "paper-meta";
    meta.textContent = `${paper.date} · ${paper.authors.join("; ")}`;

    const cats = document.createElement("div");
    cats.className = "paper-categories";
    for (const c of paper.categories) {
      const tag = document.createElement("span");
      tag.className = "tag";
      tag.textContent = c.name;
      cats.appendChild(tag);
    }

    li.appendChild(title);
    li.appendChild(meta);
    li.appendChild(cats);
    return li;
  }

  init().catch((err) => {
    console.error(err);
    els.resultCount.textContent = "Failed to load paper data.";
  });
})();
