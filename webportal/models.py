from django.db import models

class PrivacyRule(models.Model):
    title = models.CharField("Titulo", max_length=255, default='', blank=True)
    severity = models.IntegerField("Gravidade", default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Regra de Privacidade'
        verbose_name_plural = 'Regras de Privacidade'

class LGPDRequest(models.Model):
    REQ = [
        ('CONFIRMAR TRATAMENTO', 'Confirmar tratamento'),
        ('ACESSAR DADOS PESSOAIS', 'Acessar dados pessoais'),
        ('CORRIGIR DADOS', 'Corrigir dados'),
        ('SOLICITAR ANONIMIZAÇÃO', 'Solicitar anonimização'),
        ('SOLICITAR PORTABILIDADE ', 'Solicitar portabilidade'),
        ('SOLICITAR ELIMINAÇÃO DE DADOS', 'Solicitar eliminação de dados'),
        ('OBTER INFORMAÇÕES SOBRE O COMPARTILHAMENTO', 'Obter informações sobre o compartilhamento'),
        ('REVOGAR CONSENTIMENTO ', 'Revogar consentimento'),
    ]
    name = models.CharField("Nome", max_length=255, default='', blank=True)
    phone = models.CharField("Telefone", max_length=255, default='', blank=True)
    email = models.CharField("E-mail", max_length=255, default='', blank=True)
    message = models.CharField("Descrição", max_length=5000, default='', blank=True)
    type = models.CharField("Tipo", max_length=500, default='CONFIRMAR TRATAMENTO', choices=REQ)    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Solicitação LGPD'
        verbose_name_plural = 'Solicitações LGPD'

class Person(models.Model):
    name = models.CharField("Nome", max_length=255, default='')
    age = models.CharField("Idade", max_length=255, default='')    
    sex = models.CharField("Sexo", max_length=255, default='')
    birth = models.DateField("Nascimento")
    doc = models.CharField("Documento", default='0', max_length=255) # campo a ser alterado
    email = models.EmailField("Email")
    phone = models.CharField("Telefone", max_length=255, default=0)
    address = models.CharField("Endereço", max_length=255, default='')
    city = models.CharField("Cidade", max_length=255, default='')
    tipoSindicato = models.CharField("Sindicato", max_length=255, default='')
    tipoReligiao = models.CharField("Religião", max_length=255, default='')
    senhaDoUsuario = models.CharField("Senha do usuário", max_length=255, default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'

