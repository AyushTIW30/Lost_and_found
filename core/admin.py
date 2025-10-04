from django.contrib import admin
from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'date', 'location', 'claimed')
    list_filter = ('status', 'claimed')
    search_fields = ('title', 'description', 'location', 'contact')
