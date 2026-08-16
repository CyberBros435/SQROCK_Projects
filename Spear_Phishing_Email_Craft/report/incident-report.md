# Incident Report — Spear Phishing Simulation Exercise

**Incident ID:** SPEARPHISH-SIM-2026-001
**Summary:** Lab-only spear-phishing template exercise — 3 personalized awareness-training emails generated for training purposes. No real emails sent, no real targets contacted.

**Timeline:**
- 2026-08-12 — Template engine built and run against 3 sample targets

**Affected Systems:** N/A — local script execution only, no email actually sent

**Root Cause (why this attack works):** Combines spoofed-sender trust + OSINT-derived personalization (name, location) + urgency to bypass normal skepticism.

**IOCs (simulated only):**
- Spoofed sender: `it-support@sqrock.com`
- Fake verification link: `https://lab.internal`
- Urgency subject line pattern: "Action Required: account will be disabled"

**MITRE Mapping** *(manual analyst judgment)*:
- **T1566.001 — Spearphishing Attachment** *(not applicable — no attachment)*
- **T1566.002 — Spearphishing Link** — applies; fake verify-account link is the payload delivery mechanism

**Detection Method:** N/A — this is the attacker-side artifact for training; detection is covered under defender guide below.

## Defender Setup Guide — SPF / DKIM / DMARC

**SPF (Sender Policy Framework)**
Add a DNS TXT record authorizing which mail servers can send for your domain:

    v=spf1 include:_spf.google.com ~all

Blocks emails claiming to be from `@yourdomain.com` sent from unauthorized servers.

**DKIM (DomainKeys Identified Mail)**
Enable in your mail provider (Google Workspace/Microsoft 365 admin panel) — generates a cryptographic signature added to outgoing mail headers, published as a DNS TXT record. Receiving servers verify the signature to confirm the email wasn't spoofed/altered.

**DMARC (Domain-based Message Authentication, Reporting & Conformance)**
DNS TXT record telling receivers what to do when SPF/DKIM checks fail:

    v=DMARC1; p=quarantine; rua=mailto:dmarc-reports@yourdomain.com

- `p=none` — monitor only (start here)
- `p=quarantine` — send failures to spam
- `p=reject` — hard block failures (end goal once confident)

**Recommendations:**
1. Deploy SPF + DKIM + DMARC (`p=quarantine` minimum) on all company domains
2. Train staff: verify unexpected "IT" emails via internal chat/phone, never click embedded verify links directly
3. Run periodic simulated phishing campaigns (like this exercise) to measure click-rate improvement

**Lessons Learned:** Even a template with a placeholder fake domain (`https://lab.internal`) demonstrates full spear-phishing structure in under 20 lines of code — proves technical barrier to crafting convincing spear phishing is near zero; the real defense is email authentication (SPF/DKIM/DMARC) + user training, not attacker sophistication.