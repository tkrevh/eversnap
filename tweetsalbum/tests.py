from django.utils import unittest
from django.test.client import Client
from models import Picture, TUser, Album
from rest_framework.test import APIRequestFactory

class PicturesTest(unittest.TestCase):

    def setUp(self):
        self.client = Client()
        
        self.user1, created = TUser.objects.get_or_create(name='User1', screen_name='User1')
        if created:
         self.user1.save()
        self.user2, created = TUser.objects.get_or_create(name='User2', screen_name='User2')
        if created:
         self.user2.save()
        
        self.album, created = Album.objects.get_or_create(name='carnival', max_id=0)
        if created:
            self.album.save()
        
        self.picture1, created = Picture.objects.get_or_create(album=self.album, user=self.user1, url='http://pbs.twimg.com/media/BsAsDnxCQAAi2UL.jpg')
        if created:
            self.picture1.save()
        self.picture2, created = Picture.objects.get_or_create(album=self.album, user=self.user1, url='http://pbs.twimg.com/media/BsAiv3YIQAA2q34.jpg')
        if created:
            self.picture2.save()
        self.picture3, created = Picture.objects.get_or_create(album=self.album, user=self.user1, url='http://pbs.twimg.com/media/Br80x6MCIAEzq9Y.jpg')
        if created:
            self.picture3.save()
        self.picture4, created = Picture.objects.get_or_create(album=self.album, user=self.user2, url='http://pbs.twimg.com/media/Br_CxWmIYAAVyXQ.jpg')
        if created:
            self.picture4.save()
        self.picture5, created = Picture.objects.get_or_create(album=self.album, user=self.user2, url='http://pbs.twimg.com/media/Br97zU5CUAECg5J.jpg')
        if created:
            self.picture5.save()

    def test_details_view(self):
        """
        Tests that queryset for given URL address contains all Picture objects
        """
        response = self.client.get('/pictures/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['picture_list']), 5)
        
    def test_rest_api(self):
        """
        Tests REST API
        """
        response = self.client.get('/api/pictures/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['id'], 1)
        self.assertEqual(response.data['url'], self.picture1.url)

        response = self.client.get('/api/pictures/5/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['id'], 5)
        self.assertEqual(response.data['url'], self.picture5.url)

        response = self.client.get('/api/pictures/6/')
        self.assertEqual(response.status_code, 404)

        response = self.client.get('/api/pictures/')
        self.assertEqual(response.data['count'], Picture.objects.count())
