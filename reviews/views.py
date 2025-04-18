from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Review
from .forms import ReviewForm
from ads.models import Ad

@login_required
def add_review(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.recipient = ad.author
            review.ad = ad
            review.save()
            messages.success(request, 'Отзыв отправлен на модерацию!')
            return redirect('ad_detail', ad_id=ad.id)
    else:
        form = ReviewForm()
    
    return render(request, 'reviews/add_review.html', {'form': form, 'ad': ad})