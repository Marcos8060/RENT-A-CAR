from django.db import models
from django.contrib.auth.models import User
from django.forms import IntegerField
from pyuploadcare.dj.models import ImageField
from django.dispatch import receiver
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(upload_to='images/', default='default.png')
    name = models.CharField(blank=True, max_length=120)
    location = models.CharField(max_length=60, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    
    def __str__(self):
        return self.user.username

    @receiver(post_save,sender=user)
    def create_profile(sender, instance, created, **kwargs):
        if created:
          Profile.objects.create(user=instance)

    @receiver(post_save,sender=user)
    def save_profile(sender, instance, **kwargs):
        instance.profile.save()

class Car_Model(models.Model):
    name = models.CharField(max_length=150)
    model = models.CharField(max_length=150)
    human_cpty = models.CharField(max_length=150)
    luggage_cpty = models.CharField(max_length=150)
    hourly_rate  = IntegerField()
    description = models.TextField(max_length=700)
    year= IntegerField()
    image =ImageField(blank=True)
    image_interior =ImageField(blank=True)
    image_rear =ImageField(blank=True)

    def __str__(self):
        return self.title

    def save_post(self):
        self.save()    

    def delete_post(self):
        self.delete()

    @classmethod
    def search_project(cls, title):
        return cls.objects.filter(title__icontains=title).all()

    @classmethod
    def all_posts(cls):
        return cls.objects.all()



       