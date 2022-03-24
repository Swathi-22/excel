from django.shortcuts import render

# Create your views here.
def index(request):
    context = {

    }
    return render(request,'web/index.html')


def about(request):
    context = {

    }
    return render(request,'web/about.html')


def products(request):
    context = {

    }
    return render(request,'web/products.html')


def blog(request):
    context = {

    }
    return render(request,'web/blog.html')


def blogDetails(request):
    context = {

    }
    return render(request,'web/blog-details.html')


def gallery(request):
    context = {

    }
    return render(request,'web/gallery.html')


def contact(request):
    context = {

    }
    return render(request,'web/contact.html')