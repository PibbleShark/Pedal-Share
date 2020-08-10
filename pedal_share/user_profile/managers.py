from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
    # adapted from https://testdriven.io/blog/django-custom-user-model/
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of username.
    """
    def create_user(self, email, password):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.save()
        return user



