from django.db import models

# Create your models here.

from django.contrib.auth.models import User


class SearchQuery(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    query = models.CharField(max_length=120)
    timestamp = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = ("search")
        verbose_name_plural = ("search")

    def __str__(self):
        return self.query

    
