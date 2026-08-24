import datetime
import json

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

    if incident['type'] == 'vishing':
        actions += ["Flag caller ID/number", "Notify affected department",
                     "Review call logs for repeat attempts"]

    print("\nActions Taken:")
    for a in actions:
        print(f"  [x] {a}")

    report = {
        "incident": incident,
        "actions": actions,
        "timestamp": str(datetime.datetime.now())
    }

    filename = f"ir_report_{incident['type']}.json"
    with open(filename, "w") as f:
        json.dump(report, f, indent=2)
    print(f"\nIR report saved: {filename}")


ir_response({"type": "phishing", "severity": "HIGH", "user": "riya@sqrock.com"})
ir_response({"type": "vishing", "severity": "MEDIUM", "user": "ahmed@sqrock.com"})
ir_response({"type": "phishing", "severity": "CRITICAL", "user": "john@sqrock.com"})