
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from members import views as member_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Members urls
    path('', member_views.rating, name='index'),
    path('<int:pk>/', member_views.matched, name='matched'),
    path('admin/', admin.site.urls),
    path('admin/', admin.site.urls),
    path('match/',member_views.match,name='match_page'),
    path('testtem/',member_views.testtem,name='Template'),
    path('testtem/<int:pk>/',member_views.testmatch,name='testmatch'),
    path('anode/', member_views.anode,name='anode'),
    path('cathode/', member_views.cathode,name='cathode'),
    path('rating/', member_views.rating, name='rating'),
    path('profile/<int:pk>/',member_views.ProfileDetailView.as_view(),name='profile_detail'),
    path('match/like/', member_views.MatchCreateView.as_view(), name='match_create'),
    path('match/<int:pk>/', member_views.MatchDetailView.as_view(), name='match_detail'),
   
    # API urls
    path('api-taffy/', include('taffy.api.urls')),

    # Taffy urls
    path('public/', include('taffy.urls')),
    # path('message/(?P<username>.+)/$', member_views.message, name='message'),
    
    # Authentication Urls
    path('register/', member_views.register, name='register'),
    path('profile/', member_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='members/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='members/logout.html'), name='logout'),
    
    # Resete Password Urls
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='members/password_reset.html'), name='password_reset'),
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='members/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='members/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='members/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete', auth_views.PasswordResetCompleteView.as_view(
        template_name='members/password_reset_complete.html'), name='password_reset_complete'),
    # Change Password Urls
    path('password-change/', auth_views.PasswordChangeView.as_view(
        template_name='members/password_change.html'), name='password_change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='members/password_change_done.html'), name='password_change_done'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

    path('', include('taffy.urls')),
