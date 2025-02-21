# forms.py
from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['full_name', 'email', 'phone', 'interest', 'budget', 'message']  # Include 'phone' here
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Your message...'}),
        }
