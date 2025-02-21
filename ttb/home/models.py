from django.db import models

class ContactMessage(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15, null=True, blank=True)  # Make phone optional
    interest = models.CharField(max_length=200)
    budget = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.full_name} - {self.email}"
