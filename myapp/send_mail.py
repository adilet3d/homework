from django.core.mail import EmailMessage
from django.conf import settings

def send_msg(email,username):
    mail=EmailMessage(
        'Hello',
        f'Hello   {username}, Thanks for registration',
        settings.EMAIL_HOST_USER,
        [email]
    )
    mail.send()