from django.shortcuts import render
from rest_framework.response import Response
from order.serializer import OrderSerializer
from rest_framework import status
from rest_framework.views import APIView
from order.models import Order
from rest_framework.generics import GenericAPIView

class OrderAdd(GenericAPIView):
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
   
class OrderView(APIView):
   def get(self, request, input = None, format = None):
      id = input
      
      if id is not None :
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
      else:
         order = Order.objects.all()
         serializer = OrderSerializer(order, many = True)
       
         return Response(
            {
               'status': status.HTTP_200_OK,
               'message': 'order data retrieved successfully',
               'data': serializer.data
            },
         )
      
class OrderUpdate(APIView):
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
      
      