from django.test import TestCase
from django.contrib.auth import get_user_model
from django.shortcuts import reverse


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
            street_address='1234 Wayne Manor',
            city='Gotham City',
            state='NJ',
            zip_code='65755',
            message="because I'm batman!",
        )

    def test_register_view(self):
        """Test to make sure that a standard website user is created with my custom user model"""
        # adapted from https://testdriven.io/blog/django-custom-user-model/
        resp = self.client.get(reverse('user:register'))
        self.assertEqual(resp.status_code, 200)
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

    def test_login_view(self):
        """Tests user login view and url"""
        resp = self.client.get(reverse('user:login'))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.test_user.email, resp.context['form.email'])
        self.assertEqual(self.test_user.password, resp.context['form.password'])

    def test_user_detail(self):
        """Tests user detail view and url"""
        resp = self.client.get(reverse('user:detail'))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.test_user, resp.context['user'])

    def test_edit_user(self):
        """Tests that a user is edited"""
        resp = self.client.get(reverse('user:edit'))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.test_user, resp.context['form'])
