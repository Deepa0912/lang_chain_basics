import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from secret import sender_email, app_password, receiver_email
def send_email(subject, message):
    try:
        # Create email
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject

        msg.attach(MIMEText(message, 'plain'))

        # Connect to Gmail server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()

        # Login
        server.login(sender_email, app_password)

        # Send email
        server.send_message(msg)

        print("Email sent successfully!")

    except Exception as e:
        print("Error:", e)

    finally:
        server.quit()

