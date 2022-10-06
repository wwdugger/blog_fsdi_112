from django.urls import path
from .views import DraftListView, PostListView, PostCreateView, PostDetailView, PostDeleteView, PostUpdateView, DraftListView, ArchivedListView, SaleListView, ResourceListView, ExperienceListView, TwinListView


urlpatterns = [
    path('', PostListView.as_view(), name='list'),

    path('drafts/', DraftListView.as_view(), name="draft_list"),
    path('archived/', ArchivedListView.as_view(), name="archive_list"),
    path('sales/', SaleListView.as_view(), name="sale_list"),
    path('resources/', ResourceListView.as_view(), name="resource_list"),
    path('experiences/', ExperienceListView.as_view(), name="experience_list"),
    path('twins/', TwinListView.as_view(), name="twins_list"),

    path('<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('new/', PostCreateView.as_view(), name="new"),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='delete'),
]