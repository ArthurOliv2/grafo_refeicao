# 🍽️ Recomendador de Restaurantes - Maricá

## 📜 Descrição
Este projeto é uma aplicação desenvolvida em **Python com Tkinter**, utilizando conceitos de **Estruturas de Dados** como **Árvore Binária de Busca** e **Grafos**.

O sistema permite que usuários encontrem restaurantes em Maricá, baseados em:
- ✅ Tipo de comida
- ✅ Localidade (bairro)
- ✅ Quantidade de pessoas
- ✅ Orçamento total disponível

Além disso, o sistema sugere restaurantes próximos (com base na localidade e tipo de comida) utilizando grafos.

---

## 🚀 Funcionalidades
- 🔍 Filtrar restaurantes por:
  - Tipo de comida (Pizzaria, Sushi, Hamburguer, Comida Brasileira, Sobremesa)
  - Localidade (bairros de Maricá)
  - Quantidade de pessoas
  - Orçamento total (calculando preço por pessoa)
- 🌳 Utiliza **Árvore Binária** para organizar os restaurantes e filtrar por preço, tipo e localidade.
- 🔗 Utiliza **Grafos** para sugerir restaurantes próximos dentro do mesmo bairro e do mesmo tipo.
- 🖥️ Interface gráfica feita com **Tkinter**.

---

## 🏗️ Tecnologias e Bibliotecas
- 💻 **Python 3.x**
- 🖼️ **Tkinter** (Interface gráfica)
- ✅ Bibliotecas padrão do Python (sem uso de frameworks externos)

---

## 🔗 Estruturas de Dados Aplicadas
### 🌳 **Árvore Binária:**
- Organiza os restaurantes pela faixa de preço mínima.
- Permite buscar rapidamente restaurantes que atendem ao orçamento informado.

### 🔗 **Grafo:**
- Conecta restaurantes com base na **localidade (bairro)**.
- Após encontrar um restaurante, exibe os vizinhos do mesmo bairro e do mesmo tipo como **“Sugeridos Próximos”**.

---

## 🛠️ Como Executar
1️⃣ Instale o Python (versão 3.x) se ainda não tiver.  
2️⃣ Clone ou baixe este repositório.  
3️⃣ Execute o arquivo `main.py`:
```bash
python main.py
