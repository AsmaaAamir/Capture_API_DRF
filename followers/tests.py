# imports:
# --------------------------------------------
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Follower
# --------------------------------------------

class FollowerListViewTests(APITestCase):
    def setUp(self):
        """
        This will automatically run before every test method
        """
        User.objects.create_user(username='asma', password='capture')

    def test_not_logged_in_user_cant_follow(self):
        """
        test to see not loggeds in user can't follow
        """
        response = self.client.post('/followers/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

class FollowerDetailViewTests(APITestCase):
    def setUp(self):
        """
        createing few user so they can follow one and another
        """
        asma =  User.objects.create_user(username='asma', password='capture') # id:1
        aamir =  User.objects.create_user(username='aamir', password='capture1') # id:2
        adam =  User.objects.create_user(username='adam', password='capture1') # id:3

        Follower.objects.create(owner=asma, followed_id=2)
        Follower.objects.create(owner=aamir, followed_id=3)


    def test_logged_in_user_can_follow(self):
        """
        Testing to see if loggined in user can follow another user 
        """
        self.client.login(username='asma', password='capture')
        response = self.client.post('/followers/', {'followed': 3})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_can_retrieve_following_valid_id(self):
        """
        testing if user can retrieven folowing by valid id 
        """
        self.client.login(username='asma', password='capture')
        response = self.client.get('/followers/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_retrieve_following_invalid_id(self):
        """
        testing if user can retrieven folowing with out valid id 
        """
        self.client.login(username='asma', password='capture')
        response = self.client.get('/followers/9999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_unfollow(self):
        """
        Testing to see if user can unfollow user
        """
        self.client.login(username='asma', password='capture')
        response = self.client.delete('/followers/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_can_unfollow_another_user_follow(self):
        """
        Testing to see if another user can unfollow for another user for them
        """
        self.client.login(username='aamir', password='capture1')
        response = self.client.delete('/followers/1/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)