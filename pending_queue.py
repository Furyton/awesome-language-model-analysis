"""Shared helpers for the paper staging/pending queue.

New papers found by any fetcher (Scholar Inbox email, arxivist email, arXiv
search) are appended to papers/_pending/queue.csv instead of being classified
immediately. A separate step (classify_pending.py) drains that queue. This
way a failed/expensive LLM call never loses a paper -- it just stays pending
until the next run.
"""
import os
import re
import csv
import glob
import logging

from constant import ROOT, PENDING_DIR, PENDING_FILE, PENDING_FIELDS

_ARXIV_ID_RE = re.compile(r"(\d{4}\.\d{4,5})(v\d+)?")


def normalize_arxiv_id(url: str) -> str:
    """Extract a stable arXiv id from a URL for dedup, e.g.
    'http://arxiv.org/abs/2411.07602v2' -> '2411.07602'.
    Falls back to the stripped URL for non-arXiv links.
    """
    if not url:
        return ""
    match = _ARXIV_ID_RE.search(url)
    if match:
        return match.group(1)
    return url.strip().rstrip("/").lower()


def load_known_ids() -> set:
    """Scan every papers/**/papers.csv plus the pending queue and return the
    set of arXiv ids (or normalized urls) already tracked, so fetchers never
    add duplicates.
    """
    known = set()
    for path in glob.glob(os.path.join(ROOT, "**", "papers.csv"), recursive=True):
        with open(path, "r", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                url = row.get("Url", "")
                if url:
                    known.add(normalize_arxiv_id(url))

    if os.path.exists(PENDING_FILE):
        with open(PENDING_FILE, "r", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                url = row.get("Url", "")
                if url:
                    known.add(normalize_arxiv_id(url))

    return known


def load_pending() -> list:
    if not os.path.exists(PENDING_FILE):
        return []
    with open(PENDING_FILE, "r", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def append_to_pending(papers: list, source: str) -> int:
    """Append new (deduped) papers to the pending queue. Returns how many
    were actually added.
    """
    if not papers:
        return 0

    os.makedirs(PENDING_DIR, exist_ok=True)
    known = load_known_ids()

    new_rows = []
    seen_this_batch = set()
    for paper in papers:
        url = paper.get("url") or paper.get("Url", "")
        norm_id = normalize_arxiv_id(url)
        if not norm_id or norm_id in known or norm_id in seen_this_batch:
            continue
        seen_this_batch.add(norm_id)
        new_rows.append(
            {
                "Title": paper.get("title") or paper.get("Title", ""),
                "Date": paper.get("date") or paper.get("Date", ""),
                "Url": url,
                "Author": paper.get("authors") or paper.get("Author", ""),
                "Abstract": (paper.get("abstract") or paper.get("Abstract", "") or "").replace(
                    "\n", " "
                ),
                "Source": source,
            }
        )

    if not new_rows:
        logging.info(f"[{source}] no new papers (all duplicates)")
        return 0

    file_exists = os.path.exists(PENDING_FILE)
    with open(PENDING_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=PENDING_FIELDS)
        if not file_exists:
            writer.writeheader()
        writer.writerows(new_rows)

    logging.info(f"[{source}] added {len(new_rows)} new paper(s) to pending queue")
    return len(new_rows)


def rewrite_pending(remaining_rows: list):
    """Overwrite the pending queue with only the rows that are still
    unclassified (called by classify_pending.py after processing).
    """
    os.makedirs(PENDING_DIR, exist_ok=True)
    with open(PENDING_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=PENDING_FIELDS)
        writer.writeheader()
        writer.writerows(remaining_rows)
