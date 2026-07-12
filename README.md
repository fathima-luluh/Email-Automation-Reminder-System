\# 📧 Email Automation \& Reminder System



A Python-based automation system that generates and manages personalized reminder emails using CSV data. The application detects due reminders, generates email content from templates, simulates email delivery, and produces delivery reports.



\---



\## 🚀 Features



\* CSV-based contact and reminder management

\* Personalized email generation using templates

\* Automated reminder scheduling

\* Due-email detection system

\* Email simulation (Dry Run Mode)

\* Logging and report generation

\* Modular and scalable project structure



\---



\## 🛠️ Tech Stack



\* Python 3.12

\* Pandas

\* Schedule

\* Python-Dotenv

\* CSV

\* Git \& GitHub



\---



\## 📂 Project Structure



```text

Email-Automation-Reminder-System/

│

├── data/

│   ├── contacts.csv

│   └── reminders.csv

│

├── src/

│   ├── data\_loader.py

│   ├── template\_engine.py

│   ├── email\_generator.py

│   ├── due\_email\_generator.py

│   ├── email\_sender.py

│   ├── scheduler.py

│   ├── logger.py

│   └── report\_generator.py

│

├── templates/

│   └── email\_template.txt

│

├── logs/

├── outputs/

├── images/

├── main.py

├── requirements.txt

├── README.md

└── .gitignore

```



\---



\## ⚙️ Installation



\### Clone the Repository



```bash

git clone https://github.com/fathima-luluh/Email-Automation-Reminder-System.git

cd Email-Automation-Reminder-System

```



\### Create Virtual Environment



```bash

python -m venv venv

```



\### Activate Virtual Environment



\*\*Windows\*\*



```bash

venv\\Scripts\\activate

```



\### Install Dependencies



```bash

pip install -r requirements.txt

```



\---



\## ▶️ Run the Application



```bash

python main.py

```



\---



\## 📊 Sample Output



```text

EMAIL AUTOMATION \& REMINDER SYSTEM



\--- DRY RUN MODE ---

To: rahul@example.com

Subject: Automated Reminder



Hello Rahul,



This is a reminder for your upcoming Python Training.



Report saved: outputs/email\_report.csv



Automation completed successfully!

```



\---



\## 📸 Screenshots



Add screenshots inside the `images/` folder:



\* Project Structure

\* Main Execution

\* Generated Emails

\* Email Report

\* GitHub Repository



\---



\## 🔮 Future Enhancements



\* Real SMTP email sending

\* Streamlit dashboard

\* Email attachments support

\* Recurring reminders

\* Excel and PDF reports

\* Docker deployment



\---



\## 👩‍💻 Author



\*\*Fathima Luluh\*\*



GitHub: https://github.com/fathima-luluh



