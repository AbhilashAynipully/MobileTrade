from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Profile Model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='user-placeholder.jpeg', upload_to='profile_pics')

    def __str__(self):
        return self.user.username


# Profile creation on new Signup
def create_profile(sender,instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

post_save.connect(create_profile, sender=User)
