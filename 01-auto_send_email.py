import csv
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# # Variables for personalization
# ceo_name = "John Doe"
# company_name = "TechCorp"
# ceo_email = "testing@gmail.com"

# Your Outlook email credentials
# outlook_user = "yourmail@outlook.com"
# outlook_password = "yourpassword"



# Function to send an email
def send_email(to_email, subject, body, attachment_path=None):
    """
    Sends an email to a specified recipient using Outlook SMTP server.

    Args:
        to_email (str): The recipient's email address.
        subject (str): The subject of the email.
        body (str): The body of the email in HTML format.

    Returns:
        None
    """
    
    # Create a MIMEMultipart object
    msg = MIMEMultipart()
    msg['From'] = outlook_user
    msg['To'] = to_email
    msg['Subject'] = subject
    
    # Attach the email body
    msg.attach(MIMEText(body, 'html'))
    
    # Attach a file if provided
    if attachment_path:
        with open(attachment_path, 'rb') as attachment:
            part = MIMEApplication(attachment.read(), _subtype="pdf")
            part.add_header('Content-Disposition', 'attachment', filename=attachment_path)
            msg.attach(part)
    
    # Connect to the Outlook SMTP server
    server = smtplib.SMTP('smtp-mail.outlook.com', 587)
    server.starttls()
    server.login(outlook_user, outlook_password)
    
    # Send the email
    server.sendmail(outlook_user, to_email, msg.as_string())
    server.quit()
    
    print(f"Email sent successfully to '{to_email}'.")

# Function to update the CSV with flag after sending email
def update_csv(recipients, filename='00-email_list.csv'):
    """
    Updates a CSV file with the provided recipients.

    Args:
        recipients (list): A list of dictionaries containing the recipient information.
        filename (str): The name of the CSV file to update. Defaults to '00-email_list.csv'.

    Returns:
        None
    """
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['email', 'ceo_name', 'company_name', 'flag']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(recipients)

    print("CSV file updated successfully.")

# Read the CSV file
recipients = []
with open('00-email_list.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Only process rows where the flag is not set to "sent"
        recipients.append(row)

print(recipients)

# Loop through each recipient, send email, and update flag
for recipient in recipients:
    if recipient['flag'] != 'sent':
        
        # Email content
        email_body = f"""
        <html>
        <body>
            <p>Hi {recipient['ceo_name']},</p>
            <br>
            <p>I hope you're doing well 😁</p>
            <p>I'm passionate about helping companies like {recipient['company_name']} turn data into actionable insights that drive innovation. 
            With <b>over 4 years of experience</b> as a <b>Python Developer</b> specializing in <b>data analytics</b>, 
            I've helped transform complex data into actionable insights, optimize performance metrics, 
            and <b>automate processes—resulting</b> in <b>better decision-making</b> and <b>significant productivity gains</b> in the banking and finance industries.</p>

            <p>I believe my skills in <b>Python, SQL, Tableau, and web development (HTML, CSS, JS, Flask, Django, etc)</b> could be a great fit for your team. 
            I'm available to contribute 2-3 hours a day on a part-time, remote basis, and I'd love the chance to support {recipient['company_name']}'s growth.</p>

            <p>If this sounds like a good fit, I'd be happy to chat more! 
            In the meantime, I've attached my portfolio, GitHub, and resume for you to check out.</p>

            <p>Looking forward to hearing from you.</p>
            <br>
            
            <p>Best regards,</p>
            <p>Brian Cusuanto</p>
            <br>
            <a href="https://www.linkedin.com/in/brianic">Brian IC on LinkedIn</a> | <a href="https://github.com/brdx88">Brian IC on GitHub</a>
        </body>
        </html>
        """

        try:
            send_email(
                to_email = recipient['email'], 
                subject = f"Excited to Explore a Part-Time Remote Opportunity at {recipient['company_name']}", 
                body = email_body,
                attachment_path="Resume of Brian IC - 202408.pdf"
                       )
            
            # Mark the recipient as sent
            recipient['flag'] = 'sent'
            
            # Delay between emails
            print("Starting to email next recipient in 5 seconds ....")
            time.sleep(5)  # 5 seconds delay, adjust as needed
            
            
        except Exception as e:
            print(f"Failed to send email to {recipient['email']}: {str(e)}")
            continue

# Update the CSV with the new flag status
update_csv(recipients)