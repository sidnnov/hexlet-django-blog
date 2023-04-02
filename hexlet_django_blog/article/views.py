# from django.shortcuts import render
from django.shortcuts import render
# from hexlet_django_blog.views import HomePageView


# class Index(HomePageView):

#     template_name = 'article/index.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         tags = kwargs.get('tags')
#         article_id = kwargs.get('article_id')
#         context["tags"] = tags
#         context["article_id"] = article_id
#         return context

def index(request, tags, article_id):
    return render(
        request,
        "article/index.html",
        context={'article_id': article_id, 'tags': tags}
    )
