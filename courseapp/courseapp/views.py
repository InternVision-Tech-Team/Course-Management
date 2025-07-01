from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact  
from service.models import Service
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import ContactForm
from django.core.mail import send_mail
from .models import Certificate


def custom_logout(request):
    logout(request)
    return redirect('homepage')  


@login_required
def account(request):
    enrolled_courses = request.user.course_set.all() if hasattr(request.user, 'course_set') else []
    return render(request, 'account.html', {'enrolled_courses': enrolled_courses})


def homepage(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")

        Certificate.objects.create(name=name, email=email)
        messages.success(request,"Thank you for contacting us")
        return redirect ("thankyou")

    return render(request, 'index.html')



def aboutus(request):
    return render(request, 'aboutus.html')

def course(request):
    return render(request, 'course.html')

def coursedetail(request):
    return render(request, 'coursedetail.html')

def support(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        return render(request, 'thankyou.html')  
    return render(request, 'support.html')


def faqs(request):
    return render(request, 'faqs.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        Contact.objects.create(name=name, email=email, message=message)

        messages.success(request, "Thanks for contacting us!")
        return redirect("thankyou")

    return render(request, "contact.html")



def instructors(request):
    return render(request, 'instructors.html')

def cart(request):
    return render(request, 'cart.html')

def priceplan(request):
    return render(request, 'priceplan.html')

def wishlist(request):
    return render(request, 'wishlist.html')

def blog(request):
    return render(request, 'blog.html')

def thankyou(request):
    return render(request, 'thankyou.html')

def event(request):
    return render(request, 'event.html')

def eventdetail(request):
    return render(request, 'eventdetail.html')

def singlepost(request):
    return render(request, 'singlepost.html')

def shop(request):
    return render(request, 'shop.html')

def singleproduct(request):
    return render(request, 'singleproduct.html')
