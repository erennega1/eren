from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text', 'rating']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4}),
            'rating': forms.Select(attrs={'class': 'form-control'})
        }
        labels = {
            'text': 'Ваш отзыв',
            'rating': 'Ваша оценка'
        }
def clean(self):
    if self.instance and Review.objects.filter(
        ad=self.instance.ad, 
        author=self.instance.author
    ).exists():
        raise ValidationError("Вы уже оставляли отзыв на это объявление")