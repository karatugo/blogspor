from django import forms
from .models import BlogPost

# class BlogPostForm(forms.Form):
#     title = forms.CharField()
#     slug = forms.SlugField()
#     content = forms.CharField(widget=forms.Textarea)

class BlogPostModelForm(forms.ModelForm):
    # title = forms.CharField()
    class Meta:
        model = BlogPost
        fields = ["title", "slug", "content", "publish_date"]

    def clean_title(self, *args, **kwargs):
        # print(dir(self))
        instance = self.instance
        print(instance)
        title = self.cleaned_data.get("title")
        qs = BlogPost.objects.filter(title__iexact=title)
        # print(qs)
        if instance is not None:
            qs = qs.exclude(pk=instance.pk)

        if qs.exists():
            raise forms.ValidationError("This title is in use")

        return title
