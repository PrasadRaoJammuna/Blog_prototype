from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone 
from django.db import models

#User = settings.AUTH_USER_MODEL

# Create your models here.

class BlogPostQuerySet(models.QuerySet):
    def published(self):
        now = timezone.now()
        return self.filter(pub_at__lte=now)


class BlogPostManager(models.Manager):
    def get_queryset(self):
        return BlogPostQuerySet(self.model,using=self._db)

    def published(self):
        return self.get_queryset().published()





class BlogPost(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100,unique=True)
    content = models.TextField(blank=True,null=True)
    slug = models.SlugField(default='before slugField')
    images = models.ImageField(upload_to='image/',blank=True,null=True)
    pub_at = models.DateTimeField(auto_now=False,auto_now_add=False,null=True,blank=True)
    timestampp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = BlogPostManager()

    class Meta:
        ordering =['-pub_at','-updated','-timestampp']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/blog/{self.slug}"

    def get_edit_url(self):
        return f"{self.get_absolute_url}/update"

    def get_delete_url(self):
        return f"{self.get_absolute_url}/delete"
    
    
    


