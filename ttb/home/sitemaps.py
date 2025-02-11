from django.contrib.sitemaps import Sitemap
from django.urls import reverse

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

    def changefreq(self, item):
        return 'weekly'  # Example: frequency of changes (can be 'daily', 'monthly', etc.)

    def priority(self, item):
        return 0.5  # Example: priority of the URL (range: 0.0 to 1.0)
