import requests, re
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def harvest_emails(url):
    html = requests.get(url, timeout=10, verify=False).text
    print(f"[DEBUG] Fetched {len(html)} characters")  # confirms page loaded
    emails = set(re.findall(r"[\w.+-]+@[\w-]+\.[a-zA-Z]{2,}", html))
    return emails


found = harvest_emails("https://raw.githubusercontent.com/torvalds/linux/master/MAINTAINERS")

if found:
    for e in found:
        print(e)
else:
    print("No emails found on this page.")
