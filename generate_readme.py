import os
import csv
import json
import argparse

ROOT = "papers"
FILE_NAME = "papers.csv"
TEMPLATE_FILE = "README.template"
UNCATEGORIZED_TEMPLATE_FILE = "README.uncategorized.template"

# get the category_info.json
with open("category_info.json", "r") as f:
    category_info = json.load(f)

flatten_category_info = sum([v["subcategories"] for v in category_info.values()], [])
directory = [v["directory"] for v in flatten_category_info]


TEMPLATE = """
- **{}** [[paper link]]({}) {}  
{}
"""


def generate_table_of_content(category_info):
    header = "Table of Content\n====================\n<!--ts-->\n"
    header += (
        "- [Awesome Transformers LM Analytics ](#awesome-transformers-lm-analytics-)\n"
        "- [Table of Content](#table-of-content)\n"
    )
    footer = "<!--te-->\n"

    first_level_indent = "  "
    second_level_indent = "    "

    body = ""

    def gen_entry(name):
        return f"- [**{name}**](#{name.lower().replace(' ', '-').replace('/', '').replace('.', '').replace('?','').replace(',','')})"

    for category, category_info in category_info.items():
        subcategories = category_info["subcategories"]

        if len(subcategories) > 1:
            entry = gen_entry(category_info["name"])
            body += first_level_indent + entry + "\n"

        adjust_indent = (
            first_level_indent if len(subcategories) == 1 else second_level_indent
        )
        for subcategory in subcategories:
            entry = gen_entry(subcategory["name"])
            body += adjust_indent + entry + "\n"

    return header + body + footer


def generate_section_template(category_info):
    header_template = "## **{}**\n\n**[`^        back to top        ^`](#awesome-transformers-lm-analytics-)**\n\n{}"
    body_template = """
<details open>
<summary><em>paper list (click to fold / unfold)</em></summary>
<br>
{{{}}}
</details>
"""

    template = ""
    for category, category_info in category_info.items():
        template += (
            header_template.format(category_info["name"], category_info["description"])
            + "\n\n"
        )
        no_sub_header = len(category_info["subcategories"]) == 1
        for subcategory in category_info["subcategories"]:
            if not no_sub_header:
                template += (
                    "#"
                    + header_template.format(
                        subcategory["name"], subcategory["description"]
                    )
                    + "\n\n"
                )
            template += body_template.format(subcategory["directory"]) + "\n\n"

    return template


def generate_statistics_template(category_info):
    header = "**Detailed Statistics**\n\n"
    first_level_indent = ""
    second_level_indent = "  "
    body = ""

    for category, category_info in category_info.items():
        subcategories = category_info["subcategories"]

        if len(subcategories) > 1:
            body += first_level_indent + "- " + category_info["name"] + ":\n\n"

        adjust_indent = (
            first_level_indent if len(subcategories) == 1 else second_level_indent
        )
        for subcategory in subcategories:
            body += (
                adjust_indent
                + "- "
                + subcategory["name"]
                + ": *{n_"
                + subcategory["directory"]
                + "}*\n\n"
            )

    return header + body


def generate_full_template(category_info):
    table_of_content = generate_table_of_content(category_info)
    section_template = generate_section_template(category_info)
    statistics_template = generate_statistics_template(category_info)

    template_path = os.path.join(ROOT, TEMPLATE_FILE)
    with open(template_path, "r") as file:
        template_content = file.read()

    filled_content = template_content.format(
        n_papers="n_papers",
        table_of_content=table_of_content,
        section_template=section_template,
        statistics_template=statistics_template,
    )

    return filled_content


def get_section_list(topic):
    p = os.path.join(ROOT, topic, FILE_NAME)

    # read as dict, the first line is the header

    with open(p, "r") as f:
        reader = csv.DictReader(f)
        # sort by date
        reader = sorted(reader, key=lambda x: x["Date"], reverse=True)
        # sanity check of each row
        for row in reader:
            assert len(row.keys()) == 4, f"topic: {topic}, row: {row}"
            for key in row.keys():
                assert key in [
                    "Title",
                    "Date",
                    "Url",
                    "Author",
                ], f"topic: {topic}, key: {key}, row: {row}, unexpected key"

                assert row[key], f"topic: {topic}, key: {key}, row: {row}, empty value"

        paper_list = []

        # add each row to the list and check for duplicates

        for row in reader:
            paper = TEMPLATE.format(
                row["Title"], row["Url"], row["Date"], row["Author"]
            )
            if paper not in paper_list:
                paper_list.append(paper)

    return paper_list, reader


def fill_readme_template(output_path, content_dict, template_content, dry_run=False):
    filled_content = template_content.format(**content_dict)

    if not dry_run:
        with open(output_path, "w") as file:
            file.write(filled_content)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")

    args = parser.parse_args()

    content_dict = {}

    all_papers = []
    all_paper_data = []
    for d in directory:
        paper_list, paper_data_reader = get_section_list(d)
        content_dict[d] = "\n\n".join(paper_list)
        all_papers.extend(paper_list)
        content_dict["n_" + d] = len(paper_list)

        all_paper_data.extend(paper_data_reader)

    # remove duplicates

    n_unique = len(set(all_papers))

    content_dict["n_papers"] = n_unique

    template_content = generate_full_template(category_info)

    fill_readme_template(
        "README.md", content_dict, template_content, dry_run=args.dry_run
    )

    # remove duplicate in all_paper_data by Title

    all_paper_data = [dict(t) for t in {tuple(d.items()) for d in all_paper_data}]

    all_paper_data = sorted(
        all_paper_data, key=lambda x: (x["Date"], x["Title"]), reverse=True
    )

    all_papers_data = [
        TEMPLATE.format(row["Title"], row["Url"], row["Date"], row["Author"])
        for row in all_paper_data
    ]

    uncategorized_all_papers = {
        "paper-list": "\n\n".join(all_papers_data),
        "n_papers": n_unique,
    }

    uncategorized_template_path = os.path.join(ROOT, UNCATEGORIZED_TEMPLATE_FILE)
    with open(uncategorized_template_path, "r") as file:
        uncategorized_template = file.read()

    fill_readme_template(
        "README.uncategorized.md",
        uncategorized_all_papers,
        uncategorized_template,
        dry_run=args.dry_run,
    )
