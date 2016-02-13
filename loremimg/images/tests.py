from django.test import TestCase
from .models import Photo
from django.core.files import File
from PIL import Image
from django.db import IntegrityError
from rest_framework.test import APITestCase
import StringIO

class PhotoTests(TestCase):
    def setUp(self):
        Photo.objects.create(name="photo", category="PEOPLE",image=File(open("./test.png")))

    def test_Photo_members(self):
        photo = Photo.objects.get(name="photo")

        self.assertEqual(photo.name, "photo")
        self.assertEqual(photo.category, "PEOPLE")

    def test_Image(self):
        photo = Photo.objects.get(name="photo")
        im=Image.open(photo.image)
        self.assertEqual(im.size, (600, 300))

    def test_Uniqueness(self):
        with self.assertRaises(IntegrityError):
            Photo.objects.create(name="photo")

class PhotoAPITests(APITestCase):

    def setUp(self):
        Photo.objects.create(name="photo", category="PEOPLE",image=File(open("./test.png")))

    def test_Get_Image(self):
        response = self.client.get('/photo/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.has_header('content-type'))
        self.assertEqual(response._headers.get('content-type'), ('Content-Type', 'image/png'))

    def test_Get_Square(self):
        response = self.client.get('/200/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.has_header('content-type'))
        self.assertEqual(response._headers.get('content-type'), ('Content-Type', 'image/png'))

    def test_Get_Square_name(self):
        response = self.client.get('/200/photo/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.has_header('content-type'))
        self.assertEqual(response._headers.get('content-type'), ('Content-Type', 'image/png'))

    def test_Get_Rectangle(self):
        response = self.client.get('/200/100/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.has_header('content-type'))
        self.assertEqual(response._headers.get('content-type'), ('Content-Type', 'image/png'))

    def test_Get_Rectangle_name(self):
        response = self.client.get('/200/100/photo/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.has_header('content-type'))
        self.assertEqual(response._headers.get('content-type'), ('Content-Type', 'image/png'))

    def test_Get_Image_Fail(self):
        response = self.client.get('photo')
        self.assertEqual(response.status_code, 404)
