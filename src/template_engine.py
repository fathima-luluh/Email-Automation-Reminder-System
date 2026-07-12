"""
Template Engine
---------------
Loads email templates and creates personalized messages.
"""


def load_template(template_path):
    """
    Read email template file
    """

    with open(template_path, "r", encoding="utf-8") as file:
        template = file.read()

    return template



def generate_email(template, data):
    """
    Replace placeholders with actual values
    """

    message = template.format(
        name=data["name"],
        event=data["event"],
        date=data["date"],
        time=data["time"]
    )

    return message