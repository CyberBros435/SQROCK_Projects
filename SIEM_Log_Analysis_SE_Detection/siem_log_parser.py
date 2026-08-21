import re
from collections import Counter
from datetime import datetime

LOG_SAMPLE = """
2024-01-15 02:34:12 FAILED_LOGIN user=admin ip=45.33.32.156
2024-01-15 02:34:14 FAILED_LOGIN user=admin ip=45.33.32.156
2024-01-15 02:34:15 FAILED_LOGIN user=admin ip=45.33.32.156
2024-01-15 02:34:16 SUCCESS_LOGIN user=admin ip=45.33.32.156
2024-01-15 08:00:01 SUCCESS_LOGIN user=riya ip=192.168.1.10
2024-01-15 02:35:00 EMAIL_RULE_CREATED user=admin rule=forward_all
2024-01-15 03:10:22 SUCCESS_LOGIN user=jake ip=88.12.44.9
2024-01-15 03:10:25 EMAIL_RULE_CREATED user=jake rule=forward_all_external
"""

def analyze_logs(logs):
    fails = re.findall(r'FAILED_LOGIN user=(\w+) ip=([\d.]+)', logs)
    rules = re.findall(r'EMAIL_RULE_CREATED user=(\w+)', logs)
    success_logins = re.findall(r'(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) SUCCESS_LOGIN user=(\w+) ip=([\d.]+)', logs)

    print("=== SIEM Log Analysis — Alert Report ===\n")

    # Brute force detection
    fail_counts = Counter(u for u, _ in fails)
    for user, count in fail_counts.items():
        if count >= 3:
            print(f"[ALERT] Brute force detected: {user} ({count} failed attempts)")

    # Suspicious email rule creation (classic post-compromise SE indicator)
    for user in rules:
        print(f"[ALERT] Suspicious email rule created by: {user} (possible mailbox forwarding/exfil setup)")

    # Odd-hour login detection (00:00–05:00 = high-risk window)
    for date, time, user, ip in success_logins:
        hour = int(time.split(":")[0])
        if hour < 5:
            print(f"[ALERT] Odd-hour login: {user} at {time} from {ip} (outside normal business hours)")

    print("\n=== Analysis Complete ===")

analyze_logs(LOG_SAMPLE)