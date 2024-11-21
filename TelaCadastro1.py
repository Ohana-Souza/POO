from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

# Função para exibir a tela de cadastro
def mostrar_tela_cadastro(janela, acao):
    # Tela de cadastro (inicialmente oculta)
    tela_cadastro = Frame(janela)
    tela_cadastro.pack(fill=BOTH, expand=True)

    # Alterar a imagem da tela de cadastro
    caminho_imagem_cadastro1 = Image.open("TelaCadastro1.png")
    imagem_redimensionada_cadastro1 = caminho_imagem_cadastro1.resize((300,600), Image.LANCZOS)
    imagem_de_fundo_cadastro1 = ImageTk.PhotoImage(imagem_redimensionada_cadastro1)

    # Armazenar a imagem para evitar que seja descartada
    tela_cadastro.imagem_de_fundo_cadastro1 = imagem_de_fundo_cadastro1

    # Exibir a imagem no fundo da tela de cadastro
    label_imagem_de_fundo_cadastro1 = Label(tela_cadastro, image=imagem_de_fundo_cadastro1)
    label_imagem_de_fundo_cadastro1.place(x=0, y=0, relwidth=1, relheight=1)



    # Labels e campos para o cadastro
    
    nx1 = 50
    ny1 = 220
    
    ex1 = nx1
    ey1 = ny1 + 30
    
    ttk.Label(tela_cadastro, text="Email:").place(x=nx1, y=ny1)
    email_entry = ttk.Entry(tela_cadastro, font=("Arial", 12))
    email_entry.place(x=ex1, y=ey1, width=200)

    nx2 = nx1
    ny2 = ny1 + 80
    
    ex2 = nx1
    ey2 = ny2 + 30
    
    ttk.Label(tela_cadastro, text="Senha:").place(x=nx2, y=ny2)
    senha_entry = ttk.Entry(tela_cadastro, font=("Arial", 12), show="*")
    senha_entry.place(x=ex2, y=ey2, width=200)

    nx3 = nx1
    ny3 = ny2 + 80 
    
    ex3 = nx1
    ey3 = ny3 + 30

    ttk.Label(tela_cadastro, text="Confirme a senha:").place(x=nx3, y=ny3)
    conf_senha_entry = ttk.Entry(tela_cadastro, font=("Arial", 12), show="*")
    conf_senha_entry.place(x=ex3, y=ey3, width=200)

    # Botão "Entrar" da tela de cadastro
    entrar_btn = ttk.Button(tela_cadastro, text="Entrar", command=entrar, style="TButton")
    entrar_btn.place(x=50, y=(ny1 + 280), width=200, height=50)

# Função para o botão "Entrar" da tela de cadastro
def entrar():
    print("Botão 'Entrar' clicado na tela de cadastro")
