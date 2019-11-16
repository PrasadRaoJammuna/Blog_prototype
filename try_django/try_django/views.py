from django.http import HttpResponse
from django.shortcuts import render 
from .forms import ContactForm



def home_page(request):
    title ='Home'
    return render(request,'index.html',{'title':title})


def contact(request):
    title = 'Contact Us'
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm()

    return render(request,'contact.html',{'title':title,'form':form})


def about(request):
    title = 'About Us'
    return render(request,'about.html',{'title':title})


