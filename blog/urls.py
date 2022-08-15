from multiprocessing.spawn import import_main_path
from django.urls import path
from .views import (
                    CommentCreateView,
                    PostDetailView,
                    PostListView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView,
                    CommentCreateView,
                    CommentUpdateView,
                    CommentDeleteView,
                    CatagoryDetailView,
                    )
urlpatterns = [
    path('',PostListView.as_view(),name='homepage'),
    path('posts/',PostListView.as_view(),name='post_list'),
    path('post/<int:pk>',PostDetailView.as_view(),name='post_detail'),
    path('post/create',PostCreateView.as_view(),name='post_create'),
    path('post/e/<int:pk>',PostUpdateView.as_view(),name='post_update'),
    path('post/delete/<int:pk>',PostDeleteView.as_view(),name='post_delete'),
    
   

    path('post/<int:pk>/makecomment',CommentCreateView.as_view(),name='comment_create'),
    path('comment/e/<int:pk>',CommentUpdateView.as_view(),name='comment_update'),
    path('comment/delete/<int:pk>',CommentDeleteView.as_view(),name='comment_delete'),
   
    path('catagories/<int:pk>',CatagoryDetailView.as_view(),name='catagory_detail'),
]
