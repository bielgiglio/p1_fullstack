from django.urls import path
from . import views

urlpatterns = [
    path('', views.saldo_por_deposito, name='saldo_depositos'),
    path('movimentacoes/', views.lista_movimentacoes, name='lista_movimentacoes'),
    path('movimentacoes/nova/', views.nova_movimentacao, name='nova_movimentacao'),
]