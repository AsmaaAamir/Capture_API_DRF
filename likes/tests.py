# imports:
# --------------------------------------------
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Like
from posts.models import Post
# --------------------------------------------

class LikeListViewTests(APITestCase):
    def setUp(self):
        """
        This will automatically run before every test method
        """
        User.objects.create_user(username='asma', password='capture')

    def test_not_logged_in_user_cant_like(self):
        """
        test to see not loggeds in user can't like
        """
        response = self.client.post('/likes/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class LikeDetailViewTests(APITestCase):
    def setUp(self):
        """
        creating few user and posts, so they like each oth content for testing
        """
        asma =  User.objects.create_user(username='asma', password='capture') 
        aamir =  User.objects.create_user(username='aamir', password='capture1') 
        Post.objects.create(
            owner=asma, title='title 1', 
            description='testing', category='spain' # id:1
        )
        Post.objects.create(
            owner=aamir, title='title 2', 
            description='testing', category='france' # id:2
        )
        Post.objects.create(
            owner=asma, title='title 3', 
            description='testing', category='india' # id:3
        )
        Post.objects.create(
            owner=aamir, title='title 4', 
            description='testing', category='united kingdom' # id:4
        )

        Like.objects.create(owner=asma, post_id=2)
        Like.objects.create(owner=aamir, post_id=3)
    
    def test_can_logged_in_user_like_post(self):
        """
        Testing to see if a logged in user can like post
        """
        self.client.login(username='asma', password='capture')
        response = self.client.post('/likes/', {'post': 3})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_can_unlike_own_like(self):
        """
        testing to see if user can unlike a post they liked before
        """
        self.client.login(username='asma', password='capture')
        response = self.client.delete('/likes/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_can_unlike_another_user_follow(self):
        """
        Testing to see if another user can unlike for another unlike for them
        """
        self.client.login(username='aamir', password='capture1')
        response = self.client.delete('/likes/1/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_can_retrieve_current_like_valid_id(self):
        """
        Testing to see if user can retrieve a like by its valid ID
        """
        self.client.login(username='asma', password='capture')
        response = self.client.get('/likes/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
         
    def test_user_can_retrieve_invaild_id_like(self):
        """
        Testing to see if user can retrieve a like by its valid ID
        """
        self.client.login(username='asma', password='capture')
        response = self.client.get('/likes/9999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)