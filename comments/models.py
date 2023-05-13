# Imports
# -------------------------------------------------
# 3rd Parties:-
from django.db import models
from django.contrib.auth.models import User

# internal:
from posts.models import Post
# -------------------------------------------------


class Comment(models.Model):
    """
    Comment model so users can comment on the posts
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()


    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content

        