# Imports
# -------------------------------------------------
# 3rd Parties:-
from django.db import models
from django.contrib.auth.models import User

# -------------------------------------------------


class Post(models.Model):
    """
    """
    category_choices = [
        ('India', 'India'), ('China', 'China'), ('United States', 'United States'),('Nigeria', 'United States'),
        ('Brazil', 'Brazil'), ('Bangladesh', 'Bangladesh'), ('Pakistan', 'Pakistan'),('Indonesia', 'Indonesia'),
        ('Mexico', 'Mexico'), ('Russia', 'Russia'), ('Japan', 'Japan'),('Philippines', 'Philippines'),
        ('Ethiopoa', 'Ethiopoa'), ('United Kingdom', 'United Kingdom'), ('Germany', 'Germany'),('Egypt', 'Egypt'),
        ('Tanzania', 'Tanzania'), ('Iran', 'Iran'), ('Thailand', 'Thailand'),('France', 'France'),
        ('South Korea', 'South Korea'), ('Sudan', 'Sudan'), ('Algeria', 'Algeria'),('South Africa', 'South Africa'),
        ('Angola', 'Angola'), ('Peru', 'Peru'), ('Saudi Arabia', 'Saudi Arabia'),('Myanmar', 'Myanmar'),
        ('Canada', 'Canada'), ('Argentina', 'Argentina'), ('Poland', 'Poland'),('Ghana', 'Ghana'),
        ('Madagascar', 'Madagascar'), ('Morocco', 'Morocco'), ('Mozambique', 'Mozambique'),('Uganda', 'Uganda'),
        ('Chad', 'Chad'), ('Libya', 'Libya'), ('Mali', 'Mali'),('Mauritania', 'Mauritania'),
        ('Niger', 'Niger'), ('Nepal', 'Nepal'), ('Yemen', 'Yemen'),('Uzbekistan', 'Uzbekistan'),
        ('Malaysia', 'Malaysia'), ('Iraq', 'Iraq'), ('Afghanistan', 'Afghanistan'),('Burundi', 'Burundi'),
        ('Rwanda','Rwanda'), ('Bolivia','Bolivia')
    
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100, choices=category_choices, blank=True)
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