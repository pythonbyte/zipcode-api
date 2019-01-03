from django.urls import reverse


from rest_framework import status
from rest_framework.test import APIClient, APITestCase


class TestGetZipCode(APITestCase):
    def setUp(self):
        self.client = APIClient()

        self.valid_zipcode = '30330330'
        self.invalid_zipcode = '30330580'
        self.invalid_long_zipcode = '123456789101'
        self.invalid_letter_zipcode = '30330-a78'

        self.correct_return = {
            "cep": "30330330",
            "address": "Rua Campo Belo",
            "neighborhood": "São Pedro",
            "city": "Belo Horizonte",
            "state": "MG"
        }

    def test_get_zipcode(self):
        url = reverse('getzipcode', args=[self.valid_zipcode])
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_valid_zipcode_data_response(self):
        url = reverse('getzipcode', args=[self.valid_zipcode])
        response = self.client.post(url)
        self.assertEqual(response.json(), self.correct_return)

    def test_post_invalid_zipcode(self):
        url = reverse('getzipcode', args=[self.invalid_zipcode])
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_wrong_method_endpoint(self):
        url = reverse('getzipcode', args=[self.valid_zipcode])
        response = self.client.get(url)
        self.assertEqual(
            response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED
        )

    def test_invalid_long_zipcode(self):
        url = reverse('getzipcode', args=[self.invalid_long_zipcode])
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_letter_zipcode(self):
        url = reverse('getzipcode', args=[self.invalid_letter_zipcode])
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
