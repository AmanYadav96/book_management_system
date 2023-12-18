from django.contrib import admin
from django.urls import path
from author.views import *

urlpatterns = [
    path('add/',AuthorAdd.as_view(),name = 'author add'),
    path('view/',AuthorView.as_view(),name = 'author view'),
    path('view/<uuid:input>/',AuthorView.as_view(),name = 'author view by id'),
    path('update/<uuid:input>/',AuthorUpdate.as_view(),name = 'author update by id'),
    path('delete/<uuid:input>/',AuthorDelete.as_view(),name = 'author delete by id'),
]
