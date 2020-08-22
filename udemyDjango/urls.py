from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
                  path('', include('pages.urls')),
                  path('listings/', include('listings.urls')),
                  path('accounts/', include('account.urls')),
                  path('contacts/', include('contacts.urls')),
                  path('admin/', admin.site.urls),
                  path('api/', include('snippest.urls')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
