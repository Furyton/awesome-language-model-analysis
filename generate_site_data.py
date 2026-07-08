"""Build docs/data/papers.json and docs/data/categories.json for the
search webpage, from the same papers/**/papers.csv + category_info.json
that generate_readme.py reads. A paper that lives in multiple category
directories (allowed/expected -- see CONTRIBUTING.md) is merged into one
entry with multiple categories.
"""
import os
import csv
import json
import logging
import argparse

from constant import ROOT, DOCS_DIR, SITE_DATA_FILE

with open("category_info.json", "r") as f:
    category_info = json.load(f)

flattened_categories = sum([v["subcategories"] for v in category_info.values()], [])
directory_to_category = {c["directory"]: c for c in flattened_categories}


def build_papers_index() -> list:
    papers_by_url = {}

    for directory, category in directory_to_category.items():
        csv_path = os.path.join(ROOT, directory, "papers.csv")
        if not os.path.exists(csv_path):
            continue

        with open(csv_path, "r", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                url = row.get("Url", "").strip()
                if not url:
                    continue

                entry = papers_by_url.setdefault(
                    url,
                    {
                        "title": row["Title"].strip(),
                        "date": row["Date"].strip(),
                        "url": url,
                        "authors": [
                            a.strip() for a in row["Author"].split(";") if a.strip()
                        ],
                        "categories": [],
                    },
                )
                cat_ref = {"name": category["name"], "code": category["code"]}
                if cat_ref not in entry["categories"]:
                    entry["categories"].append(cat_ref)

    papers = list(papers_by_url.values())
    papers.sort(key=lambda p: p["date"], reverse=True)
    return papers


def build_categories_index() -> list:
    return [
        {
            "code": c["code"],
            "name": c["name"],
            "directory": c["directory"],
            "description": c["description"],
        }
        for c in flattened_categories
    ]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(message)s")

    papers = build_papers_index()
    categories = build_categories_index()

    logging.info(f"Indexed {len(papers)} unique paper(s) across {len(categories)} categories")

    if not args.dry_run:
        os.makedirs(os.path.dirname(SITE_DATA_FILE), exist_ok=True)
        with open(SITE_DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(papers, f, ensure_ascii=False, separators=(",", ":"))

        with open(os.path.join(DOCS_DIR, "data", "categories.json"), "w", encoding="utf-8") as f:
            json.dump(categories, f, ensure_ascii=False, indent=2)

        logging.info(f"Wrote {SITE_DATA_FILE}")
