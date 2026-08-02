from django.contrib import admin
from .models import Guest

class GuestAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'is_attending', 'number_of_guests')
    list_filter = ('is_attending',)
    search_fields = ('first_name', 'last_name')

admin.site.register(Guest, GuestAdmin)