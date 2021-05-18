from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView, DetailView
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import VendaForm, VendaObservacaoForm, VendaClienteForm, EletricosForm, HidraulicoForm, VidroForm
from .models import Venda, Eletricos, Hidraulico, Cliente, Vidro, Tinta, Esquadria, Madeira, Pedra, Maquina, \
    Ceramica, Coberta, Ferramenta, Iluminacao, Estrutura, Piso


# ______________________________________CreateView_____________________________________

class VendaCreateView(CreateView):
    form_class = VendaForm
    template_name = 'cadastrar/Venda.html'

    def get_success_url(self):
        messages.success(self.request, 'Venda cadastrada com suceso!')
        return reverse_lazy("listar_venda")


class EletricosCreateView(CreateView):
    model = Eletricos
    form_class = EletricosForm
    template_name = 'cadastrar/eletricos.html'

    def get_success_url(self):
        messages.success(self.request, 'Eletrico cadastrado com suceso!')
        return reverse_lazy("listar_eletricos")


class HidraulicoCreateView(CreateView):
    model = Hidraulico
    form_class = HidraulicoForm
    template_name = 'cadastrar/hidraulico.html'

    def get_success_url(self):
        messages.success(self.request, 'Hidraulico cadastrado com suceso!')
        return reverse_lazy("listar_hidraulico")


class ClienteCreateView(CreateView):
    model = Cliente
    template_name = 'cadastrar/cliente.html'

    def get_success_url(self):
        messages.success(self.request, 'Cliente cadastrado com suceso!')
        return reverse_lazy("listar_cliente")


class VidroCreateView(CreateView):
    model = Vidro
    template_name = 'cadastrar/vidro.html'

    def get_success_url(self):
        messages.success(self.request, 'Vidro cadastrado com suceso!')
        return reverse_lazy("listar_vidro")


class TintaCreateView(CreateView):
    model = Tinta
    form_class = VendaForm
    template_name = 'cadastrar/tinta.html'

    def get_success_url(self):
        messages.success(self.request, 'Tinta cadastrado com suceso!')
        return reverse_lazy("listar_tinta")


class EsquadriaCreateView(CreateView):
    model = Esquadria
    template_name = 'cadastrar/esquadria.html'

    def get_success_url(self):
        messages.success(self.request, 'Esquadria cadastrada com suceso!')
        return reverse_lazy("listar_esquadria")


class MadeiraCreateView(CreateView):
    model = Madeira
    template_name = 'cadastrar/madeira.html'

    def get_success_url(self):
        messages.success(self.request, 'Madeira cadastrada com suceso!')
        return reverse_lazy("listar_madeira")


class PedraCreateView(CreateView):
    model = Pedra
    template_name = 'cadastrar/pedra.html'

    def get_success_url(self):
        messages.success(self.request, 'Pedra cadastrada com suceso!')
        return reverse_lazy("listar_pedra")


class MaquinaCreateView(CreateView):
    model = Maquina
    template_name = 'cadastrar/maquina.html'

    def get_success_url(self):
        messages.success(self.request, 'Maquina cadastrada com suceso!')
        return reverse_lazy("listar_maquina")


class CeramicaCreateView(CreateView):
    model = Ceramica
    template_name = 'cadastrar/ceramica.html'

    def get_success_url(self):
        messages.success(self.request, 'Ceramica cadastrada com suceso!')
        return reverse_lazy("listar_ceramica")


class CobertaCreateView(CreateView):
    model = Coberta
    template_name = 'cadastrar/coberta.html'

    def get_success_url(self):
        messages.success(self.request, 'Coberta cadastrada com suceso!')
        return reverse_lazy("listar_coberta")


class FerramentaCreateView(CreateView):
    model = Ferramenta
    template_name = 'cadastrar/ferramenta.html'

    def get_success_url(self):
        messages.success(self.request, 'Ferramenta cadastrada com suceso!')
        return reverse_lazy("listar_ferramenta")


class IluminacaoCreateView(CreateView):
    model = Iluminacao
    template_name = 'cadastrar/iluminacao.html'

    def get_success_url(self):
        messages.success(self.request, 'Iluminacao cadastrada com suceso!')
        return reverse_lazy("listar_iluminacao")


class EstruturaCreateView(CreateView):
    model = Estrutura
    template_name = 'cadastrar/estrutura.html'

    def get_success_url(self):
        messages.success(self.request, 'Estrutura cadastrada com suceso!')
        return reverse_lazy("listar_estrutura")


class PisoCreateView(CreateView):
    model = Piso
    template_name = 'cadastrar/Piso.html'

    def get_success_url(self):
        messages.success(self.request, 'Piso cadastrado com suceso!')
        return reverse_lazy("listar_Piso")


# ______________________________________ListView_____________________________________
class VendaListView(ListView):
    model = Venda
    template_name = 'listar/venda.html'
    paginate_by = 3


# ______________________________________UpdateView_____________________________________
class VendaCorrecaoUpdateView(UpdateView):
    model = Venda
    form_class = VendaForm
    template_name = 'atualizar/venda.html'

    def get_success_url(self):
        messages.success(self.request, 'Venda atualizada com sucesso!')
        return reverse_lazy('listar_venda')


class VendaAtualizarObservacaoView(UpdateView):
    model = Venda
    form_class = VendaObservacaoForm
    template_name = 'atualizar/venda_observacao.html'

    def get_success_url(self):
        messages.success(self.request, 'Observação da venda atualizada com sucesso!')
        return reverse_lazy('listar_venda')


class VendaAtualizarClienteView(UpdateView):
    model = Venda
    form_class = VendaClienteForm
    template_name = 'atualizar/venda_cliente.html'

    def get_success_url(self):
        messages.success(self.request, 'Cliente da venda atualizada com sucesso!')
        return reverse_lazy('listar_venda')


# ______________________________________DetailView_____________________________________

class VendaView(View):
    def desabilitarVenda(self, pk: int):
        Venda.objects.filter(id=pk).update(excluido=True)
        return HttpResponseRedirect(reverse_lazy('listar_venda'))

    def habilitarVenda(self, pk: int):
        Venda.objects.filter(id=pk).update(excluido=False)
        return HttpResponseRedirect(reverse_lazy('listar_venda'))


class VendaDetailView(DetailView):
    model = Venda
    template_name = 'detalhes/venda.html'
