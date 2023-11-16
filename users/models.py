from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.conf import settings


# Profile Model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='users/', blank=True, null=True)

    def __str__(self):
        return self.user.username

    @property
    def user_picture(self):
        if self.profile_picture:
            url = self.profile_picture.url
        else:
            url = (
                settings.STATIC_URL +
                'images/users/user-placeholder.jpeg’
            )
        return url

# Profile creation on new Signup
def create_profile(sender,instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

post_save.connect(create_profile, sender=User)
