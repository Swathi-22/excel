from django.shortcuts import render
from .forms import ContactForm
from .models import Contact
from django.http import JsonResponse


# Create your views here.
def index(request):
    context = {

    }
    return render(request,'web/index.html',context)


def about(request):
    context = {

    }
    return render(request,'web/about.html',context)


def products(request):
    context = {

    }
    return render(request,'web/products.html',context)


def blog(request):
    context = {

    }
    return render(request,'web/blog.html',context)


def blogDetails(request):
    context = {

    }
    return render(request,'web/blog-details.html',context)


def gallery(request):
    context = {

    }
    return render(request,'web/gallery.html',context)


def contact(request):
    forms=ContactForm(request.POST or None)
    context = {
        'forms':forms
    }
    return render(request,'web/contact.html',context)


def SaveContactForm(request):
  
    forms=ContactForm(request.POST or None)
    if request.method=='POST':
        if forms.is_valid():
            forms.save()
    return JsonResponse({'title':'name'})