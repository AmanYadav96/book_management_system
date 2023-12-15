from django.contrib import admin
from django.urls import path
from address.views import *

urlpatterns = [
    path('add/',AddressAdd.as_view(),name = 'address add'),
    path('view/',AddressView.as_view(),name = 'address view'),
    path('view/<uuid:input>/',AddressView.as_view(),name = 'address view by id'),
    path('update/<uuid:input>/',AddressUpdate.as_view(),name = 'address update by id'),
    path('delete/<uuid:input>/',AddressDelete.as_view(),name = 'address delete by id'),
]
