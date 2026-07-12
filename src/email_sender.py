"""
Email Sender Module
-------------------
Handles email sending.
Supports dry-run testing.
"""

from email.message import EmailMessage
import smtplib
import os

from dotenv import load_dotenv

from src.logger import (
    log_success,
    log_failure
)


load_dotenv()



def send_email(
        receiver,
        subject,
        body,
        dry_run=True
):

    """
    Send email or simulate sending
    """

    try:

        if dry_run:

            print("\n--- DRY RUN MODE ---")

            print(
                f"To: {receiver}"
            )

            print(
                f"Subject: {subject}"
            )

            print(body)

            print(
                "--- EMAIL SIMULATED ---\n"
            )


            log_success(receiver)

            return True



        # Real SMTP sending

        msg = EmailMessage()

        msg["From"] = os.getenv(
            "EMAIL_ADDRESS"
        )

        msg["To"] = receiver

        msg["Subject"] = subject


        msg.set_content(body)



        with smtplib.SMTP(
            os.getenv("SMTP_SERVER"),
            int(os.getenv("SMTP_PORT"))
        ) as server:


            server.starttls()


            server.login(
                os.getenv("EMAIL_ADDRESS"),
                os.getenv("EMAIL_PASSWORD")
            )


            server.send_message(msg)



        log_success(receiver)

        return True



    except Exception as e:


        log_failure(
            receiver,
            str(e)
        )


        return False