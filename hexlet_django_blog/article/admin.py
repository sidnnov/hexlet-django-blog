from django.contrib import admin
from django.contrib.admin import DateFieldListFilter


# Register your models here.
from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'timestamp')
    search_fields = ['name', 'body']
    list_filter = (('timestamp', DateFieldListFilter),)


# admin.site.register(Article, ArticleAdmin)
