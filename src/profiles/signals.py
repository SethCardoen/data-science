from .models import Profile
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User) # defining that we send from User to the post_save
def post_save_create_profile(sender, instance, created, **kwargs):  # **kwargs is because we don't know how many elements we will import
    print(sender)
    print(instance)
    print(created)
    if created:
        Profile.objects.create(user=instance)  
