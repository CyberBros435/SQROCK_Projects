# Password Attacks — Credential Stuffing & Brute Force Simulator

Simulates a brute-force login attack against a local Flask lab server to understand credential stuffing/brute force mechanics and detection.

## Files
- `bruteforce_sim.py` — attacker-side brute force script
- `server.py` — local Flask lab server (vulnerable target for testing only)
- `report/report.md` — full write-up with screenshots

## Usage
1. Start the lab server: `python server.py`
2. In a separate terminal, run the attack: `python bruteforce_sim.py`

**Warning:** Run only against your own local lab server. Never use against systems you don't own.

Full report: [report/report.md](report/report.md)
