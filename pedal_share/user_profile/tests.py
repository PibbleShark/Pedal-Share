from django.test import TestCase
from django.contrib.auth import get_user_model
from django.shortcuts import reverse

from . import models


class UserTests(TestCase):
    """Tests for the user model."""
    def setUp(self):
        self.user = get_user_model()
        self.test_user = self.user.objects.create_user(
            email='bruce.wayne@wayneenterprises.com',
            confim_email='bruce.wayne@wayneenterprises.com',
            password='jasontoddRIP',
            confim_password='jasontoddRIP',
            first_name='Bruce',
            last_name='Wayne',
            library_name='Bat-gear',
            message="because I'm batman!",
        )

    def test_create_user(self):
        """Test to make sure that a standard website user is created with my custom user model"""
        # adapted from https://testdriven.io/blog/django-custom-user-model/

        self.assertEqual(self.test_user.email, 'bruce.wayne@wayneenterprises.com')
        self.assertTrue(self.test_user.is_active)
        self.assertFalse(self.test_user.is_staff)
        self.assertFalse(self.test_user.is_superuser)
        try:
            assert self.test_user.username not in self.test_user
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            self.user.objects.create_user()
        with self.assertRaises(TypeError):
            self.user.objects.create_user(email='')
        with self.assertRaises(ValueError):
            self.user.objects.create_user(email='', password="jasontoddRIP")

    def test_register_view(self):
        resp = self.client.get(reverse('user:register'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.test_user, resp.context['form'])