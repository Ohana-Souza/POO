import tkinter as tk
from tkinter import messagebox
from helpers import mudar_tela
from Refeicao import Refeicao
from Alimento import Alimento  # Certifique-se de que esta classe está implementada corretamente

# Tela Inicial
def Tela_Inicial(root):
    frame = tk.Frame(root)
    frame.place(relwidth=1, relheight=1)

    tk.Label(frame, text="TELA INICIAL", font=("Helvetica", 16)).pack(pady=40)
    tk.Button(frame, text="Entrar", width=20, command=lambda: mudar_tela(Tela_Login, root)).pack(pady=20)
    tk.Button(frame, text="Cadastrar", width=20, command=lambda: mudar_tela(Tela_Cadastro, root)).pack(pady=20)

# Tela de Login
def Tela_Login(root):
    frame = tk.Frame(root)
    frame.place(relwidth=1, relheight=1)

    tk.Label(frame, text="Usuário:").pack(pady=5)
    entry_usuario = tk.Entry(frame)
    entry_usuario.pack(pady=5)

    tk.Label(frame, text="Senha:").pack(pady=5)
    entry_senha = tk.Entry(frame, show="*")
    entry_senha.pack(pady=5)

    alerta_label = tk.Label(frame, text="", fg="red", font=("Helvetica", 10))
    alerta_label.pack(pady=5)

    def autenticar():
        usuario = entry_usuario.get()
        senha = entry_senha.get()
        if not usuario:
            alerta_label.config(text="Por favor, insira o nome de usuário.")
        elif not senha:
            alerta_label.config(text="Por favor, insira a senha.")
        elif usuario == "admin" and senha == "123":
            mudar_tela(Tela_Consumo1, root)
        else:
            alerta_label.config(text="Usuário ou senha inválidos.")

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

    alerta_label = tk.Label(frame, text="", fg="red", font=("Helvetica", 10))
    alerta_label.pack(pady=5)

    def cadastrar():
        email = entry_email.get()
        senha = entry_senha.get()
        conf_senha = entry_conf_senha.get()

        if not email:
            alerta_label.config(text="Por favor, insira um email.")
        elif not senha or not conf_senha:
            alerta_label.config(text="Por favor, preencha todos os campos de senha.")
        elif senha != conf_senha:
            alerta_label.config(text="As senhas não coincidem.")
        else:
            alerta_label.config(text="", fg="green")
            mudar_tela(Tela_Cadastro_PerfilMedico, root)

    tk.Button(frame, text="Avançar", width=20, command=cadastrar).pack(pady=10)
    tk.Button(frame, text="Voltar", width=20, command=lambda: mudar_tela(Tela_Inicial, root)).pack(pady=10)

# Tela de Cadastro do Perfil Médico
def Tela_Cadastro_PerfilMedico(root):
    frame = tk.Frame(root)
    frame.place(relwidth=1, relheight=1)

    tk.Label(frame, text="Toma Insulina:").pack(pady=5)
    insulina_var = tk.StringVar(value="Sim")
    tk.OptionMenu(frame, insulina_var, "Sim", "Não").pack(pady=5)

    tk.Label(frame, text="Tipo de Insulina:").pack(pady=5)
    insulina_tipo_var = tk.StringVar(value="Rápida")
    tk.OptionMenu(frame, insulina_tipo_var, "Rápida", "Lenta").pack(pady=5)

    tk.Label(frame, text="Quantidade Máxima (UI):").pack(pady=5)
    entry_quantidade = tk.Entry(frame)
    entry_quantidade.pack(pady=5)

    tk.Button(frame, text="Avançar", width=20, command=lambda: mudar_tela(Tela_Cadastro_Sucesso, root)).pack(pady=10)
    tk.Button(frame, text="Voltar", width=20, command=lambda: mudar_tela(Tela_Cadastro, root)).pack(pady=10)

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
    tk.Button(frame, text="Adicionar Alimento", width=20, command=lambda: mudar_tela(Tela_CadastroAlimento, root)).pack(pady=10)
    tk.Button(frame, text="Histórico", width=20, command=lambda: mudar_tela(Tela_Historico, root)).pack(pady=10)

# Tela de Cadastro de Alimento
def Tela_CadastroAlimento(root):
    frame = tk.Frame(root)
    frame.place(relwidth=1, relheight=1)

    refeicao = Refeicao()
    alimento_obj = Alimento()

    tk.Label(frame, text="Selecione a refeição:", font=("Helvetica", 12)).pack(pady=5)
    refeicao_var = tk.StringVar(frame)
    refeicao_var.set("Café da Manhã")
    refeicoes_opcoes = ["Café da Manhã", "Almoço", "Jantar", "Lanche"]
    dropdown_refeicao = tk.OptionMenu(frame, refeicao_var, *refeicoes_opcoes)
    dropdown_refeicao.pack(pady=5)

    tk.Label(frame, text="Selecione o alimento:", font=("Helvetica", 12)).pack(pady=5)
    alimento_var = tk.StringVar(frame)
    alimentos_lista = [alimento['descricao'] for alimento in alimento_obj.mostraTodosAlimentos()]
    
    if alimentos_lista:
        alimento_var.set(alimentos_lista[0])
        dropdown_alimento = tk.OptionMenu(frame, alimento_var, *alimentos_lista)
        dropdown_alimento.pack(pady=5)
    else:
        tk.Label(frame, text="Nenhum alimento encontrado.", fg="red").pack(pady=5)

    tk.Label(frame, text="Informe a quantidade (gramas):", font=("Helvetica", 12)).pack(pady=5)
    entry_quantidade = tk.Entry(frame)
    entry_quantidade.pack(pady=5)

    def adicionar_alimento():
        alimento_selecionado = alimento_var.get()
        quantidade = entry_quantidade.get()
        if not quantidade.isdigit() or int(quantidade) <= 0:
            messagebox.showerror("Erro", "Digite uma quantidade válida (em gramas).")
            return

        alimento_obj.adicionaAlimento(alimento_selecionado)
        refeicao.montaRefeicao(alimento_obj)
        messagebox.showinfo("Sucesso", f"{alimento_selecionado} adicionado à refeição.")

    if alimentos_lista:
        tk.Button(frame, text="Adicionar", width=20, command=adicionar_alimento).pack(pady=10)
    tk.Button(frame, text="Voltar", width=20, command=lambda: mudar_tela(Tela_Consumo1, root)).pack(pady=10)

# Tela de Histórico
def Tela_Historico(root):
    frame = tk.Frame(root)
    frame.place(relwidth=1, relheight=1)

    tk.Label(frame, text="Histórico de Consumos", font=("Helvetica", 16)).pack(pady=20)
    tk.Button(frame, text="Voltar", width=20, command=lambda: mudar_tela(Tela_Consumo1, root)).pack(pady=20)
