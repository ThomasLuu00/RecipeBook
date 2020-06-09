from rest_framework import generics
from django.views import generic
from .models import Item
from .serializers import ItemSerializer

class ListItemsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class IndexView(generic.ListView):
    """
    Provides a get method handler.
    """
    model = Item
    template_name = 'catalogue/index.html'
