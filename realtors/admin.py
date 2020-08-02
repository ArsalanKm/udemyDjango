from django.contrib import admin

from realtors.models import Realtor


class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'hire_date', 'is_mvp')
    list_display_links = ('id', 'name')
    list_editable = ('is_mvp',)
    search_fields = ('name',)
    list_per_page = 25
    pass


admin.site.register(Realtor, RealtorAdmin)
