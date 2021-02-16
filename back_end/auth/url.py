from auth.views import *
from django.urls import path,include
from auth.views import *
# from django.contrib.auth import views
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.authtoken.views import obtain_auth_token
# from auth import views as user_views
from django.contrib.auth import views as authviews

urlpatterns = [
    # path('api-token-auth/', views.obtain_auth_token),
    # path('login/', MyObtainTokenPairView.as_view(), name='login'),
    # path('',include('djoser.urls')),
    # path('',include('djoser.urls.authtoken')),
    # path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
       # Authentication Urls
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('login/', authviews.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', authviews.LogoutView.as_view(template_name='auth/logout.html'), name='logout'),

    path('register/', RegisterView.as_view(), name='auth_register'),
    path('change_password/<int:pk>/', ChangePasswordView.as_view(), name='auth_change_password'),
    path('update_profile/<int:pk>/', UpdateProfileView.as_view(), name='auth_update_profile'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('', include('rest_auth.urls')),

]
