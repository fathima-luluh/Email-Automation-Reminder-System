from src.template_engine import load_template, generate_email


template = load_template(
    "templates/email_template.txt"
)


data = {
    "name": "Rahul",
    "event": "Python Training",
    "date": "2026-07-15",
    "time": "10:00"
}


email = generate_email(template, data)


print(email)