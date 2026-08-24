# SE Attack Chain Simulator — Final Project

Full integrated CLI tool combining every module built during the SQROCK internship (OSINT scanner, GitHub profiler, phishing URL scorer, spear-phish template engine, IR automation) into one menu-driven simulation chain.

## What It Does
Menu-driven tool with 5 modules, each pulled from a prior day's project:
- `osint` — passive WHOIS/DNS/geo lookup on a domain
- `profile` — GitHub public data aggregation into a target profile
- `phish` — URL phishing risk scorer
- `template` — spear-phishing awareness email generator
- `ir` — incident response automation + JSON report

## Tools
- `requests`, `python-whois`, `re`, `json`, `datetime`, `urllib.parse` (all stdlib except requests/whois)

## Usage
```bash
pip install -r requirements.txt
python se_chain.py
```
Select a module by keyword, follow prompts, returns to menu after each run. Type `exit` to quit.

## Theory
Full attack chain modeled: **OSINT → Profile Build → Phish Craft → Delivery → Exploit → Persist**. This tool demonstrates the first 4 stages plus the defensive response (IR), showing both attacker and defender sides of the same chain — the exact structure a red team exercise uses to expose gaps before real attackers do.

## Full Analysis
See [`report/report.md`](report/report.md) and [`report.pdf`](report.pdf) for the complete live-session walkthrough covering all 5 modules.