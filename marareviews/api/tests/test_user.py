from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from model_mommy import mommy

User = get_user_model()


class UserViewTestCase(APITestCase):
    def setUp(self):
        self.user = mommy.make(User)

    # LIST
    def test_user_list_api(self):
        url = reverse('user-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    # DETAIL
    def test_user_detail_api(self):
        url = reverse('user-detail', kwargs={'pk': self.user.pk})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
