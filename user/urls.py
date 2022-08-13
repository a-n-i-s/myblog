from django.urls import path
from .views import AuthorRequestView,AuthorDetailView,authorrequeststatus,AuthorUpdateView
urlpatterns=[
  path('author/<int:pk>',AuthorDetailView.as_view(),name='author_detail'),
  path('author/e/<int:pk>',AuthorUpdateView.as_view(),name='author_update'),
  path('author/create',AuthorRequestView.as_view(),name='author_create'),
  path('author/request/<int:pk>',authorrequeststatus,name='authorrequest_status')
]