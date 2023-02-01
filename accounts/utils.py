from django.conf import settings
from django.core.mail import send_mail

#function to send email
def send_custom_email(receiver, subject, message):
    sender = settings.EMAIL_HOST_USER
    recipient_list = [receiver]
    
    send_mail(subject, message, sender, recipient_list)
    