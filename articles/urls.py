from django.urls import path
from .views import (
    ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, 
    ArticleDeleteView, CommentCreateView, CommentDeleteView, LikeToggleView
)

app_name = 'articles'

urlpatterns = [
    path('', ArticleListView.as_view(), name='index'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='detail'),
    path('new/', ArticleCreateView.as_view(), name='create'),
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='delete'),
    path('<int:pk>/comments/', CommentCreateView.as_view(), name='comments_create'),
    path('<int:article_pk>/comments/<int:comment_pk>/delete/', CommentDeleteView.as_view(), name='comments_delete'),
    path('<int:article_pk>/like/', LikeToggleView.as_view(), name='likes'),
]
