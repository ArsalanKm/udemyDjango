from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="listings"),
    path('<int:listingId>', views.listing, name="listing"),
    path('search', views.search, name="search")
]
