from django.contrib import admin
from django.urls import path
from book.views import *

urlpatterns = [
    path('add/',BookAdd.as_view(),name = 'book add'),
    path('view/',BookView.as_view(),name = 'book view'),
    path('view/<uuid:input>/',BookViewById.as_view(),name = 'book view by id'),
    path('update/<uuid:input>/',BookUpdate.as_view(),name = 'book update by id'),
    path('delete/<uuid:input>/',BookDelete.as_view(),name = 'book delete by id'),
]
