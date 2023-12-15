from django.shortcuts import render
from rest_framework.response import Response
from user.serializer import UserSerializer
from rest_framework import status
from rest_framework.views import APIView
from user.models import User
from rest_framework.generics import GenericAPIView

class UserRegister(GenericAPIView):
   serializer_class = UserSerializer

   def post(self, request, format = None):
      if User.objects.filter(user_email = request.data.get('user_email')).count()>=1 :
          
            return Response(
               {
                  'status': status.HTTP_400_BAD_REQUEST,
                  'message': "this user is already registered"
               },
            )
      
      else:   
            serializer =UserSerializer(data = request.data)
            serializer.is_valid(raise_exception = True)
            serializer.save()
    

            return Response(
               {
                  'status': status.HTTP_200_OK,
                  'message': "user is successfully Added"
               },
            )
   
class UserView(APIView):
   def get(self, request, input = None, format = None):
      id = input
      print(id)
      if id is not None :
         if User.objects.filter(user_id = id).count() >= 1:
            user=User.objects.get(user_id = id)
            serializer = UserSerializer(user)
           
           
            return Response(
               {
                  'status': status.HTTP_200_OK,
                  'message': 'user data retrieved successfully',
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
         user = User.objects.all()
         serializer = UserSerializer(user, many = True)
       
         return Response(
            {
               'status': status.HTTP_200_OK,
               'message': 'user data retrieved successfully',
               'data': serializer.data
            },
         )
      
class UserUpdate(APIView):
   def patch(self, request, input, format = None):
      id = input
      if User.objects.filter(user_id = id).count() >= 1:
         user = User.objects.get(user_id = id)
         serializer = UserSerializer(user, data = request.data, partial = True)
         serializer.is_valid(raise_exception = True)
         serializer.save() 

         return Response(
            {
               'status': status.HTTP_200_OK,
               'message':'user details updated successfully',
            }, 
         )
      else:
         
          return Response(
            {
               'status': status.HTTP_400_BAD_REQUEST,
               'message': 'Invalid ID',
            },
          )  
   
class UserDelete(APIView):
   def delete(self, request, input, format = None):
      id = input
      if User.objects.filter(user_id = id).count() >= 1:
         user=User.objects.get(user_id = id)
         user.delete()
      
         return Response(
            {
               'status': status.HTTP_200_OK,
               'message': 'user deleted successfully',
            },
         )  
      else:  
         return Response(
            {
               'status': status.HTTP_400_BAD_REQUEST,
               'message':'Invalid ID',
            },
         )  
      
      