from django.urls import path
from .views import PostDetail, PostList,AuthorDetail,AuthorList
urlpatterns = [
    path('posts/',PostList.as_view(),name='posts'),
    path('post/<int:pk>/',PostDetail.as_view(),name='post-detail'),
    path('authors/',AuthorList.as_view(),name='authors'),
    path('author/<int:pk>/',AuthorDetail.as_view(),name='author-detail'),
]
