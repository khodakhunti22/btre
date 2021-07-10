from django.contrib import admin
from .models import Realtor


class RealtorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'is_mvp', 'hire_date']
    list_display_links = ['id', 'name']
    list_filter = ['name']
    search_fields = ['name', 'description']


admin.site.register(Realtor, RealtorAdmin)
