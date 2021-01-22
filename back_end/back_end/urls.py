from django.contrib import admin
from django.urls import path ,include
from rest_framework import routers, serializers, viewsets
from api import views
from api.views import router
from api.models import *
from api import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
