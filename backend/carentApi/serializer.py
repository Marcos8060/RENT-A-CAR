from rest_framework import serializers
from .models import Profile, Car_Model, Comment
from django.contrib.auth.models import User

class Profile_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'profile_picture', 'name', 'location', 'email']
