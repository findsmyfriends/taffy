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


from api.views import BloodTypeViewSet, ConversationViewSet, DaysOfWeekViewSet, GenderViewSet, GoldmemberViewSet,  HandlerViewSet, ImageViewSet, MemberProfileViewSet, NakSusViewSet, PersonalityViewSet, RaSiViewSet, TestesViewSet,   UserViewSet
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register(r'memberproflie', MemberProfileViewSet)
router.register(r'memberproflie', MemberProfileViewSet, basename='MemberProfile')
router.register(r'image', ImageViewSet, basename='Image')
router.register(r'user', UserViewSet)
router.register(r'bloodtype', BloodTypeViewSet)
router.register(r'daysofweek', DaysOfWeekViewSet)
router.register(r'naksus', NakSusViewSet)
router.register(r'rasi', RaSiViewSet)
router.register(r'gender', GenderViewSet)
router.register(r'testes', TestesViewSet) 
router.register(r'personality', PersonalityViewSet) 
router.register(r'handler', HandlerViewSet)
router.register(r'conversation', ConversationViewSet)
router.register(r'goldmember', GoldmemberViewSet, basename='Goldmember')
# router.register(r'update', UpdateMemberProfileViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('auth.url')),
    url(r'^', include(router.urls)),
    # path('update_memberprofile/<int:pk>/', UpdateMemberProfileView.as_view(), name='update_memberprofile'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)