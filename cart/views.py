from django.shortcuts import render
from rest_framework.response import Response
from cart.serializer import CartSerializer
from rest_framework import status
from rest_framework.views import APIView
from cart.models import Cart
from rest_framework.generics import GenericAPIView,ListAPIView
from rest_framework.permissions import IsAuthenticated
from books_management_system.custom_paginations import CustomPagination
from rest_framework.filters import OrderingFilter
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from book.models import Book

class CartAdd(GenericAPIView):
   serializer_class = CartSerializer
   permission_classes = [IsAuthenticated]
   def post(self, request, format = None):
     
   
            serializer =CartSerializer(data = request.data)
            serializer.is_valid(raise_exception = True)
            serializer.save()
    

            return Response(
               {
                  'status': status.HTTP_200_OK,
                  'message': "cart item added  added is successfully "
               },
            )

class CartDelete(APIView):
   permission_classes = [IsAuthenticated]
   def delete(self, request, input, format = None):
      id = input
      if Cart.objects.filter(cart_id = id).count() >= 1:
         cart=Cart.objects.get(cart_id = id)
         cart.delete()
      
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
      
  
class CartView(ListAPIView):
   queryset = Cart.objects.all().order_by('created_at')
   serializer_class = CartSerializer
   filter_backends = [OrderingFilter, SearchFilter, DjangoFilterBackend]
   pagination_class = CustomPagination
   filterset_fields = ['cart_id', 'book_id','user_id']
   ordering_fields = ['created_at']
   search_fields = ['created_at']
  
   permission_classes = [IsAuthenticated]
   def list(self, request,id, *args, **kwargs):
        response_message = ""
        response_code = ""
        response = super().list(request, *args, **kwargs)
        cartss = []
        carts = Cart.objects.filter(user_id=id)
        for cart in carts:
            
            books_id = cart.book_id.book_id
            books = Book.objects.filter(book_id=books_id)
            for book in books:
                new_dict = {}
                new_dict = {'cart_id':cart.cart_id,'book_id': book.book_id,'title': book.title,'publication_date':book.publication_date,'ISBN':book.ISBN,'genre':book.genre,'cover_image':book.cover_image,'summary':book.summary,'price':book.price,'page_count':book.page_count,'rating':book.rating,'author':book.author,'edition':book.edition,'is_available':book.is_available,'is_ebook_available':book.is_ebook_available}
            cartss.append(new_dict)   
        return Response(
               {
                  'status': status.HTTP_200_OK,
                  'message': 'cart data retrieved successfully',
                  'data': cartss
               },
            )
class CartViewById(APIView):
    permission_classes = [IsAuthenticated] 
    def get(self, request, input = None, format = None):
      id = input
      
      if id is not None :
         if Cart.objects.filter(cart_id = id).count() >= 1:
            cart=Cart.objects.get(cart_id = id)
            serializer = CartSerializer(cart)
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

           