# Generated by Django 5.2 on 2025-04-10 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RSVP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nome Completo')),
                ('companion', models.CharField(blank=True, max_length=150, null=True, verbose_name='Nome do Acompanhante')),
                ('message', models.TextField(blank=True, max_length=125, null=True, verbose_name='Mensagem')),
                ('confirmed', models.BooleanField(default=False, verbose_name='Confirmado')),
                ('confirmed_at', models.DateTimeField(auto_now_add=True, verbose_name='Data da confirmação')),
            ],
            options={
                'verbose_name': 'Confirmação de Presença',
                'verbose_name_plural': 'Confirmações de Presença',
            },
        ),
    ]
