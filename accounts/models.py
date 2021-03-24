from django.contrib import auth
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
# Create your models here.
from django.core.validators import RegexValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.cities import city



class Helper(models.Model):
    user = models.OneToOneField(User, unique=True, related_name='profile',on_delete=models.CASCADE)
    phone_regex = RegexValidator(regex=r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$')
    phone = models.CharField(validators=[phone_regex], max_length=17)
    STATUS = (
        ('Available', ('I am available to help.')),
        ('Not Available', ('Busy right now')),
    )
    availability = models.CharField(choices=STATUS, default='Available', max_length=222)
    Verification = (
        ('Yes', ('Verified.')),
        ('No', ('Not Verified')),
    )
    verified = models.CharField(choices=Verification, default='No', max_length=222)
    city = models.CharField(choices=city, default='Calgary',max_length=222)



    def __str__(self):
        return f'Helper: {self.user.username} Verified: {self.verified}'

    def save(self, *args, **kwargs):
        super().save(*args,**kwargs)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Helper.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):

        instance.profile.save()
