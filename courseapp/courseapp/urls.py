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
    path('contact-us/',views.contact, name='contact'),
    path('thankyou/', views.thankyou, name="thankyou"),

    #PAGES TAB URL
    path('about-us/',include([
    path('', views.aboutus, name='aboutus'),
    path('instructors/',views.aboutus, name='instructors'),
    path('cart/',views.aboutus, name='cart'),
    path('wishlist/',views.aboutus, name='wishlist'),
    path('price-plan/',views.aboutus, name='priceplan'),
    path('contact/',views.aboutus, name='contact'),
    path('faqs/',views.aboutus, name='faqs'),
    path('account/',views.aboutus, name='account'),
    ])),

    #COURSE TAB URL
    path('course/', include([
    path('', views.course, name='course'),
    path('course-detail/', views.course, name='coursedetail'), 
    ])),

    #EVENT TAB URL
    path('event/', include([
    path('', views.event, name='event'),
    path('event-detail/',views.event, name='eventdetail'),
    ])),

    #BLOG TAB URL
    path('blog/', include([
    path('',views.event, name='blog'),
    path('single-post/',views.blog, name='singlepost'), 
    ])),

    #SHOP TAB URL
    path('shop/',include([
    path('',views.shop, name='shop'),
    path('single-product/', views.shop, name='singleproduct'),
    ])),

    #CONTACT TAB URL
    


    

]

