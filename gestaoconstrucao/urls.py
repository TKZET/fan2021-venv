from django.contrib import admin
from django.urls import path
from .views import VendaCreateView, EletricosCreateView, HidraulicoCreateView, ClienteCreateView, VidroCreateView \
    , TintaCreateView, EsquadriaCreateView, MadeiraCreateView, PedraCreateView, MaquinaCreateView, CeramicaCreateView \
    , CobertaCreateView, FerramentaCreateView, IluminacaoCreateView, EstruturaCreateView, PisoCreateView \
    , VendaListView, VendaCorrecaoUpdateView, VendaAtualizarObservacaoView, VendaAtualizarClienteView, VendaDetailView, \
    VendaView

urlpatterns = [
    path('cadastrar/Venda', VendaCreateView.as_view(), name="cadastrar_Venda"),
    path('cadastrar/Eletricos', EletricosCreateView.as_view(), name="cadastrar_Eletricos"),
    path('cadastrar/Hidraulico', HidraulicoCreateView.as_view(), name="cadastrar_Hidraulico"),
    path('cadastrar/Cliente', ClienteCreateView.as_view(), name="cadastrar_Cliente"),
    path('cadastrar/Vidro', VidroCreateView.as_view(), name="cadastrar_Vidro"),
    path('cadastrar/Tinta', TintaCreateView.as_view(), name="cadastrar_Tinta"),
    path('cadastrar/Esquadria', EsquadriaCreateView.as_view(), name="cadastrar_Esquadria"),
    path('cadastrar/Madeira', MadeiraCreateView.as_view(), name="cadastrar_Madeira"),
    path('cadastrar/Pedra', PedraCreateView.as_view(), name="cadastrar_Pedra"),
    path('cadastrar/Maquina', MaquinaCreateView.as_view(), name="cadastrar_Maquina"),
    path('cadastrar/Ceramica', CeramicaCreateView.as_view(), name="cadastrar_Ceramica"),
    path('cadastrar/Coberta', CobertaCreateView.as_view(), name="cadastrar_Coberta"),
    path('cadastrar/Ferramenta', FerramentaCreateView.as_view(), name="cadastrar_Ferramenta"),
    path('cadastrar/Iluminacao', IluminacaoCreateView.as_view(), name="cadastrar_Iluminacao"),
    path('cadastrar/Estrutura', EstruturaCreateView.as_view(), name="cadastrar_Estrutura"),
    path('cadastrar/Piso', PisoCreateView.as_view(), name="cadastrar_Piso"),
    path('listar/venda', VendaListView.as_view(), name="listar_venda"),
    path('atualizar/venda/<int:pk>', VendaCorrecaoUpdateView.as_view(), name="corrigir_venda"),
    path('atualizar/venda/observacao/<int:pk>', VendaAtualizarObservacaoView.as_view(),
         name="atualizar_observacao_venda"),
    path('atualizar/venda/cliente/<int:pk>', VendaAtualizarClienteView.as_view(), name="atualizar_cliente_venda"),
    path('ajax/desabilitar/venda/<int:pk>', VendaView.desabilitarVenda, name="ajax_desabilitar_venda"),
    path('ajax/habilitar/venda/<int:pk>', VendaView.habilitarVenda, name="ajax_habilitar_venda"),
    path('detalhes/venda/<int:pk>', VendaDetailView.as_view(), name="detalhes_venda"),
]
