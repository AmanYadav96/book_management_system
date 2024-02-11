from icalendar import Calendar, Event
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
# from patient.models import Patient
# from doctor.models import Doctor
# from employee.models import Employee
from bs4 import BeautifulSoup  
from pathlib import Path
# from hospital.models import Hospital

smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_username = "achieversgrand@gmail.com"
smtp_password = "bpfhbemqsenjkqud"
from_email = "achieversgrand@gmail.com"
BASE_DIR = Path(__file__).resolve().parent.parent


def send_verification_email(url, user_email):
    html_content = ""

    try:
        with open(BASE_DIR/'templates/verification.html', 'r') as file:
            html_content = file.read()
    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")

    new_url = url
    soup = BeautifulSoup(html_content, 'html.parser')
    a_tag = soup.find('a')

    if a_tag:
        a_tag['href'] = new_url

    html_content = str(soup)

    url_element = soup.find(id='url')
    if url_element:
        url_element['href'] = new_url
    html_content = str(soup)

    img_element = soup.find(id='logo-img')
    new_src = "https://hospital0000.s3.ap-south-1.amazonaws.com/Screenshot_2023-12-19_163258__1_-removebg-preview.png"
    if img_element:
        img_element['src'] = new_src
    html_content = str(soup)

    message = MIMEMultipart("alternative")
    message["Subject"] = "Verification Email"
    message["From"] = from_email
    message["To"] = user_email
    to_email = user_email
    # Attach HTML content
    html_part = MIMEText(html_content, "html")
    message.attach(html_part)
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(from_email, to_email, message.as_string())
    print('Sent mail')
    server.quit()
