from django.contrib import admin

from .models import RSVP


# Register your models here.
@admin.register(RSVP)
class RSVPAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'companion',
        'message_short',
        'confirmed',
        'confirmed_at',
    )
    list_filter = ('confirmed', 'confirmed_at')
    search_fields = ('name', 'companion')
    readonly_fields = ('confirmed_at',)
    ordering = ('-confirmed_at',)
    actions = ['confirm', 'unconfirm']

    @admin.action(description='Confirmar')
    def confirm(self, request, queryset):  # noqa: PLR6301
        queryset.update(confirmed=True)

    @admin.action(description='Desconfirmar')
    def unconfirm(self, request, queryset):  # noqa: PLR6301
        queryset.update(confirmed=False)

    # Método para exibir apenas os primeiros 20 caracteres da mensagem
    def message_short(self, obj):  # noqa: PLR6301
        return (
            obj.message[:25] + '...' if len(obj.message) > 25 else obj.message
        )

    message_short.short_description = 'Mensagem'
