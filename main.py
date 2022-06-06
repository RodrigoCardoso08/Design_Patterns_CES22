class Livraria:

    def __init__(self, nome):
        self.nome = nome
        self.livros = []
        self.autores = []
        self.clientes = []
        self.vendas_realizadas = []

    def inserir_livro(self, livro):
        self.livros.append(livro)
        self.autores.append(livro.autor)

    def alterar_livro(self, livro, novo_valor):
        for busca in self.livros:
            if busca == livro:
                livro.preco_venda = novo_valor

    def consultar_livro(self, autor):
        for livro in self.livros:
            if livro.autor == autor:
                print(livro.titulo)

    def remover_livro(self, livro):
        self.livros.remove(livro)

    def inserir_cliente(self, cliente):
        self.clientes.append(cliente)

    def alterar_cliente(self, cliente, novo_nome, novo_email):
        for cliente_buscado in self.clientes:
            if cliente_buscado == cliente:
                cliente.nome = novo_nome
                cliente.email = novo_email

    def consultar_cliente(self, cliente):
        for cliente_buscado in self.clientes:
            if cliente_buscado == cliente:
                print('Cliente encontrado com sucesso!')

    def remover_cliente(self, cliente):
        self.clientes.remove(cliente)

    def inserir_compra(self, compra):
        self.vendas_realizadas.append(compra)

    def alterar_compra(self, compra, novo_id):
        for id_busca in self.vendas_realizadas:
            if id_busca == compra.id_compra:
                compra.id_compra = novo_id

    def consultar_compra(self, compra):
        for id_busca in self.vendas_realizadas:
            if id_busca == compra.id_compra:
                print(compra.id_compra)
                print(compra.valor)

    def remover_compra(self, compra):
        self.vendas_realizadas.remove(compra)


class Livro:

    def __init__(self, titulo, autor, genero, edicao, editora, preco_venda, preco_compra, impostos):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.edicao = edicao
        self.editora = editora
        self.preco_venda = preco_venda
        self.preco_compra = preco_compra
        self.impostos = impostos
        self.preco = 0

    def calcular_preco(self, taxa):
        self.preco = self.preco_venda + taxa


class Taxa:

    def __init__(self):
        self.taxa = 0

    def calcular_taxa(self, livro):
        if livro.genero == 'romance':
            self.taxa = 1.05 * livro.preco_venda
        if livro.genero == 'acao':
            self.taxa = 1.10 * livro.preco_venda


class Pessoa:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email


class Autor(Pessoa):

    def __init__(self, nome, email, titulos_publicados):
        self.titulos_publicados = titulos_publicados
        super().__init__(nome, email)


class Cliente(Pessoa):

    def __init__(self, nome, email, compras_passadas):
        self.compras_passadas = compras_passadas
        super().__init__(nome, email)


class Compra:

    def __init__(self, id_compras, lista_de_quantidades, lista_de_valores):
        self.lista_de_quantidades = lista_de_quantidades
        self.lista_de_valores = lista_de_valores
        self.valor = 0
        self.id_compra = id_compras

    def valor_a_pagar(self):
        cont = 0
        while cont < 3:
            self.valor = self.valor + self.lista_de_valores[cont] * self.lista_de_quantidades[cont]




