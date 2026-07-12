from src.email_generator import create_emails


emails = create_emails()


for email in emails:

    print("=" * 50)

    print("TO:", email["email"])

    print(email["message"])