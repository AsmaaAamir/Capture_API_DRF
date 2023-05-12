# Imports
# -------------------------------------------------
# 3rd Parties:-
from django.db import models
from django.contrib.auth.models import User

# -------------------------------------------------


class Post(models.Model):
    """
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(
        upload_to='images/', default='https://res.cloudinary.com/doow4kmj4/image/upload/v1683901095/capture_logo_nbnr9p.jpg',
        blank=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'