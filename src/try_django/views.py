from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    title = "Hello, there."
    return render(request, "home_page.html", {"title": title})

def about_page(request):
    title = "About"
    return render(request, "home_page.html", {"title": title})

def contact_page(request):
    title = "Contact"
    return render(request, "home_page.html", {"title": title})