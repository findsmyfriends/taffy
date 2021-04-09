
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from members import views as member_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Members urls
    path('', member_views.RatingView.as_view(
        template_name='members/member_all.html'), name='member_all'),
    path('admin/', admin.site.urls),
    path('match/', member_views.match, name='Match Page'),
    path('anode/', member_views.anode, name='anode'),
    path('cathode/', member_views.cathode, name='cathode'),
    path('all/', member_views.ShowProfileAllView.as_view(
        template_name='members/rate.html'), name='profile'),
    # path('test/', member_views.TestView.as_view(
    #     template_name='members/test.html'), name='test'),
    # path('', member_views.rating, name='rating'),

    # API urls
    path('api-taffy/', include('taffy.api.urls')),

    # Taffy Post urls
    path('public/', include('taffy.urls')),
    # path('message/(?P<username>.+)/$', member_views.message, name='message'),

    # Authentication Urls
    path('register/', member_views.register, name='register'),
    path('profile/', member_views.profile, name='profile'),
    path('login/', member_views.LoginView.as_view(
        template_name='members/wellcome.html'), name='login'),
    path('logout/', member_views.logout_views, name='logout'),

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

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,
#                           document_root=settings.MEDIA_ROOT)

#     path('', include('taffy.urls')),
if settings.DEBUG:
    # import debug_toolbar
    # urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
