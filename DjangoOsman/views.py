from django.contrib.auth import login
from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth.models import User
from .models import Signup, Login, Email


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

def contacts(request):
    if request.method=="POST":
        first_name=request.POST.get("fname")
        middle_name=request.POST.get("mname")
        last_name=request.POST.get("lname")
        username = request.POST.get("username")
        password = request.POST.get("pwd")
        query1 = Login(username=username, password=password)
        query1.save()


        query=Signup(first_name=first_name,middle_name=middle_name,last_name=last_name)
        query.save()
        return redirect("/")

    # if request.method=="POST":
    #     username=request.POST.get("username")
    #     password=request.POST.get("pwd")
    #
    #     query1=Login(username=username,password=password)
    #     query1.save()
    #     return redirect("/")

    if request.method=="POST":
        email=request.POST.get("birth_day_time")


    return render(request,'contacts.html')


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
    return render(request, 'performance.html')


