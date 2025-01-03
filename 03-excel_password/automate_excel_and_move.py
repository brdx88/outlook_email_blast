# notes for enhancement:
# ubah ftp_dir sesuai dengan bulan saat ini.
    # kalau engga ada perlu create

import os
import pandas as pd
import win32com.client as win32
from ftplib import FTP

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# Define needs
file_path = r"D:\OneDrive\Documents\Personals\08-Portfolios\03-excel_password\test_excel_password.xlsx"
input_file = os.path.abspath(file_path)  # Use absolute path
password = "securepassword123"

# df = pd.read_excel(input_file)
# n_rows = len(df)
# print(n_rows)

ftp_host = "192.168.98.78"  # FTP server address
ftp_username = "SHARE_FTP"  # FTP username
ftp_password = "SHARE_FTP"  # FTP password
ftp_dir = "/PDM/OUTPUT/APMK/LEAD/2025-01/"  # FTP directory to upload file

from_email = "brian.ivan@bni.co.id"  # Your office email address
email_password = "bF54j7zh6GiUlf"  # Your office email password
to_email = "brian.ic@outlook.com"  # The recipient's email address
subject = "TESTING SEND FTP FILE"
body = f"""
dear mba Dewi,
 
sehubungan dengan kebutuhan leads debit rutin, berikut kami berikan leads sesuai dengan kriteria yang sudah kami taruh di FTP: {ftp_dir}.
Leads tersebut berisikan: x rows of data. 

seperti biasa, password akan kami berikan secara terpisah.
 
atas perhatiannya, makasi mba Dewi....
"""

def encrypt_excel_file(input_file, password):
    # Use pywin32 to set a password on the Excel file
    excel = win32.gencache.EnsureDispatch("Excel.Application")
    excel.Visible = False  # Run Excel in the background

    # Check if the file exists
    if not os.path.exists(input_file):
        print(f"Error: The file '{input_file}' does not exist.")
        return None

    workbook = excel.Workbooks.Open(input_file)
    encrypted_file = input_file.replace(".xlsx", "_protected.xlsx")

    workbook.Password = password  # Set the password
    workbook.SaveAs(encrypted_file, FileFormat=51)  # FileFormat=51 for .xlsx files
    workbook.Close()
    excel.Quit()
    print(f"Encrypted file saved at {encrypted_file}")
    return encrypted_file


def upload_to_ftp(local_file, remote_path, ftp_host, ftp_username, ftp_password):
    # Connect to FTP
    ftp = FTP(ftp_host)
    ftp.login(ftp_username, ftp_password)
    
    # Change to the target directory
    ftp.cwd(remote_path)
    
    # Open the local file and upload it
    with open(local_file, 'rb') as file:
        ftp.storbinary(f"STOR {os.path.basename(local_file)}", file)

    print(f"File {local_file} uploaded to {remote_path} on FTP server.")
    ftp.quit()

def send_email(subject, body, to_email, attachment_path=None):
    # Office SMTP server settings
    smtp_server = "smtp.office365.com"
    smtp_port = 587
    
    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    
    # Add the body of the email
    msg.attach(MIMEText(body, 'plain'))
    
    # Add an attachment if provided
    if attachment_path:
        with open(attachment_path, "rb") as attachment:
            attach_file = MIMEApplication(attachment.read(), _subtype="xlsx")
            attach_file.add_header('Content-Disposition', 'attachment', filename=attachment_path)
            msg.attach(attach_file)
    
    try:
        # Set up the server and send the email
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Secure connection
        server.login(from_email, email_password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")

def send_email_with_outlook(recipient, subject, body, attachment_path=None):
    try:
        # Create an instance of Outlook
        outlook = win32.Dispatch("Outlook.Application")
        mail = outlook.CreateItem(0)  # Create a new email

        # Set email properties
        mail.To = recipient
        mail.Subject = subject
        mail.Body = body

        # Add attachment if provided
        if attachment_path and os.path.exists(attachment_path):
            mail.Attachments.Add(attachment_path)

        # Send the email
        mail.Send()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")


# Encrypt the file
encrypted_file = encrypt_excel_file(input_file, password)

# # Clean up the original file (optional)
# if encrypted_file:
#     os.remove(input_file)

# Upload the file to FTP if encryption succeeded
if encrypted_file:
    upload_to_ftp(encrypted_file, ftp_dir, ftp_host, ftp_username, ftp_password)
    # send_email(subject, body, to_email)
    send_email_with_outlook(to_email, subject, body)