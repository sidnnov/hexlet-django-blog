from django.shortcuts import render
from django.views import View


from hexlet_django_blog.article.models import Article


class IndexView(View):

    template_name = 'article/index.html'

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'articles/index.html', context={
            'articles': articles,
        })

# def index(request, tags, article_id):
#     return render(
#         request,
#         "article/index.html",
#         context={'article_id': article_id, 'tags': tags}
#     )
