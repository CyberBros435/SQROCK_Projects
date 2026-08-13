# Incident Report — Phishing URL Batch Analysis

**Incident ID:** PHISH-DET-2026-001
**Summary:** Proactive URL risk scoring exercise — 10 sample URLs analyzed for phishing indicators using automated heuristic scoring. No actual compromise; controlled detection test.

**Timeline:**
- 2026-08-12 — Script developed and executed against 10-URL test set
- 2026-08-12 — 3 URLs scored Critical (100%), 1 High Risk (70%), 1 Low Risk (20%), 5 Clean (0%)

**Affected Systems:** N/A — static analysis only, no live systems contacted or affected

**Root Cause (why URLs scored high):**
- Keyword stuffing in subdomains (login, verify, secure, bank, account, paypal)
- Missing TLS (HTTP-only)
- Excessive subdomain chaining to obscure true root domain
- Use of low-cost/high-abuse TLDs (`.xyz`, `.ru`, `.tk`)

**IOCs (simulated/sample only — not live threats):**
- `bank-secure-update.verify-account.xyz.info`
- `paypal.com.verify-login-secure.ru`
- `update.account.bank.login.confirm-secure.tk`
- `192.168.1.1/secure/login` (raw IP)

**MITRE Mapping** *(manual analyst judgment, not a tool-generated field)*:
- **T1566 — Phishing** (parent technique)
- **T1566.002 — Spearphishing Link** — applies to all 3 Critical-scored URLs; crafted links designed to impersonate trusted services

**Detection Method:** Static heuristic URL scoring (protocol check, keyword match, subdomain depth, IP regex) — no dynamic analysis or sandboxing performed.

**Response Actions:** N/A — detection/scoring exercise only, no real threat actioned.

**Recommendations:**
1. Block/flag any URL scoring ≥70% at email gateway or proxy level
2. Add domain-age and SSL-issuer checks to reduce false positives on legitimate keyword-containing domains (e.g. `accounts.google.com`)
3. Maintain allowlist for major brand domains to prevent keyword-based false flags

**Lessons Learned:** Pure keyword + structural heuristics catch obvious phishing patterns effectively (3/3 crafted malicious URLs scored 100%) but require supplementary checks (SSL cert validation, domain reputation/age) to avoid false positives on legitimate services using trust-related terms.