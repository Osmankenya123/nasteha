"""
URL configuration for DjangoOsman project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from itertools import product
from tkinter.font import names

from django.contrib import admin
from django.urls import path
from DjangoOsman import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index, name="home"),
    path('about/', views.about, name="about"),
    path('services/', views.services, name="services"),
    # Products
    path('products/', views.products, name="products"),
    #     Agriculture
    path('agriculture/', views.agriculture, name="agriculture"),
    #     Business
    path('business/', views.business, name="business"),
    #     tourism
    path('tourism/', views.tourism, name="tourism"),
    #     offer
    path('offer/', views.offer, name="offer"),
    #     schools
    path('schools/', views.schools, name="schools"),

    path('performance/', views.performance, name="performance"),

    path('contacts/',views.contacts, name="contacts")
]
