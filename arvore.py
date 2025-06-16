class NoArvore:
    def __init__(self, nome, tipo, localidade, preco_min, preco_max):
        self.nome = nome
        self.tipo = tipo
        self.localidade = localidade
        self.preco_min = preco_min
        self.preco_max = preco_max
        self.esquerda = None
        self.direita = None

    def inserir(self, novo_no):
        if novo_no.preco_min < self.preco_min:
            if self.esquerda is None:
                self.esquerda = novo_no
            else:
                self.esquerda.inserir(novo_no)
        else:
            if self.direita is None:
                self.direita = novo_no
            else:
                self.direita.inserir(novo_no)

    def buscar(self, tipo, localidade, orcamento_individual):
        resultado = []
        if self.esquerda:
            resultado += self.esquerda.buscar(tipo, localidade, orcamento_individual)
        if (self.tipo.lower() == tipo.lower() and self.localidade.lower() == localidade.lower() and orcamento_individual >= self.preco_min):
            resultado.append((self.nome, self.preco_min, self.preco_max, self.localidade))
        if self.direita:
            resultado += self.direita.buscar(tipo, localidade, orcamento_individual)
        return resultado