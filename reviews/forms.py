from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'text']
        widgets = {
            'rating': forms.RadioSelect(choices=Review.RATING_CHOICES),
            'text': forms.Textarea(attrs={'rows': 4})
        }