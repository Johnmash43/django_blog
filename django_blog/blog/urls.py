from django.urls import path
from .views import *

urlpatterns = [
    path('',home, name="home"),
    path('blog',blog, name="blog"),
    path('about',about, name="about"),
    path('contact',contact, name="contact"),
    path('contact/form/submit',submitContactForm, name="contact.form"),
    path('form/success',successRedirect, name="contact.redirect"),
]