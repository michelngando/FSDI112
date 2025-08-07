from django.urls import path
from .views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('home/', HomePageView.as_view, name="homeTwo"),
    path('about/', HomePageView.as_view, name="about" ),
]