from django.shortcuts import render,get_object_or_404
from .forms import ContactForm
from .models import Contact,Testimonial,Gallery,Update
from django.http import JsonResponse


# Create your views here.
def index(request):
    testimonials=Testimonial.objects.all()
    context = {
        "is_index" : True,
        'testimonials':testimonials
    }
    return render(request,'web/index.html',context)


def about(request):
    context = {
        "is_about" : True,
    }
    return render(request,'web/about.html',context)


def products(request):
    context = {
        "is_product" : True,
    }
    return render(request,'web/products.html',context)


def blog(request):
    updates=Update.objects.all()
    context = {
        "is_blog" : True,
        'updates':updates
    }
    return render(request,'web/blog.html',context)


def blogDetails(request,slug):
    update = get_object_or_404(Update,slug=slug)
    updates=Update.objects.all()
    context = {
        'updates':updates,
        'update':update
    }
    return render(request,'web/blog-details.html',context)


def gallery(request):
    galleries=Gallery.objects.all()
    context = {
        "is_gallery" : True, 
        'galleries':galleries   
    }
    return render(request,'web/gallery.html',context)


def contact(request):
    forms=ContactForm(request.POST or None)
    context = {
        'forms':forms,
        "is_contact" : True,
    }
    return render(request,'web/contact.html',context)


def SaveContactForm(request):
  
    forms=ContactForm(request.POST or None)
    if request.method=='POST':
        if forms.is_valid():
            forms.save()
    return JsonResponse({'title':'name'})