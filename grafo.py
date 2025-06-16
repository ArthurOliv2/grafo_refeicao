class Grafo:
    def __init__(self):
        self.grafo = {}

    def adicionar_vertice(self, restaurante):
        if restaurante not in self.grafo:
            self.grafo[restaurante] = []

    def adicionar_aresta(self, origem, destino):
        if origem in self.grafo and destino in self.grafo:
            self.grafo[origem].append(destino)
            self.grafo[destino].append(origem)   