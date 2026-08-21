# SIEM Log Analysis for SE Attack Detection

Python log parser that flags social-engineering-related anomalies from raw log text — brute force attempts, suspicious mailbox forwarding rules, and odd-hour logins.

## What It Does
Regex-parses log lines for 3 SE indicator patterns:
- Brute force (≥3 failed logins from same user)
- Suspicious email rule creation (mailbox forwarding — common post-compromise/exfil setup)
- Odd-hour logins (successful logins between 00:00–05:00)

## Tools
- `re`, `collections.Counter` (stdlib)

## Usage
```bash
python siem_log_parser.py
```

## Theory
- SIEM = Security Information and Event Management — centralizes log analysis across sources (Windows Event Log, mail gateway, web proxy, VPN)
- SE attacks leave traces even when the "human" part succeeds: brute-force noise before a lucky guess, new forwarding rules set up post-compromise to exfil mail silently, logins at times the real user wouldn't normally be active

## Full Analysis
See [`report/report.md`](report/report.md) for parsed alerts and log-line breakdown.