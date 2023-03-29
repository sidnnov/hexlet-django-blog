# from django.shortcuts import render
from hexlet_django_blog.views import HomePageView


class ArticlePageView(HomePageView):

    template_name = 'article/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["app"] = "Article"
        return context


# def index(request):
#     app = 'Articles'
#     return render(request, 'article/index.html', context={'app': app})
