# Vishing & Smishing Simulation Scripts

Python-based generator producing awareness-training call scripts that model real vishing (voice phishing) attack patterns — built for security awareness training, not for actual social engineering use.

## What It Does
Generates 3 unique vishing scripts (IT, bank, government pretexts) showing attacker opener, hook, and a flagged red-indicator for training purposes.

## Tools
- Python (stdlib only)

## Usage
```bash
python vishing_script_generator.py
```

## Theory
- **Vishing**: voice phishing — attacker impersonates a trusted authority (IT, bank, government) by phone
- **Smishing**: SMS phishing — short links + urgency drive high click-through
- **Psychological triggers exploited**: authority (impersonating IT/bank/gov), urgency/fear (unusual activity, unpaid tax), scarcity (act now), liking (friendly first-name opener "Alex")

## Full Analysis
See [`report/report.md`](report/report.md) and [`report/incident-report.md`](report/incident-report.md).