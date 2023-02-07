from django import forms
from tempus_dominus.widgets import DatePicker
from datetime import datetime
from passagens.classe_viagem import tipos_de_classes
from passagens.validation import *

class PassaegmForms(forms.Form):
    origem = forms.CharField(label='Origem', max_length=100)
    destino = forms.CharField(label='Destino', max_length=100)
    data_ida = forms.DateField(label='Ida', widget=DatePicker())
    data_volta = forms.DateField(label='Volta', widget=DatePicker())
    data_pesquisa = forms.DateField(label='Data da pesquisa', disabled=True, initial=datetime.today)
    classe_viagem = forms.ChoiceField(label='Classe do vôo', choices=tipos_de_classes)
    informacoes = forms.CharField(
        label='Informações extras',
        max_length=200,
        widget=forms.Textarea()
    )
    email = forms.EmailField(label='Email', max_length=150)

    def clean(self):
        origem = self.cleaned_data.get('origem')
        destino = self.cleaned_data.get('destino')
        lista_de_erros = {}

        campo_numerico(origem, 'origem', lista_de_erros)
        campo_numerico(destino, 'destino', lista_de_erros)
        origem_destino_iguais(origem, destino, lista_de_erros)

        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem_erro = lista_de_erros[erro]
                self.add.error(erro, mensagem_erro)

        return self.cleaned_data

