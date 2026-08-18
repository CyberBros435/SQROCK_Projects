# Social Media Impersonation & Fake Profile Detection

Python scorer that evaluates Twitter/X-like profile data using behavioral heuristics to flag likely fake/bot accounts.

## Files
- `fake_profile_scorer.py` — scoring logic + 5 simulated profile samples
- `report/report.md` — full write-up with screenshots and analysis

## Usage
```bash
python fake_profile_scorer.py
```
Outputs a Fake Score (0–100%) per profile based on account age, follower/following ratio, profile pic presence, post count, and bio content.

**Note:** Sample profiles are simulated data for lab purposes, not scraped real accounts.

Full report: [report/report.md](report/report.md)