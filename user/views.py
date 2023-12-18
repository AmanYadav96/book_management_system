from django.shortcuts import render
from rest_framework.response import Response
from user.serializer import UserSerializer,UserLoginSerializer
from rest_framework import status
from rest_framework.views import APIView
from user.models import User
from rest_framework.generics import GenericAPIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from books_management_system.email import send_verification_email

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'access': str(refresh.access_token),
        'refresh': str(refresh)
    }


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
            email = request.data.get('user_email')
            print(email)
            
            
        
            serializer =UserSerializer(data = request.data)
            serializer.is_valid(raise_exception = True)
            email = request.data.get('user_email')
            serializer.save()
            user_email = User.objects.filter(user_email=email)
            print(user_email['user_id'])
            # print(user)
           

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
      
class UserLogin(GenericAPIView):
   serializer_class = UserLoginSerializer
   def post (self, request,format=None):
      serializer = UserLoginSerializer(data = request.data)
      email = request.data.get('user_email')
      password = request.data.get('password')
      if User.objects.filter(user_email=email).count() >= 1:
            user = User.objects.get(user_email=email)
            if  user.is_verify == True:
              if user.password == password:
                  token = get_tokens_for_user(user)
                  return Response(
                  {
                     'status': status.HTTP_200_OK,
                      'message': 'user logged in  successfully',
                      'token': token

                   },
                      )  
              else:
                  return Response(
                  {
                     'status': status.HTTP_400_BAD_REQUEST,
                      'message': 'password mismatch',
                   },
                   )  
            else:
                return Response(
                  {
                     'status': status.HTTP_400_BAD_REQUEST,
                      'message': 'Email is not verified please verify your email address',
                   },
                   )         
      else:          
           return Response(
                  {
                     'status': status.HTTP_400_BAD_REQUEST,
                      'message': 'email address is not registered',
                   },
                   )  


      