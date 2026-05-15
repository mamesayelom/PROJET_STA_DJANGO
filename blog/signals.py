#fonction Django pour envoyer un mail
from .models import Entry
from django.db.models.signals import post_save
from django.dispatch import receiver



@receiver(post_save, sender=Entry)
def notifier_admin(sender, instance, created, **kwargs):

    if created:
        print("====================================")
        print("NOUVELLE ACTIVITÉ CRÉÉE")
        print(f"Titre : {instance.title}")
        print(f"Auteur : {instance.author}")
        print(f"Catégorie : {instance.category}")
        print("====================================")
        