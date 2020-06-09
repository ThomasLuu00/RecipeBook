from rest_framework import generics, status
from rest_framework.response import Response
from .models import Item
from .serializers import ItemSerializer


class ListItemsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemDetailView(generics.RetrieveAPIView):
    """
    Provides a get method handler for a single item given an id.
    """

    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get(self, *args, **kwargs):
        try:
            item = Item.objects.get(pk=kwargs["pk"])
            return Response(ItemSerializer(item).data)
        except Item.DoesNotExist:
            return Response(data={"message": f"Item with id: {kwargs['pk']} does not exist"}, \
                status=status.HTTP_404_NOT_FOUND,)

    def put(self, request, *args, **kwargs):
        try:
            item = Item.objects.get(pk=kwargs["pk"])
            updated_item = ItemSerializer().update(item, request.data)
            return Response(ItemSerializer(updated_item).data)
        except Item.DoesNotExist:
            return Response(data={"message": f"Item with id: {kwargs['pk']} does not exist"}, \
                status=status.HTTP_404_NOT_FOUND,)
