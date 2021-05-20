from django import forms
from .models import *


class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ['cliente', 'valor', 'data_venda', 'hora_venda', 'numero_venda', 'observacao', 'comprovante_venda',
                  'venda_concluida', 'produtos']


class EletricosForm(forms.ModelForm):
    class Meta:
        model = Eletricos
        fields = ['nome', 'valor', 'Descrição']


class HidraulicoForm(forms.ModelForm):
    class Meta:
        model = Hidraulico
        fields = ['Nome', 'valor', 'Descrição']


class VidroForm(forms.ModelForm):
    class Meta:
        model = Vidro
        fields = {'Nome', 'valor', 'Descrição'}


class VendaObservacaoForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ['observacao']


class VendaClienteForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ['Cliente']
