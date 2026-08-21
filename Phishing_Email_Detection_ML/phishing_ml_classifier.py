import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report

# 50-sample labeled dataset (1=phishing, 0=legit)
emails = [
    "Verify your account now or it will be suspended",
    "Click here to claim your prize immediately",
    "Urgent: update your bank details to avoid closure",
    "Your PayPal account has been limited, verify now",
    "Confirm your identity within 24 hours or lose access",
    "Congratulations! You've won a free iPhone, claim here",
    "Your password will expire, click to reset immediately",
    "Action required: unusual login detected on your account",
    "Your package delivery failed, update payment info now",
    "Security alert: verify your Apple ID immediately",
    "You have a pending refund, click to claim",
    "Your subscription will be cancelled, update billing now",
    "Final notice: your account will be suspended today",
    "Click here to unlock your frozen bank account",
    "Verify your email to avoid permanent deletion",
    "Your tax refund is ready, verify your details",
    "Urgent: suspicious activity detected, act now",
    "Your Netflix payment failed, update card immediately",
    "Claim your inheritance now, urgent response needed",
    "Your account has been compromised, reset password now",
    "You've been selected for a cash prize, verify to claim",
    "Update your Microsoft account or lose access today",
    "Your Amazon order requires verification, click now",
    "Immediate action needed: your invoice is overdue",
    "Verify now to avoid account termination",
    "Team standup at 3pm, agenda attached",
    "Your invoice for Q2 is ready for review",
    "Meeting notes from yesterday's call",
    "Lunch tomorrow? Let me know your availability",
    "Project deadline moved to next Friday",
    "Please review the attached quarterly report",
    "Reminder: submit your timesheet by end of day",
    "Happy birthday! Hope you have a great day",
    "Can you send me the updated slides?",
    "Thanks for your help on the presentation",
    "The office will be closed for the holiday",
    "New employee handbook is now available",
    "Weekly newsletter: company updates and news",
    "Your order has shipped, tracking info attached",
    "Conference call rescheduled to 2pm",
    "Draft contract attached for your review",
    "Welcome to the team! Onboarding info inside",
    "Your subscription receipt for this month",
    "Feedback requested on the new design mockups",
    "Reminder: performance review scheduled next week",
    "Server maintenance scheduled this weekend",
    "Your flight itinerary for next week's trip",
    "Q3 budget planning meeting notes",
    "Please find attached the signed agreement",
    "Client call summary and next steps",
]

labels = [1]*25 + [0]*25  # first 25 phishing, last 25 legit

# Split for proper evaluation
X_train, X_test, y_train, y_test = train_test_split(
    emails, labels, test_size=0.2, random_state=42, stratify=labels
)

pipe = Pipeline([
    ("vec", CountVectorizer()),
    ("clf", MultinomialNB()),
])

pipe.fit(X_train, y_train)
y_pred = pipe.predict(X_test)

# Evaluation
acc = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)
report = classification_report(y_test, y_pred, target_names=["Legit", "Phishing"])

print(f"Accuracy: {acc*100:.2f}%\n")
print("Confusion Matrix:")
print(pd.DataFrame(cm, index=["Actual Legit", "Actual Phishing"], columns=["Pred Legit", "Pred Phishing"]))
print(f"\nClassification Report:\n{report}")

# Live test on new unseen examples
print("\n--- New Predictions ---")
tests = [
    "Please verify your PayPal login",
    "Meeting notes from yesterday",
    "Your account will be locked, click here now",
    "Can we reschedule our 1:1?",
]
for t in tests:
    pred = pipe.predict([t])[0]
    print(f"{'PHISHING' if pred else 'LEGIT'}: {t}")