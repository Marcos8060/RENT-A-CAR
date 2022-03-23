from django.shortcuts import render
from .serializer import Profile_Serializer, Car_Model_Serializer, User_Serializer
from rest_framework import viewsets,permissions
from .models import Profile, Car_Model
from django.contrib.auth.models import User


class Profile_viewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = Profile_Serializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
