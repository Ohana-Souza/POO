import csv
import sys
import tkinter as tk
import datetime
import re

from tkinter import messagebox, StringVar, OptionMenu, Frame, Button
from supabase import create_client, Client
from Chaves_banco import SUPABASE_URL, SUPABASE_KEY
from Alimento import Alimento
from Usuario import Usuario
from Historico_refeicao import HistoricoRefeicao
from Historico_alimentos import HistoricoAlimentos
from Perfil_Medico import PerfilMedico

from tkcalendar import DateEntry
from Nutrientes import Nutrientes
from Insulina import Asparge, Humalog, NPH, Glargina
from PIL import Image, ImageTk
from Verificadora import Verificadora
from Calculadora_Insulina import Calculadora_Insulina
import os


supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

caminho_imagem1 = os.path.join(os.path.dirname(__file__), "Telas", "1.png")
caminho_imagem2 = os.path.join(os.path.dirname(__file__), "Telas", "2.png")
caminho_imagem3 = os.path.join(os.path.dirname(__file__), "Telas", "3.png")
caminho_imagem4 = os.path.join(os.path.dirname(__file__), "Telas", "4.png")
caminho_imagem5 = os.path.join(os.path.dirname(__file__), "Telas", "5.png")
caminho_imagem6 = os.path.join(os.path.dirname(__file__), "Telas","6.png")
caminho_TACO = os.path.join(os.path.dirname(__file__), "TACO.csv")

def configurar_tela_inicial(frame):
    imagem = Image.open(caminho_imagem1)
    imagem = imagem.resize((360, 640), Image.Resampling.LANCZOS)
    bg = ImageTk.PhotoImage(imagem)

    canvas = tk.Canvas(frame, width=360, height=640)
    canvas.create_image(0, 0, anchor=tk.NW, image=bg)
    canvas.image = bg
    canvas.place(relwidth=1, relheight=1)

def configurar_fundo_login(frame):
    imagem = Image.open(caminho_imagem3)
    imagem = imagem.resize((360, 640), Image.Resampling.LANCZOS)
    bg = ImageTk.PhotoImage(imagem)

    canvas = tk.Canvas(frame, width=360, height=640)
    canvas.create_image(0, 0, anchor=tk.NW, image=bg)
    canvas.image = bg
    canvas.place(relwidth=1, relheight=1)
    
def configurar_fundo_cadastro(frame):
    imagem = Image.open(caminho_imagem2)
    imagem = imagem.resize((414, 896), Image.Resampling.LANCZOS)
    bg = ImageTk.PhotoImage(imagem)

    canvas = tk.Canvas(frame, width=360, height=640)
    canvas.create_image(0, 0, anchor=tk.NW, image=bg)
    canvas.image = bg
    canvas.place(relwidth=1, relheight=1)

def configurar_fundo_liso(frame):
    imagem = Image.open(caminho_imagem4)
    imagem = imagem.resize((414, 896), Image.Resampling.LANCZOS)
    bg = ImageTk.PhotoImage(imagem)

    canvas = tk.Canvas(frame, width=414, height=896)
    canvas.create_image(0, 0, anchor=tk.NW, image=bg)
    canvas.image = bg
    canvas.place(relwidth=1, relheight=1)

def mudar_tela(nova_tela, root, *args):
    for widget in root.winfo_children():
        widget.destroy()
    nova_tela(root, *args)

def obter_dimensoes_tela(): 
    largura_tela = 360 
    altura_tela = 640 
    centro_x = largura_tela / 2 
    return largura_tela, altura_tela, centro_x

def Tela_Inicial(root): 
    frame = tk.Frame(root) 
    frame.place(relwidth=1, relheight=1) 
    configurar_tela_inicial(frame) 
    largura_tela, altura_tela, centro_x = obter_dimensoes_tela() 
    botao1 = tk.Button(frame, text="Entrar", width=20, command=lambda: mudar_tela(Tela_Login, root)) 
    botao2 = tk.Button(frame, text="Cadastrar", width=20, command=lambda: mudar_tela(Tela_Cadastro, root)) 
    botao1.place(x=centro_x, y=8.5 * (altura_tela / 12), anchor="center") 
    botao2.place(x=centro_x, y=9.5 * (altura_tela / 12), anchor="center")

def Tela_Login(root):
    frame = tk.Frame(root)
    frame.place(relwidth=1, relheight=1)

    configurar_fundo_login(frame)

    largura_tela, altura_tela, centro_x = obter_dimensoes_tela()

    tk.Label(frame, text="Usuário:").place(x=centro_x, y=250, anchor="center")
    entry_usuario = tk.Entry(frame)
    entry_usuario.place(x=centro_x, y=280, anchor="center")

    tk.Label(frame, text="Senha:").place(x=centro_x, y=320, anchor="center")
    entry_senha = tk.Entry(frame, show="*")
    entry_senha.place(x=centro_x, y=350, anchor="center")

    error_label = tk.Label(frame, text="", fg="red")
    error_label.place(x=centro_x, y=420, anchor="center")

    def autenticar():
        email = entry_usuario.get()
        senha = entry_senha.get()
        usuario = Usuario(email)

        if usuario.autenticacao_usuario(senha):
            error_label.config(text="Login realizado com sucesso!", fg="green")
            root.after(200, lambda: mudar_tela(Tela_Consumo1, root, email))
        else:
            error_label.config(text="Usuário ou senha inválidos.", fg="red")

    tk.Button(frame, text="Login", width=20, command=autenticar).place(x=centro_x, y=490, anchor="center")
    tk.Button(frame, text="Voltar", width=20, command=lambda: mudar_tela(Tela_Inicial, root)).place(x=centro_x, y=540, anchor="center")



def Tela_Cadastro(root):
    frame = tk.Frame(root)
    frame.place(relwidth=1, relheight=1)

    configurar_fundo_cadastro(frame)

    largura_tela, altura_tela, centro_x = obter_dimensoes_tela()

    tk.Label(frame, text="Email:").place(x=centro_x, y=250, anchor="center")
    entry_email = tk.Entry(frame)
    entry_email.place(x=centro_x, y=280, anchor="center")

    tk.Label(frame, text="Senha:").place(x=centro_x, y=350, anchor="center")
    entry_senha = tk.Entry(frame, show="*")
    entry_senha.place(x=centro_x, y=380, anchor="center")

    tk.Label(frame, text="Confirmar Senha:").place(x=centro_x, y=450, anchor="center")
    entry_conf_senha = tk.Entry(frame, show="*")
    entry_conf_senha.place(x=centro_x, y=480, anchor="center")

    error_label = tk.Label(frame, text="", fg="red")
    error_label.place(x=centro_x, y=550, anchor="center")

    def cadastrar():
        email = entry_email.get()
        senha = entry_senha.get()
        conf_senha = entry_conf_senha.get()

        if senha != conf_senha:
            error_label.config(text="As senhas não coincidem.", fg="red")
            return

        if not re.match(r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$', email):
            error_label.config(text="Formato de e-mail inválido.", fg="red")
            return

        usuario = Usuario(email)
        response = usuario.insere_usuario(senha)
        print(response)

        if response is True:
            error_label.config(text="Usuário cadastrado com sucesso!", fg="green")
            root.after(2000, lambda: mudar_tela(Tela_PerfilMedico1, root, email))
        else:
            error_label.config(text="Email já cadastrado!", fg="red")

    tk.Button(frame, text="Avançar", width=20, command=cadastrar).place(x=centro_x, y=620, anchor="center")
    tk.Button(frame, text="Voltar", width=20, command=lambda: mudar_tela(Tela_Inicial, root)).place(x=centro_x, y=670, anchor="center")


def Tela_PerfilMedico1(root, email):
    frame = tk.Frame(root)
    frame.place(relwidth=1, relheight=1)

    configurar_fundo_cadastro(frame)

    largura_tela, altura_tela, centro_x = obter_dimensoes_tela()

    tk.Label(frame, text=f"Email: {email}", font=("Helvetica", 12)).place(x=centro_x, y=100, anchor="center")

    tk.Label(frame, text="Sexo:").place(x=centro_x, y=140, anchor="center")
    sexo_var = tk.StringVar()
    tk.OptionMenu(frame, sexo_var, "Masculino", "Feminino").place(x=centro_x, y=180, anchor="center")

    tk.Label(frame, text="Altura (cm):").place(x=centro_x, y=220, anchor="center")
    entry_altura = tk.Entry(frame)
    entry_altura.place(x=centro_x, y=260, anchor="center")

    tk.Label(frame, text="Peso (kg):").place(x=centro_x, y=300, anchor="center")
    entry_peso = tk.Entry(frame)
    entry_peso.place(x=centro_x, y=340, anchor="center")

    tk.Label(frame, text="Idade:").place(x=centro_x, y=380, anchor="center")
    entry_idade = tk.Entry(frame)
    entry_idade.place(x=centro_x, y=420, anchor="center")

    tk.Label(frame, text="Atividade Física:").place(x=centro_x, y=460, anchor="center")
    atividade_var = tk.StringVar()
    tk.OptionMenu(frame, atividade_var, "Sedentário", "Leve", "Moderado", "Intenso").place(x=centro_x, y=500, anchor="center")

    error_label = tk.Label(frame, text="", fg="red")
    error_label.place(x=centro_x, y=540, anchor="center")

    def avancar():
        sexo = sexo_var.get()
        altura = entry_altura.get()
        peso = entry_peso.get()
        idade = entry_idade.get()
        atividade = atividade_var.get()

        if not sexo:
            error_label.config(text="Sexo não selecionado!")
            return
        if not Verificadora.verificar_inteiro(altura, tipo="float"):
            error_label.config(text="Altura inválida!")
            return
        if not Verificadora.verificar_inteiro(peso, tipo="float"):
            error_label.config(text="Peso inválido!")
            return
        if not Verificadora.verificar_inteiro(idade, tipo="int"):
            error_label.config(text="Idade inválida!")
            return
        if not atividade:
            error_label.config(text="Atividade Física não selecionada!")
            return

        error_label.config(text="")
        mudar_tela(Tela_PerfilMedico2, root, email, sexo, altura, peso, idade, atividade)

    tk.Button(frame, text="Avançar", width=20, command=avancar).place(x=centro_x, y=580, anchor="center")
    tk.Button(frame, text="Voltar", width=20, command=lambda: mudar_tela(Tela_Cadastro, root)).place(x=centro_x, y=620, anchor="center")

def Tela_PerfilMedico2(root, email, sexo, altura, peso, idade, atividade):
    frame = tk.Frame(root)
    frame.place(relwidth=1, relheight=1)

    configurar_fundo_cadastro(frame)

    largura_tela, altura_tela, centro_x = obter_dimensoes_tela()

    tk.Label(frame, text=f"Email: {email}", font=("Helvetica", 12)).place(x=centro_x, y=100, anchor="center")

    tk.Label(frame, text="Tipo de Diabetes:").place(x=centro_x, y=140, anchor="center")
    diabetes_var = tk.StringVar()
    tk.OptionMenu(frame, diabetes_var, "Tipo 1", "Tipo 2", "Gestacional", "Pré-diabetes").place(x=centro_x, y=180, anchor="center")

    tk.Label(frame, text="Toma Insulina (Sim/Não):").place(x=centro_x, y=220, anchor="center")
    insulina_var = tk.StringVar()
    tk.OptionMenu(frame, insulina_var, "Sim", "Não").place(x=centro_x, y=260, anchor="center")

    tk.Label(frame, text="Tipo de Insulina:").place(x=centro_x, y=300, anchor="center")
    tipo_insulina_var = tk.StringVar()
    tk.OptionMenu(frame, tipo_insulina_var, "Asparge", "Humalog", "NPH", "Glargina", "Não toma").place(x=centro_x, y=340, anchor="center")

    tk.Label(frame, text="Dosagem Máxima de Insulina (unidades):").place(x=centro_x, y=380, anchor="center")
    entry_dosagem_max = tk.Entry(frame)
    entry_dosagem_max.place(x=centro_x, y=420, anchor="center")

    error_label = tk.Label(frame, text="", fg="red")
    error_label.place(x=centro_x, y=460, anchor="center")

    def salvar():
        tipo_diabetes = diabetes_var.get()
        toma_insulina = insulina_var.get()
        tipo_insulina = tipo_insulina_var.get()
        dosagem_max = entry_dosagem_max.get()

        if not tipo_diabetes:
            error_label.config(text="Tipo de Diabetes não selecionado!", fg="red")
            return
        if not toma_insulina:
            error_label.config(text="Selecione se toma insulina!", fg="red")
            return
        if not tipo_insulina:
            error_label.config(text="Tipo de Insulina não selecionado!", fg="red")
            return
        if not Verificadora.verificar_inteiro(dosagem_max, tipo="float"):
            error_label.config(text="Dosagem inválida!", fg="red")
            return

        perfil_medico = PerfilMedico(email, sexo, altura, peso, idade, atividade, tipo_diabetes, toma_insulina, tipo_insulina, dosagem_max)

        if perfil_medico.cria_perfil_medico():
            error_label.config(text="Perfil médico cadastrado com sucesso!", fg="green")
            root.after(2000, lambda: mudar_tela(Tela_Alerta, root, email))
        else:
            error_label.config(text="Reveja as informações inseridas!", fg="red")

    tk.Button(frame, text="Salvar", width=20, command=salvar).place(x=centro_x, y=500, anchor="center")
    tk.Button(frame, text="Voltar", width=20, command=lambda: mudar_tela(Tela_PerfilMedico1, root, email)).place(x=centro_x, y=540, anchor="center")

def Tela_Alerta(root, email):
    frame = tk.Frame(root)
    frame.place(relwidth=1, relheight=1)

    imagem = Image.open(caminho_imagem5)
    imagem = imagem.resize((360, 640), Image.Resampling.LANCZOS)
    bg = ImageTk.PhotoImage(imagem)

    canvas = tk.Canvas(frame, width=360, height=640)
    canvas.create_image(0, 0, anchor=tk.NW, image=bg)
    canvas.image = bg
    canvas.place(relwidth=1, relheight=1)
    
    largura_tela, altura_tela, centro_x = obter_dimensoes_tela()

    def avancar():
        mudar_tela(Tela_Consumo1, root, email)
    
    tk.Button(frame, text="Avançar", width=20, command=avancar).place(x=centro_x, y=altura_tela * 0.75, anchor="center")



def Tela_Consumo1(root, email):
    frame = tk.Frame(root)
    frame.place(relwidth=1, relheight=1)

    configurar_fundo_liso(frame)

    tk.Label(frame, text=f"Bem-vindo(a), {email}", font=("Helvetica", 16)).pack(pady=20)
    tk.Button(frame, text="Adicionar Alimento", width=20, command=lambda: mudar_tela(Tela_CadastroRefeicao, root, email)).pack(pady=10)
    tk.Button(frame, text="Histórico Nutrientes", width=20, command=lambda: mudar_tela(Tela_Historico_Nutrientes, root, email)).pack(pady=10)
    tk.Button(frame, text="Dosagem Insulina", width=20, command=lambda: mudar_tela(Tela_Historico_Insulina, root, email)).pack(pady=10)
    tk.Button(frame, text="Sair", width=20, command=sys.exit).pack(pady=10)

def Tela_CadastroRefeicao(root, email):
    frame = tk.Frame(root)
    frame.place(relwidth=1, relheight=1)

    configurar_fundo_liso(frame)

    tk.Label(frame, text="Selecione a refeição:").pack(pady=5)
    refeicao_var = tk.StringVar(value="Café da manhã")
    tk.OptionMenu(frame, refeicao_var, "Café da manhã", "Almoço", "Jantar", "Lanche").pack(pady=5)

    def avancar():
        refeicao = refeicao_var.get()
        mudar_tela(Tela_CadastroAlimento, root, email, refeicao)

    tk.Button(frame, text="Avançar", width=20, command=avancar).pack(pady=10)
    tk.Button(frame, text="Voltar", width=20, command=lambda: mudar_tela(Tela_Consumo1, root, email)).pack(pady=10)

###########################################################################################

def Tela_CadastroAlimento(root, email, refeicao):
    """
    Tela para adicionar alimentos e salvar a refeição com cálculo de insulina usando polimorfismo.
    """
    historico_refeicao = HistoricoRefeicao()
    alimentos_adicionados = []
    nutrientes = Nutrientes()

    frame = tk.Frame(root)
    frame.place(relwidth=1, relheight=1)

    configurar_fundo_liso(frame)

    tk.Label(frame, text=f"Refeição selecionada: {refeicao}", font=("Helvetica", 14)).pack(pady=10)
    tk.Label(frame, text="Selecione o alimento:").pack(pady=5)

    # Lê o arquivo CSV e extrai os alimentos
    def ler_csv(caminho_csv):
        try:
            with open(caminho_csv, newline='', encoding='utf-8') as csvfile:
                leitor = csv.DictReader(csvfile, delimiter=';')
                return [linha['descricao'] for linha in leitor]
        except (FileNotFoundError, KeyError):
            return ["Erro ao carregar alimentos"]

    lista_alimentos = ler_csv(caminho_TACO)

    # Configuração do campo de seleção de alimentos
    alimento_var = tk.StringVar(value="Selecione um alimento")
    option_menu = tk.OptionMenu(frame, alimento_var, *lista_alimentos)
    option_menu.pack(pady=5)

    tk.Label(frame, text="Buscar alimento:").pack(pady=5)
    entry_busca = tk.Entry(frame)
    entry_busca.pack(pady=5)

    def buscar_alimentos(event=None):
        termo_busca = entry_busca.get().lower()
        resultado = [alimento for alimento in lista_alimentos if termo_busca in alimento.lower()]
        menu = option_menu["menu"]
        menu.delete(0, "end")
        for alimento in resultado or ["Alimento não encontrado"]:
            menu.add_command(label=alimento, command=lambda value=alimento: alimento_var.set(value))

    entry_busca.bind("<KeyRelease>", buscar_alimentos)

    tk.Label(frame, text="Informe a quantidade (gramas):").pack(pady=5)
    entry_quantidade = tk.Entry(frame)
    entry_quantidade.pack(pady=5)

    error_label = tk.Label(frame, text="", fg="red")
    error_label.pack(pady=5)

    def adicionar_alimento():
        try:
            descricao_alimento = alimento_var.get()
            quantidade_valida = entry_quantidade.get()

            if not descricao_alimento or descricao_alimento == "Selecione um alimento":
                error_label.config(text="Por favor, selecione um alimento válido.", fg="red")
                return

            if not Verificadora.verificar_inteiro(quantidade_valida, tipo="float"):
                error_label.config(text="Insira um valor válido para a quantidade!", fg="red")
                return

            quantidade = float(quantidade_valida)
            alimento = Alimento()
            alimento.adicionaAlimento(quantidade, descricao_alimento)

            # Adiciona o alimento à lista de alimentos adicionados
            alimentos_adicionados.append(alimento)

            # Adiciona os nutrientes do alimento aos nutrientes totais
            nutrientes.adicionaNutrientes(alimento)

            error_label.config(text="Alimento adicionado com sucesso!", fg="green")
            alimento_var.set("Selecione um alimento")
            entry_quantidade.delete(0, tk.END)

        except Exception as e:
            print(f"Erro inesperado ao adicionar alimento: {e}")
            error_label.config(text="Erro inesperado ao adicionar alimento.", fg="red")

    def salvar_refeicao():
        try:
            if not alimentos_adicionados:
                error_label.config(text="Nenhum alimento foi adicionado à refeição.", fg="red")
                return

            # Calcula os nutrientes totais
            nutrientes_totais = nutrientes.obterLista()

            # Recupera o id_usuario a partir do email
            resposta_usuario = supabase.table('Usuarios').select('id').eq('email', email).execute()

            if not resposta_usuario.data:
                error_label.config(text="Usuário não encontrado.", fg="red")
                return
            
            id_usuario = resposta_usuario.data[0]['id']
            
            # Recupera o perfil médico do usuário
            resposta_perfil_medico = supabase.table('Perfil_medico').select('*').eq('id_usuario', id_usuario).execute()
            
            if not resposta_perfil_medico.data:
                error_label.config(text="Perfil médico não encontrado", fg="red")
                return
            
            # Garante que estamos lidando com um único registro do perfil médico
            perfil_medico = resposta_perfil_medico.data[0] if isinstance(resposta_perfil_medico.data, list) and resposta_perfil_medico.data else None
            
            if not perfil_medico:
                error_label.config(text="Dados do perfil médico inválidos", fg="red")
                return
            
            # Garante que as chaves existem no dicionário perfil_medico
            id_tipo_diabetes = perfil_medico.get('id_tipo_diabetes')
            peso = perfil_medico.get('peso')
            dosagem_max = perfil_medico.get('dosagem_max')
            id_tipo_insulina = perfil_medico.get('id_tipo_insulina')

            resposta_tipo_insulina = supabase.table('Tipos_insulina').select('tipo').eq('id', id_tipo_insulina).execute()
        
            if resposta_tipo_insulina.data and len(resposta_tipo_insulina.data) > 0:
                tipo_insulina = resposta_tipo_insulina.data[0]['tipo']

            resposta_tipo_diabetes = supabase.table('Tipos_diabetes').select('tipo').eq('id', id_tipo_diabetes).execute()
        
            if resposta_tipo_diabetes.data and len(resposta_tipo_diabetes.data) > 0:
                tipo_diabetes = resposta_tipo_diabetes.data[0]['tipo']

            # Verifica se todos os dados necessários estão presentes
            if not all([tipo_diabetes, peso, dosagem_max]):
                error_label.config(text="Dados do perfil médico incompletos", fg="red")
                return

            # Define a insulina como "Humalog" sempre
            if tipo_insulina == "Humalog":
                insulina = Humalog(peso, tipo_diabetes, nutrientes.total_carboidratos, nutrientes.total_proteina, dosagem_max)
            elif tipo_insulina == "Asparge":
                insulina = Asparge(peso, tipo_diabetes, nutrientes.total_carboidratos, nutrientes.total_proteina, dosagem_max)
            elif tipo_insulina == "NPH":
                insulina = NPH(peso, tipo_diabetes, nutrientes.total_carboidratos, nutrientes.total_proteina, dosagem_max)
            elif tipo_insulina == "Glargina":
                insulina = Glargina(peso, tipo_diabetes, nutrientes.total_carboidratos, nutrientes.total_proteina, dosagem_max)

            # Usa polimorfismo para calcular a dosagem de insulina
            calculadora_insulina = Calculadora_Insulina()
            insulina_calculada = calculadora_insulina.fazCalculoDosagem(insulina)

            # Salva a refeição no banco de dados
            sucesso = historico_refeicao.salvaRefeicao(email, refeicao, nutrientes_totais, insulina_calculada)

            if sucesso:
                error_label.config(text="A refeição foi salva com sucesso!", fg="GREEN")
                mudar_tela(Tela_Consumo1, root, email)
            else:
                error_label.config(text="Erro ao salvar a refeição. Verifique os dados.", fg="GREEN")
                print("Dados para depuração:")
                print("Email:", email)
                print("Refeição:", refeicao)
                print("Nutrientes totais:", nutrientes_totais)
                print("Insulina calculada:", insulina_calculada)

        except Exception as e:
            print(f"Erro ao salvar a refeição: {e}")
            error_label.config(text="Erro ao salvar a refeição.", fg="red")

    def voltar():
        mudar_tela(Tela_CadastroRefeicao, root, email)

    # Botões de ação
    tk.Button(frame, text="ADD", width=20, command=adicionar_alimento).pack(pady=10)
    tk.Button(frame, text="Avançar", width=20, command=salvar_refeicao).pack(pady=10)
    tk.Button(frame, text="Voltar", width=20, command=voltar).pack(pady=10)


#########################################################################################

def Tela_Historico_Insulina(root, email_usuario):
    frame = tk.Frame(root)
    frame.place(relwidth=1, relheight=1)
    configurar_fundo_liso(frame)

    tk.Label(frame, text="Histórico de Insulina", font=("Helvetica", 16)).pack(pady=20)
    tk.Label(frame, text="Selecione a data:").pack(pady=5)

    # Entrada de data
    data_entry = DateEntry(frame, width=12, background='darkblue', foreground='white', borderwidth=2)
    data_entry.pack(pady=5)

    tk.Label(frame, text="Selecione a refeição:").pack(pady=5)
    refeicao_var = tk.StringVar(value="Selecione uma refeição")
    refeicoes_disponiveis = ["Café da manhã", "Almoço", "Jantar", "Lanche"]
    tk.OptionMenu(frame, refeicao_var, *refeicoes_disponiveis).pack(pady=5)

    # Canvas com barra de rolagem
    canvas_frame = tk.Frame(frame)
    canvas_frame.pack(pady=10, fill="both", expand=True)

    canvas = tk.Canvas(canvas_frame)
    scrollbar = tk.Scrollbar(canvas_frame, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    
    error_label = tk.Label(frame, text="", fg="red")
    error_label.pack(pady=5)
    
    def limpar_frame():
        for widget in scrollable_frame.winfo_children():
            widget.destroy()

    def exibir_historico():
        limpar_frame()
        data_selecionada = data_entry.get_date().strftime('%Y-%m-%d')
        refeicao_selecionada = refeicao_var.get()

        # Validação das entradas
        if refeicao_selecionada == "Selecione uma refeição":
            error_label.config(text="Por favor, selecione uma refeição.", fg="red")
            return

        # Calcula e exibe o histórico de insulina
        try:
            # Instância das classes necessárias
            historico = HistoricoRefeicao()
            
            # Obtém os dados do banco
            resultado_historico = historico.mostraHistorico(data=data_selecionada, refeicao=refeicao_selecionada, usuario=email_usuario)
            
            if not resultado_historico:
                tk.Label(scrollable_frame, text="Nenhum dado encontrado para a data e refeição selecionadas.", font=("Helvetica", 10)).pack(pady=5)
                return

            tk.Label(scrollable_frame, text=f"Histórico de Insulina e Nutrientes em {data_selecionada}:", font=("Helvetica", 12, "bold")).pack(pady=5)
            
            for linha in resultado_historico.splitlines():
                tk.Label(scrollable_frame, text=linha.strip(), anchor="w", justify="left").pack(fill="x", pady=2)

        except Exception as e:
            print(f"Erro ao exibir histórico: {e}")
            tk.Label(scrollable_frame, text="Erro ao carregar o histórico. Verifique os dados.", fg="red").pack(pady=5)

    def voltar():
        mudar_tela(Tela_Consumo1, root, email_usuario)

    # Botões
    tk.Button(frame, text="Exibir Histórico", width=20, command=exibir_historico).pack(pady=10)
    tk.Button(frame, text="Limpar", width=20, command=limpar_frame).pack(pady=10)
    tk.Button(frame, text="Voltar", width=20, command=voltar).pack(pady=10)
 
 
 
def Tela_Historico_Nutrientes(root, email_usuario):
    frame = tk.Frame(root)
    frame.place(relwidth=1, relheight=1)
    configurar_fundo_liso(frame)

    largura_tela, altura_tela, centro_x = obter_dimensoes_tela()

    tk.Label(frame, text="Histórico de Alimentos", font=("Helvetica", 16)).place(x=centro_x, y=50, anchor="center")
    tk.Label(frame, text="Selecione a data:").place(x=centro_x, y=100, anchor="center")

    # Entrada de data
    data_entry = DateEntry(frame, width=12, background='darkblue', foreground='white', borderwidth=2)
    data_entry.place(x=centro_x, y=130, anchor="center")

    tk.Label(frame, text="Selecione a refeição:").place(x=centro_x, y=160, anchor="center")
    refeicao_var = tk.StringVar(value="Selecione uma refeição")
    refeicoes_disponiveis = ["Café da manhã", "Almoço", "Jantar", "Lanche"]
    tk.OptionMenu(frame, refeicao_var, *refeicoes_disponiveis).place(x=centro_x, y=190, anchor="center")

    tk.Label(frame, text="Selecione a propriedade para exibir:").place(x=centro_x, y=220, anchor="center")
    propriedade_var = tk.StringVar(value="Todas")
    propriedades_disponiveis = ["Todas", "Proteína", "Carboidrato", "Fibra", "Lipídeo", "Energia"]
    tk.OptionMenu(frame, propriedade_var, *propriedades_disponiveis).place(x=centro_x, y=250, anchor="center")

    # Canvas com barra de rolagem
    canvas_frame = tk.Frame(frame)
    canvas_frame.place(x=0, y=300, width=largura_tela, height=altura_tela-400)

    canvas = tk.Canvas(canvas_frame)
    scrollbar = tk.Scrollbar(canvas_frame, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    def limpar_frame():
        for widget in scrollable_frame.winfo_children():
            widget.destroy()

    def exibir_historico():
        limpar_frame()
        data_selecionada = data_entry.get_date().strftime('%Y-%m-%d')
        refeicao_selecionada = refeicao_var.get()
        propriedade_selecionada = propriedade_var.get()

        # Validação das entradas
        if refeicao_selecionada == "Selecione uma refeição":
            messagebox.showerror("Erro", "Por favor, selecione uma refeição.")
            return

        # Obtém o histórico de alimentos do banco
        historico = HistoricoAlimentos().mostraHistorico(
            data=data_selecionada,
            refeicao=refeicao_selecionada,
            usuario=email_usuario
        )

        if not historico:
            tk.Label(scrollable_frame, text="Nenhum dado encontrado para a data selecionada.", font=("Helvetica", 10)).pack(pady=5)
        else:
            tk.Label(scrollable_frame, text=f"Histórico de Alimentos em {data_selecionada}:", font=("Helvetica", 12, "bold")).pack(pady=5)

            for entrada in historico:
                descricao_alimento = entrada['Alimentos']['descricao']
                refeicao = entrada['Refeicao']['refeicao']
                tk.Label(scrollable_frame, text=f"Alimento: {descricao_alimento} - Refeição: {refeicao}", anchor="w", justify="left", font=("Helvetica", 10, "bold")).pack(fill="x", pady=2)
                
                if propriedade_selecionada == "Todas":
                    for chave, valor in entrada.items():
                        if chave not in ["Alimentos", "Refeicao", "dia"]:
                            tk.Label(scrollable_frame, text=f"{chave.capitalize()}: {valor}", anchor="w", justify="left").pack(fill="x", pady=2)
                else:
                    propriedade = propriedade_selecionada.lower()
                    if propriedade in entrada:
                        tk.Label(scrollable_frame, text=f"{propriedade.capitalize()}: {entrada[propriedade]}", anchor="w", justify="left").pack(fill="x", pady=2)

    def voltar():
        mudar_tela(Tela_Consumo1, root, email_usuario)

    tk.Button(frame, text="Exibir Histórico", width=20, command=exibir_historico).place(x=centro_x, y=altura_tela-90, anchor="center")
    tk.Button(frame, text="Limpar", width=20, command=limpar_frame).place(x=centro_x, y=altura_tela-60, anchor="center")
    tk.Button(frame, text="Voltar", width=20, command=voltar).place(x=centro_x, y=altura_tela-30, anchor="center")

###############################################################################

root = tk.Tk()
root.title("Contagem de Carboidratos")
root.geometry("360x640")
mudar_tela(Tela_Inicial, root)
root.mainloop()