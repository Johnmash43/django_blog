from django.shortcuts import render
from  .models import Writer

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