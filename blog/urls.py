from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blogs/', views.BlogListView.as_view(), name='blog-list'),
    path('blog/new/', views.BlogCreateView.as_view(), name='blog-create'),
    path('blog/<int:pk>/edit/', views.BlogUpdateView.as_view(), name='blog-update'),
    path('blog/<int:pk>/delete/', views.BlogDeleteView.as_view(), name='blog-delete'),
] 