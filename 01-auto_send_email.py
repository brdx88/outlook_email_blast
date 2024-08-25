import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Variables for personalization
ceo_name = "John Doe"
company_name = "TechCorp"
ceo_email = "testing@gmail.com"
title_email = f"Excited to Explore a Part-Time Remote Opportunity at {company_name}"

# Your Outlook email credentials
outlook_user = "yourmail@outlook.com"
outlook_password = "yourpassword"


# Function to send an email
def send_email(to_email, subject, body):
    # Create a MIMEMultipart object
    msg = MIMEMultipart()
    msg['From'] = outlook_user
    msg['To'] = to_email
    msg['Subject'] = subject
    
    # Attach the body of the email
    msg.attach(MIMEText(body, 'html'))
    
    # Connect to the Outlook SMTP server
    server = smtplib.SMTP('smtp-mail.outlook.com', 587)
    server.starttls()  # Secure the connection
    server.login(outlook_user, outlook_password)
    
    # Send the email
    server.sendmail(outlook_user, to_email, msg.as_string())
    server.quit()
    
    print(f"Email sent successfully to '{to_email}'.")

# Email content
email_body = f"""
<html>
<body>
    <p>Hi {ceo_name},</p>
    <br>
    <p>I hope you're doing well 😁</p>
    <p>I'm passionate about helping companies like {company_name} harness the power of data to drive innovation. 
    With <b>over 4 years of experience</b> as a <b>Python Developer</b> specializing in <b>data analytics</b>, 
    I've helped transform complex data into actionable insights, optimize performance metrics, 
    and <b>automate processes—resulting</b> in <b>better decision-making</b> and <b>significant productivity gains</b> in the banking and finance industries.</p>

    <p>I believe my skills in <b>Python, SQL, Tableau, and web development (HTML, CSS, JS, Flask, Django, etc)</b> could be a great fit for your team. 
    I'm available to contribute 2-3 hours a day on a part-time, remote basis, and I'd love the chance to support {company_name}'s growth.</p>

    <p>If this sounds like a good fit, I'd be happy to chat more! 
    In the meantime, I've attached my portfolio and GitHub for you to check out.</p>

    <p>Looking forward to hearing from you.</p>
    <br>
    
    <p>Best regards,</p>
    <p>Brian Cusuanto</p>
    <br>
    <a href="https://www.linkedin.com/in/brianic">Brian IC on LinkedIn</a> | <a href="https://github.com/brdx88">Brian IC on GitHub</a>
</body>
</html>
"""

# Send the email
send_email(ceo_email, title_email, email_body)
