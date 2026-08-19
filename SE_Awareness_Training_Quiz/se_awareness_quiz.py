import json
from datetime import datetime

QUESTIONS = [
    {"q": "An email asks you to verify your password via a link. You should:",
     "opts": ["A) Click the link", "B) Call IT directly", "C) Reply with password"],
     "ans": "B", "exp": "Always verify via official channels, never click email links."},

    {"q": "You find a USB drive in the parking lot. You should:",
     "opts": ["A) Plug it in to check", "B) Hand to security", "C) Keep it"],
     "ans": "B", "exp": "USB drops are a classic baiting attack vector."},

    {"q": "A caller claims to be IT and asks for your password to 'fix an issue'. You should:",
     "opts": ["A) Give it, they're IT", "B) Refuse and report the call", "C) Give a fake password"],
     "ans": "B", "exp": "Legitimate IT never asks for your password over the phone."},

    {"q": "You get a text saying your bank account is locked, with a link to 'unlock' it. You should:",
     "opts": ["A) Click the link immediately", "B) Ignore and call your bank directly", "C) Forward to friends"],
     "ans": "B", "exp": "This is smishing — verify via the bank's official app/number, never the link."},

    {"q": "A new coworker you've never met asks you to hold the door (no badge). You should:",
     "opts": ["A) Hold the door, be polite", "B) Ask them to badge in separately", "C) Ignore them"],
     "ans": "B", "exp": "Tailgating bypasses physical access control — always require individual badge-in."},

    {"q": "An 'urgent' email from your CEO asks you to buy gift cards immediately. You should:",
     "opts": ["A) Buy them right away", "B) Verify via a separate known channel first", "C) Reply asking for more details"],
     "ans": "B", "exp": "CEO fraud/BEC relies on urgency + authority. Always verify via phone/known channel."},

    {"q": "A website login page has a URL like 'paypal-secure-login.xyz'. This is:",
     "opts": ["A) Normal, PayPal uses many domains", "B) Likely a phishing domain", "C) Safe because it says 'secure'"],
     "ans": "B", "exp": "Legit PayPal only uses paypal.com — keyword stuffing + odd TLD is a phishing indicator."},

    {"q": "You receive an email with an unexpected invoice attachment (.zip) from an unknown sender. You should:",
     "opts": ["A) Open it to check", "B) Delete/report without opening", "C) Forward to a coworker to check"],
     "ans": "B", "exp": "Unexpected attachments are a common malware delivery method — never open blindly."},

    {"q": "Someone on LinkedIn you don't know asks detailed questions about your company's internal tools. You should:",
     "opts": ["A) Answer to be helpful", "B) Decline and report if suspicious", "C) Ask a colleague to answer instead"],
     "ans": "B", "exp": "This is OSINT-gathering/pretexting — oversharing internal details enables future SE attacks."},

    {"q": "MFA (Multi-Factor Authentication) protects against credential theft because:",
     "opts": ["A) It makes passwords longer", "B) It requires a second proof of identity beyond password", "C) It blocks all phishing emails"],
     "ans": "B", "exp": "Even if a password is stolen, MFA blocks login without the second factor."},
]

def run_quiz():
    score = 0
    results = []

    for i, q in enumerate(QUESTIONS, 1):
        print(f"\nQ{i}: {q['q']}")
        for o in q['opts']:
            print(f"  {o}")
        ans = input("Your answer (A/B/C): ").strip().upper()

        correct = (ans == q['ans'])
        if correct:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong. {q['exp']}")

        results.append({
            "question": q['q'],
            "your_answer": ans,
            "correct_answer": q['ans'],
            "correct": correct
        })

    print(f"\nScore: {score}/{len(QUESTIONS)}")

    report = {
        "timestamp": str(datetime.now()),
        "score": score,
        "total": len(QUESTIONS),
        "percentage": round((score / len(QUESTIONS)) * 100, 1),
        "answers": results
    }

    with open("quiz_score_report.json", "w") as f:
        json.dump(report, f, indent=2)
    print("Score report saved to quiz_score_report.json")

run_quiz()