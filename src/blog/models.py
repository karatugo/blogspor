from django.conf import settings
from django.db import models

# Create your models here.
User = settings.AUTH_USER_MODEL

class BlogPost(models.Model): #blogpost_set -> queryset
    # id = models.IntegerField() # primary key
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True) # hello world -> hello-world
    content = models.TextField(null=True, blank=True)

    # >>> from django.contrib.auth import get_user_model
    # >>> User = get_user_model()
    # >>> User
    # <class 'django.contrib.auth.models.User'>
    # >>> User.objects.first().blogpost_set.all()
    # <QuerySet [<BlogPost: BlogPost object (1)>, <BlogPost: BlogPost object (2)>, <BlogPost: BlogPost object (3)>, <BlogPost: BlogPost object (4)>, <BlogPost: BlogPost object (5)>, <BlogPost: BlogPost object (6)>, <BlogPost: BlogPost object (7)>, <BlogPost: BlogPost object (8)>, <BlogPost: BlogPost object (9)>, <BlogPost: BlogPost object (10)>, <BlogPost: BlogPost object (11)>, <BlogPost: BlogPost object (12)>, <BlogPost: BlogPost object (13)>, <BlogPost: BlogPost object (14)>, <BlogPost: BlogPost object (15)>]>
    #
    # OR:
    #
    # >>> from blog.models import BlogPost
    # >>> qs = BlogPost.objects.filter(user__id=1)
    
    def get_absolute_url(self):
        return f"/blog/{self.slug}"

    def get_edit_url(self):
        return f"{self.get_absolute_url()}/edit"

    def get_delete_url(self):
        return f"{self.get_absolute_url()}/delete"