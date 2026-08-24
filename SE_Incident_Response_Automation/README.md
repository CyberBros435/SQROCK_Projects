# SE Incident Response Plan

Python IR automation script that triggers containment actions automatically based on social engineering incident type and severity, then logs a JSON incident report.

## What It Does
Takes an incident dict (type, severity, user) → prints IR trigger log → runs severity-based and type-based containment actions → saves a timestamped JSON report per incident.

## Tools
- `datetime`, `json` (stdlib)

## Usage
```bash
python ir_automation.py
```

## Theory
- **IR Phases**: Preparation → Identification → Containment → Eradication → Recovery → Lessons Learned
- SE incidents require: account lockout, forensic email analysis, user notification
- Documentation is critical for legal, compliance, and insurance purposes — every action is logged with timestamp

## Full Analysis
See [`report/report.md`](report/report.md) for all 3 incident runs, JSON reports, and the 1-page IR playbook.