from django.urls import path
from .views import ListItemsView, ItemDetailView

urlpatterns = [
    path('items/', ListItemsView.as_view(), name="item-all"),
    path('item/<int:pk>/', ItemDetailView.as_view(), name="item-detail")
]