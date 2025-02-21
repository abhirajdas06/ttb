from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from .forms import ContactForm  # Ensure your form has fields corresponding to the model
from .models import ContactMessage  # Import the model

from django.contrib.sitemaps import Sitemap

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
            # Save the form data to the database as a new ContactMessage instance
            contact_message = form.save()

            # Send an email to info@thetechbuzz.in
            send_mail(
                'New Contact Us Submission',
                f'You have a new message from {contact_message.full_name}.\n\n'
                f'Email: {contact_message.email}\n\n'
                f'Phone: {contact_message.phone}\n\n'  # Include the phone number
                f'Interest: {contact_message.interest}\n\n'
                f'Budget: {contact_message.budget}\n\n'
                f'Message: {contact_message.message}',
                settings.DEFAULT_FROM_EMAIL,
                ['info@thetechbuzz.in'],
                fail_silently=False,
            )

            # Redirect to a success page after submission
            return redirect('success')
    else:
        form = ContactForm()

    return render(request, 'contact/contact_us.html', {'form': form})

def success_page(request):
    return render(request, 'contact/success.html')


class StaticViewSitemap(Sitemap):
    def items(self):
        return [
            'home', 
            'about', 
            'service', 
            'digital_marketing', 
            'website_development', 
            'software_development', 
            'app_development', 
            'email_marketing', 
            'whatsapp_marketing', 
            'ivr_marketing', 
            'contact_us', 
            'success'
        ]

    def location(self, item):
        return reverse(item)