from django.urls import path
from hexlet_django_blog.article.views import Index


urlpatterns = [
    path("<str:tags>/<int:article_id>/", Index.as_view(), name="article"),
]
