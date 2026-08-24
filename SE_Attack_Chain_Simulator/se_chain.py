# se_chain.py — Full SE Simulation Chain
import sys
import json
import re
import datetime
from urllib.parse import urlparse

MODULES = {
    "osint"    : "Run passive OSINT on a domain",
    "profile"  : "Build target profile from public GitHub data",
    "phish"    : "Score a URL for phishing indicators",
    "template" : "Generate spear-phishing training email",
    "ir"       : "Trigger incident response workflow",
}

# ---------- Day 1: OSINT ----------
def run_osint():
    import whois, socket, requests
    domain = input("Enter domain to scan: ").strip()
    try:
        w = whois.whois(domain)
        ip = socket.gethostbyname(domain)
        geo = requests.get(f"http://ip-api.com/json/{ip}", timeout=5).json()
        print(f"Registrar : {w.registrar}")
        print(f"IP        : {ip}")
        print(f"Location  : {geo.get('city')}, {geo.get('country')}")
    except Exception as e:
        print(f"[ERROR] OSINT scan failed: {e}")

# ---------- Day 5: GitHub Profile ----------
def run_profile():
    import requests
    username = input("Enter GitHub username: ").strip()
    try:
        base = "https://api.github.com"
        u = requests.get(f"{base}/users/{username}").json()
        repos = requests.get(f"{base}/users/{username}/repos").json()
        langs = {}
        for r in repos[:10]:
            if r.get('language'):
                langs[r['language']] = langs.get(r['language'], 0) + 1
        profile = {
            "name": u.get("name"), "company": u.get("company"),
            "location": u.get("location"), "public_repos": u.get("public_repos"),
            "top_langs": langs, "bio": u.get("bio")
        }
        print(json.dumps(profile, indent=2))
    except Exception as e:
        print(f"[ERROR] Profile build failed: {e}")

# ---------- Day 3: Phishing URL Scorer ----------
KEYWORDS = ["login", "verify", "secure", "update", "account", "bank", "paypal"]

def phish_score(url):
    p = urlparse(url)
    score = 0
    if not url.startswith("https"):
        score += 30
    for kw in KEYWORDS:
        if kw in p.netloc:
            score += 20
    if p.netloc.count('.') > 3:
        score += 25
    if re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', p.netloc):
        score += 40
    return min(score, 100)

def run_phish():
    url = input("Enter URL to score: ").strip()
    print(f"{url} -> Risk: {phish_score(url)}%")

# ---------- Day 6: Spear Phish Template ----------
def spear_phish_template(target):
    return f"""
From    : it-support@{target['company'].lower()}.com
To      : {target['email']}
Subject : Action Required: Your {target['company']} account will be disabled

Hi {target['name']},

Our security team noticed a login from {target['location']}.
Please verify your account within 24 hours to avoid suspension.

[Verify Account] -> https://lab.internal

Regards,
IT Security Team
"""

def run_template():
    target = {
        "name": input("Target name: ").strip(),
        "email": input("Target email: ").strip(),
        "company": input("Target company: ").strip(),
        "location": input("Target location: ").strip(),
    }
    print(spear_phish_template(target))

# ---------- Day 9: Incident Response ----------
def ir_response(incident):
    print(f"\n=== INCIDENT RESPONSE TRIGGERED ===")
    print(f"Time     : {datetime.datetime.now()}")
    print(f"Type     : {incident['type']}")
    print(f"Severity : {incident['severity']}")

    actions = []
    if incident['severity'] in ('HIGH', 'CRITICAL'):
        actions += ["LOCK user account", "Revoke active sessions",
                     "Notify SOC team", "Preserve mail logs"]
    if incident['type'] == 'phishing':
        actions += ["Quarantine email", "Block sender domain",
                     "Scan attachments in sandbox"]

    print("\nActions Taken:")
    for a in actions:
        print(f"  [x] {a}")

    report = {"incident": incident, "actions": actions,
               "timestamp": str(datetime.datetime.now())}
    with open("ir_report_chain.json", "w") as f:
        json.dump(report, f, indent=2)
    print("\nIR report saved: ir_report_chain.json")

def run_ir():
    incident = {
        "type": input("Incident type (phishing/vishing): ").strip(),
        "severity": input("Severity (LOW/MEDIUM/HIGH/CRITICAL): ").strip().upper(),
        "user": input("Affected user email: ").strip(),
    }
    ir_response(incident)

# ---------- Menu ----------
def menu():
    print("\n=== SE CHAIN SIMULATOR ===")
    print("Sqrock Cybersecurity Internship — Final Project")
    print("=" * 45)
    for k, v in MODULES.items():
        print(f"  [{k}] {v}")

    choice = input("\nSelect module (or 'exit'): ").strip().lower()

    if choice == "exit":
        print("Session ended.")
        return
    elif choice == "osint":
        run_osint()
    elif choice == "profile":
        run_profile()
    elif choice == "phish":
        run_phish()
    elif choice == "template":
        run_template()
    elif choice == "ir":
        run_ir()
    else:
        print("Invalid choice.")

    menu()

if __name__ == "__main__":
    menu()