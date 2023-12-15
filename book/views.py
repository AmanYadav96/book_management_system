from rest_framework.response import Response
from book.serializer import BookSerializer
from rest_framework import status
from rest_framework.views import APIView
from .models import Book
from rest_framework.generics import GenericAPIView

class BookAdd(GenericAPIView):
   serializer_class = BookSerializer

   def post(self, request, format = None):
      if Book.objects.filter(title = request.data.get('title')).count() >= 1:
          
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
   
class BookView(APIView):
   def get(self, request, input = None, format = None):
      id = input
      print(id)
      if id is not None :
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
      else:
         book = Book.objects.all()
         serializer = BookSerializer(book, many = True)
       
         return Response(
            {
               'status': status.HTTP_200_OK,
               'message': 'Books data retrieved successfully',
               'data': serializer.data
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