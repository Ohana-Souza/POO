import tkinter as tk
from tkinter import messagebox
from supabase import create_client, Client
from ArquivosJU25_12.Chaves_banco import SUPABASE_URL, SUPABASE_KEY
from ArquivosJU25_12.Usuario import Usuario

# Conectar ao Supabase
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Função para redimensionar a imagem (agora removida, pois não precisamos dela)
def redimensionar_imagem(event):
    pass

# Função para mudar de tela
def mudar_tela(nova_tela):
    for widget in root.winfo_children():
        widget.destroy()
    nova_tela()

# Tela Inicial
def Tela_Inicial():
    frame = tk.Frame(root)
    frame.place(x=0, y=0, relwidth=1, relheight=1)
    
    tk.Label(frame, text="TELA INICIAL", font=("Helvetica", 16)).pack(pady=40)
    btn_entrar = tk.Button(frame, text="Entrar", width=20, command=lambda: mudar_tela(Tela_Login))
    btn_entrar.pack(pady=40)
    btn_cadastrar = tk.Button(frame, text="Cadastrar", width=20, command=lambda: mudar_tela(Tela_Cadastro))
    btn_cadastrar.pack(pady=40)


def Tela_Login():
    frame = tk.Frame(root)
    frame.place(x=0, y=0, relwidth=1, relheight=1)

    tk.Label(frame, text="Usuário:").pack(pady=5)
    entry_usuario = tk.Entry(frame)
    entry_usuario.pack(pady=5)

    tk.Label(frame, text="Senha:").pack(pady=5)
    entry_senha = tk.Entry(frame, show="*")
    entry_senha.pack(pady=5)

    def autenticar():
        usuario = Usuario(entry_usuario.get())
        usuario.autenticacao_usuario(entry_senha.get())
        mudar_tela(Tela_Consumo1)

    btn_avancar = tk.Button(frame, text="Avançar", width=20, command=autenticar)
    btn_avancar.pack(pady=10)
    btn_voltar = tk.Button(frame, text="Voltar", width=20, command=lambda: mudar_tela(Tela_Inicial))
    btn_voltar.pack(pady=10)

# Tela Cadastro
def Tela_Cadastro():
    frame = tk.Frame(root)
    frame.place(x=0, y=0, relwidth=1, relheight=1)

    tk.Label(frame, text="Email:").pack(pady=5)
    entry_email = tk.Entry(frame)
    entry_email.pack(pady=5)

    tk.Label(frame, text="Senha:").pack(pady=5)
    entry_senha = tk.Entry(frame)
    entry_senha.pack(pady=5)

    tk.Label(frame, text="Conf.senha:").pack(pady=5)
    entry_conf_senha = tk.Entry(frame)
    entry_conf_senha.pack(pady=5)

    def cadastrar():
        if entry_senha.get() == entry_conf_senha.get():
            usuario = Usuario(entry_email.get())
            if usuario.insere_usuario(entry_senha.get()):
                mudar_tela(Tela_Cadastro_PerfilMedico)
        else:
            tk.messagebox.showerror("Erro", "As senhas não coincidem.")

    btn_avancar = tk.Button(frame, text="Avançar", width=20, command=cadastrar)
    btn_avancar.pack(pady=10)
    btn_voltar = tk.Button(frame, text="Voltar", width=20, command=lambda: mudar_tela(Tela_Inicial))
    btn_voltar.pack(pady=10)


# Tela Cadastro Perfil Médico
def Tela_Cadastro_PerfilMedico():
    frame = tk.Frame(root)
    frame.place(x=0, y=0, relwidth=1, relheight=1)
    tk.Label(frame, text="Toma Insulina:").pack(pady=5)
    toma_insulina = ["SIM", "NÃO"]
    toma_insulina_var = tk.StringVar(frame)
    toma_insulina_var.set(toma_insulina[0])
    toma_insulina_menu = tk.OptionMenu(frame, toma_insulina_var, *toma_insulina)
    toma_insulina_menu.pack(pady=5)
    tk.Label(frame, text="Tipo de Insulina:").pack(pady=5)
    tipos_insulina = ["T1", "T2", "T3", "T4"]
    tipo_insulina_var = tk.StringVar(frame)
    tipo_insulina_var.set(tipos_insulina[0])
    tipo_insulina_menu = tk.OptionMenu(frame, tipo_insulina_var, *tipos_insulina)
    tipo_insulina_menu.pack(pady=5)
    tk.Label(frame, text="Quantidade MAX (UI):").pack(pady=5)
    entry_especialidade = tk.Entry(frame)
    entry_especialidade.pack(pady=5)
    btn_avancar = tk.Button(frame, text="Avançar", width=20, command=lambda: mudar_tela(Tela_Cadastro_Sucesso))
    btn_avancar.pack(pady=10)
    btn_voltar = tk.Button(frame, text="Voltar", width=20, command=lambda: mudar_tela(Tela_Cadastro))
    btn_voltar.pack(pady=10)

# Tela Cadastro Sucesso
def Tela_Cadastro_Sucesso():
    frame = tk.Frame(root)
    frame.place(x=0, y=0, relwidth=1, relheight=1)
    tk.Label(frame, text="Cadastro realizado com sucesso!").pack(pady=10)
    btn_avancar = tk.Button(frame, text="Avançar", width=20, command=lambda: mudar_tela(Tela_Consumo1))
    btn_avancar.pack(pady=10)

# Tela Consumo 1
def Tela_Consumo1():
    frame = tk.Frame(root)
    frame.place(x=0, y=0, relwidth=1, relheight=1)
    btn_avancar = tk.Button(frame, text="Histórico", width=20, command=lambda: mudar_tela(Tela_Historico))
    btn_avancar.pack(pady=10)
    btn_avancar = tk.Button(frame, text="Adicionar", width=20, command=lambda: mudar_tela(Tela_CadastroAlimento))
    btn_avancar.pack(pady=10)

# Tela Cadastro Alimento (menu rolante)
def Tela_CadastroAlimento():
    frame = tk.Frame(root)
    frame.place(x=0, y=0, relwidth=1, relheight=1)
    # Buscar alimentos do banco de dados
    alimento_obj = Alimento()
    alimentos = alimento_obj.mostraTodosAlimentos()
    if not alimentos:
        tk.Label(frame, text="Não foi possível carregar alimentos").pack(pady=5)
        return
    tk.Label(frame, text="Selecione um Alimento:").pack(pady=5)
    combo_alimento = tk.StringVar(frame)
    combo_alimento.set(alimentos[0])  # Definir o primeiro alimento como selecionado por padrão
    dropdown = tk.OptionMenu(frame, combo_alimento, *alimentos)
    dropdown.pack(pady=5)
    btn_avancar = tk.Button(frame, text="Avançar", width=20, command=lambda: mudar_tela(Tela_CadastroAlimentoQuantidade))
    btn_avancar.pack(pady=10)
    btn_voltar = tk.Button(frame, text="Voltar", width=20, command=lambda: mudar_tela(Tela_Consumo1))
    btn_voltar.pack(pady=10)

# Tela Cadastro Alimento Quantidade
def Tela_CadastroAlimentoQuantidade():
    frame = tk.Frame(root)
    frame.place(x=0, y=0, relwidth=1, relheight=1)
    tk.Label(frame, text="Quantidade:").pack(pady=5)
    entry_quantidade = tk.Entry(frame)
    entry_quantidade.pack(pady=5)
    btn_avancar = tk.Button(frame, text="Avançar", width=20, command=lambda: mudar_tela(Tela_Consumo1))
    btn_avancar.pack(pady=10)
    btn_voltar = tk.Button(frame, text="Voltar", width=20, command=lambda: mudar_tela(Tela_CadastroAlimento))
    btn_voltar.pack(pady=10)

# Tela Histórico
def Tela_Historico():
    frame = tk.Frame(root)
    frame.place(x=0, y=0, relwidth=1, relheight=1)
    tk.Label(frame, text="Histórico de Consumos:").pack(pady=10)
    # Simulação de histórico (pode ser uma lista, etc.)
    tk.Label(frame, text="Alimento")
    btn_voltar = tk.Button(frame, text="Voltar", width=20, command=lambda: mudar_tela(Tela_Consumo1))
    btn_voltar.pack(pady=10)

# Configuração inicial
root = tk.Tk()
root.title("Sistema de Cadastro e Consumo")
root.geometry("800x600")  # Tamanho ajustado para a janela

# Ligar o evento de redimensionamento
root.bind("<Configure>", redimensionar_imagem)

# Iniciar a Tela Inicial
mudar_tela(Tela_Inicial)

root.mainloop()
