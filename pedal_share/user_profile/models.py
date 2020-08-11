from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from star_ratings.models import Rating


class CustomUser(AbstractBaseUser, PermissionsMixin):
    # adapted from https://testdriven.io/blog/django-custom-user-model/
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=15)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=35)
    library_name = models.CharField(max_length=115)
    street_address = models.CharField(max_length=30)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=12)
    zip_code = models.IntegerField()
    message = models.TextField(
        verbose_name='Add a custom message to potential borrowers',
        null=True)
    image = models.ImageField(
        verbose_name='upload an image',
        null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class Ratings(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    rating = GenericRelation(Rating, related_query_name='user')





