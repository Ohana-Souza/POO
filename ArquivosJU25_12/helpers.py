import tkinter as tk

# Função para mudar de tela
def mudar_tela(nova_tela, root, *args):
    for widget in root.winfo_children():
        widget.destroy()
    nova_tela(root, *args)
