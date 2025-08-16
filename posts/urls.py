from django.urls import path
from .views import (
    PostListView   
)

urlpatterns = [
    path('list/', PostListView.as_view(), name="post_list"),
    path('new/', PostCreateView.as_view(), name="new_post")
    path('<int:pk>/', PostDetailView.as_view(), name="post_detail")
    path("int:pk>/delete/", PostDeleteView.as_view(), name="post_delete")
    path('<int:pk>/edit/', PostUpdateView.as_view(), name= "post_update")
]