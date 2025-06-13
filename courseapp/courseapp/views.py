from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request,'index.html')   # You must have templates/index.html

def aboutus(request):
    return render(request,'base.html')  

def courses(request):
    return HttpResponse("This is the courses page.")

def course_detail(request, course_id):
    return HttpResponse(course_id)
