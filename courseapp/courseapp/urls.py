"""
URL configuration for courseapp project.

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
from django.contrib import admin
from django.urls import path
from courseapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),
    #PAGES
    path('about-us/', views.aboutus, name='about-us'),
    path('course/', views.course, name='course'), #dynamic URL for course detail
    path('account/', views.account, name='account'),
    path('contact-us/',views.contact, name='contact'),
    path('faqs/', views.faqs, name='faqs'),
    path('instructors/', views.instructors, name='instructors'),
    path('cart/',views.cart, name='cart'),
    path('price-plan/',views.priceplan, name='priceplan'),
    path('wishlist/', views.wishlist, name='wishlist'),
    #COURSES
    path('course/',views.course, name='course'),  
    path('blog/',views.blog , name='blog'),
    path('thank-you/', views.thankyou, name="thankyou"),

]

