from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Ad, Favorite
from users.models import Profile
from notifications.models import Notification

def ad_list(request):
    
    if request.user.is_authenticated:
        unread_notifications = Notification.objects.filter(user=request.user, is_read=False)
    else:
        unread_notifications = []

    query = request.GET.get('q', '')
    price_min = request.GET.get('price_min')
    price_max = request.GET.get('price_max')
    category = request.GET.get('category')

    ads = Ad.objects.all()

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
        'category': category,
        'unread_notifications': unread_notifications,
    })


def ad_detail(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id)
    return render(request, 'ads/ad_detail.html', {'ad': ad})

@login_required
def ad_create(request):
    if request.method == 'POST':
        form = AdForm(request.POST, request.FILES)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.user = request.user
            ad.save()
            return redirect('ad_list')
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
            return redirect('ad_list')
    else:
        form = AdForm(instance=ad)
    return render(request, 'ads/ad_form.html', {'form': form})

@login_required
def ad_delete(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id, user=request.user)
    if request.method == 'POST':
        ad.delete()
        return redirect('ad_list')
    return render(request, 'ads/ad_confirm_delete.html', {'ad': ad})

@login_required
def my_ads(request):
    ads = Ad.objects.filter(user=request.user).order_by('-id')
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
    favorites = Favorite.objects.filter(user=request.user).select_related('ad')
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
