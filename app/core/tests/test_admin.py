"""Test Admin functions"""
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase, Client


class AdminSiteTests(TestCase):
    """Test Admin"""
    def setUp(self):
        """Set up test"""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@example.com',
            password='admin123'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='test@example.com',
            password='test123',
            name='Test User'
        )

    def test_users_listed(self):
        """Test that users are listed on user page"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)
        self.assertContains(res, self.user.email)
        self.assertContains(res, self.user.name)

    def test_user_edit_page(self):
        """Test that edit page works"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)
        self.assertEquals(res.status_code, 200)

    def test_user_create_page(self):
        """Test that create user page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)
        self.assertEquals(res.status_code, 200)
