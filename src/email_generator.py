"""
Email Generator Module
----------------------
Creates personalized emails
from CSV data and templates.
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



def create_emails():

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


    for index, row in data.iterrows():

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