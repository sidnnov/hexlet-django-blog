from django.urls import path
from hexlet_django_blog.article.views import index


urlpatterns = [
    path("<str:tags>/<int:article_id>/", index, name="article"),
]
