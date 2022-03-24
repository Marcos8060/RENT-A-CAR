from turtle import title
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
    human_cpty = models.IntegerField()
    luggage_cpty = models.IntegerField()
    hourly_rate  = models.IntegerField()
    description = models.TextField(max_length=700)
    year= models.DateField()
    image =models.ImageField(upload_to='images/', default='default.png')
    image_interior =models.ImageField(upload_to='images/', default='default.png')
    image_rear =models.ImageField(upload_to='images/', default='default.png')

    def __str__(self):
        return self.name

    def save_carModel(self):
        self.save()    

    def delete_carModel(self):
        self.delete()

    @classmethod
    def search_carModel(cls, title):
        return cls.objects.filter(title__icontains= 'model').all()

    @classmethod
    def all_carModels(cls):
        return cls.objects.all()


class Comment(models.Model):
    title = models.CharField(max_length=150)
    comment = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    carModel = models.ForeignKey(Car_Model, on_delete=models.CASCADE, null=True, related_name='comment')

    def save_comments(self):
        self.save()

    @classmethod
    def get_comments(cls, id):
        comments= Comment.objects.filter(post_id=id).all()
        return comments
    
    def __str__(self):
        return self.comment
   