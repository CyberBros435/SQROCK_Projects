# Phishing URL Detector

Python script that scores URLs for phishing risk using pattern-based heuristics — protocol check, suspicious keywords, subdomain depth, and raw-IP detection. Detects phishing indicators; does not create or host phishing content.

## What It Does
Scores each URL 0–100% based on 4 weighted red flags:
- No HTTPS (+30)
- Phishing keyword in domain — login/verify/secure/update/account/bank/paypal (+20 each)
- Excessive subdomains, >3 dots (+25)
- Raw IP address instead of domain (+40)

## Tools
- `re`, `urllib.parse` (stdlib only — no dependencies)

## Usage
```bash
python phishing_detector.py
```

## Theory
- **Homograph attacks**: visually identical characters from different alphabets (e.g. Cyrillic "а" vs Latin "a") used to fake trusted domains
- **Subdomain abuse**: `paypal.login.evil.com` — `evil.com` is the real domain, `paypal.login` is a fake subdomain prefix designed to trick users reading left-to-right
- **Missing TLS**: legitimate login/payment pages always use HTTPS; HTTP on a sensitive-looking URL is a major red flag

## Full Analysis
See [`report/report.md`](report/report.md) and [`report/incident-report.md`](report/incident-report.md) for test results and scoring breakdown.