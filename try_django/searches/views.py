from django.shortcuts import render
from django.db.models import Q

# Create your views here.
from django.contrib.auth.models import User 
from .models import SearchQuery
from blog.models import BlogPost




def search(request):
    query = request.GET.get('q',None)
    user = None
    posts = BlogPost.objects.filter(Q(title__icontains=query) | Q(slug__icontains=query) | Q(content__icontains=query) )
    if request.user.is_authenticated:
        user = request.user
    SearchQuery.objects.create(user=user,query=query)


    return render(request,'search/search.html',{'query':query,'posts':posts})

