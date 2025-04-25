from django import forms
from .models import Review
from django.core.exceptions import ValidationError

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text', 'rating']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'rating': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'text': 'Ваш отзыв',
            'rating': 'Оценка'
        }

def clean(self):
    cleaned_data = super().clean()
    
    return cleaned_data