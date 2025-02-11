"""
URL configuration for ttb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap 

urlpatterns = [
    path('', views.index, name="home"),
    path('about-us', views.about, name="about"),
    path('services', views.service, name="service"),
    path('services/digital-marketing', views.digital_marketing, name="digital_marketing"),
    path('services/website-development', views.website_development, name="website_development"),
    path('services/software-development', views.software_development, name="software_development"),
    path('services/app-development', views.app_development, name="app_development"),
    path('services/email-marketing', views.email_marketing, name="email_marketing"),
    path('services/whatsapp-marketing', views.whatsapp_marketing, name="whatsapp_marketing"),
    path('services/ivr-marketing', views.ivr_marketing, name="ivr_marketing"),
    path('contact/', views.contact_us, name='contact_us'),
    path('success/', views.success_page, name='success'),
    path('sitemap.xml', sitemap, {'sitemaps': {'static': StaticViewSitemap}}),  # Add this line for the sitemap

]
