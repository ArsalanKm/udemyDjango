from django.contrib import admin

# Register your models here.
from contacts.models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'listing', 'email', 'contact_date','user')
    list_display_links = ('id', 'name','user')
    search_fields = ('name', 'email', 'listing')
    list_per_page = 25
    pass


admin.site.register(Contact, ContactAdmin)
