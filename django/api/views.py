from rest_framework import generics, status
from rest_framework.response import Response
from .models import Ingredient
from .serializers import IngredientSerializer

class ListIngredientsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

    def post(self, request, *args, **kwargs):
        ingredient = Ingredient.objects.create(
            name=request.data["name"],
            description=request.data["description"]
        )
        return Response(IngredientSerializer(ingredient).data, status=status.HTTP_201_CREATED)

class IngredientDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Provides a get method handler for a single ingredient given an id.
    """

    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

    def get(self, *args, **kwargs):
        try:
            ingredient = Ingredient.objects.get(pk=kwargs["pk"])
            return Response(IngredientSerializer(ingredient).data)
        except Ingredient.DoesNotExist:
            return Response(data={"message": f"Ingredient with id: {kwargs['pk']} does not exist"}, \
                status=status.HTTP_404_NOT_FOUND,)

    def put(self, request, *args, **kwargs):
        try:
            ingredient = Ingredient.objects.get(pk=kwargs["pk"])
            updated_ingredient = IngredientSerializer().update(ingredient, request.data)
            return Response(IngredientSerializer(updated_ingredient).data)
        except Ingredient.DoesNotExist:
            return Response(data={"message": f"Ingredient with id: {kwargs['pk']} does not exist"}, \
                status=status.HTTP_404_NOT_FOUND,)

    def delete(self, request, *args, **kwargs):
        try:
            ingredient = Ingredient.objects.get(pk=kwargs["pk"])
            ingredient.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Ingredient.DoesNotExist:
            return Response(data={"message": f"Ingredient with id: {kwargs['pk']} does not exist"}, \
                status=status.HTTP_404_NOT_FOUND,)