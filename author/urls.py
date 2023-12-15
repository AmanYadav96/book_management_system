from django.contrib import admin
from django.urls import path
from author.views import *

urlpatterns = [
    path('add/',AuthorAdd.as_view(),name = 'author add'),
]
