from model1.models import Student
import time
from django.core.mail import send_mail , EmailMessage
from django.conf import settings


def run_this_func():
    print("Start execution")
    time.sleep(1)
    print("Execution completed")



def sent_email_to_user():
    subject = "This email is from django server"
    message = "This is a test message from django server email"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ["gopalbera6335@gmail.com"]

    try:
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        print("Email sent successfully")
    except Exception as e:
        print(f"Error sending email: {e}")


def send_email_with_attachment(subject , message , recipient_list , file_path):
    mail = EmailMessage(subject = subject , body = message ,
                        from_email = settings.EMAIL_HOST_USER , to = recipient_list)
    mail.attach_file(file_path)
    mail.send()