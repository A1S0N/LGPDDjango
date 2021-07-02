from django.db import models

class PrivacyRule(models.Model):
    title = models.CharField("Titulo", max_length=255, default='', blank=True)
    severity = models.DecimalField("Gravidade", default=0, decimal_places=10, max_digits=20)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Regra de Privacidade'
        verbose_name_plural = 'Regras de Privacidade'

class LGPDRequest(models.Model):
    name = models.CharField("Nome", max_length=255, default='', blank=True)
    phone = models.CharField("Telefone", max_length=255, default='', blank=True)
    email = models.CharField("E-mail", max_length=255, default='', blank=True)
    message = models.CharField("Mensagem", max_length=255, default='', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Solicitação LGPD'
        verbose_name_plural = 'Solicitações LGPD'
