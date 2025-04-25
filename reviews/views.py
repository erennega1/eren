from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm

@login_required
def add_review(request, ad_id):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.ad_id = ad_id
            review.save()
    return redirect('ad_detail', ad_id=ad_id)