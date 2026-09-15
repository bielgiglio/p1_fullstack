from django.shortcuts import render, redirect
from .models import Produto, Deposito, Movimentacao
from .forms import MovimentacaoForm

def saldo_por_deposito(request):
    depositos = Deposito.objects.all()
    produtos = Produto.objects.all()
    relatorio = []

    for dep in depositos:
        itens_deposito = []
        for prod in produtos:
            entradas = Movimentacao.objects.filter(deposito=dep, produto=prod, tipo='ENTRADA')
            saidas = Movimentacao.objects.filter(deposito=dep, produto=prod, tipo='SAIDA')

            total_entradas = sum(m.quantidade for m in entradas)
            total_saidas = sum(m.quantidade for m in saidas)
            saldo = total_entradas - total_saidas

            itens_deposito.append({
                'produto': prod,
                'saldo': saldo,
                'ponto_pedido': prod.ponto_pedido,
                'alerta_reposicao': saldo <= prod.ponto_pedido
            })

        relatorio.append({
            'deposito': dep,
            'itens': itens_deposito
        })

    return render(request, 'estoque/saldo_depositos.html', {'relatorio': relatorio})


def lista_movimentacoes(request):
    movimentacoes = Movimentacao.objects.all().order_by('-data')
    return render(request, 'estoque/lista_movimentacoes.html', {'movimentacoes': movimentacoes})


def nova_movimentacao(request):
    if request.method == 'POST':
        form = MovimentacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('saldo_depositos')
    else:
        form = MovimentacaoForm()

    return render(request, 'estoque/form_movimentacao.html', {'form': form})