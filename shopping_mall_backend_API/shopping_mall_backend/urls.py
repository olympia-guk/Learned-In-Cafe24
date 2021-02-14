"""shopping_mall_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="shopping mall backend API",
        default_version='v1',
        terms_of_service='https://www.google.com/policies/terms/',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger<str:format>', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('docs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('api/v1/members/', include('member.urls')),
    path('api/v1/malls/', include('mall.urls')),
    path('api/v1/categories/', include('category.urls')),
    path('api/v1/items/', include('item.urls')),
    path('api/v1/carts/', include('cart.urls')),
    path('api/v1/nonMembers/', include('non_member.urls')),
    path('api/v1/orders/', include('order.urls')),
    path('api/v1/orderItems/', include('order_item.urls')),
    path('api/v1/shippings/', include('shipping.urls')),

]