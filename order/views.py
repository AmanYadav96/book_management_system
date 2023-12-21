from django.shortcuts import render
from rest_framework.response import Response
from order.serializer import OrderSerializer
from rest_framework import status
from rest_framework.views import APIView
from order.models import Order
from rest_framework.generics import GenericAPIView,ListAPIView
from rest_framework.permissions import IsAuthenticated
from books_management_system.custom_paginations import CustomPagination
from rest_framework.filters import OrderingFilter
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

class OrderAdd(GenericAPIView):
   permission_classes = [IsAuthenticated]
   serializer_class = OrderSerializer

   def post(self, request, format = None):
     
   
            serializer =OrderSerializer(data = request.data)
            serializer.is_valid(raise_exception = True)
            serializer.save()
    

            return Response(
               {
                  'status': status.HTTP_200_OK,
                  'message': "order is successfully "
               },
            )
   
class OrderView(ListAPIView):
   queryset = Order.objects.all().order_by('-order_date')
   serializer_class = OrderSerializer
   filter_backends = [OrderingFilter, SearchFilter, DjangoFilterBackend]
   pagination_class = CustomPagination
   filterset_fields = ['user_id','order_id','book_id','address_id','order_date','order_time','delivery_date','delivery_time']
   ordering_fields = ['-order_date','-order_time']
   search_fields = ['user_id','book_id','address_id','order_date','order_time']
  
   permission_classes = [IsAuthenticated]
   def list(self, request, *args, **kwargs):
        response_message = ""
        response_code = ""
        response = super().list(request, *args, **kwargs)
 
           
        return Response(
               {
                  'status': status.HTTP_200_OK,
                  'message': 'order data retrieved successfully',
                  'data': response.data
               },
            )
   
class OrderViewById(APIView):
   permission_classes = [IsAuthenticated]
   def get(self, request, input = None, format = None):
      id = input
      
      if Order.objects.filter(order_id = id).count() >= 1:
            order=Order.objects.get(order_id = id)
            serializer = OrderSerializer(order)
           
           
            return Response(
               {
                  'status': status.HTTP_200_OK,
                  'message': 'order data retrieved successfully',
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
    
      
class OrderUpdate(APIView):
   permission_classes = [IsAuthenticated]
   def patch(self, request, input, format = None):
      id = input
      if Order.objects.filter(order_id = id).count() >= 1:
         order = Order.objects.get(order_id = id)
         serializer = OrderSerializer(order, data = request.data, partial = True)
         serializer.is_valid(raise_exception = True)
         serializer.save() 

         return Response(
            {
               'status': status.HTTP_200_OK,
               'message':'order details updated successfully',
            }, 
         )
      else:
         
          return Response(
            {
               'status': status.HTTP_400_BAD_REQUEST,
               'message': 'Invalid ID',
            },
          )  
   
class OrderDelete(APIView):
   permission_classes = [IsAuthenticated]
   def delete(self, request, input, format = None):
      id = input
      if Order.objects.filter(order_id = id).count() >= 1:
         order=Order.objects.get(order_id = id)
         order.delete()
      
         return Response(
            {
               'status': status.HTTP_200_OK,
               'message': 'order deleted successfully',
            },
         )  
      else:  
         return Response(
            {
               'status': status.HTTP_400_BAD_REQUEST,
               'message':'Invalid ID',
            },
         )  
      
      