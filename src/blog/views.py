from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

# Create your views here.
from .forms import BlogPostModelForm
from .models import BlogPost

## C.R.U.D. operations
def blog_post_list_view(request):
    # list out objects
    # could be search
    qs = BlogPost.objects.all() #.published()
    # qs = BlogPost.objects.filter(publish_date__lte=timezone.now)
    template_name = "blog/list.html"
    context = {"object_list": qs}
    return render(request, template_name, context)

@staff_member_required
@login_required
def blog_post_create_view(request):
    # use django forms
    form = BlogPostModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        form = BlogPostModelForm()

    template_name = "form.html"
    context = {"form": form}
    return render(request, template_name, context)

def blog_post_detail_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = "blog/detail.html"
    context = {"object": obj}
    return render(request, template_name, context)

@staff_member_required
def blog_post_update_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    form = BlogPostModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    
    template_name = "form.html"
    context = {
        "title": "Update {}".format(obj.title), 
        "form": form
    }

    return render(request, template_name, context)

@staff_member_required
def blog_post_delete_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = "blog/delete.html"
    if request.method == "POST":
        obj.delete()
        return redirect("/blog")

    context = {"object": obj}
    return render(request, template_name, context)