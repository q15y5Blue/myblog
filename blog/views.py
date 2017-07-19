from django.shortcuts import render
from django.http import HttpResponse
from . import models


def index(request):
    articles = models.Article.objects.all()
    # 三个参数1 request， 2、Templates（html）路径 3 、参数{dict}
    return render(request, 'index.html', {'articles':  articles})


# 根据ID获取 article 的值
def aticle_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'article_page.html', {'article': article})


def edit_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'edit_page.html', {'article': article})


def edit_action(request):
    title= request.POST.get('title','TITLE')
    content = request.POST.get('content','CONTENT')
    models.Article.objects.create(title=title,content=content)
    # return index(request)
    articles = models.Article.objects.all()
    return render(request, 'index.html', {'articles': articles})