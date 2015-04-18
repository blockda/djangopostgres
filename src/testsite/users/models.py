# Define a custom User class to work with django-social-auth
from django.contrib.auth.models import AbstractUser
from django.db import models

#user profile code from http://www.lucas-dev.com/blog/entry/psa-full-example.html

class CustomUser(AbstractUser):
    pass

class UserProfile(models.Model):
	user = models.OneToOneField(CustomUser)
	photo = models.TextField()
