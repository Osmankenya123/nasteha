

from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def products(request):
    return render(request, 'products.html')


# Agriculture
def agriculture(request):
    return render(request, 'agriculture.html')


# Business
def business(request):
    return render(request, 'business.html')


# Offer
def offer(request):
    return render(request, 'offer.html')


# tourism
def tourism(request):
    return render(request, 'tourism.html')


# Schools
def schools(request):
    return render(request, 'schools.html')

# performance
def performance(request):
    return render( request,'performance.html')
