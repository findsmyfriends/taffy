from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    add_comment, 
    # ProfileListView,
    # profileMember
)


urlpatterns = [
    # path('', PostListView.as_view(), name='index'),
    # path('', profileMember, name='index'),
    path('testtem/',views.testtem,name='Template'),
    path('anode/', views.anode,name='anode'),
    path('cathode/', views.cathode,name='cathode'),
    path('rating/', views.rating, name='rating'),
    path('', views.rating, name='index'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user_posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('about/', views.about, name='about'),
    path('post/<int:pk>/comment/', add_comment, name='add_comment'),
    
]
