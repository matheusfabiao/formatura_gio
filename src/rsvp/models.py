from django.db import models


# Create your models here.
class RSVP(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nome Completo')
    companion = models.CharField(
        max_length=150,
        verbose_name='Nome do Acompanhante',
        blank=True,
        null=True,
    )
    message = models.TextField(
        verbose_name='Mensagem', blank=True, null=True, max_length=125
    )
    confirmed = models.BooleanField(verbose_name='Confirmado', default=False)
    confirmed_at = models.DateTimeField(
        verbose_name='Data da confirmação', auto_now_add=True
    )

    class Meta:
        verbose_name = 'Confirmação de Presença'
        verbose_name_plural = 'Confirmações de Presença'

    def __str__(self):
        status = 'Confirmado' if self.confirmed else 'Não Confirmado'
        return f'{self.name} - {status}'
