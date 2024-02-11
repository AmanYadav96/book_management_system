from django.contrib import admin
from django.urls import path
from order.views import *

urlpatterns = [
    path('add/',OrderAdd.as_view(),name = 'order add'),
    path('view/',OrderView.as_view(),name = 'order view'),
    path('view/<uuid:id>/',OrderViewByUser.as_view(),name = 'order view'),
    path('view/<uuid:input>/',OrderViewById.as_view(),name = 'order view by id'),
    path('update/<uuid:input>/',OrderUpdate.as_view(),name = 'order update by id'),
    path('delete/<uuid:input>/',OrderDelete.as_view(),name = 'order delete by id'),
]
