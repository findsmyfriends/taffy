from django.urls import path,include
from auth.views import *
# from django.contrib.auth import views
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # path('api-token-auth/', views.obtain_auth_token),
    # path('login/', MyObtainTokenPairView.as_view(), name='login'),
    # path('',include('djoser.urls')),
    # path('',include('djoser.urls.authtoken')),
    # path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('change_password/<int:pk>/', ChangePasswordView.as_view(), name='auth_change_password'),
    path('update_profile/<int:pk>/', UpdateProfileView.as_view(), name='auth_update_profile'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('', include('rest_auth.urls')),

]
