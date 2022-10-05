from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView
)

urlpatterns = [
    path('', PostListView.as_view(), name='list'),
    path('new/', PostCreateView.as_view(), name='new'),
    path('<int:pk>/', PostDetailView.as_view(), name='detail'),
]