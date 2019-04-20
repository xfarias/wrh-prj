from django.shortcuts import render
from .models import *
from django.shortcuts import render
from django.db.models import Count
# Create your views here.

def index(request):

    vaga = Vaga.objects.all().order_by('salario')
    vagaempresa = Vaga.objects.all(
    ).order_by('empresa').values(
        'empresa__nome'
    ).annotate(count=Count('empresa__nome'))

    vagaclt = Vaga.objects.filter(tipo_contrato='CLT'
    ).order_by('titulo').values('titulo'
    ).annotate(count=Count('titulo'))



    vagapj = Vaga.objects.filter(tipo_contrato='PJ'
    ).order_by('titulo').values('titulo'
    ).annotate(count=Count('titulo'))


    return render(request,'index.html', {
        'vaga': vaga,
        'vagaempresa': vagaempresa,
        'vagaclt': vagaclt,
        'vagapj': vagapj,


})