from django.contrib import admin
from .models import *
# Register your models here.


admin.site.site_header = 'Estamos Contratando'
admin.site.site_title = ' WRH - Administração'

class VagaAdmin(admin.ModelAdmin):
        list_display = ('titulo','descricao','salario','empresa','requisitos')

        list_filter = ('titulo','empresa','requisitos')

        def empresa(self,obj):
            return obj.empresa.nome

        def requisitos(self,obj):
            return obj.requisitos.requisitos_especificos

class EmpresaAdmin(admin.ModelAdmin):

        list_display =('nome','endereco','cidade')

class RequisitosAdmin(admin.ModelAdmin):
     list_display = ('requisitos_especificos','requisitos_gerais')



admin.site.register(Vaga, VagaAdmin)
admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Requisitos, RequisitosAdmin)
