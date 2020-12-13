from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client


class AdminSiteTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='test@test.com',
            password='passbyme123'
        )
        # Automatically log-in client using
        # Client() helper function force_login
        # which uses Django built-in authentication.
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='tesst@test.com',
            password='passmeby123',
            name='Test User',
        )

    def test_users_listed(self):
        """Test if users are listed on the user page"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)
