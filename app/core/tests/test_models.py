from django.test import TestCase
from django.contrib.auth import get_user_model


class TestModels(TestCase):

    # test that user can be created
    def test_can_create_user(self):

        email = 'email@email.com'
        password = 'password'

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_user_email_is_normalized(self):
        email = 'email@EMAIL.com'
        password = 'password'

        user = get_user_model().objects.create_user(
            email, password
        )

        self.assertEqual(user.email, email.lower())

    # test value error is raised if no email is passed
    def test_invalid_email_new_user(self):

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'password')

    # test super user can be created
    def test_can_create_super_user(self):

        email = 'super@email.com'
        password = 'password'

        super_user = get_user_model().objects.create_super_user(
            email, password)

        self.assertTrue(super_user.is_admin)
        self.assertTrue(super_user.is_super)
