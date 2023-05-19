# imports:
# --------------------------------------------
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Profile
# --------------------------------------------

class ProfileDetailviewtest(APITestCase):
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
       
    def test_user_update_someone_else_profile(self):
        """
        testing to see if user can update another user profile
        """  

    def test_not_logged_ser_updated_their_profile(self):
        """
        testing is use can update their own profile if the are not logged in 
        """

    def test_user_can_view_current_profile_vaild_id(self):
        """
        testing to see if user can view current profile with valid id
        """

    def test_user_cant_view_profile_invalid_id(self):
        """
        testing if user can view proffile with invaild id
        """

    def test_user_can_delet_their_own_profild(self):
        """
        testing if user can delete their own profile
        """

    def test_can_user_delete_someone_else_profile(self):
        """
        testing is another user can delet another user profile
        """