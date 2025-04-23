from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class AdAPITests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test', password='test')
        self.client.login(username='test', password='test')

    def test_create_ad_unauthenticated(self):
        self.client.logout()
        response = self.client.post(reverse('create_ad'), {'title': 'Test'})
        self.assertEqual(response.status_code, 403)
