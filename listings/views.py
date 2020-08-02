from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Listing


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
    return render(request, "listings/search.html")
    pass
