# Incident Report — OSINT Target Profiling Exercise

**Incident ID:** OSINT-SE-2026-001
**Summary:** Controlled OSINT exercise — public GitHub API data aggregated into target profiles for 2 usernames to demonstrate SE recon methodology and exposure risk. No private data accessed, no direct contact with targets.

**Timeline:**
- 2026-08-12 — Profiler built and run against CyberBros435 (self) and torvalds (public figure, consent implicit via public API)

**Affected Systems:** N/A — public API data only, read-only

**Root Cause (why this data is exposable):** GitHub's public API exposes profile bio, company, location, and repo metadata by default — no authentication required.

**IOCs (data points harvested, not malicious):**
- Bio text revealing specialty/interest area
- Location field
- Company/org affiliation
- Language distribution across repos (tech stack fingerprint)

**MITRE Mapping** *(manual analyst judgment)*:
- **T1593 — Search Open Websites/Domains** (parent)
- **T1593.003 — Code Repositories** — directly applicable; GitHub used as the OSINT source

**Detection Method:** N/A — passive OSINT via public API, no detection applicable (not an attack, a recon methodology demo)

**Response Actions:** None required — no live target compromised or contacted.

**Recommendations:**
1. Minimize bio/location detail on public profiles unless operationally necessary
2. Review repo READMEs for accidental credential/infra leaks (common companion risk to this recon method)
3. Treat public GitHub profile as equivalent exposure to a public resume — assume it's read by adversaries

**Lessons Learned:** A single unauthenticated API call reconstructs a meaningful SE profile (specialty, location, tech stack) in seconds — proves how low the cost of basic OSINT recon is for attackers, and why minimizing public profile detail matters even on "just a coding profile."