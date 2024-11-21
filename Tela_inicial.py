from tkinter import *
from PIL import ImageTk, Image

# Função chamada quando o botão "Entrar" for clicado
def entrar():
    print("Botão 'Entrar' clicado")

# Função chamada quando o botão "Cadastrar" for clicado
def cadastrar():
    print("Botão 'Cadastrar' clicado")

# Criação da janela
janela = Tk()

# Dimensão da tela alterada para 300x600
janela.geometry('300x600')  # Agora a tela tem 300x600
janela.title("Interface Gráfica")

# Abrir e redimensionar a imagem
caminho_imagem = Image.open("image_teste.png")
imagem_redimensionada = caminho_imagem.resize((300,600), Image.LANCZOS)  # Redimensionando a imagem para a nova tela

# Converter a imagem para o formato adequado para o Tkinter
imagem_de_fundo = ImageTk.PhotoImage(imagem_redimensionada)

# Exibir a imagem no fundo
label_imagem_de_fundo = Label(janela, image=imagem_de_fundo)  # Usar 'imagem_de_fundo' aqui
label_imagem_de_fundo.place(x=0, y=0, relwidth=1, relheight=1)

# Criar o botão "Entrar"
botao_entrar = Button(janela, text="Entrar", command=entrar, font=("Arial", 16), bg="green", fg="white")
botao_entrar.place(x=50, y=450, width=200, height=50)

# Criar o botão "Cadastrar"
botao_cadastrar = Button(janela, text="Cadastrar", command=cadastrar, font=("Arial", 16), bg="blue", fg="white")
botao_cadastrar.place(x=50, y=520, width=200, height=50)

# Inicia o loop principal da interface gráfica
janela.mainloop()
