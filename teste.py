import tkinter as tk
from PIL import Image, ImageTk

def redimensionar_imagem(event):
    # Redimensionar a imagem de acordo com o tamanho da janela
    largura = event.width
    altura = event.height
    imagem = Image.open("tpos.jpeg")
    imagem = imagem.resize((largura, altura), Image.LANCZOS)
    imagem_tk = ImageTk.PhotoImage(imagem)

    # Adicionar a imagem ao canvas
    canvas.create_image(0, 0, anchor=tk.NW, image=imagem_tk)
    canvas.image = imagem_tk  # Manter referência da imagem

# Configuração inicial da janela principal
root = tk.Tk()
root.title("Exibição de Imagem Redimensionável")
root.geometry("800x600")

# Configurando o canvas
canvas = tk.Canvas(root)
canvas.pack(fill=tk.BOTH, expand=True)

# Carregar e adicionar a imagem inicial
imagem_inicial = Image.open("tpos.jpeg")
imagem_inicial = imagem_inicial.resize((800, 600), Image.LANCZOS)
imagem_tk_inicial = ImageTk.PhotoImage(imagem_inicial)
canvas.create_image(0, 0, anchor=tk.NW, image=imagem_tk_inicial)
canvas.image = imagem_tk_inicial  # Manter referência da imagem

# Adicionando textos na frente da imagem
canvas.create_text(400, 50, text="Bem-vindo!", fill="white", font=("Helvetica", 24, "bold"))
canvas.create_text(400, 550, text="Aproveite sua estadia!", fill="white", font=("Helvetica", 20, "italic"))

# Ligar o evento de redimensionamento
root.bind("<Configure>", redimensionar_imagem)

# Inicia a janela principal
root.mainloop()
