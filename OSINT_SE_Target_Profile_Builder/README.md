# OSINT + SE: Target Profile Builder

Python tool that aggregates a GitHub user's public data (bio, location, repos, top languages) into a structured JSON target profile — demonstrates how attackers build SE profiles from public data, and what defenders should minimize exposing.

## What It Does
Pulls public GitHub API data for a username → builds JSON profile: name, company, location, repo count, top languages (from first 10 repos), bio.

## Tools
- `requests`, `json` (stdlib)

## Usage
```bash
python github_osint_profiler.py
```

## Theory
- Attackers combine GitHub + LinkedIn + Twitter to build full target profiles: name, role, tech stack, colleagues, habits
- Tech stack exposure (top_langs) reveals what systems/frameworks a target works with — useful for crafting believable technical pretexts
- Defender takeaway: minimize public bio/company/location fields if not operationally necessary

## Full Analysis
See [`report/report.md`](report/report.md) and [`report/incident-report.md`](report/incident-report.md).