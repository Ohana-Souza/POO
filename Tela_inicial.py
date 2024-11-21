"""import tkinter as tk
from tkinter import ttk

# Função para calcular carboidratos
def calcular_carboidratos():
    # Obtém os valores da refeição, alimento e quantidade selecionados pelo usuário
    refeicao = refeicao_var.get()
    alimento = alimento_var.get()
    quantidade = quantidade_var.get()
    
    # Valores de carboidratos por 100g (exemplo)
    alimentos = {
        'Arroz': 28,
        'Feijão': 27,
        'Pão': 15,
        'Batata': 17,
        'Maçã': 25,
        'Banana': 27
    }
    
    # Calcula a quantidade de carboidratos com base na seleção e quantidade
    carboidratos = alimentos.get(alimento, 0) * (quantidade / 100)
    
    # Atualiza o label de resultado com as informações calculadas
    resultado_label.config(text=f'Refeição: {refeicao}\nAlimento: {alimento}\nQuantidade: {quantidade}g\nCarboidratos: {carboidratos:.2f}g')

# Criação da janela principal do aplicativo
janela = tk.Tk()
janela.title("Contador de Carboidratos")
janela.geometry("550x350+205+205")
janela.resizable(True, True)
janela['bg'] = "green"

# Variáveis para armazenar os valores das seleções
refeicao_var = tk.StringVar()
alimento_var = tk.StringVar()
quantidade_var = tk.DoubleVar()

# Seleção da refeição
ttk.Label(janela, text="Selecione a refeição:").grid(column=0, row=0)
refeicoes = ['Almoço', 'Café', 'Janta', 'Lanche']
refeicao_combo = ttk.Combobox(janela, textvariable=refeicao_var, values=refeicoes)
refeicao_combo.grid(column=1, row=0)

# Valores de carboidratos por 100g (exemplo)
alimentos = {
    'Arroz': 28,
    'Feijão': 27,
    'Pão': 15,
    'Batata': 17,
    'Maçã': 25,
    'Banana': 27
}

# Seleção do alimento
ttk.Label(janela, text="Selecione o alimento:").grid(column=0, row=1)
alimento_combo = ttk.Combobox(janela, textvariable=alimento_var, values=list(alimentos.keys()))
alimento_combo.grid(column=1, row=1)

# Entrada da quantidade
ttk.Label(janela, text="Quantidade (g):").grid(column=0, row=2)
quantidade_entry = ttk.Entry(janela, textvariable=quantidade_var)
quantidade_entry.grid(column=1, row=2)

# Botão para calcular
calcular_btn = ttk.Button(janela, text="Calcular Carboidratos", command=calcular_carboidratos)
calcular_btn.grid(column=0, row=3, columnspan=2)

# Label para mostrar o resultado
resultado_label = ttk.Label(janela, text="", justify=tk.LEFT)
resultado_label.grid(column=0, row=4, columnspan=2)

# Inicia o loop principal da interface gráfica, mantendo a janela aberta
janela.mainloop()
"""


from tkinter import *
from PIL import ImageTk, Image

janela = Tk()

# Dimensão base tela celular
janela.geometry('900x1600')
janela.title("Interface Gráfica")

# Abrir e redimensionar a imagem
caminho_imagem = Image.open("image_teste.png")
imagem_redimensionada = caminho_imagem.resize((450,800), Image.LANCZOS)

# Converter a imagem para o formato adequado para o Tkinter
imagem_de_fundo = ImageTk.PhotoImage(imagem_redimensionada)

# Exibir a imagem no fundo
label_imagem_de_fundo = Label(janela, image=imagem_de_fundo)  # Usar 'imagem_de_fundo' aqui
label_imagem_de_fundo.place(x=0, y=0, relwidth=1, relheight=1)

# Inicia o loop principal da interface gráfica
janela.mainloop()
