"""Fetch Scholar Inbox's daily digest directly via its own JSON API,
authenticated with your personal magic-link `sha_key` (the same token
embedded in the link at the top of every digest email you get).

The real login endpoint is `GET https://api.scholar-inbox.com/api/login/{sha_key}/`
-- a same-origin call on the API host itself, confirmed by reading the
open-source `scholarinboxcli` package's implementation
(github.com/mrshu/scholarinboxcli). The www.scholar-inbox.com/login?sha_key=...
page is just the frontend SPA route; it calls this same endpoint via
client-side JS, which is why it wasn't visible in browser network inspection
and why hitting that page URL directly (an earlier version of this script)
didn't actually authenticate a fresh, cookie-less client -- it happened to
"work" in a browser only because that browser already had an unrelated,
pre-existing logged-in session.

Unlike the old approach (a manually-copied session cookie that expired every
~7 days), this mints a fresh cookie from the permanent sha_key at the start
of every run, so there's nothing to refresh by hand.

SCHOLAR_INBOX_SHA_KEY is a bearer credential for your account (it can see
your reading history/ratings) -- treat it like a password: GitHub secret
only, never commit it, never print it in logs.
"""
import logging
import argparse
from datetime import datetime, timedelta

import requests

from constant import SCHOLAR_INBOX_SHA_KEY
from pending_queue import append_to_pending

API_BASE = "https://api.scholar-inbox.com"
LOGIN_URL_TEMPLATE = API_BASE + "/api/login/{sha_key}/"
DIGEST_URL = API_BASE + "/api/"


def _login_session() -> requests.Session:
    session = requests.Session()
    session.headers.update(
        {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"
            )
        }
    )
    resp = session.get(LOGIN_URL_TEMPLATE.format(sha_key=SCHOLAR_INBOX_SHA_KEY), timeout=30)
    resp.raise_for_status()

    cookie_names = [c.name for c in session.cookies]
    logging.debug(f"After login: cookies set = {cookie_names}")
    if not cookie_names:
        logging.warning(
            "Login request succeeded (200) but no cookies were set -- "
            "the sha_key may be invalid/revoked."
        )

    return session


def fetch_digest_for_date(session: requests.Session, date: str) -> list:
    """date in MM-DD-YYYY (the site's own format)."""
    resp = session.get(DIGEST_URL, params={"date": date}, timeout=30)
    if resp.status_code == 401:
        logging.debug(f"401 response body: {resp.text[:500]!r}")
    resp.raise_for_status()
    data = resp.json()

    papers = []
    for item in data.get("digest_df", []):
        # Scholar Inbox also indexes bioRxiv/medRxiv/ChemRxiv/OA proceedings;
        # this list only tracks arXiv.
        if item.get("source") != "arxiv" or not item.get("arxiv_id"):
            continue

        authors = item.get("authors", "") or ""
        papers.append(
            {
                "title": (item.get("title") or "").strip(),
                "abstract": (item.get("abstract") or "").replace("\n", " ").strip(),
                "date": item.get("publication_date") or data.get("current_digest_date", ""),
                "url": f"https://arxiv.org/abs/{item['arxiv_id']}",
                "authors": ";".join(a.strip() for a in authors.split(",") if a.strip()),
            }
        )
    return papers


def fetch_recent(days: int = 3) -> list:
    if not SCHOLAR_INBOX_SHA_KEY:
        logging.info("SCHOLAR_INBOX_SHA_KEY not set, skipping Scholar Inbox fetch.")
        return []

    try:
        session = _login_session()
    except Exception as e:
        logging.error(f"Scholar Inbox login failed: {e}")
        return []

    by_url = {}
    for i in range(days):
        d = (datetime.utcnow() - timedelta(days=i)).strftime("%m-%d-%Y")
        try:
            papers = fetch_digest_for_date(session, d)
        except Exception as e:
            logging.warning(f"Scholar Inbox fetch failed for {d}: {e}")
            continue
        logging.info(f"Scholar Inbox {d}: {len(papers)} arXiv paper(s)")
        for p in papers:
            by_url[p["url"]] = p

    return list(by_url.values())


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--days", type=int, default=3)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--debug", action="store_true")
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.debug else logging.INFO, format="%(message)s"
    )

    papers = fetch_recent(days=args.days)
    logging.info(f"Scholar Inbox total: {len(papers)} paper(s)")

    if not args.dry_run:
        append_to_pending(papers, source="scholar_inbox_api")
    else:
        for p in papers[:10]:
            print(f"- {p['date']} {p['title']}")
