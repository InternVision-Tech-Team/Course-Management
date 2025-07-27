from django.shortcuts import render, redirect

def account(request):
    return render(request, 'account.html')

def homepage(request):
    return render(request, 'index.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def course(request):
    return render(request, 'course.html')

def coursedetail(request):
    return render(request, 'coursedetail.html')

def support(request):
    return render(request, 'support.html')

def faqs(request):
    return render(request, 'faqs.html')

def contact(request):
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
