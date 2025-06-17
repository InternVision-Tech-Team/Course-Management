from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages

def homepage(request):
    return render(request, 'index.html')

def aboutus(request):
    return render(request, 'base.html')

def course(request):
    return render(request, 'course.html')

def account(request):
    return render(request, 'account.html')

def faqs(request):
    return render(request, 'faqs.html')

def contact(request):
    if request.method == "POST":
        
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # You can save this to a database or send an email here
        messages.success(request, "Thanks for contacting us!")
        return redirect("thankyou")  # Redirect to another page

    return render(request, "contact.html")

def instructors(request):
    return render(request, 'instructors.html')

def cart(request):
    return render(request, 'cart.html')

def priceplan(request):
    return render(request, 'priceplan.html')

def wishlist(request):
    return render(request, 'wishlist.html')

def course(request):
    return render(request, 'course.html')

def blog (request):
    return render(request,'blog.html')

def thankyou (request):
    return render(request,'thankyou.html')

