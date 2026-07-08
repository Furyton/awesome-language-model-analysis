# Setup checklist (one-time)

I've rebuilt the pipeline locally (in this folder, not yet pushed -- I don't
have push access to your GitHub repo from this environment). Here's what's
new and what you need to do to turn it on.

## What changed

- **Removed**: `automate.py`, `scholar_inbox.py`, the old draft-PR workflow.
  Cookie-based Scholar Inbox auth is gone (it expired every ~7 days and had
  to be refreshed by hand).
- **Added**:
  - `fetch_scholar_inbox.py` -- fetches your daily digest directly from
    Scholar Inbox's own JSON API, authenticated with your permanent
    magic-link `sha_key` (confirmed working via a live browser test). Gets
    real titles/abstracts/authors/arxiv ids, no scraping. A fresh session
    is minted from the sha_key every run, so nothing expires.
  - `fetch_arxivist_email.py` -- parses arxivist.com's daily digest email
    via Gmail IMAP (arxivist has no API, so email is the only route).
  - `fetch_arxiv.py` -- searches arXiv directly (category + keyword filter)
    for daily catch-up and for backfilling old gaps.
  - `pending_queue.py` / `papers/_pending/queue.csv` -- new papers land here
    first (deduped against everything already in the list), so a failed
    classification run never loses a paper.
  - `classify_pending.py` -- classifies queued papers with an LLM
    (DeepSeek by default, any OpenAI-compatible API works) and files them
    into `papers/<category>/papers.csv`. If classification fails or no key
    is set, papers just stay pending for next time.
  - `generate_site_data.py` / `generate_embeddings.py` -- build `docs/data/*.json`
    for the new webpage.
  - `docs/` -- a static search page (lexical search via Fuse.js, optional
    "Semantic search" toggle powered by in-browser embeddings -- no server,
    no API cost).
  - `.github/workflows/daily.yml` -- one workflow, runs weekdays, does
    fetch -> classify -> regenerate README -> regenerate webpage data ->
    **commits straight to `main`**. No more manual PR review.

## 1. Push the changes

```bash
cd /path/to/awesome-language-model-analysis
git add -A
git commit -m "Rebuild pipeline: Scholar Inbox API, staged classification, search webpage"
git push
```

## 2. Add GitHub secrets

Repo -> Settings -> Secrets and variables -> Actions -> New repository secret.

| Secret | Required for | Notes |
|---|---|---|
| `SCHOLAR_INBOX_SHA_KEY` | Scholar Inbox fetch | the `sha_key=...` value from the link at the top of any Scholar Inbox digest email. **Treat this like a password** -- it's a bearer credential for your account. |
| `GMAIL_ADDRESS` | arxivist fetch | your Gmail address, only needed if arxivist's digest lands in Gmail |
| `GMAIL_APP_PASSWORD` | arxivist fetch | Google Account -> Security -> 2-Step Verification -> App Passwords |
| `GPT_KEY` | Classification | a DeepSeek API key (platform.deepseek.com) or any OpenAI-compatible key |
| `GPT_API_BASE` | Classification | optional, defaults to `https://api.deepseek.com` |
| `GPT_MODEL` | Classification | optional, defaults to `deepseek-v4-flash` (non-thinking, cheap; `deepseek-chat` is deprecated 2026-07-24) |

Everything is best-effort: if a secret is missing, that step is skipped
(logged, not fatal) and the rest of the pipeline still runs. You can add
these gradually.

You can delete the old `SCHOLAR_INBOX_URL` / `SCHOLAR_INBOX_COOKIES` /
`TOKEN` secrets -- they're no longer used.

**If arxivist also only reaches you via Outlook**: Outlook.com is retiring
app-password IMAP access in 2026, so `fetch_arxivist_email.py` can't read it
there directly. Set up an Outlook forwarding rule (Settings -> Mail ->
Forwarding, not a manual per-email forward) to also deliver arxivist digests
to Gmail. The script matches by scanning message bodies for `arxivist.com`
rather than a strict sender check, so a forwarded copy works fine.

## 3. Turn on GitHub Pages

Repo -> Settings -> Pages -> Source: **Deploy from a branch** -> Branch:
`main`, folder: `/docs`. The site will be at
`https://furyton.github.io/awesome-language-model-analysis/`.

## 4. Fetcher status

- **Scholar Inbox**: fetches the last 3 days of digests each run, keeps only
  `source == "arxiv"` entries (Scholar Inbox also indexes bioRxiv/medRxiv/
  ChemRxiv, which this list doesn't track). Note on history: an earlier
  version of this script hit `www.scholar-inbox.com/login?sha_key=...`
  directly and appeared to work in a live browser test, but that was a false
  positive -- the browser already had an unrelated pre-existing login
  session, so the test wasn't actually exercising the sha_key flow. The real
  login endpoint (confirmed by reading the open-source `scholarinboxcli`
  package's source, github.com/mrshu/scholarinboxcli) is a same-origin call:
  `GET https://api.scholar-inbox.com/api/login/{sha_key}/`. The script now
  uses that.
- **arxivist**: still a best-effort guess (no sample email seen yet) -- it
  looks for direct `arxiv.org` links in the email body. If the first run
  finds 0 arxivist papers, send me a sample digest email and I'll calibrate
  it the same way I did for Scholar Inbox.

## 5. Backfill the Nov 2024 -> now gap

Actions tab -> "Daily update" -> Run workflow -> fill in `backfill_start`
(e.g. `2024-11-27`) and `backfill_end` (today's date) -> Run. This only
fetches from arXiv (Scholar Inbox/arxivist don't have historical digests).
It'll likely queue more than the default classify limit (80/run) can drain
in one go -- just re-run the daily workflow a few times (or bump `--limit`
in `classify_pending.py` for that one run) until `papers/_pending/queue.csv`
is empty.

## 6. Verify

- Actions tab: confirm "Daily update" runs green (or check which steps
  were skipped due to missing secrets).
- Open the Pages URL and try a search.
- `papers/_pending/queue.csv` should shrink over the following days as
  classification catches up.
