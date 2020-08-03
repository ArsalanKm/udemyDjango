from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Listing
from listings.choices import bedroom_choices, price_choices, state_choices


# Create your views here.

def index(request):
    listings = Listing.objects.order_by('-id').filter(is_published=True)
    paginator = Paginator(listings, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'listings': page_obj}

    return render(request, "listings/listings.html", context)
    pass


def listing(request, pk):
    obj = get_object_or_404(Listing, pk=pk)
    context = {"listing": obj}
    return render(request, "listings/listing.html", context)


def search(request):
    queryset_list = Listing.objects.order_by('list_date')
    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)
            pass
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    if 'state' in request.GET:
        state = request.GET['state']
        if state and state != "*":
            queryset_list = queryset_list.filter(state__iexact=state)

    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms and bedrooms != '*':
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

    if 'price' in request.GET:
        price = request.GET['price']
        if price and price != "*":
            queryset_list = queryset_list.filter(price__lte=price)

    paginator = Paginator(queryset_list, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'bedroom_choices': bedroom_choices, 'price_choices': price_choices,
               'state_choices': state_choices, 'listings': page_obj,
               'values': request.GET
               }
    return render(request, "listings/search.html", context)
    pass
