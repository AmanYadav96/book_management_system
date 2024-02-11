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
from book.models import Book

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
   
class OrderViewByUser(ListAPIView):
   queryset = Order.objects.all().order_by('order_date')
   serializer_class = OrderSerializer
   filter_backends = [OrderingFilter, SearchFilter, DjangoFilterBackend]
   pagination_class = CustomPagination
   filterset_fields = ['order_id', 'book_id','user_id']
   ordering_fields = ['order_date']
   search_fields = ['order_date']
  
   permission_classes = [IsAuthenticated]
   def list(self, request,id, *args, **kwargs):
        response_message = ""
        response_code = ""
        response = super().list(request, *args, **kwargs)
        orders = []
        orderss = Order.objects.filter(user_id=id)
        for order in orderss:
            print(order)
            # books_id = order.book_id.book_id
            # books = Book.objects.filter(book_id=books_id)
            # for book in books:
            #     new_dict = {}
            #     new_dict = {'order_id':order.order_id,'book_id': book.book_id,'title': book.title,'publication_date':book.publication_date,'ISBN':book.ISBN,'genre':book.genre,'cover_image':book.cover_image,'summary':book.summary,'price':book.price,'page_count':book.page_count,'rating':book.rating,'author':book.author,'edition':book.edition,'is_available':book.is_available,'is_ebook_available':book.is_ebook_available,'order_date':order.order_date,'order_time':order.order_time}
            # orders.append(new_dict)   
        return Response(
               {
                  'status': status.HTTP_200_OK,
                  'message': 'cart data retrieved successfully',
                  'data': response.data
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
      
      