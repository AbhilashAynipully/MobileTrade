from django.db import models
from django_resized import ResizedImageField
from django.contrib.auth.models import User
from django.conf import settings
from users.models import Profile

class Mobile(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    colour = models.CharField(max_length=20, null=True, blank= True)
    memory = models.CharField(max_length=20, null=True, blank= True)
    price = models.IntegerField()
    added_time = models.DateTimeField(auto_now_add=True)
    comments = models.TextField(blank=True, null=True)
    mobile_pic1 = ResizedImageField(upload_to='mobiles/',blank=True)
    mobile_pic2 = ResizedImageField(upload_to='mobiles/', blank=True)
    mobile_pic3 = ResizedImageField(upload_to='mobiles/', blank=True)
    mobile_pic4 = ResizedImageField(upload_to='mobiles/', blank=True)
    
    def __str__(self):
        return f'{self.brand} + {self.model}'

    @property
    def default_picture(self):
        if self.mobile_pic1:
            url = self.mobile_pic_1.url
        else:
            url = (
                settings.STATIC_URL +
                'images/mobile-placeholder.jpeg'
            )
        return url


