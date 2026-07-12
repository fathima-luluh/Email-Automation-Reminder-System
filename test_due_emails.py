from src.due_email_generator import create_due_emails

emails = create_due_emails()

print("Due Emails:", len(emails))

for email in emails:
    print(email["email"])