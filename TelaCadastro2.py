from tkinter import *
from tkinter import ttk

# Função para exibir a tela de cadastro 2 (Perfil Médico)
def mostrar_tela_cadastro2(janela):
    # Tela de cadastro 2 (inicialmente oculta)
    tela_cadastro2 = Frame(janela)
    tela_cadastro2.pack(fill=BOTH, expand=True)

    # Alterar a imagem da tela de cadastro 2
    caminho_imagem_cadastro2 = Image.open("TelaCadastro2.png")  # Atualize para o caminho da imagem de fundo, se necessário
    imagem_redimensionada_cadastro2 = caminho_imagem_cadastro2.resize((300,600), Image.LANCZOS)
    imagem_de_fundo_cadastro2 = ImageTk.PhotoImage(imagem_redimensionada_cadastro2)

    # Armazenar a imagem para evitar que seja descartada
    tela_cadastro2.imagem_de_fundo_cadastro2 = imagem_de_fundo_cadastro2

    # Exibir a imagem no fundo da tela de cadastro 2
    label_imagem_de_fundo_cadastro2 = Label(tela_cadastro2, image=imagem_de_fundo_cadastro2)
    label_imagem_de_fundo_cadastro2.place(x=0, y=0, relwidth=1, relheight=1)

    # Labels e campos para o cadastro médico
    nx1 = 50
    ny1 = 220

    # Campo Sexo
    ttk.Label(tela_cadastro2, text="Sexo:").place(x=nx1, y=ny1)
    sexo_var = StringVar()
    sexo_combobox = ttk.Combobox(tela_cadastro2, textvariable=sexo_var, values=["Masculino", "Feminino"], font=("Arial", 12))
    sexo_combobox.place(x=nx1, y=ny1 + 30, width=200)
    sexo_combobox.set("Masculino")  # valor inicial

    # Campo Altura
    ttk.Label(tela_cadastro2, text="Altura (em cm):").place(x=nx1, y=ny1 + 80)
    altura_entry = ttk.Entry(tela_cadastro2, font=("Arial", 12))
    altura_entry.place(x=nx1, y=ny1 + 110, width=200)

    # Campo Idade
    ttk.Label(tela_cadastro2, text="Idade:").place(x=nx1, y=ny1 + 160)
    idade_entry = ttk.Entry(tela_cadastro2, font=("Arial", 12))
    idade_entry.place(x=nx1, y=ny1 + 190, width=200)

    # Campo "Faz Exercício"
    ttk.Label(tela_cadastro2, text="Faz Exercício?").place(x=nx1, y=ny1 + 240)
    exercicio_var = StringVar()
    exercicio_combobox = ttk.Combobox(tela_cadastro2, textvariable=exercicio_var, values=["Sim", "Não"], font=("Arial", 12))
    exercicio_combobox.place(x=nx1, y=ny1 + 270, width=200)
    exercicio_combobox.set("Sim")  # valor inicial

    # Campo Tipo de Diabetes
    ttk.Label(tela_cadastro2, text="Tipo de Diabetes:").place(x=nx1, y=ny1 + 320)
    diabetes_var = StringVar()
    diabetes_combobox = ttk.Combobox(tela_cadastro2, textvariable=diabetes_var, values=["Tipo 1", "Tipo 2", "Pré-Diabetes"], font=("Arial", 12))
    diabetes_combobox.place(x=nx1, y=ny1 + 350, width=200)
    diabetes_combobox.set("Tipo 1")  # valor inicial

    # Campo Toma Insulina
    ttk.Label(tela_cadastro2, text="Toma Insulina?").place(x=nx1, y=ny1 + 400)
    insulina_var = StringVar()
    insulina_combobox = ttk.Combobox(tela_cadastro2, textvariable=insulina_var, values=["Sim", "Não"], font=("Arial", 12))
    insulina_combobox.place(x=nx1, y=ny1 + 430, width=200)
    insulina_combobox.set("Sim")  # valor inicial

    # Botão para concluir o cadastro e passar para a próxima tela
    concluir_btn = ttk.Button(tela_cadastro2, text="Concluir Cadastro", command=concluir_cadastro, style="TButton")
    concluir_btn.place(x=50, y=(ny1 + 500), width=200, height=50)

# Função para concluir o cadastro (exemplo de ação no botão "Concluir Cadastro")
def concluir_cadastro():
    print("Cadastro médico concluído!")
    # Ação de continuar ou salvar dados pode ser adicionada aqui
