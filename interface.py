import tkinter as tk
from tkinter import messagebox
from dados import raiz, g, tipos, localidades
from estilo import CORES, FONTES, ESPACAMENTO


def vizinhos_do_mesmo_tipo(grafo, restaurante, tipo_desejado):
    vizinhos = grafo.vizinhos(restaurante)
    return [v for v in vizinhos if tipos[v].lower() == tipo_desejado.lower()]


def iniciar_interface():
    def buscar_restaurantes():
        try:
            tipo = var_tipo.get()
            localidade = var_local.get()
            pessoas = int(entry_pessoas.get())
            orcamento_total = float(entry_orcamento.get())

            orcamento_individual = orcamento_total / pessoas

            encontrados = raiz.buscar(tipo, localidade, orcamento_individual)

            if encontrados:
                resultado = ""
                for nome, min_preco, max_preco, loc in encontrados:
                    vizinhos = vizinhos_do_mesmo_tipo(g, nome, tipo)
                    vizinhos_str = ", ".join(vizinhos) if vizinhos else "Nenhum"
                    resultado += (
                        f"- {nome} (R$ {min_preco} a R$ {max_preco} por pessoa) - {loc}\n"
                        f"  → Sugeridos próximos: {vizinhos_str}\n\n"
                    )
                messagebox.showinfo("Restaurantes Encontrados", resultado)
            else:
                messagebox.showinfo(
                    "Sem resultados",
                    "Nenhum restaurante encontrado dentro do orçamento."
                )
        except Exception as e:
            messagebox.showerror("Erro", f"Verifique os dados inseridos.\n{e}")

    janela = tk.Tk()
    janela.title("🍽️ Recomendador de Restaurantes - Maricá")
    janela.geometry("800x700")
    janela.configure(bg=CORES["fundo"])

    janela.columnconfigure(0, weight=1)

    label = tk.Label(
        janela,
        text="Monte seu roteiro gastronômico 🍕🍣🍔",
        font=FONTES["titulo"],
        bg=CORES["fundo"],
        fg=CORES["texto"],
        anchor="center"
    )
    label.grid(row=0, column=0, pady=30, sticky="n")

    frame = tk.Frame(janela, bg=CORES["fundo"])
    frame.grid(row=1, column=0, sticky="n", padx=40, pady=20)

    frame.columnconfigure(0, weight=1)

    tk.Label(frame, text="Tipo de comida:", bg=CORES["fundo"], fg=CORES["texto"], font=FONTES["label"]).grid(row=0, column=0, pady=10)
    var_tipo = tk.StringVar(janela)
    var_tipo.set("Pizzaria")
    tk.OptionMenu(frame, var_tipo, "Pizzaria", "Sushi", "Hamburguer", "Comida Brasileira", "Sobremesa").grid(row=1, column=0, sticky="ew", pady=8)

    tk.Label(frame, text="Localidade:", bg=CORES["fundo"], fg=CORES["texto"], font=FONTES["label"]).grid(row=2, column=0, pady=10)
    var_local = tk.StringVar(janela)
    var_local.set(localidades[0])
    tk.OptionMenu(frame, var_local, *localidades).grid(row=3, column=0, sticky="ew", pady=8)

    tk.Label(frame, text="Quantidade de pessoas:", bg=CORES["fundo"], fg=CORES["texto"], font=FONTES["label"]).grid(row=4, column=0, pady=10)
    entry_pessoas = tk.Entry(frame, font=FONTES["label"])
    entry_pessoas.grid(row=5, column=0, sticky="ew", pady=8)

    tk.Label(frame, text="Orçamento total (R$):", bg=CORES["fundo"], fg=CORES["texto"], font=FONTES["label"]).grid(row=6, column=0, pady=10)
    entry_orcamento = tk.Entry(frame, font=FONTES["label"])
    entry_orcamento.grid(row=7, column=0, sticky="ew", pady=8)

    botao = tk.Button(
        frame,
        text="🔍 Buscar Restaurantes",
        command=buscar_restaurantes,
        bg=CORES["botao_bg"],
        fg=CORES["botao_fg"],
        font=FONTES["botao"],
        relief="flat",
        padx=ESPACAMENTO["padx"],
        pady=ESPACAMENTO["pady"]
    )
    botao.grid(row=8, column=0, pady=25, sticky="ew")

    janela.mainloop()