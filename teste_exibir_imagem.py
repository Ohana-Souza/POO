import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def teste_tkinter_pillow():
    root = tk.Tk()
    root.title("Teste de Importação")

    # Teste de Messagebox
    def exibir_mensagem():
        messagebox.showinfo("Informação", "Tkinter e Pillow estão funcionando!")

    # Teste de Imagem
    frame = tk.Frame(root)
    frame.pack(padx=20, pady=20)

    try:
        imagem = Image.open(r"C:\Users\ohana\Downloads\codigo feito\POO\tinicial.jpeg")  # Substitua pelo caminho correto
        imagem_tk = ImageTk.PhotoImage(imagem)
        label_imagem = tk.Label(frame, image=imagem_tk)
        label_imagem.image = imagem_tk  # Manter referência da imagem
        label_imagem.pack(pady=10)
    except Exception as e:
        print("Erro ao carregar imagem:", e)

    btn_mensagem = tk.Button(root, text="Exibir Mensagem", command=exibir_mensagem)
    btn_mensagem.pack(pady=10)

    root.mainloop()

teste_tkinter_pillow()
