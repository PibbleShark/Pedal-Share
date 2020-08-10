from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from star_ratings.models import Rating
from address.models import AddressField


class CustomUser(AbstractBaseUser, PermissionsMixin):
    # adapted from https://testdriven.io/blog/django-custom-user-model/
    email = models.EmailField(_('email address'), unique=True)
    password = models.CharField(max_length=15)
    first_name = models.CharField(_('first name'), max_length=20)
    last_name = models.CharField(_('last name'), max_length=35)
    library_name = models.CharField(_('name your pedal library'), max_length=115)
    message = models.TextField(
        _('Add a message to potential borrowers'),
        null=True)
    address = AddressField(_('address'))
    image = models.ImageField(_('profile picture'))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class Ratings(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    rating = GenericRelation(Rating, related_query_name='user')





