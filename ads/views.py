from django.http import HttpResponse

def ad_list(request):
    return HttpResponse("Здесь будет список объявлений.")

def ad_detail(request, ad_id):
    return HttpResponse(f"Детальная страница объявления с ID {ad_id}.")
