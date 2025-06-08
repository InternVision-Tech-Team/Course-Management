from django.http import HttpResponse

def aboutus(request):
    return HttpResponse("This is the about us page.")