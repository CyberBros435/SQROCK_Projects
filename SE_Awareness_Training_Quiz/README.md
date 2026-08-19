# Social Engineering Awareness Training Module

Interactive CLI quiz engine testing SE awareness across 10 realistic scenarios (phishing, vishing, smishing, tailgating, BEC, pretexting, malware delivery, MFA) — built as a training tool, modeled on real programs like GoPhish/KnowBe4.

## What It Does
Presents 10 scenario-based multiple-choice questions one at a time, gives immediate feedback + explanation on wrong answers, tracks score, and exports a full results report to JSON.

## Tools
- `json`, `datetime` (stdlib)

## Usage
```bash
python se_awareness_quiz.py
```
Answer each question (A/B/C). Final score + `quiz_score_report.json` generated at completion.

## Theory
- Training is the #1 defense against social engineering — technical controls can't stop a human being socially manipulated
- Effective training needs: realistic scenarios, immediate feedback, repetition
- Real-world programs (GoPhish, KnowBe4) using this exact model reduce phishing click rates by 70%+

## Full Analysis
See [`report/report.md`](report/report.md) for question coverage, test run, and JSON output analysis.