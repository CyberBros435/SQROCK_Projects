# Report: Password Attacks — Credential Stuffing / Brute Force Simulation

## Objective
Understand brute-force login attack logic and build a foundation for rate-limit detection.

## Theory
- **Credential stuffing**: reusing leaked username:password pairs against other login endpoints.
- **Brute force**: systematic guessing of credentials.
- **Dictionary attack**: brute force using a pre-built wordlist.
- **Defenses**: account lockout, CAPTCHA, MFA, breach monitoring, rate limiting.

## Setup
Local Flask server (`server.py`) simulates a login endpoint at `/login` with hardcoded valid credentials (`admin:letmein`) for lab testing.

![VS Code project structure](p1.png)

## Execution

### Attempt 1 — server not running
Ran `bruteforce_sim.py` before starting the server — connection error confirms error handling works.

![Connection error](p2.png)

### server.py code
![server.py source](p3.png)

### bruteforce_sim.py code
![bruteforce_sim.py source](p4.png)

### Attempt 2 — server running
Started `server.py`, then ran the attack script.

![Server running, requests logged](p5.png)

Flask access log shows the attack sequence: four `401` (failed) attempts followed by one `200` (success) on `letmein`.

### Result
![CMD output — password found](p6.png)

Script correctly identified the valid password from the wordlist:

    [-] Failed: 123456
    [-] Failed: password
    [-] Failed: admin
    [+] FOUND: admin:letmein

## MITRE ATT&CK Mapping
| TTP ID | Tactic | Technique |
|--------|--------|-----------|
| T1110.001 | Credential Access | Brute Force: Password Guessing |
| T1110.004 | Credential Access | Brute Force: Credential Stuffing |

## Detection / Defense Notes
- Flask access log shows 4x `401` in ~2 sec from same IP → rate-limit trigger candidate.
- Splunk detection: `sourcetype=flask_access status=401 | stats count by src_ip | where count > 3`
- Defensive fix: Flask-Limiter (`@limiter.limit("3/minute")`) on `/login` route.
- Production defenses: account lockout after N attempts, CAPTCHA, MFA, breach-monitoring integration (HaveIBeenPwned API).

## Deliverable Status
✅ Script demo on local lab
⬜ Defensive rate limiter implementation (next iteration)