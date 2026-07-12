"""
Email Automation & Reminder System
----------------------------------
Main application runner.
"""

from src.due_email_generator import (
    create_due_emails
)
from src.email_sender import (
    send_email
)
from src.report_generator import (
    save_report
)


def main():

    print("=" * 60)
    print("EMAIL AUTOMATION & REMINDER SYSTEM")
    print("=" * 60)

    emails = create_due_emails()

    if len(emails) == 0:

        print("\nNo reminders are due.")

        return

    for email in emails:

        send_email(
            receiver=email["email"],
            subject="Automated Reminder",
            body=email["message"],
            dry_run=True
        )

    report = save_report(emails)

    print(
        f"\nReport saved: {report}"
    )

    print(
        "\nAutomation completed successfully!"
    )


if __name__ == "__main__":
    main()