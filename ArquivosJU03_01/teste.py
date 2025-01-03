import csv
import sys
import tkinter as tk
from tkinter import messagebox
from supabase import create_client, Client
from Chaves_banco import SUPABASE_URL, SUPABASE_KEY
from Alimento import Alimento
from Usuario import Usuario
import re
from PIL import Image, ImageTk

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def configurar_fundo(frame):
    imagem = Image.open(r"C:\Users\ohana\OneDrive\Área de Trabalho\UFMG\4° PERIODO\POO\VERSAO COM INTERFACE PROJETO\POO\POO\ArquivosJU03_01\tpos.jpeg")
    imagem = imagem.resize((360, 640), Image.Resampling.LANCZOS)
    bg = ImageTk.PhotoImage(imagem)

    # Canvas para exibir a imagem
    canvas = tk.Canvas(frame, width=360, height=640)
    canvas.create_image(0, 0, anchor=tk.NW, image=bg)
    canvas.image = bg
    canvas.place(relwidth=1, relheight=1)

# Função para mudar de tela
def mudar_tela(nova_tela, root, *args):
    for widget in root.winfo_children():
        widget.destroy()
    nova_tela(root, *args)

#Tela Inicial
def Tela_Inicial(root):
    frame = tk.Frame(root)
    frame.place(relwidth=1, relheight=1)

    imagem = Image.open(r"C:\Users\ohana\OneDrive\Área de Trabalho\UFMG\4° PERIODO\POO\VERSAO COM INTERFACE PROJETO\POO\POO\ArquivosJU03_01\tinicial.jpeg")
    imagem = imagem.resize((360, 640), Image.Resampling.LANCZOS)
    bg = ImageTk.PhotoImage(imagem)

    # Canvas para exibir a imagem
    canvas = tk.Canvas(frame, width=360, height=640)
    canvas.create_image(0, 0, anchor=tk.NW, image=bg)
    canvas.image = bg
    canvas.place(relwidth=1, relheight=1)

    # Widgets sobre a imagem
    tk.Label(frame, text="TELA INICIAL", font=("Helvetica", 16), bg="#ffffff", fg="#333333").pack(pady=40)
    tk.Button(frame, text="Entrar", width=20, command=lambda: mudar_tela(Tela_Login, root)).pack(pady=20)
    tk.Button(frame, text="Cadastrar", width=20, command=lambda: mudar_tela(Tela_Cadastro, root)).pack(pady=20)

#Tela de Login
def Tela_Login(root):
    frame = tk.Frame(root)
    frame.place(relwidth=1, relheight=1)

    # Aplica o fundo
    configurar_fundo(frame)

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
        usuario = Usuario(email)

        if not usuario.autenticacao_usuario(senha):
            error_label.config(text="Usuário ou senha inválidos.", fg="red")
        else:
            error_label.config(text="Login realizado com sucesso!", fg="green")
            root.after(2000, lambda: mudar_tela(Tela_Consumo1, root))

    tk.Button(frame, text="Login", width=20, command=autenticar).pack(pady=10)
    tk.Button(frame, text="Voltar", width=20, command=lambda: mudar_tela(Tela_Inicial, root)).pack(pady=10)

# Tela de Cadastro
def Tela_Cadastro(root):
    frame = tk.Frame(root)
    frame.place(relwidth=1, relheight=1)

    # Aplica o fundo
    configurar_fundo(frame)

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

        # Validando o e-mail
        usuario.email = email
        if not re.match(r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$', usuario.email):
            error_label.config(text="Formato de e-mail inválido.", fg="red")
            return

        response = usuario.insere_usuario(senha)

        # Atualiza o label de erro com a resposta de insere_usuario
        if response == True:
            error_label.config(text="Usuário cadastrado com sucesso!", fg="green")
            root.after(2000, lambda: mudar_tela(Tela_Consumo1, root))
        else:
            error_label.config(text=response, fg="red")

    tk.Button(frame, text="Avançar", width=20, command=cadastrar).pack(pady=10)
    tk.Button(frame, text="Voltar", width=20, command=lambda: mudar_tela(Tela_Inicial, root)).pack(pady=10)


# Tela de Consumo
# Tela de Consumo
def Tela_Consumo1(root):
    frame = tk.Frame(root)
    frame.place(relwidth=1, relheight=1)

    # Aplica o fundo
    configurar_fundo(frame)

    tk.Label(frame, text="Tela de Consumo", font=("Helvetica", 16)).pack(pady=20)
    tk.Button(frame, text="Adicionar Alimento", width=20, command=lambda: mudar_tela(Tela_CadastroRefeicao, root)).pack(pady=10)
    tk.Button(frame, text="Histórico", width=20, command=lambda: mudar_tela(Tela_Historico, root)).pack(pady=10)
    # Botão de Sair
    tk.Button(frame, text="Sair", width=20, command=sys.exit).pack(pady=10)

# Tela de Cadastro de Refeição
def Tela_CadastroRefeicao(root):
    frame = tk.Frame(root)
    frame.place(relwidth=1, relheight=1)

    # Aplica o fundo
    configurar_fundo(frame)

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

    # Aplica o fundo
    configurar_fundo(frame)

    tk.Label(frame, text=f"Refeição selecionada: {refeicao}").pack(pady=5)
    tk.Label(frame, text="Selecione o alimento:").pack(pady=5)

    # Lê o arquivo CSV e extrai os alimentos
    def ler_csv(caminho_csv):
        alimentos = []
        try:
            with open(caminho_csv, newline='', encoding='utf-8') as csvfile:
                leitor = csv.DictReader(csvfile, delimiter=';')  # Define ';' como delimitador
                for linha in leitor:
                    alimentos.append(linha['descricao'])
        except FileNotFoundError:
            alimentos.append("Arquivo não encontrado")
        except KeyError:
            alimentos.append("Erro no formato do CSV")
        return alimentos

    # Lendo o CSV
    lista_alimentos = ler_csv(r"C:\Users\ohana\OneDrive\Área de Trabalho\UFMG\4° PERIODO\POO\VERSAO COM INTERFACE PROJETO\POO\POO\ArquivosJU03_01\TACO.csv")

    # Populando o OptionMenu
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

# Tela de Histórico
def Tela_Historico(root):
    frame = tk.Frame(root)
    frame.place(relwidth=1, relheight=1)

    # Aplica o fundo
    configurar_fundo(frame)

    tk.Label(frame, text="Histórico de Consumos", font=("Helvetica", 16)).pack(pady=20)

    historico = ler_historico("consumos.txt")

    # Exibe os últimos 3 itens do histórico
    for item in historico[-3:]:
        tk.Label(frame, text=item).pack(pady=5)

    tk.Button(frame, text="Voltar", width=20, command=lambda: mudar_tela(Tela_Consumo1, root)).pack(pady=20)

def ler_historico(caminho_arquivo):
    historico = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()
            # Remove espaços em branco e quebras de linha
            historico = [linha.strip() for linha in linhas if linha.strip()]
    except FileNotFoundError:
        historico.append("Nenhum histórico encontrado")
    return historico

root = tk.Tk()
root.title("Contagem de Carboidratos")
root.geometry("360x640")
mudar_tela(Tela_Inicial, root)
root.mainloop()
