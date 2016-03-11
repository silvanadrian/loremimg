from django.test import TestCase
from .models import Photo
from django.core.files import File
from PIL import Image
from django.db import IntegrityError
from rest_framework.test import APITestCase
from django.core.files.uploadedfile import SimpleUploadedFile
import os

class PhotoTests(TestCase):
    def setUp(self):
        script_dir = os.path.dirname(__file__)
        Photo.objects.create(name="photo", category="PEOPLE",
        image = SimpleUploadedFile(name='test.png', content=open(script_dir + "/test.png", 'rb').read(), content_type='image/png'))

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
        script_dir = os.path.dirname(__file__)
        Photo.objects.create(name="photo", category="people",
        image = SimpleUploadedFile(name='test.png', content=open(script_dir + "/test.png", 'rb').read(), content_type='image/png'))

    def get_random_Image(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.has_header("content-type"))
        self.assertEqual(response._headers.get("content-type"), ("Content-Type", "image/png"))

    def test_Get_Image(self):
        response = self.client.get("/photo/")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.has_header("content-type"))
        self.assertEqual(response._headers.get("content-type"), ("Content-Type", "image/png"))

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

    def test_Get_Random_Category_Image(self):
        response = self.client.get('/category/people/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.has_header('content-type'))
        self.assertEqual(response._headers.get('content-type'), ('Content-Type', 'image/png'))

    def test_Get_Square_Category_Image(self):
        response = self.client.get('/category/people/200/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.has_header('content-type'))
        self.assertEqual(response._headers.get('content-type'), ('Content-Type', 'image/png'))

    def test_Get_Rectangle_Category_Image(self):
        response = self.client.get('/category/people/200/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.has_header('content-type'))
        self.assertEqual(response._headers.get('content-type'), ('Content-Type', 'image/png'))

    def test_Get_Random_Category_Image_Fail(self):
        response = self.client.get('/category/wewe/')
        self.assertEqual(response.status_code, 404)

    def test_Get_Rectangle_Category_Image_Fail(self):
        response = self.client.get('/category/wewe/200/200/')
        self.assertEqual(response.status_code, 404)

    def test_Get_Square_Category_Image_Fail(self):
        response = self.client.get('/category/wewe/200/')
        self.assertEqual(response.status_code, 404)

    def test_Get_Image_Fail(self):
        response = self.client.get('photo')
        self.assertEqual(response.status_code, 404)

class PhotoAPITestsFail(APITestCase):
    def setUp(self):
        script_dir = os.path.dirname(__file__)

    def test_Get_Image_Fail(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 404)

    def test_Get_Square_Image_Fail(self):
        response = self.client.get('/200/')
        self.assertEqual(response.status_code, 404)

    def test_Get_Rectangle_Image_Fail(self):
        response = self.client.get('/200/400/')
        self.assertEqual(response.status_code, 404)

    def test_Get_Name_Image_Fail(self):
        response = self.client.get('/200/400/hallo/')
        self.assertEqual(response.status_code, 404)
