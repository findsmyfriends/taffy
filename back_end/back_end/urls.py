"""back_end URL Configuration

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
from api.views import *
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'memberproflie', MemberProfileViewSet)
# router.register(r'memberproflie', MemberProfileViewSet, basename='MemberProfile')
# router.register(r'image', ImageViewSet, basename='Image')
router.register(r'image', ImageViewSet)
router.register(r'user', UserViewSet,basename='User')
router.register(r'bloodtype', BloodTypeViewSet)
router.register(r'daysofweek', DaysOfWeekViewSet)
router.register(r'naksus', NakSusViewSet)
router.register(r'rasi', RaSiViewSet)
router.register(r'gender', GenderViewSet)
router.register(r'testes', TestesViewSet) 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('auth.url')),
    url(r'^', include(router.urls)),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)