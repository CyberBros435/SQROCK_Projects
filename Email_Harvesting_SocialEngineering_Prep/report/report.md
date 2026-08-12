# Email Harvesting & Social Engineering Prep — Report

**Analyst:** Mudasir Zia | **Date:** 2026-08-12 | **Tool:** email_harvester.py

## Objective
Scrape emails from a public web source using regex, and understand how attackers use email harvesting as the first step of social engineering / pretexting campaigns.

## Methodology
1. `requests.get(url).text` → fetch raw HTML
2. `re.findall(r'[\w.+-]+@[\w-]+\.[a-zA-Z]{2,}', html)` → regex match against raw text
3. Deduplicate with `set()`

## Test Log — Full Sequence

The task's suggested target (`testphp.vulnweb.com`) and several follow-up targets were tested. Most returned zero results — this is documented as a finding in itself, not a failure of the script.

| # | Target | Result | Reason |
|---|---|---|---|
| 1 | `testphp.vulnweb.com` | Connection timeout | Site unreachable from local network (verified via `ping` + `curl`, 100% packet loss, port 80 connect timeout) |
| 2 | `demo.testfire.net` | SSL handshake failure | Certificate expired (`SEC_E_CERT_EXPIRED`) — legacy demo site, dead cert |
| 3 | `demo.testfire.net` (with `verify=False`) | 0 emails, 8360 chars fetched | Page loaded successfully; homepage has no plaintext emails |
| 4 | `demo.testfire.net/feedback.aspx` | 0 emails, 38520 chars fetched | Page loaded; no plaintext emails present |
| 5 | `w3schools.com` (about/help page) | 0 emails, 406 chars fetched | Minimal page content, no emails |
| 6 | GitHub Gist raw URL | 0 emails, 14 chars fetched | URL returned near-empty response (redirect/invalid path) |
| 7 | `en.wikipedia.org/wiki/Email_address` | 0 emails, 126 chars fetched | Page returned minimal content (likely redirect or stub, not full article HTML) |
| 8 | `raw.githubusercontent.com/torvalds/linux/master/MAINTAINERS` | **250+ emails found** | Linux kernel maintainers file — public, plaintext, always-available dataset |

## Screenshots (in sequence)

**Setup / Code**
![Script and project structure](1.png)

**Attempt 1 — testphp.vulnweb.com timeout**
![Connection timeout traceback](2.png)
![ping testphp.vulnweb.com — 100% packet loss](3.png)
![ping direct IP — 100% packet loss](4.png)
![curl -v port 80 timeout](5.png)

**Attempt 2 — testfire.net SSL failure**
![SEC_E_CERT_EXPIRED via curl](6.png)

**Attempt 3–4 — testfire.net fixed but empty**
![0 emails, homepage](7.png)
![0 emails, feedback page](8.png)

**Attempt 5 — w3schools**
![0 emails, w3schools](9.png)

**Attempt 6 — GitHub Gist**
![0 emails, 14 chars](10.png)

**Attempt 7 — Wikipedia**
![0 emails, Wikipedia stub](11.png)

**Attempt 8 — SUCCESS — Linux MAINTAINERS file**
![Emails found — batch 1](12.png)
![Emails found — batch 2](13.png)
![Emails found — batch 3](14.png)
![Emails found — batch 4](15.png)
![Emails found — batch 5](16.png)
![Emails found — batch 6](17.png)
![Emails found — batch 7](18.png)
![Emails found — batch 8](19.png)
![Emails found — batch 9](20.png)
![Emails found — batch 10](21.png)
![eicar.org manual verification — no plaintext email visible](22.png)
![Emails found — batch 11](23.png)
![Emails found — batch 12](24.png)
![Emails found — batch 13](25.png)
![Emails found — batch 14](26.png)
![Emails found — batch 15](27.png)
![Emails found — batch 16](28.png)
![Emails found — batch 17](29.png)
![Emails found — final batch](30.png)

## Findings

**Why most modern sites returned zero results:**
- Business/product sites use contact forms instead of exposed emails
- Some use HTML entity encoding (`&#99;&#111;...`) to defeat simple regex scrapers
- Some build `mailto:` links dynamically via JavaScript, which static `requests.get()` never executes/renders
- These are deliberate anti-spam-harvesting defenses

**Why the Linux MAINTAINERS file worked:**
- It's a plaintext file, not rendered HTML — no JS obfuscation possible
- Open-source project maintainers intentionally publish emails for contribution/patch workflows
- Served directly via `raw.githubusercontent.com` with no CDN/WAF stripping

## How Attackers Use This (Write-Up)

Email harvesting is typically the **first phase of a social engineering campaign**, feeding directly into pretexting:

1. **Recon** — attacker scrapes public sources (company website, GitHub commit logs, LinkedIn, conference speaker lists, open-source contributor files like MAINTAINERS) to build a target list of real, active email addresses tied to real names and roles.
2. **Pretexting** — using the harvested name + email + inferred role (e.g. "kernel maintainer," "finance team," "IT admin"), the attacker crafts a believable fake identity or scenario — e.g. impersonating IT support, a vendor, or a colleague — to justify an unusual request.
3. **Delivery** — the harvested email becomes the actual delivery target for phishing, spear-phishing, or business email compromise (BEC) attempts, often personalized using OSINT gathered about that specific person (their project, their commits, their public activity) to increase credibility.
4. **Why open-source projects are high-value targets** — files like MAINTAINERS are goldmines: real names, real emails, real organizational affiliation (company domains like `@intel.com`, `@nvidia.com`, `@redhat.com` directly reveal employer), all voluntarily public.

**Defensive takeaway**: this is exactly why modern corporate sites hide emails behind forms/JS — every plaintext email on a public page is a harvestable pretexting entry point.

## Ethics Note
No private, unauthorized, or personal-account data was accessed. All harvested emails were already intentionally and voluntarily made public by their owners (open-source maintainers) for legitimate collaboration purposes — a valid "domain you have implicit permission to observe" per the task's ethics boundary, since MAINTAINERS files exist specifically to be publicly readable.