# Imports
# -------------------------------------------------
# 3rd Parties:-
from django.db import models
from django.contrib.auth.models import User

# internal:
from posts.models import Post
# -------------------------------------------------


class Like(models.Model):
    """
    Allowing user to like post. like model is related to owner and post. While 
    making sure user doesn't like the same post twice.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'post']

    def __str__(self):
        return f'{self.owner} {self.post}'