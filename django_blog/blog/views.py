from django.shortcuts import render
from  .models import Writer
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    user= Writer("Cynthia","Wangari")    

    context = {
        'first_name':'John',
        'last_name':'Mash',
        "writer": user
    }
    return render(request, "index.html", context)

def blog(request):
    context = {
      
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
       number = form_dat["number"]
       message = form_data["message"]


       return HttpResponseRedirect("/form/success")
    
    else:
        return HttpResponseRedirect("/")  


def successRedirect(request):
    context = {
      
    }
    return render(request, "success.html", context)         


    


