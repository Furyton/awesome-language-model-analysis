"""Fetch candidate papers directly from the arXiv API (no account needed).

Used both for:
- daily supplementary fetch (catches anything Scholar Inbox / arxivist missed)
- one-off backfill over a date range (e.g. to fill the Nov 2024 -> now gap)

Respects arXiv's rate-limit guidance (one request per ~3s, <=100 results per
page). Results are filtered by category + keyword (abstract) match; the LLM
classifier still makes the final call on relevance, so keyword matching here
is intentionally broad rather than precise.
"""
import re
import time
import logging
import argparse
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta

from constant import ARXIV_CATEGORIES, ARXIV_KEYWORDS
from pending_queue import append_to_pending

ARXIV_API = "http://export.arxiv.org/api/query"
NS = {"atom": "http://www.w3.org/2005/Atom"}
PAGE_SIZE = 100
RATE_LIMIT_SECONDS = 3


def _build_query(date_filter: str = None) -> str:
    cat_query = " OR ".join(f"cat:{c}" for c in ARXIV_CATEGORIES)
    kw_query = " OR ".join(f'abs:"{kw}"' for kw in ARXIV_KEYWORDS)
    query = f"({cat_query}) AND ({kw_query})"
    if date_filter:
        query += f" AND {date_filter}"
    return query


def _request(query: str, start: int, max_results: int) -> ET.Element:
    params = {
        "search_query": query,
        "start": start,
        "max_results": max_results,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    }
    url = f"{ARXIV_API}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"User-Agent": "awesome-lm-analysis-bot/1.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return ET.fromstring(resp.read())


def _parse_entry(entry) -> dict:
    title = entry.find("atom:title", NS).text.strip().replace("\n", " ")
    title = " ".join(title.split())
    abstract = entry.find("atom:summary", NS).text.strip().replace("\n", " ")
    abstract = " ".join(abstract.split())
    published = entry.find("atom:published", NS).text[:10]  # YYYY-MM-DD
    url = entry.find("atom:id", NS).text.strip()
    authors = [
        a.find("atom:name", NS).text
        for a in entry.findall("atom:author", NS)
        if a.find("atom:name", NS) is not None
    ]

    return {
        "title": title,
        "abstract": abstract,
        "date": published,
        "url": url,
        "authors": ";".join(authors),
    }


def search(date_filter: str = None, max_total: int = 2000) -> list:
    query = _build_query(date_filter)
    logging.info(f"arXiv query: {query}")

    papers = []
    start = 0
    while start < max_total:
        root = _request(query, start, PAGE_SIZE)
        entries = root.findall("atom:entry", NS)
        if not entries:
            break

        for entry in entries:
            try:
                papers.append(_parse_entry(entry))
            except Exception as e:
                logging.debug(f"Skipping malformed entry: {e}")

        logging.info(f"Fetched {len(entries)} entries (offset {start})")

        if len(entries) < PAGE_SIZE:
            break

        start += PAGE_SIZE
        time.sleep(RATE_LIMIT_SECONDS)

    return papers


def fetch_recent(days: int = 3) -> list:
    since = (datetime.utcnow() - timedelta(days=days)).strftime("%Y%m%d0000")
    now = datetime.utcnow().strftime("%Y%m%d2359")
    date_filter = f"submittedDate:[{since} TO {now}]"
    return search(date_filter)


def fetch_range(start_date: str, end_date: str) -> list:
    """start_date / end_date in YYYY-MM-DD."""
    start = start_date.replace("-", "") + "0000"
    end = end_date.replace("-", "") + "2359"
    date_filter = f"submittedDate:[{start} TO {end}]"
    return search(date_filter, max_total=5000)


def _normalize_title(title: str) -> str:
    title = title.lower()
    title = re.sub(r"[^a-z0-9 ]", " ", title)
    return " ".join(title.split())


def resolve_by_title(title: str) -> dict:
    """Look up a paper on arXiv by its exact title (used for sources like
    Scholar Inbox / arxivist that link through their own site rather than
    directly to arxiv.org). Returns None if no confident match is found --
    the paper is likely on a non-arXiv venue (bioRxiv, ACL, etc.) which this
    automation doesn't handle.
    """
    escaped = title.replace('"', "")
    query = f'ti:"{escaped}"'

    try:
        root = _request(query, start=0, max_results=5)
    except Exception as e:
        logging.warning(f"arXiv title lookup failed for '{title}': {e}")
        return None

    target = _normalize_title(title)
    for entry in root.findall("atom:entry", NS):
        try:
            parsed = _parse_entry(entry)
        except Exception:
            continue
        if _normalize_title(parsed["title"]) == target:
            return parsed

    logging.info(f"No confident arXiv match for: {title}")
    return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["daily", "backfill"], default="daily")
    parser.add_argument("--days", type=int, default=3, help="daily mode: lookback window")
    parser.add_argument("--start", help="backfill mode: YYYY-MM-DD")
    parser.add_argument("--end", help="backfill mode: YYYY-MM-DD")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--debug", action="store_true")
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.debug else logging.INFO, format="%(message)s"
    )

    if args.mode == "daily":
        results = fetch_recent(days=args.days)
    else:
        if not args.start or not args.end:
            raise SystemExit("--start and --end are required for backfill mode")
        results = fetch_range(args.start, args.end)

    logging.info(f"arXiv returned {len(results)} candidate paper(s)")

    if not args.dry_run:
        append_to_pending(results, source="arxiv_search")
    else:
        for p in results[:10]:
            print(f"- {p['date']} {p['title']}")
