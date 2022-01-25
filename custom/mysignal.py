from django.db.models.signals import post_save
from django.dispatch import receiver
from custom.models import (
	Question, Answer
)
from django.core.mail import send_mail
from django.conf import settings

@receiver(post_save, sender=Question)
def create_question(sender, instance, created, **kwargs):
    if created:
        send_mail(
     		subject=f"{instance.student.email} - Ask {instance.title}",
		    message=instance.text,
		    from_email=settings.EMAIL_HOST_USER,
		    recipient_list=[settings.EMAIL_HOST_USER],
		    fail_silently=False
		 )


@receiver(post_save, sender=Answer)
def create_answer(sender, instance, created, **kwargs):
    if created:
        send_mail(
     		subject=f"{instance.mentor.email} - Answer {instance.question}",
		    message=instance.ans,
		    from_email=settings.EMAIL_HOST_USER,
		    recipient_list=[instance.student],
		    fail_silently=False
		 )