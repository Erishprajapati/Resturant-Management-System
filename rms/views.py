# from django.shortcuts import render
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from .models import *
# from .serializers import CategorySerializer
# from rest_framework import status
# @api_view(['GET','POST'])  # Restrict this view to GET requests only
# def category_list(request):
#     if request.method == 'GET':  
#         category = Category.objects.all()  # Fetch all Category objects from the database
#         serializer = CategorySerializer(category, many=True)  # Serialize them
#         return Response(serializer.data)  # Return the serialized data as JSON
#     else:
#         serializer = CategorySerializer(data = request.data)
#         serializer.is_valid(raise_exception = True) #to check the user sent data is valid or not
#         serializer.save()
        
#         return Response({"Details": "Data has been created"}, status = status.HTTP_201_CREATED)
# @api_view(['GET'])    
# def category_details(request,pk):
#     if request.method == "GET":
#         category = Category.objects.get(pk = pk) #user sent pk = pk
#         serializer = CategorySerializer(category)
#         return Response(serializer.data)
#     else:
#         items = OrderItem.objects.get(food__category = category ).count()
#         if items> 0:
#             return Response({"Details" : "Orderitem related to this category exists"})
#         category.delete()
#         return Response({"Details" : "Category Deleted successfully"}, status = status.HTTP_404_NOT_FOUND)
       
from django.shortcuts import render
from rest_framework.response import Response
from django.http import HttpResponse
from .models import *
from .serializers import CategorySerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.serializers import ValidationError
from .serializers import CategorySerializer
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework import generics

# @api_view(['GET','POST']) #Create your views here.
# def category_list(request):
#    if request.method == 'GET':
#       category = Category.objects.all()
#       serializer = CategorySerializer(category,many = True)
#       return Response(serializer.data)
#    else: #here is two method working get and post means read and create the data
#       serializer = CategorySerializer(data = request.data)
#       serializer.is_valid(raise_exception = True)
#       serializer.save()
#       return Response({"details":"Data has been created"},status=status.HTTP_201_CREATED)
 

# @api_view(['GET','DELETE', 'PUT'])
# def category_details(request,pk):
#    try:
#       category = Category.objects.get(pk=pk)
#    except Category.DoesNotExist:
#       return Response({"details":"Category does not exist"},status=status.HTTP_404_NOT_FOUND)
   
#    if request.method == "GET":
#       serializer = CategorySerializer(category)
#       return Response(serializer.data)
   
#    elif request.method == "PUT": #handling updates in the foods
#       serializer = CategorySerializer(category, data=request.data)
#       if serializer.is_valid():
#          serializer.save()
#          return Response({"Details": "Category updated successfully", "data" :serializer.data}) #the message are sent in key and value pairs
#       #what if the error are founf and category cannot be updated then 
#       return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST) #the error)
#    elif request.method == "DELETE":
#       items = OrderItem.objects.filter(foods__category=category).count()
#       if items > 0:
#          raise ValidationError({"Details": "items are left in this category."})
#       else:
#          category.delete()
#          return Response({"Details" : "Category deleted successfully."})
      
# class CategoryDetailAPIView(APIView):
#    def get(self,request,pk):
#       category = get_object_or_404(Category, pk = pk) #if object is found then display otherwise show the error of 404 and primary key = primary key which user sends
#       serializer = CategorySerializer(category) #convert the complex data into json format or readable format
#       return Response(serializer.data)
class CategoryListCreateAPIView(generics.ListCreateAPIView):
   queryset = Category.objects.all()
   serializer_class = CategorySerializer
   
class CategoryListDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def delete(self, request, *args, **kwargs):
        category = self.get_object()
        items = OrderItem.objects.filter(foods__category=category).count()

        if items > 0:
            raise ValidationError({"Details": "Items are unable to delete"})

        response = super().delete(request, *args, **kwargs)
        return Response({"message": "Category deleted successfully!"})

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return Response({
            "message": "Category updated successfully!",
            "data": response.data
        })
   # def put(self,request,pk):
   #    category = get_object_or_404(Category, pk = pk) 
   #    serializer = CategorySerializer(category, data = request.data)
   #    if serializer.is_valid():
   #       serializer.save()
   #       return Response({"Details" : "Category updated successfully"})
   #    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
                      
   # def delete(self,request,pk):
   #    category = get_object_or_404(Category, pk = pk)
   #    items = Order.objects.filter(foods__category=category).count()
   #    if items > 0:
   #       raise ValidationError({"Details" : "Items are left in this category"})
   #    category.delete()
   #    return Response({"Details": "Category deleted successfully"})