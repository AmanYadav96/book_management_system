from rest_framework.response import Response
from book.serializer import BookSerializer
from rest_framework import status
from rest_framework.views import APIView
from .models import Book
from rest_framework.generics import GenericAPIView,ListAPIView
from books_management_system.custom_paginations import CustomPagination
from rest_framework.filters import OrderingFilter
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

class BookAdd(GenericAPIView):
   serializer_class = BookSerializer

   def post(self, request, format = None):
      if Book.objects.filter(ISBN = request.data.get('ISBN')).count() >= 1:

            return Response(
               {
                  'status': status.HTTP_400_BAD_REQUEST,
                  'message': "this book is already Added"
               },
            )
      
      else:   
            serializer = BookSerializer(data = request.data)
            serializer.is_valid(raise_exception = True)
            serializer.save()
    

            return Response(
               {
                  'status': status.HTTP_200_OK,
                  'message': "book is successfully Added"
               },
            )
   
class BookView(ListAPIView):
   queryset = Book.objects.all().order_by('publication_date')
   serializer_class = BookSerializer
   filter_backends = [OrderingFilter, SearchFilter, DjangoFilterBackend]
   pagination_class = CustomPagination
   filterset_fields = ['book_id','title','genre','price','rating','author','edition']
   ordering_fields = ['publication_date','author','title','price','rating','is_available']
   search_fields = ['created_at','title','genre','price','rating','edition','is_available']
  
   def list(self, request, *args, **kwargs):
        response_message = ""
        response_code = ""
        response = super().list(request, *args, **kwargs)
 
           
        return Response(
               {
                  'status': status.HTTP_200_OK,
                  'message': 'Book data retrieved successfully',
                  'data': response.data
               },
            )
class BookViewById(APIView):
   
   def get(self, request, input = None, format = None):
    
         if Book.objects.filter(book_id = id).count() >= 1:
            book=Book.objects.get(book_id = id)
            serializer = BookSerializer(book)
           
           
            return Response(
               {
                  'status': status.HTTP_200_OK,
                  'message': 'book data retrieved successfully',
                  'data': serializer.data
               },
            )
         else:  
            return Response(
               {
                  'status': status.HTTP_400_BAD_REQUEST,
                  'message': 'INVALID ID',
               },
    
            )
class BookUpdate(APIView):
   def patch(self, request, input, format = None):
      id = input
      if Book.objects.filter(book_id = id).count() >= 1:
         book = Book.objects.get(book_id = id)
         serializer = BookSerializer(book, data = request.data, partial = True)
         serializer.is_valid(raise_exception = True)
         serializer.save() 

         return Response(
            {
               'status': status.HTTP_200_OK,
               'message':'books details updated successfully',
            }, 
         )
      else:
         
          return Response(
            {
               'status': status.HTTP_400_BAD_REQUEST,
               'message': 'Invalid ID',
            },
          )  
   
class BookDelete(APIView):
   def delete(self, request, input, format = None):
      id = input
      if Book.objects.filter(book_id = id).count() >= 1:
         book=Book.objects.get(book_id = id)
         book.delete()
      
         return Response(
            {
               'status': status.HTTP_200_OK,
               'message': 'Book deleted successfully',
            },
         )  
      else:  
         return Response(
            {
               'status': status.HTTP_400_BAD_REQUEST,
               'message':'Invalid ID',
            },
         )  