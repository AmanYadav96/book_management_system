"""books_management_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.views.generic import TemplateView

get_schema_view = get_schema_view(
    openapi.Info(
        title="Hospital Management System",
        default_version='v1',),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include([path('api_schema', get_schema_view.as_view(), name="api_schema"),path('docs/', TemplateView.as_view(template_name='docs.html',extra_context={'schema_url': 'api_schema'}), name='docs'),
    path('api/book/',include('book.urls')),
    path('api/author/',include('author.urls')),
    path('api/user/',include('user.urls')),
    path('api/order/',include('order.urls')),
    path('api/address/',include('address.urls')),
    path('api/order_history/',include('order_history.urls')),
    path('api/cart/',include('cart.urls')),
      ]))
]

