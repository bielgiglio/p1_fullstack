from django.contrib import admin
from .models import Fornecedor, Deposito, Produto, Movimentacao

admin.site.register(Fornecedor)
admin.site.register(Deposito)
admin.site.register(Produto)
admin.site.register(Movimentacao)