from django.urls import path

from .views import LikeToggleAPIView, NopeToggleAPIView

urlpatterns = [
    path('<int:pk>/like/', LikeToggleAPIView.as_view(), name='like_api'),
    path('<int:pk>/nope/', NopeToggleAPIView.as_view(), name='nope_api')
]
