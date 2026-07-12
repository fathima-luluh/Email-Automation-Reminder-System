from src.email_sender import send_email


send_email(
    receiver="rahul@example.com",
    subject="Python Training Reminder",
    body="""
Hello Rahul,

Your Python Training is scheduled tomorrow.

Regards,
Automation System
""",
    dry_run=True
)