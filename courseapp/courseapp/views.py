from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact  

def homepage(request):
    return render(request, 'index.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def course(request):
    return render(request, 'course.html')

def coursedetail(request):
    return render(request, 'coursedetail.html')

def account(request):
    return render(request, 'account.html')

def faqs(request):
    return render(request, 'faqs.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # ✅ Save to database using the correct model name
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
