from django.contrib import admin
from .models import Guest

# This class customizes how the Guest database looks to your Mom
class GuestAdmin(admin.ModelAdmin):
    # 1. Shows these details as neat columns in the table
    list_display = ('first_name', 'last_name', 'is_attending', 'number_of_guests')
    
    # 2. Creates a clickable filter box on the right side of the screen
    list_filter = ('is_attending',)
    
    # 3. Adds a search bar at the top so she can quickly find a specific aunt or uncle
    search_fields = ('first_name', 'last_name')

# Register the blueprint AND the new custom admin layout
admin.site.register(Guest, GuestAdmin)