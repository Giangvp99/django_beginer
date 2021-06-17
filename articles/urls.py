from django.urls import path

from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleEditView,
    ArticleDeleteView,
    ArticleCreateView,
)

app_name = "articles"
urlpatterns = [
    path("new/", ArticleCreateView.as_view(), name="new"),
    path("<int:pk>/edit/", ArticleEditView.as_view(), name="edit"),
    path("<int:pk>/delete/", ArticleDeleteView.as_view(), name="delete"),
    path("<int:pk>/", ArticleDetailView.as_view(), name="detail"),
    path("", ArticleListView.as_view(), name="list"),
]
