# Email Harvesting & Social Engineering Prep — Passive OSINT

Python script that scrapes email addresses from public web pages using regex, and documents the real-world friction of doing this against modern (spam-protected) websites vs. legacy/public data sources.

## What It Does
- Fetches raw HTML from a target URL
- Extracts email addresses using regex: `[\w.+-]+@[\w-]+\.[a-zA-Z]{2,}`
- Prints all unique matches found

## Tools
- `requests`
- `re` (stdlib)

## Usage
```bash
pip install -r requirements.txt
python email_harvester.py
```

## Ethics Boundary
Per task instructions: only target domains you own, have written permission for, or are explicitly public/legal test targets (e.g. intentionally vulnerable test sites, public open-source project data). This project did not scrape any private, unauthorized, or personal data.

## Key Learning
Modern real-world websites (business sites, product pages) rarely expose plaintext emails anymore — they use contact forms, JavaScript-rendered addresses, or obfuscation (HTML entity encoding, `mailto:` construction via JS) specifically to defeat scrapers like this one. This project hit that wall directly across 6+ target attempts before finding a valid public dataset.

## Full Analysis
See [`report/report.md`](report/report.md) for the full test sequence (failures included), findings, and screenshots.