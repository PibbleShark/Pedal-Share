from django.core.mail import send_mail
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from star_ratings.models import AbstractBaseRating


from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """Custom user model."""
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=20)
    last_name = models.CharField(_('last name'), max_length=35)
    library_name = models.CharField(_('library name'), max_length=115)
    street_address = models.CharField(_('street address'), max_length=30)
    city = models.CharField(_('city'), max_length=20)
    state = models.CharField(_('state'), max_length=12)
    zip_code = models.CharField(_('zip code'), max_length=5)
    message = models.TextField(
        _('Add a custom message to potential borrowers'),
        default="")
    image = models.ImageField(
        _('upload an image'),
        upload_to='images/',
        blank=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        """Returns the first and last name separated by a space."""
        full_name = '{} {}'.format(self.first_name, self.last_name)
        return full_name.strip()

    def get_sort_name(self):
        """Returns the first."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Sends an email to the user"""
        send_mail(subject, message, from_email, [self.email], **kwargs)


class UserRatings(AbstractBaseRating):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    comments = models.TextField(
        _('comments'),
        max_length=115,
        blank=True
    )
