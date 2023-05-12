
# Imports
# -------------------------------------------------
# 3rd Parties:-
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# -------------------------------------------------


class Profile(models.Model):
    """
    A class for the profile model created one-to-one
    relationship with the user. Its auto created when a user is
    created.
    """
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True)
    bio = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../capture_logo_nbnr9p'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        """
        Retuning information of the profile owner
        """
        return f"{self.owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
