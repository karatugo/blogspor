from django.db import models

# Create your models here.

class BlogPost(models.Model):
    # id = models.IntegerField() # primary key
    title = models.TextField()
    slug = models.SlugField() # hello world -> hello-world
    content = models.TextField(null=True, blank=True)
