import os
import json

ROOT = "papers"
PENDING_DIR = "papers/_pending"
PENDING_FILE = f"{PENDING_DIR}/queue.csv"
PENDING_FIELDS = ["Title", "Date", "Url", "Author", "Abstract", "Source"]

DOCS_DIR = "docs"
SITE_DATA_FILE = f"{DOCS_DIR}/data/papers.json"

if os.path.exists("debug_secret.json"):
    with open("debug_secret.json") as f:
        os.environ.update(json.load(f))


def _env(name, default=None):
    return os.environ.get(name, default)


# --- LLM classification (OpenAI-compatible; DeepSeek, OpenAI, etc.) ---
# DeepSeek default: GPT_API_BASE=https://api.deepseek.com, GPT_MODEL=deepseek-v4-flash
# (deepseek-v4-flash, non-thinking mode -- cheap, fine for this classification task.
# The older "deepseek-chat" alias is deprecated 2026-07-24.)
GPT_MODEL = _env("GPT_MODEL", "deepseek-v4-flash")
GPT_API_BASE = _env("GPT_API_BASE", "https://api.deepseek.com")
GPT_KEY = _env("GPT_KEY")  # required to actually classify; pending queue is used if absent

# --- Gmail IMAP (for parsing arxivist digest emails) ---
GMAIL_ADDRESS = _env("GMAIL_ADDRESS")
GMAIL_APP_PASSWORD = _env("GMAIL_APP_PASSWORD")
IMAP_HOST = _env("IMAP_HOST", "imap.gmail.com")

# --- Scholar Inbox: authenticated via the permanent magic-link sha_key
# (see fetch_scholar_inbox.py). This is a bearer credential for your
# account -- keep it a GitHub secret only, never commit it.
SCHOLAR_INBOX_SHA_KEY = _env("SCHOLAR_INBOX_SHA_KEY")

# --- arXiv search fallback / backfill ---
ARXIV_CATEGORIES = ["cs.CL", "cs.LG", "stat.ML"]
ARXIV_KEYWORDS = [
    "in-context learning",
    "chain-of-thought",
    "chain of thought",
    "hallucination",
    "scaling law",
    "emergent ability",
    "grokking",
    "transformer expressivity",
    "transformer capacity",
    "mechanistic interpretability",
    "training dynamics",
    "generalization",
    "language model",
    "large language model",
    "attention mechanism",
    "tokenization",
    "layer normalization",
    "memorization",
    "reversal curse",
]
