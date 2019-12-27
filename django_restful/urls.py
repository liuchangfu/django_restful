"""django_restful URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from api import views
from rest_framework_swagger.views import get_swagger_view
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer

routers = routers.DefaultRouter()
routers.register('users', views.UserViewSet)
routers.register('groups', views.GroupViewSet)

schema_view = get_schema_view(title='api_docs', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])
# schema_view = get_swagger_view(title='api')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(routers.urls)),
    path('api_auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api_docs/', schema_view),
]
