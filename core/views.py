from django.shortcuts import render
from .models import *
from django.shortcuts import render
# Create your views here.

def index(request):

    vagas = Vaga.objects.all()

    return render(request, 'index.html', {
        'vagas': vagas.order_by('salario')
    })