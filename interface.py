import tkinter as tk
from tkinter import messagebox
from dados import raiz, g, tipos, localidades


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
    janela.title("Recomendador de Restaurantes - Maricá")
    janela.geometry("500x500")
    janela.configure(bg="#F0F0F0")

    label = tk.Label(
        janela, text="Monte seu roteiro gastronômico",
        font=("Arial", 16), bg="#F0F0F0"
    )
    label.pack(pady=10)

    label_tipo = tk.Label(janela, text="Escolha o tipo de comida:", bg="#F0F0F0")
    label_tipo.pack()
    var_tipo = tk.StringVar(janela)
    var_tipo.set("Pizzaria")
    dropdown = tk.OptionMenu(janela, var_tipo, "Pizzaria", "Sushi", "Hamburguer", "Comida Brasileira", "Sobremesa")
    dropdown.pack()

    label_local = tk.Label(janela, text="Escolha a localidade:", bg="#F0F0F0")
    label_local.pack()
    var_local = tk.StringVar(janela)
    var_local.set("Centro")
    dropdown_local = tk.OptionMenu(janela, var_local, *localidades)
    dropdown_local.pack()

    label_pessoas = tk.Label(janela, text="Quantidade de pessoas:", bg="#F0F0F0")
    label_pessoas.pack()
    entry_pessoas = tk.Entry(janela)
    entry_pessoas.pack()

    label_orcamento = tk.Label(janela, text="Orçamento total (R$):", bg="#F0F0F0")
    label_orcamento.pack()
    entry_orcamento = tk.Entry(janela)
    entry_orcamento.pack()

    botao = tk.Button(
        janela, text="Buscar Restaurantes", command=buscar_restaurantes,
        bg="#4CAF50", fg="white"
    )
    botao.pack(pady=20)

    janela.mainloop()