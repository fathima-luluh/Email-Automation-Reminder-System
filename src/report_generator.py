"""
Report Generator
Creates email delivery reports.
"""

import pandas as pd
from datetime import datetime
import os


def save_report(emails):

    os.makedirs(
        "outputs",
        exist_ok=True
    )

    report_data = []

    for email in emails:

        report_data.append(
            {
                "Name": email["name"],
                "Email": email["email"],
                "Status": "Simulated Sent",
                "Timestamp": datetime.now()
            }
        )

    report = pd.DataFrame(
        report_data
    )

    file_path = (
        "outputs/email_report.csv"
    )

    report.to_csv(
        file_path,
        index=False
    )

    return file_path