from django import forms
from .models import Movimentacao

class MovimentacaoForm(forms.ModelForm):
    class Meta:
        model = Movimentacao
        fields = ['produto', 'deposito', 'tipo', 'quantidade']

    def clean(self):
        cleaned_data = super().clean()
        produto = cleaned_data.get('produto')
        deposito = cleaned_data.get('deposito')
        tipo = cleaned_data.get('tipo')
        quantidade = cleaned_data.get('quantidade')

        if produto and deposito and tipo and quantidade:
            if quantidade <= 0:
                self.add_error('quantidade', 'A quantidade precisa ser maior que zero.')

            if tipo == 'SAIDA':
                entradas = Movimentacao.objects.filter(deposito=deposito, produto=produto, tipo='ENTRADA')
                saidas = Movimentacao.objects.filter(deposito=deposito, produto=produto, tipo='SAIDA')

                total_entradas = sum(m.quantidade for m in entradas)
                total_saidas = sum(m.quantidade for m in saidas)
                saldo_disponivel = total_entradas - total_saidas

                if quantidade > saldo_disponivel:
                    self.add_error('quantidade', f'Saldo insuficiente. Esse depósito possui apenas {saldo_disponivel} unidade(s) disponível(is).')

        return cleaned_data