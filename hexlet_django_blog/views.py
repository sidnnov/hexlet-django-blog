from django.urls import reverse
from django.views.generic.base import TemplateView
from django.shortcuts import redirect, render


class HomePageView(TemplateView):

    def get(self, request):
        return render(request, 'index.html')


def about(request):
    return render(request, "about.html")
