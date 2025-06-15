from django.conf import settings
from django.core.mail import send_mail


def send_email_confirm(url, email):
    send_mail(
        subject="Подтвержение регистрации на сайте StudyMate",
        message=f"Для подтверждения регистрации, перейдите по ссылке {url}",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email],
    )
