"""
Logging Module
--------------
Tracks email automation activity.
"""

import logging
import os


# Create logs folder if not exists

os.makedirs(
    "logs",
    exist_ok=True
)


logging.basicConfig(
    filename="logs/email_activity.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)



def log_success(email):

    logging.info(
        f"Email sent successfully to {email}"
    )



def log_failure(email, error):

    logging.error(
        f"Email failed for {email} - {error}"
    )
