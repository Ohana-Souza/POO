import tkinter as tk
from tkinter import messagebox
from supabase import create_client, Client
from Chaves_banco import SUPABASE_URL, SUPABASE_KEY
from Alimento import Alimento
from Usuario import Usuario
import re

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Função para mudar de tela
def mudar_tela(nova_tela, root, *args):
    for widget in root.winfo_children():
        widget.destroy()
    nova_tela(root, *args)

# Tela Inicial
def Tela_Inicial(root):
    frame = tk.Frame(root)
    frame.place(relwidth=1, relheight=1)

    tk.Label(frame, text="TELA INICIAL", font=("Helvetica", 16)).pack(pady=40)
    tk.Button(frame, text="Entrar", width=20, command=lambda: mudar_tela(Tela_Login, root)).pack(pady=20)
    tk.Button(frame, text="Cadastrar", width=20, command=lambda: mudar_tela(Tela_Cadastro, root)).pack(pady=20)

#Tela de Login
def Tela_Login(root):
    frame = tk.Frame(root)
    frame.place(relwidth=1, relheight=1)

    tk.Label(frame, text="Usuário:").pack(pady=5)
    entry_usuario = tk.Entry(frame)
    entry_usuario.pack(pady=5)

    tk.Label(frame, text="Senha:").pack(pady=5)
    entry_senha = tk.Entry(frame, show="*")
    entry_senha.pack(pady=5)

    error_label = tk.Label(frame, text="", fg="red")
    error_label.pack(pady=5)

    def autenticar():
        email = entry_usuario.get()
        senha = entry_senha.get()
        usuario = Usuario.autenticacao_usuario(email)

        response = usuario.autenticacao_usuario(senha)

        error_label.config(text=response, fg="red")
                        
        if response == True:
            error_label.config(text="Login realizado com sucesso!", fg="green")
            root.after(2000, lambda: mudar_tela(Tela_Consumo1, root))

    tk.Button(frame, text="Avançar", width=20, command=autenticar).pack(pady=10)
    tk.Button(frame, text="Voltar", width=20, command=lambda: mudar_tela(Tela_Inicial, root)).pack(pady=10)



# Tela de Cadastro
def Tela_Cadastro(root):
    frame = tk.Frame(root)
    frame.place(relwidth=1, relheight=1)

    tk.Label(frame, text="Email:").pack(pady=5)
    entry_email = tk.Entry(frame)
    entry_email.pack(pady=5)

    tk.Label(frame, text="Senha:").pack(pady=5)
    entry_senha = tk.Entry(frame, show="*")
    entry_senha.pack(pady=5)

    tk.Label(frame, text="Confirmar Senha:").pack(pady=5)
    entry_conf_senha = tk.Entry(frame, show="*")
    entry_conf_senha.pack(pady=5)

    error_label = tk.Label(frame, text="", fg="red")
    error_label.pack(pady=5)

    def cadastrar():
        email = entry_email.get()
        senha = entry_senha.get()
        conf_senha = entry_conf_senha.get()

        if senha != conf_senha:
            error_label.config(text="As senhas não coincidem.", fg="red")
            return

        usuario = Usuario(email)
        
        # Validate email by calling the setter
        usuario.email = email
        if not re.match(r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$', usuario.email):
            error_label.config(text="Formato de e-mail inválido.", fg="red")
            return

        response = usuario.insere_usuario(senha)

        # Update the error label with the response from insere_usuario
        if response == True:
            error_label.config(text="Usuário cadastrado com sucesso!", fg="green")
            root.after(2000, lambda: mudar_tela(Tela_Cadastro_Sucesso, root))
        else:
            error_label.config(text=response, fg="red")

    tk.Button(frame, text="Avançar", width=20, command=cadastrar).pack(pady=10)
    tk.Button(frame, text="Voltar", width=20, command=lambda: mudar_tela(Tela_Inicial, root)).pack(pady=10)

# Tela de Cadastro de Sucesso
def Tela_Cadastro_Sucesso(root):
    frame = tk.Frame(root)
    frame.place(relwidth=1, relheight=1)

    tk.Label(frame, text="Cadastro realizado com sucesso!", font=("Helvetica", 14)).pack(pady=40)
    tk.Button(frame, text="Avançar", width=20, command=lambda: mudar_tela(Tela_Consumo1, root)).pack(pady=20)

# Tela de Consumo
def Tela_Consumo1(root):
    frame = tk.Frame(root)
    frame.place(relwidth=1, relheight=1)

    tk.Label(frame, text="Tela de Consumo", font=("Helvetica", 16)).pack(pady=20)
    tk.Button(frame, text="Adicionar Alimento", width=20, command=lambda: mudar_tela(Tela_CadastroRefeicao, root)).pack(pady=10)
    tk.Button(frame, text="Histórico", width=20, command=lambda: mudar_tela(Tela_Historico, root)).pack(pady=10)

# Tela de Cadastro de Refeição
def Tela_CadastroRefeicao(root):
    frame = tk.Frame(root)
    frame.place(relwidth=1, relheight=1)

    tk.Label(frame, text="Selecione a refeição:").pack(pady=5)
    refeicao_var = tk.StringVar(value="Café da Manhã")
    tk.OptionMenu(frame, refeicao_var, "Café da Manhã", "Almoço", "Jantar").pack(pady=5)

    def avancar():
        refeicao = refeicao_var.get()
        mudar_tela(Tela_CadastroAlimento, root, refeicao)

    tk.Button(frame, text="Avançar", width=20, command=avancar).pack(pady=10)
    tk.Button(frame, text="Voltar", width=20, command=lambda: mudar_tela(Tela_Consumo1, root)).pack(pady=10)

# Tela de Cadastro de Alimento
def Tela_CadastroAlimento(root, refeicao):
    frame = tk.Frame(root)
    frame.place(relwidth=1, relheight=1)

    tk.Label(frame, text=f"Refeição selecionada: {refeicao}").pack(pady=5)
    tk.Label(frame, text="Selecione o alimento:").pack(pady=5)

    alimento_obj = Alimento()
    alimentos = alimento_obj.mostraTodosAlimentos()
    lista_alimentos = [alimento['descricao'] for alimento in alimentos]

    if lista_alimentos:
        alimento_var = tk.StringVar(value=lista_alimentos[0])
    else:
        alimento_var = tk.StringVar(value="Nenhum alimento encontrado")

    tk.OptionMenu(frame, alimento_var, *lista_alimentos).pack(pady=5)

    tk.Label(frame, text="Informe a quantidade (gramas):").pack(pady=5)
    entry_quantidade = tk.Entry(frame)
    entry_quantidade.pack(pady=5)

    def salvar():
        with open("consumos.txt", "a") as file:
            file.write(f"Refeição: {refeicao}, Alimento: {alimento_var.get()}, Quantidade: {entry_quantidade.get()}g\n")

    def voltar():
        with open("consumos.txt", "r") as file:
            lines = file.readlines()
        with open("consumos.txt", "w") as file:
            file.writelines(lines[:-1])
        mudar_tela(Tela_CadastroRefeicao, root)

    def avancar():
        salvar()
        messagebox.showinfo("Informação", "Informações salvas com sucesso!")
        mudar_tela(Tela_Consumo1, root)

    tk.Button(frame, text="Salvar", width=20, command=salvar).pack(pady=10)
    tk.Button(frame, text="Avançar", width=20, command=avancar).pack(pady=10)
    tk.Button(frame, text="Voltar", width=20, command=voltar).pack(pady=10)

def Tela_Historico(root):
    frame = tk.Frame(root)
    frame.place(relwidth=1, relheight=1)

    tk.Label(frame, text="Histórico de Consumos", font=("Helvetica", 16)).pack(pady=20)
    tk.Button(frame, text="Voltar", width=20, command=lambda: mudar_tela(Tela_Consumo1, root)).pack(pady=20)

root = tk.Tk()
root.title("Contagem de Carboidratos")
root.geometry("800x600")
mudar_tela(Tela_Inicial, root)
root.mainloop()
