from django.contrib import admin
from django.urls import path
from cart.views import *

urlpatterns = [
    path('add/',CartAdd.as_view(),name = 'order history add'),
    path('view/',CartView.as_view(),name = 'order view'),
    path('view/<uuid:input>/',CartView.as_view(),name = 'order view by id'),
    path('delete/<uuid:input>/',CartDelete.as_view(),name = 'order history delete by id'),
]
