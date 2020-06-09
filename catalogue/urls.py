from django.urls import path
from .views import ListItemsView, IndexView

urlpatterns = [
    path('items/', ListItemsView.as_view(), name="item-all"),
]