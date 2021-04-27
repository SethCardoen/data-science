from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #each user can only have one profile
    bio = models.TextField(default="no biography") # add a textfield to type your biography
    avatar = models.ImageField(upload_to='avatars', default='no_picture.png') # add an image of your avatar 
    created = models.DateTimeField(auto_now=True) # add a date and time of the creation of the user
    updated = models.DateTimeField(auto_now=True) # add the date and time from the update 

    def __str__(self): #define a function to output a string, self to represent an instance
        return f"Profile of {self.user.username}"
