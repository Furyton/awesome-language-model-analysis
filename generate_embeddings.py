"""Precompute paper embeddings for the webpage's optional semantic search.

Uses fastembed (ONNX, no torch, CPU-only, ~intra-minute for our corpus size)
with the same base model family (all-MiniLM-L6-v2) that the browser side
loads via transformers.js, so query and document vectors live in the same
space and a simple cosine similarity works.

Best-effort: if fastembed isn't installed or the model can't be downloaded
(e.g. no network), this step is skipped and the site just falls back to
lexical-only search -- it never blocks the rest of the pipeline.
"""
import os
import json
import logging
import argparse

from constant import DOCS_DIR, SITE_DATA_FILE

MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
EMBEDDINGS_FILE = os.path.join(DOCS_DIR, "data", "embeddings.json")


def build_text(paper: dict, abstracts: dict) -> str:
    abstract = abstracts.get(paper["url"], "")
    return f"{paper['title']}. {abstract}".strip()


def main(dry_run: bool = False):
    if not os.path.exists(SITE_DATA_FILE):
        logging.warning(f"{SITE_DATA_FILE} not found -- run generate_site_data.py first.")
        return

    with open(SITE_DATA_FILE, "r", encoding="utf-8") as f:
        papers = json.load(f)

    abstracts_path = os.path.join("papers", "_abstracts.json")
    abstracts = {}
    if os.path.exists(abstracts_path):
        with open(abstracts_path, "r", encoding="utf-8") as f:
            abstracts = json.load(f)

    try:
        from fastembed import TextEmbedding
    except ImportError:
        logging.warning("fastembed not installed -- skipping semantic embeddings.")
        return

    try:
        model = TextEmbedding(model_name=MODEL_NAME)
        texts = [build_text(p, abstracts) for p in papers]
        vectors = list(model.embed(texts))
    except Exception as e:
        logging.warning(f"Embedding generation failed ({e}) -- skipping semantic embeddings.")
        return

    payload = {
        "model": MODEL_NAME,
        "urls": [p["url"] for p in papers],
        # round to keep file size sane; cosine similarity doesn't need full precision
        "vectors": [[round(float(x), 5) for x in vec] for vec in vectors],
    }

    logging.info(f"Computed {len(vectors)} embedding(s), dim={len(vectors[0]) if vectors else 0}")

    if not dry_run:
        os.makedirs(os.path.dirname(EMBEDDINGS_FILE), exist_ok=True)
        with open(EMBEDDINGS_FILE, "w", encoding="utf-8") as f:
            json.dump(payload, f, separators=(",", ":"))
        logging.info(f"Wrote {EMBEDDINGS_FILE}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    main(dry_run=args.dry_run)
