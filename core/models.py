from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    STATUS_CHOICES = (
        ('lost', 'Lost'),
        ('found', 'Found'),
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    date = models.DateField()
    location = models.CharField(max_length=200, blank=True)
    contact = models.CharField(max_length=200, blank=True)
    photo = models.ImageField(upload_to='items/', blank=True, null=True)
    claimed = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.status})"
