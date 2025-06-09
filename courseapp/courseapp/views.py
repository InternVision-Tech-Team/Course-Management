from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    data={
        'title': 'home page'
    }
    return render(request, 'index.html',data)  # You must have templates/index.html

def aboutus(request):
    return render(request, 'contact.html')  

def courses(request):
    return HttpResponse("This is the courses page.")

def course_detail(request, course_id):
    return HttpResponse(course_id)
