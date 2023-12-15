from django.contrib import admin
from django.urls import path
from order_history.views import *

urlpatterns = [
    path('add/',OrderHistoryAdd.as_view(),name = 'order history add'),
    path('view/',OrderHistoryView.as_view(),name = 'order history view'),
    path('view/<uuid:input>/',OrderHistoryView.as_view(),name = 'order history view by id'),
    path('update/<uuid:input>/',OrderHistoryUpdate.as_view(),name = 'order history update by id'),
    path('delete/<uuid:input>/',OrderHistoryDelete.as_view(),name = 'order history delete by id'),
]
