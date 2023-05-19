# imports:
# --------------------------------------------
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Profile
# --------------------------------------------

class ProfileDetailViewTest(APITestCase):
    def setUp(self):
        """
        creating two profile for testing 
        """
        User.objects.create_user(username='asma', password='capture')
        User.objects.create_user(username='aamir', password='capture1')

    def test_user_update_their_own_profile(self):
        """
        testing to see if user can update their own profile
        """
        self.client.login(username='asma', password='capture')
        response = self.client.put('/profiles/1/', {'bio': 'testing to see if its updated'})
        profile = Profile.objects.filter(pk=1).first()
        self.assertEqual(profile.bio, 'testing to see if its updated')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
       
    def test_user_update_someone_else_profile(self):
        """
        testing to see if user can update another user profile
        """  
        self.client.login(username='asma', password='capture')
        response = self.client.put('/profiles/2/', {'bio': 'testing to see if its updated'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


    def test_not_logged_user_updated_their_profile(self):
        """
        testing is use can update their own profile if the are not logged in 
        """
        response = self.client.put('/profiles/1/', {'bio': 'testing to see if its updated'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        

    def test_user_can_view_current_profile_vaild_id(self):
        """
        testing to see if user can view current profile with valid id
        """
        self.client.login(username='asma', password='capture')
        response = self.client.get('/profiles/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_view_profile_invalid_id(self):
        """
        testing if user can view profile with invaild id
        """
        self.client.login(username='asma', password='capture')
        response = self.client.get('/profiles/9999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_delete_their_own_profile(self):
        """
        testing if user can delete their own profile
        """
        self.client.login(username='asma', password='capture')
        response = self.client.delete('/profiles/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


    def test_user_can_delete_another_user_profile(self):
        """
        testing user can deleted another user posts
        """
        self.client.login(username='asma', password='capture')
        response = self.client.delete('/profiles/2/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    