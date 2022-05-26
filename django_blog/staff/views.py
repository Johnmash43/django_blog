from django.shortcuts import render
from blog.models import *
from django.http import JsonResponse

# Create your views here.



def dashboard(request):

    context = {}

    return render(request, "dashboard.html",context)


def categories(request):

    categories = Category.objects.all()

    context = {
        "categories" : categories
    }    
    return render(request,"category.html", context)


def articles(request):

    articles = Article.objects.all()

    context = {
        "articles" : articles
    }    
    return render(request,"articles.html", context)


def deleteArticle(request,id):

    try:
        article = Article.objects.get(pk = id)

    except Article.DoesNotExist:

        return JsonResponse({"success",False})

    article.delete()

    data = {
        "success": True
    }        

    return JsonResponse(data)

