
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from members import views as member_views
from members import tests
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Taffy ADMIN urls
    path('admin/', admin.site.urls),

    # Members urls

    path('', member_views.GetRatingView.as_view(
        template_name='members/member_all.html'), name='member_all'),
    path('match/', member_views.match, name='Match Page'),
    path('setting/', member_views.setting_view, name='setting'),

    # Members urls for tests.py
    path('test/', tests.tests, name='test'),


    # Test urls

    # path('test/', member_views.MemberProfileUpdateView.as_view(
    #     template_name='members/profile.html'), name='profile'),
    # path('all/', member_views.ShowProfileAllView.as_view(
    #     template_name='members/rate.html'), name='profile'),


    # API urls

    path('api-taffy/', include('taffy.api.urls')),

    # taffy Post urls

    path('public/', include('taffy.urls')),


    # Authentication Urls

    path('register/', member_views.RegisterView.as_view(
        template_name='members/register.html'), name='register'),
    path('login/', member_views.LoginView.as_view(
        template_name='members/wellcome.html'), name='login'),
    path('logout/', member_views.logout_views, name='logout'),
    path('profile/', member_views.profile, name='profile'),

    # path('profile/', member_views.MemberProfileUpdateView.as_view(
    #     template_name='members/profile.html'), name='profile'),



    # Resete Password Urls

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
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     # import debug_toolbar
#     # urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
#     urlpatterns += static(settings.MEDIA_URL,
#                           document_root=settings.MEDIA_ROOT)

