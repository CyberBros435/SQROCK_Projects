def spear_phish_template(target):
    return f"""
From : it-support@{target['company'].lower()}.com
To : {target['email']}
Subject : Action Required: Your {target['company']} account will be disabled

Hi {target['name']},

Our security team noticed a login from {target['location']}. 
Please verify your account within 24 hours to avoid suspension.

[Verify Account] -> https://lab.internal

Regards,
IT Security Team
"""

targets = [
    {"name": "Riya Sharma", "email": "riya@company.com", "company": "Sqrock", "location": "Bangalore, India"},
    {"name": "Ahmed Khan", "email": "ahmed@company.com", "company": "Sqrock", "location": "Karachi, Pakistan"},
    {"name": "John Miller", "email": "john@company.com", "company": "Sqrock", "location": "London, UK"}
]

for t in targets:
    print(spear_phish_template(t))
