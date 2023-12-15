from rest_framework.response import Response
from address.serializer import AddressSerializer
from rest_framework import status
from rest_framework.views import APIView
from .models import Address
from rest_framework.generics import GenericAPIView

# Create your views here.
class AddressAdd(GenericAPIView):
    serializer_class = AddressSerializer
    def post(self, request,format=None):
       
            serializer = AddressSerializer(data = request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(
               {
                  'status': status.HTTP_200_OK,
                  'message': "address is successfully Added"
               },
            )
        
   
class AddressView(APIView):
   def get(self, request, input = None, format = None):
      id = input
      print(id)
      if id is not None :
         if Address.objects.filter(address_id = id).count() >= 1:
            address=Address.objects.get(address_id = id)
            serializer = AddressSerializer(address)
           
           
            return Response(
               {
                  'status': status.HTTP_200_OK,
                  'message': 'address data retrieved successfully',
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
         address = Address.objects.all()
         serializer = AddressSerializer(address, many = True)
       
         return Response(
            {
               'status': status.HTTP_200_OK,
               'message': 'address data retrieved successfully',
               'data': serializer.data
            },
         )
      
class AddressUpdate(APIView):
   def patch(self, request, input, format = None):
      id = input
      if Address.objects.filter(address_id = id).count() >= 1:
         address = Address.objects.get(address_id = id)
         serializer = AddressSerializer(address, data = request.data, partial = True)
         serializer.is_valid(raise_exception = True)
         serializer.save() 

         return Response(
            {
               'status': status.HTTP_200_OK,
               'message':'address details updated successfully',
            }, 
         )
      else:
         
          return Response(
            {
               'status': status.HTTP_400_BAD_REQUEST,
               'message': 'Invalid ID',
            },
          )  
   
class AddressDelete(APIView):
   def delete(self, request, input, format = None):
      id = input
      if Address.objects.filter(address_id = id).count() >= 1:
         address=Address.objects.get(address_id = id)
         address.delete()
      
         return Response(
            {
               'status': status.HTTP_200_OK,
               'message': 'address deleted successfully',
            },
         )  
      else:  
         return Response(
            {
               'status': status.HTTP_400_BAD_REQUEST,
               'message':'Invalid ID',
            },
         )  