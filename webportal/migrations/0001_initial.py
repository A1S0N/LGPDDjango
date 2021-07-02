# Generated by Django 3.2.5 on 2021-07-02 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LGPDRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=255, verbose_name='Nome')),
                ('phone', models.CharField(blank=True, default='', max_length=255, verbose_name='Telefone')),
                ('email', models.CharField(blank=True, default='', max_length=255, verbose_name='E-mail')),
                ('message', models.CharField(blank=True, default='', max_length=255, verbose_name='Mensagem')),
            ],
            options={
                'verbose_name': 'Solicitação LGPD',
                'verbose_name_plural': 'Solicitações LGPD',
            },
        ),
        migrations.CreateModel(
            name='PrivacyRule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=255, verbose_name='Titulo')),
                ('severity', models.DecimalField(decimal_places=10, default=0, max_digits=20, verbose_name='Gravidade')),
            ],
            options={
                'verbose_name': 'Regra de Privacidade',
                'verbose_name_plural': 'Regras de Privacidade',
            },
        ),
    ]