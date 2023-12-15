from rest_framework.response import Response
from author.serializer import AuthorSerializer
from rest_framework import status
from rest_framework.views import APIView
from .models import Author
from rest_framework.generics import GenericAPIView

# Create your views here.
class AuthorAdd(GenericAPIView):
    serializer_class = AuthorSerializer
    def post(self, request,format=None):
        if Author.objects.filter(author_email=request.data.get('author_email')).count() >= 1 :
            return Response(
               {
                  'status': status.HTTP_400_BAD_REQUEST,
                  'message': "this author is already Added"
               },
            ) 
        else:
            serializer = AuthorSerializer(data = request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(
               {
                  'status': status.HTTP_200_OK,
                  'message': "author is successfully Added"
               },
            )
        
   
class BookView(APIView):
   def get(self, request, input = None, format = None):
      id = input
      print(id)
      if id is not None :
         if Author.objects.filter(author_id = id).count() >= 1:
            author=Author.objects.get(author_id = id)
            serializer = AuthorSerializer(author)
           
           
            return Response(
               {
                  'status': status.HTTP_200_OK,
                  'message': 'Author data retrieved successfully',
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
         author = Author.objects.all()
         serializer = AuthorSerializer(author, many = True)
       
         return Response(
            {
               'status': status.HTTP_200_OK,
               'message': 'Books data retrieved successfully',
               'data': serializer.data
            },
         )
      
class AuthorUpdate(APIView):
   def patch(self, request, input, format = None):
      id = input
      if Author.objects.filter(author_id = id).count() >= 1:
         author = Author.objects.get(author_id = id)
         serializer = AuthorSerializer(author, data = request.data, partial = True)
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
   
class HospitalDelete(APIView):
   def delete(self, request, input, format = None):
      id = input
      if Author.objects.filter(book_id = id).count() >= 1:
         author=Author.objects.get(book_id = id)
         Author.delete()
      
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