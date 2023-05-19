# imports:
# --------------------------------------------
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

# internal:
from .models import Post
# --------------------------------------------

class PostListViewTests(APITestCase):
    """
    This will automatically run before every test method
    """
    def setUp(self):
        User.objects.create_user(username='asma', password='capture')

    def test_can_list_posts(self):
        """
        Testing to see if the posts are listed in the database
        """
        asma = User.objects.get(username='asma')
        Post.objects.create(owner=asma, title='title')
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))
    

    def test_logged_in_user_can_create_post(self):
        """
        Testing to see if a logged-in user may post
        """
        self.client.login(username='asma', password='capture')
        response = self.client.post('/posts/', {'title': 'post title', 'category': 'Japan'})
        count_post = Post.objects.count()
        self.assertEqual(count_post, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_not_logged_in_cant_create_post(self):
        """
        Test to ensure that a user who is not logged in cannot create a post.
        """
        response = self.client.post('/posts/', {'title': 'post title', 'category': 'Japan'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_make_sure_all_requied_field_included(self):
        """
        Testing to ensure that no post can be made without all of the fields being completed 
        """
        self.client.login(username='asma', password='capture')
        response = self.client.post('/posts/', {'category': 'Japan'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class PostDetailViewTests(APITestCase):
    def setUp(self):
        """
        Creating 2 user to test for the post details
        """
        asma = User.objects.create_user(username='asma', password='capture')
        aamir = User.objects.create_user(username='aamir', password='capture1')
        Post.objects.create(
            owner=asma, title='title 1',
            description='test', category='Spain'
        )
        Post.objects.create(
            owner=aamir, title='title 2 ',
            description='test', category='france'
        )


    def test_can_retrieve_existing_post_using_valid_id(self):
        """
        Trying to retrieve  posts with a valid ID.  
        """
        response = self.client.get('/posts/1/')
        self.assertEqual(response.data['title'], 'title 1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_post_using_invalid_id(self):
        """
        Trying to retrieve post with a invalid Id
        """
        response = self.client.get('/posts/99999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_their_post(self):
        """
        Testing if user can update their own post
        """
        self.client.login(username='asma', password='capture')
        response = self.client.put('/posts/1/', {'title': 'new title', 'category': 'Canada'})
        post = Post.objects.filter(pk=1).first()
        self.assertEqual(post.title, 'new title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_another_users_post(self):
        """
        Testing is user any edit another post thats not their.
        """
        self.client.login(username='asma', password='capture')
        response = self.client.put('/posts/2/', {'title': ' a new title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_can_delete_their_own_post(self):
        """
        testing is user can deleted their own post
        """
        self.client.login(username='asma', password='capture')
        response = self.client.delete('/posts/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_cant_delet_another_user_post(self):
        """
        testing user can deleted another user posts
        """
        self.client.login(username='asma', password='capture')
        response = self.client.delete('/posts/2/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    