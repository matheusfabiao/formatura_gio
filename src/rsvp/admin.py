from django.contrib import admin

from .models import RSVP


# Register your models here.
@admin.register(RSVP)
class RSVPAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'companion',
        'message',
        'confirmed',
        'confirmed_at',
    )
    list_filter = ('confirmed', 'confirmed_at')
    search_fields = ('name', 'companion')
    readonly_fields = ('confirmed_at',)
    ordering = ('-confirmed_at',)
    actions = ['confirm', 'unconfirm']

    @admin.action(description='Confirmar')
    def confirm(cls, request, queryset):
        queryset.update(confirmed=True)

    @admin.action(description='Desconfirmar')
    def unconfirm(cls, request, queryset):
        queryset.update(confirmed=False)
