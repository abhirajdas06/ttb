from django.shortcuts import render, redirect
from .forms import ContactForm

# Create your views here.
def index(request):
    return render(request, "home/index.html")

def about(request):
    return render(request, "about/about.html")

def service(request):
    return render(request, "service/service.html")

def digital_marketing(request):
    return render(request, "service/digital-marketing.html")

def website_development(request):
    return render(request, "service/website-development.html")


def software_development(request):
    return render(request, "service/software-development.html")

def app_development(request):
    return render(request, "service/app-development.html")

def email_marketing(request):
    return render(request, "service/email-marketing.html")

def whatsapp_marketing(request):
    return render(request, "service/whatsapp-marketing.html")

def ivr_marketing(request):
    return render(request, "service/ivr-marketing.html")


def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('success')  # Redirect to a success page after submission
    else:
        form = ContactForm()

    return render(request, 'contact/contact_us.html', {'form': form})

def success_page(request):
    return render(request, 'contact/success.html')