from django.contrib import admin
from django.urls import path
from cart.views import *

urlpatterns = [
    path('add/',CartAdd.as_view(),name = 'cart add'),
    path('view/<uuid:id>',CartView.as_view(),name = 'cart view'),
    # path('view/<uuid:input>',CartView.as_view(),name = 'order view'),
    path('view/<uuid:input>/',CartViewById.as_view(),name = 'cart view by id'),
    path('delete/<uuid:input>/',CartDelete.as_view(),name = 'cart delete by id'),
]
