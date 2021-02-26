from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    # PostDeleteView,
    UserPostListView,
    # ProfileListView,
    add_comment, rating,
    # profileMember
)


urlpatterns = [
    # path('', PostListView.as_view(), name='index'),
    path('', views.rating, name='index'),
    # path('', profileMember, name='index'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user_posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    # path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('about/', views.about, name='about'),
    path('post/<int:pk>/comment/', add_comment, name='add_comment'),
    path('rating/',views.rating, name="testes rating")
]
