import warnings

warnings.simplefilter(action="ignore", category=UserWarning)
import logging
import argparse
from constant import ROOT
from classifier import categorize_paper
from scholar_inbox import get_scholar_inbox_digest

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Automate the process of categorizing papers"
    )
    parser.add_argument("--dry-run", action="store_true", help="Enable debug mode")
    parser.add_argument("--debug", action="store_true", help="Enable debug mode")

    args = parser.parse_args()

    is_dry_run = args.dry_run
    is_debug = args.debug

    logging.basicConfig(
        level=logging.DEBUG if is_debug else logging.INFO,
        format="[%(asctime)s - L%(lineno)4s : %(funcName)-15s] %(message)s"
        if is_debug
        else "%(message)s",
        handlers=[
            logging.StreamHandler(),
        ]
        + ([logging.FileHandler("debug.log")] if not is_dry_run else []),
    )
    logging.getLogger("requests").setLevel(logging.CRITICAL)
    logging.getLogger("urllib3").setLevel(logging.CRITICAL)
    logging.getLogger("httpx").setLevel(logging.CRITICAL)
    logging.getLogger("urllib3").propagate = False

    # Get the latest papers from Scholar Inbox
    papers = get_scholar_inbox_digest()

    categorization_result = (
        {}
    )  # {category: {category_name, category_directory, [papers]}}

    # Categorize each paper
    for paper in papers:
        title = paper["title"]
        abstract = paper["abstract"]
        categories = categorize_paper(title, abstract)

        if categories is None:
            continue

        for category in categories:
            cate_name = category["name"]
            cate_dir = category["directory"]

            if cate_dir not in categorization_result:
                categorization_result[cate_name] = {
                    "category_name": cate_name,
                    "category_directory": cate_dir,
                    "papers": [],
                }

            categorization_result[cate_name]["papers"].append(paper)

    assert categorization_result, "No papers were categorized"

    pull_request_body = ""

    for category in categorization_result.values():
        pull_request_body += f"## {category['category_name']}\n\n"

        for paper in category["papers"]:
            authors = paper["authors"]
            pull_request_body += (
                f"- \"{paper['title']}\",{paper['date']},\"{paper['url']}\", {authors}\n\n"
            )

        pull_request_body += "\n"

    logging.info(pull_request_body)

    print_all_paper = "\n\n---\n ## All Digest Papers From Scholar Inbox\n\n"

    # print in markdown format with link format
    for paper in papers:
        authors = paper["authors"]
        # print_all_paper += f"- [{paper['title']}]({paper['url']}), {authors}\n\n"
        print_all_paper += f"- \"{paper['title']}\",{paper['date']},\"{paper['url']}\", {authors}\n\n"

    logging.info(print_all_paper)

    if not is_dry_run:
        for category in categorization_result.values():
            with open(
                f"{ROOT}/{category['category_directory']}/papers.csv", "a"
            ) as file:
                for paper in category["papers"]:
                    authors = paper["authors"]
                    file.write(
                        f"\n\"{paper['title']}\",{paper['date']},{paper['url']},{authors}\n"
                    )
