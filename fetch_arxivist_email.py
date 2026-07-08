"""Parse arxivist.com's daily digest email via Gmail IMAP.

arxivist.com uses Google Sign-In and has no public API/RSS, so (unlike
Scholar Inbox, which has a working magic-link API -- see
fetch_scholar_inbox.py) email parsing is the only practical route here.

Requires GMAIL_ADDRESS + GMAIL_APP_PASSWORD env vars (see SETUP.md). If
they're not set, this is skipped -- optional, not required for the rest of
the pipeline to run.

NOTE: no real arxivist digest email was available while building this, so
the parsing below is a best-effort guess (it looks for direct arxiv.org
links in the email body). If a run finds 0 papers, send a sample digest
email and the parsing can be calibrated the same way Scholar Inbox's was.
"""
import os
import re
import imaplib
import email
import logging
from datetime import datetime, timedelta

from constant import GMAIL_ADDRESS, GMAIL_APP_PASSWORD, IMAP_HOST
from pending_queue import append_to_pending

ARXIVIST_MARKER = os.environ.get("ARXIVIST_MARKER", "arxivist.com")

ARXIVIST_LINK_RE = re.compile(
    r'<a[^>]+href="(https?://arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})(?:v\d+)?[^"]*)"[^>]*>(.*?)</a>',
    re.IGNORECASE | re.DOTALL,
)


def _get_html_body(msg) -> str:
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/html":
                charset = part.get_content_charset() or "utf-8"
                return part.get_payload(decode=True).decode(charset, errors="ignore")
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                charset = part.get_content_charset() or "utf-8"
                return part.get_payload(decode=True).decode(charset, errors="ignore")
        return ""
    else:
        charset = msg.get_content_charset() or "utf-8"
        return msg.get_payload(decode=True).decode(charset, errors="ignore")


def _fetch_recent_messages(imap: imaplib.IMAP4_SSL, since_days: int) -> list:
    since = (datetime.utcnow() - timedelta(days=since_days)).strftime("%d-%b-%Y")
    status, data = imap.search(None, f"(SINCE {since})")
    if status != "OK" or not data or not data[0]:
        return []

    messages = []
    for msg_id in data[0].split():
        status, msg_data = imap.fetch(msg_id, "(RFC822)")
        if status != "OK":
            continue
        messages.append(email.message_from_bytes(msg_data[0][1]))
    return messages


def _parse_arxivist_html(html: str) -> list:
    papers = []
    seen = set()
    for url, arxiv_id, inner_html in ARXIVIST_LINK_RE.findall(html):
        if arxiv_id in seen:
            continue
        title = re.sub(r"<[^>]+>", " ", inner_html)
        title = " ".join(title.split()).strip()
        if not title or len(title) < 8:
            continue
        seen.add(arxiv_id)
        papers.append(
            {
                "url": f"https://arxiv.org/abs/{arxiv_id}",
                "title": title,
                "abstract": "",
                "date": datetime.utcnow().strftime("%Y-%m-%d"),
                "authors": "",
            }
        )
    return papers


def fetch_recent(since_days: int = 2) -> list:
    if not GMAIL_ADDRESS or not GMAIL_APP_PASSWORD:
        logging.info("GMAIL_ADDRESS/GMAIL_APP_PASSWORD not set, skipping arxivist fetch.")
        return []

    try:
        imap = imaplib.IMAP4_SSL(IMAP_HOST)
        imap.login(GMAIL_ADDRESS, GMAIL_APP_PASSWORD)
        imap.select("INBOX")
    except Exception as e:
        logging.error(f"IMAP login failed: {e}")
        return []

    try:
        messages = _fetch_recent_messages(imap, since_days)
        logging.info(f"Scanning {len(messages)} recent email(s) for arxivist digests")

        papers = []
        for msg in messages:
            html = _get_html_body(msg)
            if html and ARXIVIST_MARKER in html:
                papers.extend(_parse_arxivist_html(html))

        by_url = {p["url"]: p for p in papers}
        return list(by_url.values())
    finally:
        try:
            imap.close()
            imap.logout()
        except Exception:
            pass


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--days", type=int, default=2)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--debug", action="store_true")
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.debug else logging.INFO, format="%(message)s"
    )

    papers = fetch_recent(since_days=args.days)
    logging.info(f"arxivist: {len(papers)} candidate paper(s)")

    if not args.dry_run:
        append_to_pending(papers, source="arxivist_email")
    else:
        for p in papers[:10]:
            print(f"- {p['title']} ({p['url']})")
