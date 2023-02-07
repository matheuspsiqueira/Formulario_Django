from django.shortcuts import render
from passagens.forms import PassaegmForms

def index(request):
    form = PassaegmForms()
    contexto = {'form':form}
    return render(request, 'index.html', contexto)

def revisao_consulta(request):
    if request.method == 'POST':
        form = PassaegmForms(request.POST)
        contexto = {'form':form}
        return render(request, 'minha_consulta.html', contexto)