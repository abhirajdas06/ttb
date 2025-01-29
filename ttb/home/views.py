from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, "home/index.html")

def about(request):
    return render(request, "about/about.html")

def service(request):
    return render(request, "service/service.html")

def digital_marketing(request):
    return render(request, "service/digital-marketing.html")