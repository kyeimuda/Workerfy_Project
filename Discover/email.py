# This module handles emails and their contents to be sent

from django.core.mail import send_mail
from django.conf import settings
from .models import WorkerfyUser

def send_verification_email(user):
    verification_code = user.verification_code
    verification_link = f"{settings.SITE_URL}/intro/verification_by_email.html"
    subject = 'Verify your email address'
    message = f" Hi [User's Name], \n\n Congratulations on joining Workerfy! We’re thrilled to have you as part of our community of skilled tradespeople and clients. \n\n\
    This is your verification code: {verification_code}\n\n\
    To complete your setup, please {verification_link}(#) to verify your account. Copy the code provided on the linked page and enter it back into your profile to activate your account.\n\n\
    Welcome aboard, and here’s to connecting with new clients and growing your business!\n\n\
    Best,\n\
    The Workerfy Team\n"
    from_email = settings.DEFAULT_FROM_EMAIL
    print(user.email)
    recipient_list = [user.email]
    send_mail(subject, message, from_email, recipient_list)

    return None
