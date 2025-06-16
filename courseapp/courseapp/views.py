from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

def homepage(request):
    return render(request, 'index.html')

def aboutus(request):
    return render(request, 'base.html')

def course_detail(request, course_id):
    return HttpResponse(f"Course ID: {course_id}")

def account(request):
    return render(request, 'account.html')

def faqs(request):
    return render(request, 'faqs.html')

def contact(request):
    return render(request, 'contact.html')

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

def userform(request):
    data = {}
    if request.method == 'POST':
        try:
            n1 = int(request.POST.get('username', 0))
            n2 = int(request.POST.get('password', 0))
            ans = n1 + n2
            data = {
                'n1': n1,
                'n2': n2,
                'output': ans
            }
            return HttpResponseRedirect('/about-us/')
        
        except ValueError:

            data['error'] = "Please enter valid numbers for username and password."

    return render(request, 'userform.html', data)

def submitform(request):
    return HttpResponse(request )