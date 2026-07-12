from src.data_loader import (
    load_contacts,
    load_reminders,
    merge_data
)


contacts = load_contacts(
    "data/contacts.csv"
)


reminders = load_reminders(
    "data/reminders.csv"
)


final_data = merge_data(
    contacts,
    reminders
)


print(final_data)