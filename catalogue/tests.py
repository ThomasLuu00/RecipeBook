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
            Item.objects.create(name=name, description=description)

    def fetch_an_item(self, pk=0):
        return self.client.get(reverse("item-detail", kwargs={
            "version": "v1",
            "pk": pk,
        }))

    def setUp(self):
        # add test data
        self.create_item("wooden sword", "A simple wooden sword.")
        self.create_item("tree branch", "A tree branch picked up off the ground.")
        self.create_item("love is wicked", "brick and lace")
        self.create_item("jam rock", "damien marley")
        self.valid_song_id = 1
        self.invalid_song_id = 100


class GetAllItemTest(BaseViewTest):

    def test_get_all_item(self):
        """
        This test ensures that all item added in the setUp method
        exist when we make a GET request to the item/ endpoint
        """

        # Hit the API endpoint
        response = self.client.get(
            reverse("item-all", kwargs={"version": "v1"})
        )

        # Fetch and serialize data from the database
        expected = Item.objects.all()
        serialized = ItemSerializer(expected, many=True)

        # Compare actual to expected values
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class GetOneItemTest(BaseViewTest):
    
    def test_get_valid_item(self):
        """
        This test ensures that an item of a given valid id is returned.
        """

        # Hit the api endpoint
        response = self.fetch_an_item(self.valid_song_id)
        
        # Fetch and serialize data from the database
        expected = Item.objects.get(pk=self.valid_song_id)
        serialized = ItemSerializer(expected)

        # Compare actual to expected values
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_get_invalid_item(self):
        """
        This test ensures proper handling of a given invalid id.
        """

        # Hit the api endpoint
        response = self.fetch_an_item(self.invalid_song_id)

        # Compare actual to expected values
        self.assertEqual(response.data["message"], f"Item with id: {self.invalid_song_id} does not exist")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)