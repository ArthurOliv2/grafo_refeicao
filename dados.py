from arvore import NoArvore
from grafo import Grafo
from restaurantes import restaurantes

raiz = None
for r in restaurantes:
    novo_no = NoArvore(
        r["nome"], r["tipo"], r["localidade"], r["preco_min"], r["preco_max"]
    )
    if raiz is None:
        raiz = novo_no
    else:
        raiz.inserir(novo_no)

g = Grafo()
for r in restaurantes:
    g.adicionar_vertice(r["nome"])

for origem in restaurantes:
    for destino in restaurantes:
        if (origem["nome"] != destino["nome"] and origem["localidade"] == destino["localidade"]):
            g.adicionar_aresta(origem["nome"], destino["nome"])

tipos = {r["nome"]: r["tipo"] for r in restaurantes}
localidades = list(set(r["localidade"] for r in restaurantes))

