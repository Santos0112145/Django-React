from django.contrib import admin  # pyright: ignore[reportMissingImports]
from .models import Item

# Register your models here.
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name', 'description')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('name', 'description')
        }),
        ('Fechas', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    list_per_page = 20
