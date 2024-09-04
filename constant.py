import os

ROOT = "papers"

SCHOLAR_INBOX_URL = os.environ["SCHOLAR_INBOX_URL"]
SCHOLAR_INBOX_COOKIES = {
    "session": os.environ["SCHOLAR_INBOX_COOKIES"]
}  # update every 7 days

GPT_MODEL = "gpt-4o-mini"

GPT_API_BASE = os.environ["GPT_API_BASE"]
GPT_KEY = os.environ["GPT_KEY"]
