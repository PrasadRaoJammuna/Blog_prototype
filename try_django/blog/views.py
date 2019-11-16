from django.shortcuts import render,redirect,Http404,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import BlogPost
from .forms import BlogPostForm,BlogPostModelForm

# Create your views here.

def blog_post(request):
   # posts = get_object_or_404(BlogPost,)
    posts = BlogPost.objects.all().published()
    return render(request,'blog/blog.html',{'posts':posts})

def post_detail(request,slug):
    try:
        post = BlogPost.objects.filter(slug=slug)
    except BlogPost.DoesNotExist:
        raise Http404
    except ValueError:
        raise Http404
    
    #post = get_object_or_404(BlogPost,slug=slug)
    return render(request,'blog/post.html',{'post':post})


@login_required
def post_create(request):
    #form = BlogPostForm(request.POST or None)
    form = BlogPostModelForm(request.POST or None ,request.FILES or None)
    if form.is_valid():
       #method-1: obj = BlogPost.objects.create(**form.cleaned_data)
       
       obj = form.save(commit=False)
       obj.user = request.user
       #obj.title = form.cleaned_data.get('title')
       #obj.slug = form.cleaned_data.get('slug')
       #obj.content = form.cleaned_data.get('content')
       obj.save()

       form = BlogPostModelForm()

    context ={'form':form,'title':'New Post'}
    template = 'blog/post_create.html'

    return render(request,template,context)


@login_required
def post_update(request,slug):
    obj = get_object_or_404(BlogPost,slug=slug)
    form = BlogPostModelForm(request.POST or None,request.FILES or None,instance=obj)
    if form.is_valid():
        form.save()
    return render(request,'blog/post_create.html',{'form':form,'title':'Post Update'})



@login_required
def delete_post(request,slug):
    obj = get_object_or_404(BlogPost,slug=slug)
    #if request.method == 'POST':
    #obj.delete() #we can create a template or pop for delete confirmations
    obj.delete()
    return redirect('blog')


@login_required
def dashboard(request):
    posts = BlogPost.objects.all()
    return render(request,'blog/dashboard.html',{'posts':posts})

