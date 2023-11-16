from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.conf import settings


# Profile Model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
  

    def __str__(self):
        return self.user.username

# Profile creation on new Signup
def create_profile(sender,instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

post_save.connect(create_profile, sender=User)
