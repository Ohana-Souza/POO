import tkinter as tk
from tkinter import ttk
from Alimento import Alimento
from Refeicao import Refeicao

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Refeições")
        self.refeicao = Refeicao()
        self.tela_inicial()

    def centralizar_tela(self, janela):
        janela.update_idletasks()
        largura = janela.winfo_width()
        altura = janela.winfo_height()
        x = (janela.winfo_screenwidth() // 2) - (largura // 2)
        y = (janela.winfo_screenheight() // 2) - (altura // 2)
        janela.geometry(f"{largura}x{altura}+{x}+{y}")

    def limpar_tela(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def tela_inicial(self):
        self.limpar_tela()

        frame = tk.Frame(self.root)
        frame.pack(expand=True)

        tk.Label(frame, text="Bem-vindo ao Sistema de Refeições", font=("Arial", 16)).pack(pady=10)

        tk.Button(frame, text="Entrar", font=("Arial", 14), command=self.tela_login).pack(pady=10)
        tk.Button(frame, text="Cadastrar", font=("Arial", 14), command=self.tela_cadastro).pack(pady=10)

        self.centralizar_tela(self.root)

    def tela_login(self):
        self.limpar_tela()

        frame = tk.Frame(self.root)
        frame.pack(expand=True)

        tk.Label(frame, text="Login", font=("Arial", 16)).pack(pady=10)
        tk.Entry(frame, font=("Arial", 14), width=30).pack(pady=5)
        tk.Entry(frame, font=("Arial", 14), show="*", width=30).pack(pady=5)

        tk.Button(frame, text="Avançar", font=("Arial", 14), command=self.tela_consumo1).pack(pady=10)
        tk.Button(frame, text="Voltar", font=("Arial", 14), command=self.tela_inicial).pack(pady=10)

        self.centralizar_tela(self.root)

    def tela_cadastro(self):
        self.limpar_tela()

        frame = tk.Frame(self.root)
        frame.pack(expand=True)

        tk.Label(frame, text="Cadastro", font=("Arial", 16)).pack(pady=10)
        for _ in range(3):
            tk.Entry(frame, font=("Arial", 14), width=30).pack(pady=5)

        tk.Button(frame, text="Avançar", font=("Arial", 14), command=self.tela_cadastro_perfil_medico).pack(pady=10)
        tk.Button(frame, text="Voltar", font=("Arial", 14), command=self.tela_inicial).pack(pady=10)

        self.centralizar_tela(self.root)

    def tela_cadastro_perfil_medico(self):
        self.limpar_tela()

        frame = tk.Frame(self.root)
        frame.pack(expand=True)

        tk.Label(frame, text="Cadastro - Perfil Médico", font=("Arial", 16)).pack(pady=10)
        for _ in range(6):
            tk.Entry(frame, font=("Arial", 14), width=30).pack(pady=5)

        tk.Button(frame, text="Avançar", font=("Arial", 14), command=self.tela_cadastro_insulina).pack(pady=10)
        tk.Button(frame, text="Voltar", font=("Arial", 14), command=self.tela_cadastro).pack(pady=10)

        self.centralizar_tela(self.root)

    def tela_cadastro_insulina(self):
        self.limpar_tela()

        frame = tk.Frame(self.root)
        frame.pack(expand=True)

        tk.Label(frame, text="Cadastro - Insulina", font=("Arial", 16)).pack(pady=10)
        for _ in range(2):
            tk.Entry(frame, font=("Arial", 14), width=30).pack(pady=5)

        tk.Button(frame, text="Avançar", font=("Arial", 14), command=self.tela_cadastro_sucesso).pack(pady=10)
        tk.Button(frame, text="Voltar", font=("Arial", 14), command=self.tela_cadastro_perfil_medico).pack(pady=10)

        self.centralizar_tela(self.root)

    def tela_cadastro_sucesso(self):
        self.limpar_tela()

        frame = tk.Frame(self.root)
        frame.pack(expand=True)

        tk.Label(frame, text="Cadastro realizado com sucesso!", font=("Arial", 16)).pack(pady=10)
        tk.Button(frame, text="Voltar para o início", font=("Arial", 14), command=self.tela_inicial).pack(pady=10)

        self.centralizar_tela(self.root)

    def tela_consumo1(self):
        self.limpar_tela()

        frame = tk.Frame(self.root)
        frame.pack(expand=True)

        tk.Label(frame, text="Consumo - Refeição", font=("Arial", 16)).pack(pady=10)
        tk.Button(frame, text="Selecionar Alimento", font=("Arial", 14), command=self.tela_cadastro_alimento).pack(pady=10)
        tk.Button(frame, text="Voltar", font=("Arial", 14), command=self.tela_inicial).pack(pady=10)

        self.centralizar_tela(self.root)

    def tela_cadastro_alimento(self):
        self.limpar_tela()

        frame = tk.Frame(self.root)
        frame.pack(expand=True)

        tk.Label(frame, text="Cadastro de Alimento", font=("Arial", 16)).pack(pady=10)

        alimentos = []
        alimentos_data = Alimento().mostraTodosAlimentos()
        if alimentos_data:
            for item in alimentos_data:
                alimentos.append(item.get("descricao"))

        selecionado = tk.StringVar()

        tk.Label(frame, text="Selecione um alimento:", font=("Arial", 14)).pack(pady=5)
        menu = ttk.Combobox(frame, textvariable=selecionado, values=alimentos, state="readonly", font=("Arial", 14))
        menu.pack(pady=10)

        def confirmar_alimento():
            descricao = selecionado.get()
            if descricao:
                alimento = Alimento()
                for item in alimentos_data:
                    if item.get("descricao") == descricao:
                        alimento.descricao = item.get("descricao")
                        alimento.nutrientes = [
                            item.get("energia(kcal)", 0),
                            item.get("proteina(g)", 0),
                            item.get("lipideos(g)", 0),
                            item.get("carboidrato(g)", 0),
                            item.get("fibra(g)", 0),
                        ]
                        self.refeicao.montaRefeicao(alimento)
                        break
                self.tela_cadastro_alimento_quantidade()
            else:
                tk.messagebox.showerror("Erro", "Selecione um alimento antes de confirmar.")

        tk.Button(frame, text="Confirmar", font=("Arial", 14), command=confirmar_alimento).pack(pady=10)
        tk.Button(frame, text="Voltar", font=("Arial", 14), command=self.tela_consumo1).pack(pady=10)

        self.centralizar_tela(self.root)

    def tela_cadastro_alimento_quantidade(self):
        self.limpar_tela()

        frame = tk.Frame(self.root)
        frame.pack(expand=True)

        tk.Label(frame, text="Informe a quantidade em gramas", font=("Arial", 16)).pack(pady=10)
        entry = tk.Entry(frame, font=("Arial", 14), width=30)
        entry.pack(pady=5)

        def confirmar_quantidade():
            try:
                gramas = int(entry.get())
                if gramas <= 0:
                    raise ValueError
                tk.messagebox.showinfo("Sucesso", f"Alimento adicionado com {gramas} gramas!")
                self.tela_consumo1()
            except ValueError:
                tk.messagebox.showerror("Erro", "Informe uma quantidade válida em gramas.")

        tk.Button(frame, text="Confirmar", font=("Arial", 14), command=confirmar_quantidade).pack(pady=10)
        tk.Button(frame, text="Voltar", font=("Arial", 14), command=self.tela_cadastro_alimento).pack(pady=10)

        self.centralizar_tela(self.root)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
