from django import forms
from .models import ContactMessage
from django_recaptcha.fields import ReCaptchaField

class ContactForm(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = ContactMessage
        fields = ['full_name', 'email', 'phone', 'interest', 'budget', 'message', 'captcha']
