import smtplib
from email.mime.text import MIMEText

def send_email():
    sender = 'keer10122003@gmail.com'
    receiver = 'keerthi.ec21@sahyadri.edu.in'
    msg = MIMEText('Hello, this is a test email.')
    msg['Subject'] = 'Test Email'
    msg['From'] = sender
    msg['To'] = receiver

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender, "Kiyokiyo31.")
        server.sendmail(sender, receiver, msg.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {str(e)}")
