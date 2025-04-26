from django.db import models


# Create your models here.
class RSVP(models.Model):
    """Modelo de confirmação de presença"""

    name = models.CharField(max_length=150, verbose_name='Nome Completo')
    email = models.EmailField(verbose_name='E-mail', unique=True)
    companion = models.CharField(
        max_length=150,
        verbose_name='Nome do Acompanhante',
        blank=True,
        null=True,
    )
    companion_email = models.EmailField(
        verbose_name='E-mail do Acompanhante',
        blank=True,
        null=True,
        unique=True,
    )
    message = models.TextField(
        verbose_name='Mensagem', blank=True, null=True, max_length=125
    )
    confirmed = models.BooleanField(verbose_name='Confirmado', default=False)
    confirmed_at = models.DateTimeField(
        verbose_name='Data da confirmação', auto_now_add=True
    )

    class Meta:
        """Define o nome do modelo no painel de administração"""

        verbose_name = 'Confirmação de Presença'
        verbose_name_plural = 'Confirmações de Presença'

    def __str__(self):
        """Devolve uma representação em string do modelo

        Returns:
            str: nome do convidado e o status de confirmação
        """
        status = 'Confirmado' if self.confirmed else 'Não Confirmado'
        return f'{self.name} - {status}'
