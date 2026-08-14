# Incident Report — Vishing Simulation Exercise

**Incident ID:** VISHING-SIM-2026-001
**Summary:** Controlled awareness-training exercise — 3 vishing scripts generated and reviewed to model social engineering call patterns for staff training. No real calls made, no real targets contacted.

**Timeline:**
- 2026-08-12 — Script generator built and executed, 3 pretexts produced

**Affected Systems:** N/A — simulation only, no live systems or people contacted

**Root Cause (why this attack vector works):** Exploits authority bias + urgency/fear response; bypasses technical controls entirely by targeting human trust.

**IOCs (simulated):**
- Caller claiming "IT Support" requesting password reset
- Caller claiming "Bank Fraud Dept" citing suspicious transaction
- Caller claiming "Government Official" citing unpaid tax

**MITRE Mapping** *(manual analyst judgment)*:
- **T1566 — Phishing** (parent)
- **T1598 — Phishing for Information** — applies here; goal is credential/info harvesting via voice, not malware delivery

**Detection Method:** N/A (awareness training artifact, not a live detection exercise)

**Response Actions:** Distribute scripts + red-flag list to staff as training material.

**Recommendations:**
1. Train staff: legitimate IT/bank/gov never ask for passwords over phone
2. Mandate callback verification via officially published numbers only
3. Report any password-request call to security team immediately

**Lessons Learned:** Script reuse across 3 different pretexts (IT/bank/gov) with identical credential-harvesting hook shows how cheaply attackers scale vishing — one script template, multiple authority masks.