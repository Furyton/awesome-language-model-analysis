import os
import json

ROOT = "papers"

if os.path.exists("debug_secret.json"):
    with open("debug_secret.json") as f:
        os.environ.update(json.load(f))

SCHOLAR_INBOX_URL = os.environ["SCHOLAR_INBOX_URL"]
SCHOLAR_INBOX_COOKIES = {
    "session": os.environ["SCHOLAR_INBOX_COOKIES"]
}  # update every 7 days

GPT_MODEL = "gpt-4o-mini"

GPT_API_BASE = os.environ["GPT_API_BASE"]
GPT_KEY = os.environ["GPT_KEY"]
