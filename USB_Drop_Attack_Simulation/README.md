# USB Drop Attack Simulation

Simulates a benign "USB drop" payload that logs system recon info on execution — demonstrates what a real AutoRun-based payload would collect, for awareness/defense training.

## Files
- `usb_payload_sim.py` — recon payload simulator (stdlib only, no external deps)
- `report/recon_log.txt` — sample output from execution
- `report/report.md` — full write-up with screenshots

## Usage
```bash
python usb_payload_sim.py
```
Generates `recon_log.txt` in the working directory with hostname, OS, user, timestamp, and cwd.

**Note:** Fully benign — no persistence, no exfiltration, no network calls. Simulation only.

Full report: [report/report.md](report/report.md)