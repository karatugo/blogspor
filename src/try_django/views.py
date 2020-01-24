from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

from .forms import ContactForm
from blog.models import BlogPost

def home_page(request):
    title = "Hello, there."
    qs = BlogPost.objects.all()[:5]
    context = {
        "title": "Welcome to Try Django", 
        "blog_list": qs
    }

    return render(request, "home.html", context)

def about_page(request):
    title = "About"
    context = {"title": title}
    return render(request, "home_page.html", context)

def contact_page(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm()

    title = "Contact us"
    context = {
        "title": title, 
        "form": form
        }
    return render(request, "form.html", context)

def example_page(request):
    context = {"title": "example"}
    template_name = "title.txt"
    template_obj = get_template (template_name)
    rendered_string = template_obj.render(context)
    return HttpResponse(rendered_string)