from django.contrib import admin
from django.urls import path
from user.views import *

urlpatterns = [
    path('register/',UserRegister.as_view(),name = 'user add'),
    path('view/',UserView.as_view(),name = 'book view'),
    path('view/<uuid:input>/',UserView.as_view(),name = 'book view by id'),
    path('update/<uuid:input>/',UserUpdate.as_view(),name = 'book update by id'),
    path('delete/<uuid:input>/',UserDelete.as_view(),name = 'book delete by id'),
    path('login/',UserLogin.as_view(),name = 'user login'),
]