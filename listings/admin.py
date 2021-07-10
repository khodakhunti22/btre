from django.contrib import admin

from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'is_published',  'city', 'realtors']
    list_display_links = ['id', 'title']
    list_editable = ['is_published']
    list_filter = ['city', 'state', 'realtors']


admin.site.register(Listing, ListingAdmin)
