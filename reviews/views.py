from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Review
from .forms import ReviewForm
from ads.models import Ad

@login_required
def add_review(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id)

    if Review.objects.filter(ad=ad, author=request.user).exists():
        messages.warning(request, 'Вы уже оставляли отзыв на это объявление.')
        return redirect('ad_detail', ad_id=ad.id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.ad = ad
            review.author = request.user
            review.save()
            messages.success(request, 'Спасибо за ваш отзыв!')
            return redirect('ad_detail', ad_id=ad.id)
    else:
        form = ReviewForm()

    return render(request, 'reviews/add_review.html', {'form': form, 'ad': ad})