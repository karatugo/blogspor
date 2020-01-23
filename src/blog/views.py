from django.http import Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .forms import BlogPostForm
from .models import BlogPost

## C.R.U.D. operations
def blog_post_list_view(request):
    # list out objects
    # could be search
    qs = BlogPost.objects.all()
    template_name = "blog/list.html"
    context = {"object_list": qs}
    return render(request, template_name, context)

def blog_post_create_view(request):
    # use django forms
    form = BlogPostForm(request.POST or None)
    if form.is_valid():
        obj = BlogPost.objects.create(**form.cleaned_data)
        form = BlogPostForm()

    template_name = "form.html"
    context = {"form": form}
    return render(request, template_name, context)

def blog_post_detail_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = "blog/detail.html"
    context = {"object": obj}
    return render(request, template_name, context)

def blog_post_update_view(request):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = "blog/update.html"
    context = {"object": obj, "form": None}
    return render(request, template_name, context)

def blog_post_delete_view(request):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = "blog/delete.html"
    context = {"object": obj}
    return render(request, template_name, context)