"""
Due Email Generator
Creates emails only for reminders
whose date and time have arrived.
"""

from src.data_loader import (
    load_contacts,
    load_reminders,
    merge_data
)

from src.template_engine import (
    load_template,
    generate_email
)

from src.scheduler import is_due


def create_due_emails():

    contacts = load_contacts(
        "data/contacts.csv"
    )

    reminders = load_reminders(
        "data/reminders.csv"
    )

    data = merge_data(
        contacts,
        reminders
    )

    template = load_template(
        "templates/email_template.txt"
    )

    emails = []

    for _, row in data.iterrows():

        if is_due(
            str(row["date"]),
            str(row["time"])
        ):

            email_data = {
                "name": row["name"],
                "event": row["event"],
                "date": row["date"],
                "time": row["time"]
            }

            message = generate_email(
                template,
                email_data
            )

            emails.append(
                {
                    "name": row["name"],
                    "email": row["email"],
                    "message": message
                }
            )

    return emails