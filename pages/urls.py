from django.urls import path
from .views import HomePageView, AboutPageView



urlpatterns = [
    path('', HomePageView.as_view(),name='home'),
    path('create', AboutPage.as_view(), name='about'),
]

