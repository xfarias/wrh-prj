from django.db import models

# Create your models here.

TIPO_CONTRATO_CHOICES = [
    ('PJ', 'Pessoa Juridica'),
    ('CLT', 'Consolidação das Leis do Trabalho')
]


class Vaga(models.Model):
    titulo = models.CharField(max_length=30, null=False)
    descricao = models.TextField(null=False)
    salario = models.FloatField(null=False)
    tipo_contrato = models.CharField(choices=TIPO_CONTRATO_CHOICES, null=False, max_length=50)
    status = models.BooleanField(null=False, default=1)
    empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE)
    requisitos = models.ForeignKey('Requisitos', on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo


class Empresa(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Empresa", null=False)
    endereco = models.CharField(max_length=250, verbose_name="Endereço", null=False)
    cidade = models.CharField(max_length=80, verbose_name="Cidade")
    estado = models.CharField(max_length=100, verbose_name="estado")

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['-id']
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'


class Requisitos(models.Model):
    requisitos_especificos = models.TextField(null=False, verbose_name="Requisitos Específicos")
    requisitos_gerais = models.TextField(null=False, verbose_name="Requisitos Gerais")


    def __str__(self):
        return self.requisitos_especificos

    class Meta:
        ordering = ['-id']
        verbose_name = 'Requisito'
        verbose_name_plural = 'Requisitos'