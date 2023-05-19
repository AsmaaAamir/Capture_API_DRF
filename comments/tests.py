# imports:
# --------------------------------------------
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Comment
from posts.models import Post
# --------------------------------------------

class CommentListViewTests(APITestCase):
    def setUp(self):
        """
        This will automatically run before every test method
        """
        User.objects.create_user(username='asma', password='capture')

    def test_not_logged_in_user_cant_comment(self):
        """
        test to see not loggeds in user can't comment
        """
        response = self.client.post('/comments/', {'content': 'comment on post'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

class CommentDetailViewTests(APITestCase):
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

        Comment.objects.create(owner=asma, post_id=1, content='comment 1')
        Comment.objects.create(owner=aamir, post_id=2,  content='comment 2')

    def test_can_logged_in_user_comment_post(self):
        """
        Testing to see if a logged in user can comment on post
        """
        self.client.login(username='asma', password='capture')
        response = self.client.post('/comments/', {'post': 1, 'content': 'A new comment :)'})
        count_comment = Comment.objects.count()
        self.assertEqual(count_comment, 3)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_delete_their_own_comment(self):
        """
        testing if user can deleted their own comment form post
        """
        self.client.login(username='asma', password='capture')
        response = self.client.delete('/comments/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_can_user_delete_another_user_comment(self):
        """
        testing is user can delet anpther user comment from post
        """
        self.client.login(username='aamir', password='capture1')
        response = self.client.delete('/comments/1/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    
    def test_can_retrieve_current_comment(self):
        """
        testing is user can gte current comment by its valid id 
        """
        self.client.login(username='asma', password='capture')
        response = self.client.get('/comments/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_can_retrieve_invalid_id_comment(self):
        """
        testing if user can get comment by invalid id
        """   
        self.client.login(username='asma', password='capture')
        response = self.client.get('/comments/9999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)