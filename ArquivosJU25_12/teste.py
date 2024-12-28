import tkinter as tk
from tkinter import messagebox

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

    def autenticar():
        usuario = entry_usuario.get()
        senha = entry_senha.get()
        if usuario == "admin" and senha == "123":
            mudar_tela(Tela_Consumo1, root)
        else:
            messagebox.showerror("Erro", "Usuário ou senha inválidos.")

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

    def cadastrar():
        if entry_senha.get() == entry_conf_senha.get():
            mudar_tela(Tela_Cadastro_PerfilMedico, root)
        else:
            messagebox.showerror("Erro", "As senhas não coincidem.")

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

    tk.Label(frame, text="Selecione a refeição:").pack(pady=5)
    refeicao_var = tk.StringVar(value="Café da Manhã")
    tk.OptionMenu(frame, refeicao_var, "Café da Manhã", "Almoço", "Jantar").pack(pady=5)

    tk.Label(frame, text="Selecione o alimento:").pack(pady=5)
    alimento_var = tk.StringVar(value="Arroz")
    tk.OptionMenu(frame, alimento_var, "Arroz", "Feijão", "Carne").pack(pady=5)

    tk.Label(frame, text="Informe a quantidade (gramas):").pack(pady=5)
    entry_quantidade = tk.Entry(frame)
    entry_quantidade.pack(pady=5)

    tk.Button(frame, text="Adicionar", width=20, command=lambda: mudar_tela(Tela_Consumo1, root)).pack(pady=10)
    tk.Button(frame, text="Voltar", width=20, command=lambda: mudar_tela(Tela_Consumo1, root)).pack(pady=10)

# Tela de Histórico
def Tela_Historico(root):
    frame = tk.Frame(root)
    frame.place(relwidth=1, relheight=1)

    tk.Label(frame, text="Histórico de Consumos", font=("Helvetica", 16)).pack(pady=20)
    tk.Button(frame, text="Voltar", width=20, command=lambda: mudar_tela(Tela_Consumo1, root)).pack(pady=20)

# Inicialização do programa
def main():
    root = tk.Tk()
    root.title("Contagem de Carboidratos")
    root.geometry("400x400")
    Tela_Inicial(root)
    root.mainloop()

if __name__ == "__main__":
    main()
