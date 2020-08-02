from django.shortcuts import render
from django.http import HttpResponse

from listings.models import Listing
from realtors.models import Realtor


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[: 3]
    context = {'listings': listings}
    return render(request, "pages/index.html", context)
    pass


def about(request):
    realtors = Realtor.objects.order_by("hire_date")
    mvp_seller = Realtor.objects.filter(is_mvp=True)
    context = {'realtors': realtors, 'mvp_sellers': mvp_seller}
    return render(request, "pages/about.html", context)
