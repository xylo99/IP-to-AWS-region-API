from django.test import TestCase
from django.contrib.auth import get_user_model
import re

class ModelTests(TestCase):
    def test_if_create_user_with_email_successful(self):
        email = 'test_user@test_user.com'
        pw = 'testuserpass321'
        user = get_user_model().objects.create_user(
            email=email,
            password=pw
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(pw))

    def test_if_super_user_created(self):
        user = get_user_model().objects.create_user(
            'test@test.com',
            'passmeby234'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_if_ip_converted_to_region(self):
        user = get_user_model().objects.create_user(
            'tesit@test.com',
            'pass33by234'
        )

        self.assertTrue(re.match(r"^[A-Z][A-Z]", user.region))
