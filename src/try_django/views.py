from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

def home_page(request):
    title = "Hello, there."
    context = {"title": title}
    return render(request, "home.html", context)

def about_page(request):
    title = "About"
    context = {"title": title}
    return render(request, "home_page.html", context)

def contact_page(request):
    title = "Contact"
    context = {"title": title}
    return render(request, "home_page.html", context)

def example_page(request):
    context = {"title": "example"}
    template_name = "title.txt"
    template_obj = get_template (template_name)
    rendered_string = template_obj.render(context)
    return HttpResponse(rendered_string)