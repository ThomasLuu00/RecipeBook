from django.urls import path
from .views import ListIngredientsView, IngredientDetailView

urlpatterns = [
    path('ingredients/', ListIngredientsView.as_view(), name="ingredient-all"),
    path('ingredient/<int:pk>/', IngredientDetailView.as_view(), name="ingredient-detail")
]