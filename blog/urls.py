from django.urls import path 
from .views import (BlogView,
PostView,
AddPostView,
DeleteView,
UpdatePostView,
HomeView,
MyPostsView,
CategoryView
)


urlpatterns = [
    path('', HomeView, name="homeview"),
    path('blog/', BlogView, name="blogview"),
    path('blog/post/<int:pk>/', PostView, name="postview"),
    path('blog/posts/add/', AddPostView, name="addpostview"),
    path('blog/post/delete/<int:pk>/', DeleteView, name="deleteview"),
    path('blog/post/update/<int:pk>/', UpdatePostView, name="updatepostview"),
    path('blog/posts/my-posts/', MyPostsView, name="mypostsview"),
    path('blog/categories/', CategoryView, name="categoryview"),
]