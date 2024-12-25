import tkinter as tk
from tkinter import messagebox

# Função para mudar de tela
def mudar_tela(nova_tela):
    for widget in root.winfo_children():
        widget.destroy()
    nova_tela()

# Tela Inicial
def Tela_Inicial():
    # Cria a janela da tela inicial
    frame = tk.Frame(root)
    frame.pack(padx=20, pady=20)

    btn_entrar = tk.Button(frame, text="Entrar", width=20, command=lambda: mudar_tela(Tela_Login))
    btn_entrar.pack(pady=10)

    btn_cadastrar = tk.Button(frame, text="Cadastrar", width=20, command=lambda: mudar_tela(Tela_Cadastro))
    btn_cadastrar.pack(pady=10)

# Tela de Login
def Tela_Login():
    # Cria a janela da tela de login
    frame = tk.Frame(root)
    frame.pack(padx=20, pady=20)

    tk.Label(frame, text="Usuário:").pack(pady=5)
    entry_usuario = tk.Entry(frame)
    entry_usuario.pack(pady=5)

    tk.Label(frame, text="Senha:").pack(pady=5)
    entry_senha = tk.Entry(frame, show="*")
    entry_senha.pack(pady=5)

    btn_avancar = tk.Button(frame, text="Avançar", width=20, command=lambda: mudar_tela(Tela_Consumo1))
    btn_avancar.pack(pady=10)

    btn_voltar = tk.Button(frame, text="Voltar", width=20, command=lambda: mudar_tela(Tela_Inicial))
    btn_voltar.pack(pady=10)

# Tela de Cadastro
def Tela_Cadastro():
    # Cria a janela de cadastro
    frame = tk.Frame(root)
    frame.pack(padx=20, pady=20)

    tk.Label(frame, text="Nome Completo:").pack(pady=5)
    entry_nome = tk.Entry(frame)
    entry_nome.pack(pady=5)

    tk.Label(frame, text="Email:").pack(pady=5)
    entry_email = tk.Entry(frame)
    entry_email.pack(pady=5)

    tk.Label(frame, text="Telefone:").pack(pady=5)
    entry_telefone = tk.Entry(frame)
    entry_telefone.pack(pady=5)

    btn_avancar = tk.Button(frame, text="Avançar", width=20, command=lambda: mudar_tela(Tela_Cadastro_PerfilMedico))
    btn_avancar.pack(pady=10)

    btn_voltar = tk.Button(frame, text="Voltar", width=20, command=lambda: mudar_tela(Tela_Inicial))
    btn_voltar.pack(pady=10)

# Tela Cadastro Perfil Médico
def Tela_Cadastro_PerfilMedico():
    # Cria a janela de cadastro de perfil médico
    frame = tk.Frame(root)
    frame.pack(padx=20, pady=20)

    tk.Label(frame, text="CRM:").pack(pady=5)
    entry_crm = tk.Entry(frame)
    entry_crm.pack(pady=5)

    tk.Label(frame, text="Especialidade:").pack(pady=5)
    entry_especialidade = tk.Entry(frame)
    entry_especialidade.pack(pady=5)

    tk.Label(frame, text="Endereço Consultório:").pack(pady=5)
    entry_endereco = tk.Entry(frame)
    entry_endereco.pack(pady=5)

    tk.Label(frame, text="Cidade:").pack(pady=5)
    entry_cidade = tk.Entry(frame)
    entry_cidade.pack(pady=5)

    tk.Label(frame, text="Telefone Consultório:").pack(pady=5)
    entry_telefone_consultorio = tk.Entry(frame)
    entry_telefone_consultorio.pack(pady=5)

    tk.Label(frame, text="E-mail Consultório:").pack(pady=5)
    entry_email_consultorio = tk.Entry(frame)
    entry_email_consultorio.pack(pady=5)

    btn_avancar = tk.Button(frame, text="Avançar", width=20, command=lambda: mudar_tela(Tela_Cadastro_Insulina))
    btn_avancar.pack(pady=10)

    btn_voltar = tk.Button(frame, text="Voltar", width=20, command=lambda: mudar_tela(Tela_Cadastro))
    btn_voltar.pack(pady=10)

# Tela Cadastro Insulina
def Tela_Cadastro_Insulina():
    # Cria a janela de cadastro de insulina
    frame = tk.Frame(root)
    frame.pack(padx=20, pady=20)

    tk.Label(frame, text="Tipo de Insulina:").pack(pady=5)
    entry_tipo_insulina = tk.Entry(frame)
    entry_tipo_insulina.pack(pady=5)

    tk.Label(frame, text="Dose Recomendada:").pack(pady=5)
    entry_dose = tk.Entry(frame)
    entry_dose.pack(pady=5)

    btn_avancar = tk.Button(frame, text="Avançar", width=20, command=lambda: mudar_tela(Tela_Cadastro_Sucesso))
    btn_avancar.pack(pady=10)

    btn_voltar = tk.Button(frame, text="Voltar", width=20, command=lambda: mudar_tela(Tela_Cadastro_PerfilMedico))
    btn_voltar.pack(pady=10)

# Tela Cadastro Sucesso
def Tela_Cadastro_Sucesso():
    # Cria a janela de sucesso
    frame = tk.Frame(root)
    frame.pack(padx=20, pady=20)

    tk.Label(frame, text="Cadastro realizado com sucesso!").pack(pady=10)

    btn_voltar = tk.Button(frame, text="Voltar", width=20, command=lambda: mudar_tela(Tela_Inicial))
    btn_voltar.pack(pady=10)

# Tela Consumo 1
def Tela_Consumo1():
    # Cria a janela de consumo 1
    frame = tk.Frame(root)
    frame.pack(padx=20, pady=20)

    btn_avancar = tk.Button(frame, text="Avançar", width=20, command=lambda: mudar_tela(Tela_Cadastro_PerfilMedico))
    btn_avancar.pack(pady=10)

    btn_voltar = tk.Button(frame, text="Voltar", width=20, command=lambda: mudar_tela(Tela_Inicial))
    btn_voltar.pack(pady=10)

# Tela Cadastro Alimento (menu rolante)
def Tela_CadastroAlimento():
    # Cria a janela de cadastro de alimento
    frame = tk.Frame(root)
    frame.pack(padx=20, pady=20)

    tk.Label(frame, text="Selecione um Alimento:").pack(pady=5)
    alimentos = ['Arroz', 'Feijão', 'Carne', 'Fruta']
    combo_alimento = tk.StringVar(frame)
    combo_alimento.set(alimentos[0])
    dropdown = tk.OptionMenu(frame, combo_alimento, *alimentos)
    dropdown.pack(pady=5)

    btn_avancar = tk.Button(frame, text="Avançar", width=20, command=lambda: mudar_tela(Tela_CadastroAlimentoQuantidade))
    btn_avancar.pack(pady=10)

    btn_voltar = tk.Button(frame, text="Voltar", width=20, command=lambda: mudar_tela(Tela_Consumo1))
    btn_voltar.pack(pady=10)

# Tela Cadastro Alimento Quantidade
def Tela_CadastroAlimentoQuantidade():
    # Cria a janela de cadastro de quantidade de alimento
    frame = tk.Frame(root)
    frame.pack(padx=20, pady=20)

    tk.Label(frame, text="Quantidade:").pack(pady=5)
    entry_quantidade = tk.Entry(frame)
    entry_quantidade.pack(pady=5)

    btn_avancar = tk.Button(frame, text="Avançar", width=20, command=lambda: mudar_tela(Tela_Consumo1))
    btn_avancar.pack(pady=10)

    btn_voltar = tk.Button(frame, text="Voltar", width=20, command=lambda: mudar_tela(Tela_CadastroAlimento))
    btn_voltar.pack(pady=10)

# Tela Histórico
def Tela_Historico():
    # Cria a janela de histórico
    frame = tk.Frame(root)
    frame.pack(padx=20, pady=20)

    tk.Label(frame, text="Histórico de Consumos:").pack(pady=10)

    # Simulação de histórico (pode ser uma lista, etc.)
    tk.Label(frame, text="Alimento 1: 100g").pack(pady=5)
    tk.Label(frame, text="Alimento 2: 200g").pack(pady=5)

    btn_voltar = tk.Button(frame, text="Voltar", width=20, command=lambda: mudar_tela(Tela_Consumo1))
    btn_voltar.pack(pady=10)

# Configuração inicial
root = tk.Tk()
root.title("Sistema de Cadastro e Consumo")
root.geometry("400x400")

# Inicia a Tela Inicial
mudar_tela(Tela_Inicial)

root.mainloop()
