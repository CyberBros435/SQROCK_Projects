import re
from urllib.parse import urlparse

KEYWORDS = ["login", "verify", "secure", "update", "account", "bank", "paypal"]


def phish_score(url):
    p = urlparse(url)
    score = 0

    if not url.startswith("https"):
        score += 30

    for kw in KEYWORDS:
        if kw in p.netloc:
            score += 20

    if p.netloc.count(".") > 3:
        score += 25

    if re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", p.netloc):
        score += 40

    return min(score, 100)


# urls = ["https://paypal-login.evil.com/verify", "https://github.com"]
urls = [
    "https://paypal-login.evil.com/verify",
    "https://github.com",
    "http://192.168.1.1/secure/login",
    "https://accounts.google.com",
    "https://bank-secure-update.verify-account.xyz.info",
    "https://www.amazon.com",
    "http://paypal.com.verify-login-secure.ru",
    "https://outlook.office.com",
    "https://update.account.bank.login.confirm-secure.tk",
    "https://www.wikipedia.org"
]

for u in urls:
    print(f"{u} -> Risk: {phish_score(u)}%")