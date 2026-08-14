def generate_vishing_script(target_company, attacker_role, pretext):
    script = f"""
=== VISHING AWARENESS SCRIPT ===
Caller Role : {attacker_role}
Target Org  : {target_company}
Pretext     : {pretext}

[OPENER]
'Hi, this is Alex from IT Support at {target_company}.
We detected unusual activity on your account.'

[HOOK]
'I need to verify your identity — can you confirm
your employee ID and current password?'

[RED FLAG for Awareness]
-> Legitimate IT will NEVER ask for passwords.
-> Always verify via official internal channels.
"""
    return script

print(generate_vishing_script("Sqrock IT", "IT Support", "Password Reset"))
print(generate_vishing_script("National Bank", "Bank Fraud Dept", "Suspicious Transaction Alert"))
print(generate_vishing_script("Tax Authority", "Government Official", "Unpaid Tax Warning"))



