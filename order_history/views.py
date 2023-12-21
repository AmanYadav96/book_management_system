from django.shortcuts import render
from rest_framework.response import Response
from order_history.serializer import OrderHistorySerializer
from rest_framework import status
from rest_framework.views import APIView
from order_history.models import OrderHistory
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated

class OrderHistoryAdd(GenericAPIView):
   serializer_class = OrderHistorySerializer
   permission_classes = [IsAuthenticated]

   def post(self, request, format = None):
     
   
            serializer =OrderHistorySerializer(data = request.data)
            serializer.is_valid(raise_exception = True)
            serializer.save()
    

            return Response(
               {
                  'status': status.HTTP_200_OK,
                  'message': "order history added is successfully "
               },
            )
   
class OrderHistoryView(APIView):
   
   def get(self, request, input = None, format = None):
      id = input
      permission_classes = [IsAuthenticated]
      if id is not None :
         if OrderHistory.objects.filter(order_id = id).count() >= 1:
            order_history=OrderHistory.objects.get(history_id = id)
            serializer = OrderHistorySerializer(order_history)
           
           
            return Response(
               {
                  'status': status.HTTP_200_OK,
                  'message': 'order history data retrieved successfully',
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
         order_history = OrderHistory.objects.all()
         serializer = OrderHistorySerializer(order_history, many = True)
       
         return Response(
            {
               'status': status.HTTP_200_OK,
               'message': 'order history data retrieved successfully',
               'data': serializer.data
            },
         )
      
class OrderHistoryUpdate(APIView):
   permission_classes = [IsAuthenticated]
   def patch(self, request, input, format = None):
      id = input
      if OrderHistory.objects.filter(history_id = id).count() >= 1:
         order_history = OrderHistory.objects.get(history_id = id)
         serializer = OrderHistorySerializer(order_history, data = request.data, partial = True)
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
   
class OrderHistoryDelete(APIView):
   permission_classes = [IsAuthenticated]
   def delete(self, request, input, format = None):
      id = input
      if OrderHistory.objects.filter(history_id = id).count() >= 1:
         order_history=OrderHistory.objects.get(history_id = id)
         order_history.delete()
      
         return Response(
            {
               'status': status.HTTP_200_OK,
               'message': 'order history deleted successfully',
            },
         )  
      else:  
         return Response(
            {
               'status': status.HTTP_400_BAD_REQUEST,
               'message':'Invalid ID',
            },
         )  
      
      