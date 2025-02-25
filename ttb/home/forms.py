from django import forms
from .models import ContactMessage
from hcaptcha.fields import hCaptchaField

class ContactForm(forms.ModelForm):
    captcha = hCaptchaField()

    class Meta:
        model = ContactMessage
        fields = ['full_name', 'email', 'phone', 'interest', 'budget', 'message', 'captcha']
