# OSINT Passive Reconnaissance Scanner

Python script that performs passive OSINT (Open-Source Intelligence) gathering on a domain — WHOIS registrar data, DNS resolution, and IP geolocation — using only public data sources with zero direct contact to target infrastructure.

## What It Does
- Fetches WHOIS registrar info for a domain
- Resolves domain to IP via DNS
- Looks up IP geolocation (city, country) via ip-api.com

## Tools
- `python-whois`
- `requests`
- `socket` (stdlib)

## Usage
```bash
pip install -r requirements.txt
python osint_scanner.py
```
Enter a domain when prompted (e.g. `sqrock.cloud`).

## Passive vs Active Recon
This tool is **passive only** — no packets sent to the target beyond a standard DNS lookup, no scanning, no direct probing. Contrast with active recon (Nmap port scans, banner grabbing) which touches the target directly and can be logged/detected by the target's systems.

## Full Analysis
See [`report.md`](report.md) for tested domains, findings, and screenshots.