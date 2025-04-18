from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class ChatTests(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(username='user1')
        self.user2 = User.objects.create(username='user2')

    def test_message_creation(self):
        self.client.force_login(self.user1)
        response = self.client.post('/chat/send/', {
            'recipient_id': self.user2.id,
            'text': 'Привет!'
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Message.objects.count(), 1)