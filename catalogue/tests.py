from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Item
from .serializers import ItemSerializer

class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_item(name="", description=""):
        if name != "" and description != "":
            item.objects.create(name=name, description=description)

    def setUp(self):
        # add test data
        self.create_item("wooden sword", "A simple wooden sword.")
        self.create_item("tree branch", "A tree branch picked up off the ground.")
        self.create_item("love is wicked", "brick and lace")
        self.create_item("jam rock", "damien marley")


class GetAllItemTest(BaseViewTest):

    def test_get_all_item(self):
        """
        This test ensures that all item added in the setUp method
        exist when we make a GET request to the item/ endpoint
        """

        # hit the API endpoint
        response = self.client.get(
            reverse("item-all", kwargs={"version": "v1"})
        )

        # fetch the data from db
        expected = item.objects.all()
        serialized = itemSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)




