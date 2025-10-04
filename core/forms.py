from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['title', 'description', 'status', 'date', 'location', 'contact', 'photo']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }
