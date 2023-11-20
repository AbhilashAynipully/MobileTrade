from .models import Mobile

def filter_mobiles(request):
    mobiles = Mobile.objects.all().order_by('-added_time')

    if 'brand' in request.GET:
        brand = request.GET['brand']
        if brand:
            mobiles = mobiles.filter(brand__iexact=brand)

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        if min_price:
            mobiles = mobiles.filter(price__gte=min_price)

    if 'max_price' in request.GET:
        max_price = request.GET['max_price']
        if max_price:
            mobiles = mobiles.filter(price__lte=max_price)
            
    return mobiles