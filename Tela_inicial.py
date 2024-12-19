from tkinter import *
from PIL import ImageTk, Image
import TelaCadastro1  # Importa a TelaCadastro1
import TelaCadastro2  # Importa a TelaCadastro2

# Função chamada quando o botão "Cadastrar" for clicado
def cadastrar():
    # Esconde a tela inicial
    tela_inicial.pack_forget()

    # Exibe a tela de cadastro 1
    TelaCadastro1.mostrar_tela_cadastro(janela)

# Função chamada quando o botão "Entrar" for clicado
def entrar():
    # Esconde a tela inicial
    tela_inicial.pack_forget()

    # Exibe a tela de cadastro 1
    TelaCadastro1.mostrar_tela_cadastro(janela)

# Criação da janela principal
janela = Tk()

# Dimensão da tela inicial
janela.geometry('300x600')
janela.title("Interface Gráfica")

# Tela inicial com a imagem de fundo
tela_inicial = Frame(janela)
tela_inicial.pack(fill=BOTH, expand=True)

# Abrir e redimensionar a imagem para a tela inicial
caminho_imagem = Image.open("image_teste.png")
imagem_redimensionada = caminho_imagem.resize((300,600), Image.LANCZOS)  # Redimensionando a imagem para 300x600

# Converter a imagem para o formato adequado para o Tkinter
imagem_de_fundo = ImageTk.PhotoImage(imagem_redimensionada)

# Exibir a imagem no fundo
label_imagem_de_fundo = Label(tela_inicial, image=imagem_de_fundo)
label_imagem_de_fundo.place(x=0, y=0, relwidth=1, relheight=1)

# Criar o botão "Entrar"
botao_entrar = Button(tela_inicial, text="Entrar", command=entrar, font=("Arial", 16), bg="green", fg="white")
botao_entrar.place(x=50, y=450, width=200, height=50)

# Criar o botão "Cadastrar"
botao_cadastrar = Button(tela_inicial, text="Cadastrar", command=cadastrar, font=("Arial", 16), bg="blue", fg="white")
botao_cadastrar.place(x=50, y=520, width=200, height=50)

# Inicia o loop principal da interface gráfica
janela.mainloop()
