from django.test import TestCase

from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        "Test creating a new user with an email is successful"
        email = "test@abc.com"
        password = "testone"

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = "test@ABC.cOM"
        user = get_user_model().objects.create_user(email, 'testone')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'testone')

    def test_create_new_super_user(self):
        user = get_user_model().objects.create_superuser(
            'test@abc.com',
            'testone'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
