from django.shortcuts import render, get_object_or_404
from .models import Ad
def ad_list(request):
    ads = Ad.objects.all()
    return render(request, 'ads/ad_list.html', {"ads": ads})
def ad_detail(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id)
    return render(request, 'ads/ad_detail.html', {'ad': ad})