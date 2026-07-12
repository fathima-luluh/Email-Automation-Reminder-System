"""
Data Loader Module
------------------
Reads contacts and reminder CSV files.
"""

import pandas as pd


def load_contacts(file_path):
    """
    Read contacts CSV file
    """

    contacts = pd.read_csv(file_path)

    return contacts



def load_reminders(file_path):
    """
    Read reminders CSV file
    """

    reminders = pd.read_csv(file_path)

    return reminders



def merge_data(contacts, reminders):
    """
    Combine contacts and reminders
    using name column
    """

    merged = pd.merge(
        contacts,
        reminders,
        on="name"
    )

    return merged