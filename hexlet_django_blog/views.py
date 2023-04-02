from django.urls import reverse
from django.views.generic.base import TemplateView
from django.shortcuts import redirect, render


class HomePageView(TemplateView):

    def get(self, request):
        return redirect(reverse(
            'article', kwargs={'tags': 'python', 'article_id': 42})
        )


def about(request):
    return render(request, "about.html")
