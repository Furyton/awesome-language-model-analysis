"""Drain the pending queue: classify each paper with the LLM and file it
into papers/<category>/papers.csv. Designed to be safe to interrupt --
whatever hasn't been processed yet (or fails) just stays in the pending
queue for the next run.
"""
import os
import csv
import logging
import argparse

from constant import ROOT, GPT_KEY
from classifier import categorize_paper
from pending_queue import load_pending, rewrite_pending


def classify_all(limit=None, dry_run=False):
    pending = load_pending()
    if not pending:
        logging.info("Pending queue is empty, nothing to classify.")
        return

    if not GPT_KEY:
        logging.warning(
            "GPT_KEY is not set -- skipping classification. "
            f"{len(pending)} paper(s) remain pending."
        )
        return

    to_process = pending if limit is None else pending[:limit]
    remaining = [] if limit is None else pending[limit:]

    classified_count = 0
    dropped_count = 0

    for i, paper in enumerate(to_process):
        title = paper["Title"]
        try:
            categories = categorize_paper(title, paper.get("Abstract", ""))
        except Exception as e:
            logging.error(f"Classification failed on '{title}': {e}")
            logging.warning(
                f"Stopping early; {len(to_process) - i} + {len(remaining)} "
                "paper(s) remain pending for the next run."
            )
            remaining = to_process[i:] + remaining
            break

        if not categories:
            logging.info(f"Dropped (not in scope): {title}")
            dropped_count += 1
            continue

        classified_count += 1
        logging.info(
            f"Classified '{title}' -> {[c['name'] for c in categories]}"
        )

        if dry_run:
            continue

        for category in categories:
            csv_path = os.path.join(ROOT, category["directory"], "papers.csv")
            os.makedirs(os.path.dirname(csv_path), exist_ok=True)
            file_exists = os.path.exists(csv_path)
            with open(csv_path, "a", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                if not file_exists:
                    writer.writerow(["Title", "Date", "Url", "Author"])
                writer.writerow(
                    [title, paper["Date"], paper["Url"], paper["Author"]]
                )

    if not dry_run:
        rewrite_pending(remaining)

    logging.info(
        f"Done. Classified: {classified_count}, dropped: {dropped_count}, "
        f"still pending: {len(remaining)}"
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--limit",
        type=int,
        default=60,
        help="Max papers to classify in one run (keeps API cost/time bounded).",
    )
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--debug", action="store_true")
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.debug else logging.INFO,
        format="%(message)s",
    )
    logging.getLogger("httpx").setLevel(logging.CRITICAL)
    logging.getLogger("urllib3").setLevel(logging.CRITICAL)

    classify_all(limit=args.limit, dry_run=args.dry_run)
