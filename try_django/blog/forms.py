from django import forms
from .models import BlogPost 

class BlogPostForm(forms.Form):
    title = forms.CharField()
    images = forms.ImageField()
    slug = forms.SlugField()
    content = forms.CharField(widget=forms.Textarea)
  # pub_at = forms.DateTimeField()



#Model Forms
class BlogPostModelForm(forms.ModelForm):
    class Meta:
        model = BlogPost 
        fields = ['title','slug','content','images','pub_at']

    def clean_slug(self,*args, **kwargs):
        instance = self.instance

        slug = self.cleaned_data.get('slug')
        qs = BlogPost.objects.filter(slug=slug)
        if instance is not None:
            qs = qs.exclude(pk=instance.pk)
        if qs.exists():
            raise forms.ValidationError('This slug already we have')
        return slug 

