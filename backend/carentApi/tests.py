from urllib.request import CacheFTPHandler
from django.test import TestCase

from .models import *

class TestProfile(TestCase):
    def setUp(self):
        self.user = User(id=1, username='Prime', password='123qwerty')
        self.user.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))

    def test_save_user(self):
        self.user.save()

    def test_delete_user(self):
        self.user.delete()

class TestCarModel(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='Prime')
        self.carModel = Car_Model.objects.create(id=1, name= 'Mercedece G-wagon', model='Mercedece', human_cpty='5 persons',
                     luggage_cpty='200kg', hourly_rate='5000' , description= 'The Mercedes-Benz G-Class, in American English sometimes called G-Wagon, is a four-wheel drive automobile manufactured by Magna Stey', year='2021', image='test_img1.png', image_interior='test_img2.png', image_rear='test_img3.png')
    def test_instance(self):
        self.assertTrue(isinstance(self.carModel, Car_Model))

    def test_save_carModel(self):
        self.carModel.save_carModel()
        carModel = Car_Model.objects.all()
        self.assertTrue(len(carModel) > 0)

    def test_get_carModel(self):
        self.carModel.save()
        carModels = Car_Model.all_carModels()
        self.assertTrue(len(carModels) > 0)

    def test_search_carModel(self):
        self.carModel.save()
        carModel = Car_Model.search_carModel('Mercedece')
        self.assertTrue(len(carModel) > 0)

    def test_delete_carModel(self):
        self.carModel.delete_carModel()
        carModel = Car_Model.search_project('test')
        self.assertTrue(len(carModel) < 1)
