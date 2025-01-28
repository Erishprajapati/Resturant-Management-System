from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Category
from .serializers import CategorySerializer

@api_view(['GET'])  # Restrict this view to GET requests only
def category_list(request):
    categories = Category.objects.all()  # Fetch all Category objects from the database
    serializer = CategorySerializer(categories, many=True)  # Serialize them
    return Response(serializer.data)  # Return the serialized data as JSON
