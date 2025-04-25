from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Ad, Favorite
from users.models import Profile
from notifications.models import Notification
from .forms import AdForm
from django.contrib import messages 
from reviews.models import Review
def ad_list(request):
    query = request.GET.get('q', '')
    price_min = request.GET.get('price_min')
    price_max = request.GET.get('price_max')
    category = request.GET.get('category')

    ads = Ad.objects.all().order_by('-created_at')

    if query:
        ads = ads.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        )

    if price_min:
        ads = ads.filter(price__gte=price_min)

    if price_max:
        ads = ads.filter(price__lte=price_max)

    if category:
        ads = ads.filter(category=category)

    paginator = Paginator(ads, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'ads/ad_list.html', {
        'page_obj': page_obj,
        'query': query,
        'price_min': price_min,
        'price_max': price_max,
        'category': category
    })



def ad_detail(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id)

    
    user_review_exists = False
    if request.user.is_authenticated and request.user != ad.user:
        user_review_exists = Review.objects.filter(ad=ad, author=request.user).exists()

    
    review_count = ad.ad_reviews.count()

    return render(request, 'ads/ad_detail.html', {
        'ad': ad,
        'user_review_exists': user_review_exists,
        'review_count': review_count
    })

@login_required
def ad_create(request):
    if request.method == 'POST':
        form = AdForm(request.POST, request.FILES)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.user = request.user
            ad.save()
            messages.success(request, 'Объявление успешно создано!')
            return redirect('ad_detail', ad_id=ad.id)
    else:
        form = AdForm()
    
    return render(request, 'ads/ad_form.html', {'form': form})

@login_required
def ad_edit(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id, user=request.user)
    if request.method == 'POST':
        form = AdForm(request.POST, request.FILES, instance=ad)
        if form.is_valid():
            form.save()
            messages.success(request, 'Объявление успешно обновлено!')
            return redirect('ad_detail', ad_id=ad.id)
    else:
        form = AdForm(instance=ad)
    return render(request, 'ads/ad_form.html', {'form': form, 'ad': ad})

@login_required
def ad_delete(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id, user=request.user)
    
    if request.method == 'POST':
        ad.delete()
        messages.success(request, 'Объявление успешно удалено!')
        return redirect('ad_list')
    
    return render(request, 'ads/ad_confirm_delete.html', {'ad': ad})
    
    return render(request, 'ads/ad_confirm_delete.html', {'ad': ad})
@login_required
def my_ads(request):
    ads = Ad.objects.filter(user=request.user).order_by('-created_at')
    paginator = Paginator(ads, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'ads/my_ads.html', {'page_obj': page_obj})

@login_required
def toggle_favorite(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id)
    favorite, created = Favorite.objects.get_or_create(user=request.user, ad=ad)
    if not created:
        favorite.delete()
    return redirect('ad_list')

@login_required
def favorite_ads(request):
    favorites = Favorite.objects.filter(user=request.user).select_related('ad').order_by('-ad__created_at')
    ads = [f.ad for f in favorites]
    return render(request, 'ads/favorites.html', {'ads': ads})

@login_required
def profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'ads/profile.html', {'form': form, 'profile': profile})

@login_required
def ad_create(request):
    if request.method == 'POST':
        form = AdForm(request.POST, request.FILES)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.user = request.user
            ad.save()
            messages.success(request, 'Объявление успешно создано!')
            return redirect('ad_detail', ad_id=ad.id)
    else:
        form = AdForm()
    
    return render(request, 'ads/ad_form.html', {'form': form})
