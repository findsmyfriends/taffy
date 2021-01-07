from django.contrib import admin
from django.urls import path ,include
from rest_framework import routers, serializers, viewsets
from api.models import *
from api import views


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'is_staff']


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


### -----------------
class BloodTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BloodType
        fields = ['id', 'bloodtype']


class BloodTypeViewSet(viewsets.ModelViewSet):
    queryset = BloodType.objects.all()
    serializer_class = BloodTypeSerializer


### -----------------
# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
router.register(r'bloodtype', BloodTypeViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
