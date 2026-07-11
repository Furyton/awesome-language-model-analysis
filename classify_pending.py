"""Drain the pending queue: classify each paper with the LLM and file it
into papers/<category>/papers.csv. Designed to be safe to interrupt --
whatever hasn't been processed yet (or fails) just stays in the pending
queue for the next run.
"""
import os
import csv
import logging
import argparse

import openai

from constant import ROOT, GPT_KEY
from classifier import categorize_paper
from pending_queue import load_pending, rewrite_pending

# Errors that mean "the whole setup is broken" (bad key, no credit, etc.) --
# stop immediately rather than burning through the rest of the batch making
# the same failed call over and over.
FATAL_ERROR_TYPES = (openai.AuthenticationError, openai.PermissionDeniedError)


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
    error_count = 0

    for i, paper in enumerate(to_process):
        title = paper["Title"]
        try:
            categories = categorize_paper(title, paper.get("Abstract", ""))
        except FATAL_ERROR_TYPES as e:
            logging.error(f"Classification failed on '{title}': {e}")
            logging.warning(
                f"This looks like a broken key/credentials, not a one-off -- stopping early. "
                f"{len(to_process) - i} + {len(remaining)} paper(s) remain pending for the next run."
            )
            remaining = to_process[i:] + remaining
            break
        except Exception as e:
            # transient/one-off failure (rate limit, timeout, bad response for
            # this one paper) -- skip it and keep going, don't lose the batch
            logging.warning(f"Skipping '{title}' after error: {e}")
            error_count += 1
            remaining.append(paper)
            continue

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
            with open(csv_path, "a", encoding="utf-8") as f:
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
        f"errors (retrying next run): {error_count}, still pending: {len(remaining)}"
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
