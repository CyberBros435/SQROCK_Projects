# Spear Phishing Email Craft (Lab Only)

Python template engine generating personalized spear-phishing awareness-training emails using OSINT-style target data — built strictly for security-awareness training, never for real use.

## What It Does
Takes target OSINT data (name, email, company, location) and generates a realistic spear-phishing email showing spoofed sender, personalized hook, and fake urgency link.

## Tools
- Python (stdlib)

## Usage
```bash
python phishing_simulation.py
```

## Theory
- **Spear phishing** targets one specific individual using gathered OSINT (vs. bulk generic phishing)
- **Key elements**: spoofed sender domain, personal hook (name + real/plausible location), urgency + malicious link
- **Defense — email authentication standards**:
  - **SPF** (Sender Policy Framework) — DNS record listing which servers can send mail for a domain
  - **DKIM** (DomainKeys Identified Mail) — cryptographic signature proving email wasn't altered in transit
  - **DMARC** (Domain-based Message Authentication) — policy telling receiving servers what to do when SPF/DKIM fail (quarantine/reject), plus reporting

## Full Analysis
See [`report/report.md`](report/report.md) and [`report/incident-report.md`](report/incident-report.md) for the 3 generated emails, analysis, and defender setup guide.