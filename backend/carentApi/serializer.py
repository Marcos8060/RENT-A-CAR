from rest_framework import serializers
from .models import Profile, Car_Model, Comment
from django.contrib.auth.models import User

class Profile_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'profile_picture', 'name', 'location', 'email']


class User_Serializer(serializers.ModelSerializer):
    profile = Profile_Serializer(read_only=True)
    class Meta:
        model = User
        fields = ['id','username', 'profile', 'carModels']

class Comments_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','title', 'comment', 'carModel','user']

class Car_Model_Serializer(serializers.ModelSerializer):
    comment = Comments_Serializer(many=True)
    class Meta:
        model = Car_Model
        fields = ['id', 'name', 'model', 'human_cpty','luggage_cpty','hourly_rate', 'description','year','image', 'image_interior','image_rear', 'comment' ]
