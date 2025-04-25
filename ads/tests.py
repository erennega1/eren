from django.test import TestCase
from django.contrib.auth.models import User
from .models import Ad

class AdTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.ad = Ad.objects.create(
            title='Test Ad',
            author=self.user,
            price=100,
        )

    def test_ad_creation(self):
        self.assertEqual(self.ad.title, 'Test Ad')
