from django.shortcuts import render


def index(request):
    app = 'Articles'
    return render(request, 'article/index.html', context={'app': app})
# Create your views here.
