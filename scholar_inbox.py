import json
import logging
import requests

from constant import SCHOLAR_INBOX_URL, SCHOLAR_INBOX_COOKIES


def get_scholar_inbox_digest():
    # Make the GET request with cookies
    response = requests.get(
        SCHOLAR_INBOX_URL,
        cookies=SCHOLAR_INBOX_COOKIES,
        proxies={"http": None, "https": None},
    )

    logging.debug(f"Response status code: {response.status_code}")

    # Check if the request was successful
    if response.status_code == 200:
        result = response.json()
        digest = result.get("digest_df", [])
        assert digest, "Failed to fetch data from Scholar Inbox API. No digest found."

        short_digest = []
        for item in digest:
            short_digest.append(
                {
                    "title": item["title"],
                    "abstract": item["abstract"][:200]
                    + "..."
                    + item["abstract"][-200:],
                    # split by , and then join by ; with no space
                    "authors": ";".join(item["authors"].split(",")),
                    "date": item["publication_date"],
                    "url": item["url"],
                }
            )

        logging.info(f"Retrieved {len(short_digest)} papers from Scholar Inbox")

        pretty_short_digest = json.dumps(short_digest, indent=2)
        logging.debug(f"Digest:\n{pretty_short_digest}")

        return short_digest
    else:
        raise Exception(
            f"Failed to fetch data from Scholar Inbox API. Status code: {response.status_code}"
        )
