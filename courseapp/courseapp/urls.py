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
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),
    path('about-us/', views.aboutus, name='aboutus'),
    path('course/', views.course, name='course'),
    path('account/', views.account, name='account'),
    path('contact-us/',views.contact, name='contact'),
    path('faqs/', views.faqs, name='faqs'),
    path('instructors/', views.instructors, name='instructors'),
    path('cart/',views.cart, name='cart'),
    path('price-plan/',views.priceplan, name='priceplan'),
    path('wishlist/', views.wishlist, name='wishlist'), 

    path('course/', include([
    path('', views.course, name='course'),
    path('course-detail/', views.course, name='coursedetail'), 
    ])),
    path('course-detail/', views.course, name='coursedetail'),

    path('event/', include([
    path('', views.event, name='event'),
    path('event-detail/',views.event, name='eventdetail'),
    ])),
    path('event-detail/',views.event, name='eventdetail'),

    path('blog/',views.blog , name='blog'),
    path('thankyou/', views.thankyou, name="thankyou"),
    path('single-post/',views.singlepost , name='singlepost'),
    path('shop/',views.shop, name='shop'),
    path('single-product/',views.singleproduct , name='singleproduct'),
    

]

