from django.shortcuts import render
from django.http import HttpResponseRedirect,JsonResponse
from .models import *
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.
def home(request):
    ##Tis returns a Queryset containing all articles in the database.
    articles = Article.objects.filter(Status = Article.LIVE).filter(created_at__year = 2022 )

    context = {
        "articles": articles
    }
    return render(request, "index.html", context)

def blog(request):
    articles = Article.objects.filter(Status = Article.LIVE)
    context = {
        "articles": articles
    }
    
    return render(request, "blog.html", context)

def about(request):
    context = {
      
    }
    return render(request, "about.html", context)


def contact(request):
    context = {
      
    }
    return render(request, "contact.html", context)    


def submitContactForm(request):

    if request.method == "POST":
       
       form_data = request.POST
       email = form_data["email"]
       name = form_data["name"]
       number = form_data["number"]
       message = form_data["message"]

      

       return HttpResponseRedirect("/form/success")
    
    else:
        return HttpResponseRedirect("/")  


def successRedirect(request):
    context = {
      
    }
    return render(request, "success.html", context)         


def ajaxContactSubmission(request):

    email= request.POST["email"]
    name= request.POST["name"]
    number= request.POST["number"]
    message = request.POST["message"]

    feedback = Feedback.objects.create(
           name = name,
           message = message,
           email = email
       )

    send_mail(
           "New message",
           "Hi admin,you have a new message",
           "admin@gmail.com",
           ['admin@gmail.com'],
           fail_silently=False,
       )

    context={
        "success": True,
        "message": "Thank you "+name+" for your message"
    }

    return JsonResponse(context)


def getArticleDetails(request, id):

    try:
        article = Article.objects.get(pk = id)

    except Article.DoesNotExist:

        messages.info(request,"Sorry, this article does not exist")    
        return HttpResponseRedirect("/")

    article = Article.objects.get(pk = id)
    categories = Category.objects.all()
    other_articles = Article.objects.exclude(pk = id)

    context = {
        "article" : article,
        "categories" : categories,
        "more_articles" : other_articles,
    }

    return render(request,"article-details.html", context)


def searchArticles(request):

    query = request.POST["query"]

    articles = Article.objects.filter(
        Status = Article.LIVE).filter(
            content__contains = query
        )

    context = {
        "articles" : articles
    }

    return render(request,"blog.html",context)


def redirectAfterLogin(request):

    if request.user.is_superuser:
        ##Redirect to the dashboard
        return HttpResponseRedirect("staff/dashboard")


    else:

        ##Redirect to blog/posts
        return HttpResponseRedirect("/blog")
                


    


