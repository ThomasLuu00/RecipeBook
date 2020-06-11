from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Item
from .serializers import ItemSerializer
from rest_framework.utils import json

class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_item(name="", description=""):
        if name != "" and description != "":
            Item.objects.create(name=name, description=description)

    def fetch_item(self, pk=0):
        return self.client.get(reverse("item-detail", kwargs={
            "version": "v1",
            "pk": pk,
        }))

    def update_item(self, pk=0, **kwargs):
        return self.client.put(reverse("item-detail", kwargs={
            "version": "v1",
            "pk": pk,
            }),
            data=json.dumps(kwargs["data"]), 
            content_type="application/json"
        )

    def delete_item(self, pk=0):
        return self.client.delete(reverse("item-detail", kwargs={
            "version": "v1",
            "pk": pk,
        }))

    def setUp(self):
        # add test data
        self.create_item("wooden sword", "A simple wooden sword.")
        self.create_item("tree branch", "A tree branch picked up off the ground.")
        self.create_item("love is wicked", "brick and lace")
        self.create_item("jam rock", "damien marley")
        self.valid_item_id = 1
        self.invalid_item_id = 100
        self.update_id = 2
        self.delete_id = 3
        self.valid_data = {
            "name": "Test",
            "description": "Test description",
        }
        self.invalid_data: {
            "name": "",
            "description": "",
        }



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

class ItemDetailViewTest(BaseViewTest):
    
    def test_get_item_valid_id(self):
        """
        This test ensures that an item of a given valid id is returned.
        """

        # Hit the api endpoint
        response = self.fetch_item(self.valid_item_id)
        
        # Fetch and serialize data from the database
        expected = Item.objects.get(pk=self.valid_item_id)
        serialized = ItemSerializer(expected)

        # Compare actual to expected values
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_get_item_invalid_id(self):
        """
        This test ensures GET properly handles a given invalid id.
        """

        # Hit the api endpoint
        response = self.fetch_item(self.invalid_item_id)

        # Compare actual to expected values
        self.assertEqual(response.data["message"], f"Item with id: {self.invalid_item_id} does not exist")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_item_valid_id(self):
        """
        This test ensures that an item of a given valid id is updated and returned.
        """

        # Hit the api endpoint
        response = self.update_item(pk=self.update_id, data=self.valid_data)
        
        # Fetch and serialize data from the database
        expected = Item.objects.get(pk=self.update_id)
        serialized = ItemSerializer(expected)
        
        # Compare actual to expected values
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_update_item_invalid_id(self):
        """
        This test ensures PUT properly handles a given invalid id.
        """

        # Hit the api endpoint
        response = self.update_item(pk=self.invalid_item_id, data=self.valid_data)
        
        # Compare actual to expected values
        self.assertEqual(response.data["message"], f"Item with id: {self.invalid_item_id} does not exist")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_item_valid_id(self):
        """
        This test ensures that an item is properly deleted given a valid id.
        """

        # Hit the api endpoint
        response = self.delete_item(pk=self.delete_id)
        
        # Fetch and serialize data from the database
        user = Item.objects.filter(pk=self.delete_id)
        #serialized = ItemSerializer(expected)
        
        # Compare actual to expected values
        self.assertEqual(user.exists(), False)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_item_invalid_id(self):
        """
        This test ensures DELETE properly handles a given invalid id.
        """

        # Hit the api endpoint
        response = self.delete_item(pk=self.invalid_item_id)
        
        # Compare actual to expected values
        self.assertEqual(response.data["message"], f"Item with id: {self.invalid_item_id} does not exist")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)