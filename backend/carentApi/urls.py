from django import views
from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('profile', views.Profile_viewSet)
router.register('car_models', views.CarModel_viewSet)
router.register('car_models/<int:pk>', views.Car_details_viewSet)
router.register('users', views.User_viewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    


]