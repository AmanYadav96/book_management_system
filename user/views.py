from django.shortcuts import render
from rest_framework.response import Response
from user.serializer import UserSerializer,UserLoginSerializer,UserProfileSerializer
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
            Response.status_code = status.HTTP_400_BAD_REQUEST
            return Response(
               {
                  'status': status.HTTP_400_BAD_REQUEST,
                  'message': "this user is already registered"
               },
            )
      
      else:   
            email = request.data.get('user_email')
            serializer =UserSerializer(data = request.data)
            serializer.is_valid(raise_exception = True)
            email = request.data.get('user_email')
            serializer.save()
            user_email = User.objects.filter(user_email=email)
            user = User.objects.get(user_email=email)
            user_id = str(user.user_id)
            verification_token = get_tokens_for_user(user)
            url = 'https://book-management-system-omega.vercel.app/api/user/verification/?user_id=' + \
            user_id + '&token=' + verification_token['access']
            send_verification_email(url,email)
            Response.status_code = status.HTTP_200_OK
            return Response(
               {
                  'status': status.HTTP_200_OK,
                  'message': "user is successfully Added"
               },
            )
   
class UserView(APIView):
   permission_classes = [IsAuthenticated]
   def get(self, request, input = None, format = None):
      id = input
      print(id)
      if id is not None :
         if User.objects.filter(user_id = id).count() >= 1:
            user=User.objects.get(user_id = id)
            serializer = UserSerializer(user)
            Response.status_code = status.HTTP_200_OK
           
            return Response(
               {
                  'status': status.HTTP_200_OK,
                  'message': 'user data retrieved successfully',
                  'data': serializer.data
               },
            )
         else:  
            Response.status_code = status.HTTP_400_BAD_REQUEST
            return Response(
               {
                  'status': status.HTTP_400_BAD_REQUEST,
                  'message': 'INVALID ID',
               },
            )  
      else:
         user = User.objects.all()
         serializer = UserSerializer(user, many = True)
         Response.status_code = status.HTTP_200_OK
         return Response(
            {
               'status': status.HTTP_200_OK,
               'message': 'user data retrieved successfully',
               'data': serializer.data
            },
         )
      
class UserUpdate(APIView):
   permission_classes = [IsAuthenticated]
   def patch(self, request, input, format = None):
      id = input
      if User.objects.filter(user_id = id).count() >= 1:
         user = User.objects.get(user_id = id)
         serializer = UserSerializer(user, data = request.data, partial = True)
         serializer.is_valid(raise_exception = True)
         serializer.save() 
         Response.status_code = status.HTTP_200_OK
         return Response(
            {
               'status': status.HTTP_200_OK,
               'message':'user details updated successfully',
            }, 
         )
      else:
          Response.status_code = status.HTTP_400_BAD_REQUEST
          return Response(
            {
               'status': status.HTTP_400_BAD_REQUEST,
               'message': 'Invalid ID',
            },
          )  
   
class UserDelete(APIView):
   permission_classes = [IsAuthenticated]
   def delete(self, request, input, format = None):
      id = input
      if User.objects.filter(user_id = id).count() >= 1:
         user=User.objects.get(user_id = id)
         user.delete()
         Response.status_code = status.HTTP_200_OK
         return Response(
            {
               'status': status.HTTP_200_OK,
               'message': 'user deleted successfully',
            },
         )  
      else: 
         Response.status_code = status.HTTP_400_BAD_REQUEST 
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
              if user.user_password == password:
                  token = get_tokens_for_user(user)
                  Response.status_code = status.HTTP_200_OK
                  return Response(
                  {
                     'status': status.HTTP_200_OK,
                     'message': 'user logged in  successfully',
                     'token': token,
                     'user_id': user.user_id,
                     'user_role':user.user_role

                   },
                      )  
              else:
                  Response.status_code = status.HTTP_400_BAD_REQUEST
                  return Response(
                  {
                     'status': status.HTTP_400_BAD_REQUEST,
                      'message': 'password mismatch',
                   },
                   )  
            else:
                Response.status_code = status.HTTP_400_BAD_REQUEST
                return Response(
                  {
                     'status': status.HTTP_400_BAD_REQUEST,
                      'message': 'Email is not verified please verify your email address',
                   },
                   )         
      else:  
           Response.status_code = status.HTTP_400_BAD_REQUEST        
           return Response(
                  {
                     'status': status.HTTP_400_BAD_REQUEST,
                      'message': 'email address is not registered',
                   },
                   )  

class UserVerificationView(APIView):
    serializer_class = UserProfileSerializer
    def post(self, request, format=None):
        token = request.POST.get('token')
        id = request.POST.get('user_id')
        print(id, token)
        user = User.objects.get(user_id=id)
        user.status = True
        Response.status_code = status.HTTP_200_OK
        return Response(
            {
                'status': status.HTTP_200_OK,
                'message': "User Verified",
            },
        )
