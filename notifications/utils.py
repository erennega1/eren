from django.core.mail import send_mail

def send_email_notification(subject, message, recipient):
    send_mail(
        subject,
        message,
        'noreply@yourdomain.com',
        [recipient],
        fail_silently=False,
    )