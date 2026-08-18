# Baiting & Watering Hole Attack Simulation

Python honeypot link tracker that logs visitor metadata (timestamp, IP, path, user-agent) when a "bait" link is clicked — simulates tracking victims of a baiting/watering-hole attack for awareness and detection purposes.

## Files
- `honeypot_server.py` — HTTP honeypot server (stdlib only, no external deps)
- `report/report.md` — full write-up with screenshots and log analysis

## Usage
```bash
python honeypot_server.py
```
Server starts on `http://localhost:8080`. Any GET request to any path is logged and returns "Thanks for visiting!".

**Note:** Local lab only — no real bait links distributed, no real victims tracked.

Full report: [report/report.md](report/report.md)