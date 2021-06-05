from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save

# Create your models here.
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='1.jpg')

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def save_profile(sender, **kwargs):
    if kwargs['created']:
        Profile.objects.create(user=kwargs['instance'])
# post_save.connect(save_profile, sender=User)
