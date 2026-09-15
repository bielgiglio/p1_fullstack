# Controle de Estoque — MVP (P1)

Projeto desenvolvido para a disciplina de **Laboratório de Programação Full Stack** (Universidade de Vassouras) referente à entrega **P1 — MVP Funcional** do Projeto 10.

A aplicação consiste em um sistema monolítico em **Django puro** com persistência em banco relacional **PostgreSQL**, arquitetada no padrão **MVT** (Model-View-Template) e conteinerizada com **Docker Compose**.

---

## Funcionalidades (P1)

* **Gestão das 4 Entidades Centrais:** Produto, Depósito, Fornecedor e Movimentação.
* **Cálculo Dinâmico de Saldo por Depósito:** Totalização automática de estoque considerando entradas e saídas por localização física.
* **Ponto de Pedido:** Indicação visual de alerta de reposição quando o saldo atinge ou fica abaixo da cota mínima configurada.
* **Validação de Saldo Insuficiente:** Bloqueio no formulário para impedir saídas superiores ao saldo disponível no depósito selecionado.
* **Histórico de Movimentações:** Visualização cronológica de todas as entradas e saídas registradas.
* **Painel Administrativo:** Gestão e cadastros completos via Django Admin.

---

## Tecnologias Utilizadas

* **Linguagem:** Python 3.11
* **Framework:** Django 5 (Django puro com DTL)
* **Banco de Dados:** PostgreSQL 15
* **Containerização:** Docker e Docker Compose
* **Gerenciamento de Credenciais:** `python-dotenv`

---

## Estrutura do Projeto

```text
controle_estoque/
├── controle_estoque/       # Configurações do projeto Django (settings, urls, wsgi)
├── estoque/                # App do sistema
│   ├── migrations/         # Arquivos de migração
│   ├── templates/estoque/  # Templates HTML com DTL e herança de base.html
│   ├── admin.py            # Registro das entidades no Django Admin
│   ├── forms.py            # ModelForm com validação de saldo
│   ├── models.py           # Modelos: Fornecedor, Deposito, Produto, Movimentacao
│   ├── urls.py             # Rotas do app
│   └── views.py            # Regras de negócio e cálculo de saldo
├── .env                    # Variáveis de ambiente (ignorado no Git)
├── .env.example            # Exemplo de variáveis de ambiente
├── .gitignore              # Regras de exclusão do Git
├── docker-compose.yml      # Configuração dos serviços Web e Banco
├── Dockerfile              # Instruções de build da imagem Python/Django
├── manage.py
└── requirements.txt        # Dependências do projeto
```

## Como Executar com Docker
# 1. Clonar o repositório
```bash
git clone https://github.com/bielgiglio/p1_fullstack
cd controle_estoque
```

# 2. Configurar o arquivo de variáveis de ambiente
Crie um arquivo .env na raiz do projeto com base no .env.example:

```bash
Snippet de código
DB_NAME=estoque_db
DB_USER=postgres
DB_PASSWORD=senha
DB_HOST=db
```
# 3. Subir os containers
Construa a imagem e inicialize os serviços:
```bash
docker compose up --build
```

(O container aplicará as migrações no banco de dados automaticamente na inicialização).

# 4. Criar o usuário administrador
Com os containers ativos, abra outro terminal no diretório do projeto e execute:

```Bash
docker compose exec web python manage.py createsuperuser
```

## Rotas da Aplicação

* ```bash / ``` — Painel com os saldos calculados por depósito e status do ponto de pedido

* ```bash /movimentacoes/``` — Lista com o histórico de entradas e saídas

* ```bash /movimentacoes/nova/``` — Formulário para registrar movimentações de estoque

* ```bash /admin/``` — Acesso ao painel administrativo nativo do Django

