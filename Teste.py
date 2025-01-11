import csv
import sys
import tkinter as tk
import datetime
import re

from tkinter import messagebox,StringVar, OptionMenu, Frame, Button
from supabase import create_client, Client
from Chaves_banco import SUPABASE_URL, SUPABASE_KEY
from Alimento import Alimento
from Usuario import Usuario
from Historico_refeicao import HistoricoRefeicao
from Perfil_Medico import PerfilMedico
from tkcalendar import DateEntry
from Nutrientes import Nutrientes
from Insulina import Asparge, Humalog
from PIL import Image, ImageTk
from Verificadora import Verificadora

import os
#print(f"Localização do arquivo Historico_refeicao: {os.path.abspath(HistoricoRefeicao.__module__)}") 

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

caminho_imagem1 = os.path.join(os.path.dirname(__file__), "Telas", "1.png")
caminho_imagem2 = os.path.join(os.path.dirname(__file__), "Telas", "2.png")
caminho_imagem3 = os.path.join(os.path.dirname(__file__), "Telas", "3.png")
caminho_imagem4 = os.path.join(os.path.dirname(__file__), "Telas", "4.png")
caminho_imagem5 = os.path.join(os.path.dirname(__file__), "Telas", "5.png") #imagem aviso
caminho_TACO = os.path.join(os.path.dirname(__file__), "TACO.csv")

def configurar_fundo_login(frame):
    imagem = Image.open(caminho_imagem3)
    imagem = imagem.resize((360, 640), Image.Resampling.LANCZOS)
    bg = ImageTk.PhotoImage(imagem)

    # Canvas para exibir a imagem
    canvas = tk.Canvas(frame, width=360, height=640)
    canvas.create_image(0, 0, anchor=tk.NW, image=bg)
    canvas.image = bg
    canvas.place(relwidth=1, relheight=1)
    
def configurar_fundo_cadastro(frame):
    imagem = Image.open(caminho_imagem2)
    imagem = imagem.resize((360, 640), Image.Resampling.LANCZOS)
    bg = ImageTk.PhotoImage(imagem)

    # Canvas para exibir a imagem
    canvas = tk.Canvas(frame, width=360, height=640)
    canvas.create_image(0, 0, anchor=tk.NW, image=bg)
    canvas.image = bg
    canvas.place(relwidth=1, relheight=1)

def configurar_fundo_liso(frame):
    imagem = Image.open(caminho_imagem4)
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

# Tela Inicial
def Tela_Inicial(root):
    frame = tk.Frame(root)
    frame.place(relwidth=1, relheight=1)

    imagem = Image.open(caminho_imagem1)
    imagem = imagem.resize((360, 640), Image.Resampling.LANCZOS)
    bg = ImageTk.PhotoImage(imagem)

    canvas = tk.Canvas(frame, width=360, height=640)
    canvas.create_image(0, 0, anchor=tk.NW, image=bg)
    canvas.image = bg
    canvas.place(relwidth=1, relheight=1)

    tk.Label(frame, text="TELA INICIAL", font=("Helvetica", 16), bg="#ffffff", fg="#333333").pack(pady=40)
    tk.Button(frame, text="Entrar", width=20, command=lambda: mudar_tela(Tela_Login, root)).pack(pady=20)
    tk.Button(frame, text="Cadastrar", width=20, command=lambda: mudar_tela(Tela_Cadastro, root)).pack(pady=20)

# Tela de Login
def Tela_Login(root):
    frame = tk.Frame(root)
    frame.place(relwidth=1, relheight=1)

    configurar_fundo_login(frame)

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

        if usuario.autenticacao_usuario(senha):
            error_label.config(text="Login realizado com sucesso!", fg="green")
            # Passe o email diretamente
            root.after(200, lambda: mudar_tela(Tela_Consumo1, root, email))
        else:
            error_label.config(text="Usuário ou senha inválidos.", fg="red")

    tk.Button(frame, text="Login", width=20, command=autenticar).pack(pady=10)
    tk.Button(frame, text="Voltar", width=20, command=lambda: mudar_tela(Tela_Inicial, root)).pack(pady=10)

def Tela_Cadastro(root):
    frame = tk.Frame(root)
    frame.place(relwidth=1, relheight=1)

    # Aplica o fundo
    configurar_fundo_cadastro(frame)

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

        # Validando o e-mail
        if not re.match(r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$', email):
            error_label.config(text="Formato de e-mail inválido.", fg="red")
            return

        usuario = Usuario(email)
        response = usuario.insere_usuario(senha)
        print(response)

        if response is True:
            error_label.config(text="Usuário cadastrado com sucesso!", fg="green")
            # Passa o email para a próxima tela
            root.after(2000, lambda: mudar_tela(Tela_PerfilMedico1, root, email))
        else:
            error_label.config(text="Email já cadastrado!", fg="red")

    tk.Button(frame, text="Avançar", width=20, command=cadastrar).pack(pady=10)
    tk.Button(frame, text="Voltar", width=20, command=lambda: mudar_tela(Tela_Inicial, root)).pack(pady=10)


def Tela_PerfilMedico1(root, email):
    frame = tk.Frame(root)
    frame.place(relwidth=1, relheight=1)

    tk.Label(frame, text=f"Email: {email}", font=("Helvetica", 12)).pack(pady=5)

    tk.Label(frame, text="Sexo:").pack(pady=5)
    sexo_var = tk.StringVar()
    tk.OptionMenu(frame, sexo_var, "Masculino", "Feminino").pack(pady=5)

    tk.Label(frame, text="Altura (cm):").pack(pady=5)
    entry_altura = tk.Entry(frame)
    entry_altura.pack(pady=5)

    tk.Label(frame, text="Peso (kg):").pack(pady=5)
    entry_peso = tk.Entry(frame)
    entry_peso.pack(pady=5)

    tk.Label(frame, text="Idade:").pack(pady=5)
    entry_idade = tk.Entry(frame)
    entry_idade.pack(pady=5)

    tk.Label(frame, text="Atividade Física:").pack(pady=5)
    atividade_var = tk.StringVar()
    tk.OptionMenu(frame, atividade_var, "Sedentário", "Leve", "Moderado", "Intenso").pack(pady=5)

    error_label = tk.Label(frame, text="", fg="red")
    error_label.pack(pady=5)

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

    tk.Button(frame, text="Avançar", width=20, command=avancar).pack(pady=10)
    tk.Button(frame, text="Voltar", width=20, command=lambda: mudar_tela(Tela_Cadastro, root)).pack(pady=10)

# Segunda Tela
def Tela_PerfilMedico2(root, email, sexo, altura, peso, idade, atividade):
    frame = tk.Frame(root)
    frame.place(relwidth=1, relheight=1)

    tk.Label(frame, text=f"Email: {email}", font=("Helvetica", 12)).pack(pady=5)

    tk.Label(frame, text="Tipo de Diabetes:").pack(pady=5)
    diabetes_var = tk.StringVar()
    tk.OptionMenu(frame, diabetes_var, "Tipo 1", "Tipo 2", "Gestacional", "Pré-diabetes").pack(pady=5)

    tk.Label(frame, text="Toma Insulina (Sim/Não):").pack(pady=5)
    insulina_var = tk.StringVar()
    tk.OptionMenu(frame, insulina_var, "Sim", "Não").pack(pady=5)

    tk.Label(frame, text="Tipo de Insulina:").pack(pady=5)
    tipo_insulina_var = tk.StringVar()
    tk.OptionMenu(frame, tipo_insulina_var, "Asperge", "Humalog", "NPH", "Glargina").pack(pady=5)

    tk.Label(frame, text="Dosagem Máxima de Insulina (unidades):").pack(pady=5)
    entry_dosagem_max = tk.Entry(frame)
    entry_dosagem_max.pack(pady=5)

    error_label = tk.Label(frame, text="", fg="red")
    error_label.pack(pady=5)

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

        perfil = PerfilMedico(email, sexo, altura, peso, idade, atividade, tipo_diabetes, toma_insulina, tipo_insulina, dosagem_max)

        if perfil.cria_perfil_medico():
            error_label.config(text="Perfil médico cadastrado com sucesso!", fg="green")
            root.after(2000, lambda: mudar_tela(Tela_Alerta, root, email))
        else:
            error_label.config(text="Reveja as informações inseridas!", fg="red")

    tk.Button(frame, text="Salvar", width=20, command=salvar).pack(pady=10)
    tk.Button(frame, text="Voltar", width=20, command=lambda: mudar_tela(Tela_PerfilMedico1, root, email)).pack(pady=10)


def Tela_Alerta(root,email):
    
    frame = tk.Frame(root)
    frame.place(relwidth=1, relheight=1)
    
    configurar_fundo_liso(frame)
    
    def avancar():
        mudar_tela(Tela_Consumo1,root, email)
    
    tk.Button(frame, text="Avançar", width=20, command=avancar).pack(pady=10)


# Tela de Consumo
def Tela_Consumo1(root, email):
    frame = tk.Frame(root)
    frame.place(relwidth=1, relheight=1)

    configurar_fundo_liso(frame)

    tk.Label(frame, text=f"Bem-vindo(a), {email}", font=("Helvetica", 16)).pack(pady=20)
    tk.Button(frame, text="Adicionar Alimento", width=20, command=lambda: mudar_tela(Tela_CadastroRefeicao, root, email)).pack(pady=10)
    tk.Button(frame, text="Histórico Nutrientes", width=20, command=lambda: mudar_tela(Tela_Historico, root, email)).pack(pady=10)
    tk.Button(frame, text="Histórico Insulina", width=20, command=lambda: mudar_tela(Tela_Historico_Insulina, root, email)).pack(pady=10)
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

def Tela_CadastroAlimento(root, email, refeicao):
    historico = HistoricoRefeicao()
    frame = tk.Frame(root)
    frame.place(relwidth=1, relheight=1)

    configurar_fundo_liso(frame)

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
    lista_alimentos = ler_csv(caminho_TACO)

    # Função de busca
    def buscar_alimentos(event=None):
        termo_busca = entry_busca.get().lower()
        resultado = [alimento for alimento in lista_alimentos if termo_busca in alimento.lower()]
        menu = option_menu["menu"]
        menu.delete(0, "end")
        if resultado:
            for alimento in resultado:
                menu.add_command(label=alimento, command=lambda value=alimento: alimento_var.set(value))
        else:
            menu.add_command(label="Alimento digitado não listado", command=lambda: None)

    # Populando o OptionMenu
    alimento_var = tk.StringVar(value="Selecione um alimento")

    option_menu = tk.OptionMenu(frame, alimento_var, *lista_alimentos)
    option_menu.pack(pady=5)

    tk.Label(frame, text="Buscar alimento:").pack(pady=5)
    entry_busca = tk.Entry(frame)
    entry_busca.pack(pady=5)
    entry_busca.bind("<KeyRelease>", buscar_alimentos)

    tk.Label(frame, text="Informe a quantidade (gramas):").pack(pady=5)
    entry_quantidade = tk.Entry(frame)
    entry_quantidade.pack(pady=5)

    error_label = tk.Label(frame, text="", fg="red")
    error_label.pack(pady=5)
            
    def salvar():
        try:            
            descricao_alimento = alimento_var.get()

            if not descricao_alimento or descricao_alimento == "Alimento digitado não listado":
                error_label.config(text="Por favor, selecione um alimento válido.", fg="red")
                return

            quantidade_valida = entry_quantidade.get()
            
            if not Verificadora.verificar_inteiro(quantidade_valida, tipo="float"):
                error_label.config(text="Insira um valor válido!", fg="red")
                return
            
            quantidade = float(entry_quantidade.get())
            alimento = Alimento()
            alimento.adicionaAlimento(descricao_alimento, quantidade)

            if not alimento.nutrientes:
                error_label.config(text=" Erro ao carregar nutrientes do alimento.", fg="red")
                         
            # Exibe os nutrientes no terminal para depuração
            print(f"Alimento: {alimento.descricao}, Nutrientes: {alimento.nutrientes}")

            # Salva no histórico
            if historico.salvaRefeicao(email, refeicao, alimento.descricao, alimento.nutrientes):
                error_label.config(text="Refeição salva com sucesso!", fg="green")
            else:
                error_label.config(text="Falha ao salvar a refeição. Verifique os dados.", fg="red")
                                    
        except ValueError as ve:
            print(f"Erro de validação: {ve}")
            error_label.config(text=f"Erro: {ve}", fg="red")
        except Exception as e:
            print(f"Erro inesperado: {e}")
            error_label.config(text="Erro inesperado ao salvar. Verifique os dados.", fg="red")



    def voltar():
        mudar_tela(Tela_CadastroRefeicao, root, email)

    def avancar():
        mudar_tela(Tela_Consumo1, root, email)

    tk.Button(frame, text="Salvar", width=20, command=salvar).pack(pady=10)
    tk.Button(frame, text="Avançar", width=20, command=avancar).pack(pady=10)
    tk.Button(frame, text="Voltar", width=20, command=voltar).pack(pady=10)


# Tela de Histórico
def Tela_Historico(root, usuario_email):
    frame = tk.Frame(root)
    frame.place(relwidth=1, relheight=1)
    configurar_fundo_liso(frame)

    tk.Label(frame, text="Histórico de Consumos", font=("Helvetica", 16)).pack(pady=20)
    tk.Label(frame, text="Selecione a data:").pack(pady=5)

    # Entrada de data
    data_entry = DateEntry(frame, width=12, background='darkblue', foreground='white', borderwidth=2)
    data_entry.pack(pady=5)

    # Seletor de refeição
    tk.Label(frame, text="Selecione a refeição:").pack(pady=5)
    refeicao_var = StringVar(value="Selecione uma refeição")
    refeicoes_disponiveis = ["Café da manhã", "Almoço", "Jantar", "Lanche"]  # Refeições disponíveis
    OptionMenu(frame, refeicao_var, *refeicoes_disponiveis).pack(pady=5)

    # Seletor de propriedade
    propriedades = ["proteina", "carboidrato", "fibra", "lipideo", "energia"]
    propriedade_var = StringVar(value="proteina")
    tk.Label(frame, text="Selecione a propriedade a ser exibida:").pack(pady=5)
    OptionMenu(frame, propriedade_var, *propriedades).pack(pady=5)

    historico_frame = tk.Frame(frame)
    historico_frame.pack(pady=10, fill="both", expand=True)

    def limpar_frame():
        for widget in historico_frame.winfo_children():
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
        if propriedade_selecionada not in propriedades:
            messagebox.showerror("Erro", "Propriedade selecionada inválida.")
            return

        # Obtém o histórico do banco
        historico = HistoricoRefeicao().mostraHistorico(data=data_selecionada, refeicao=refeicao_selecionada, usuario_email=usuario_email)

        if not historico:
            tk.Label(historico_frame, text="Nenhum dado encontrado para a data selecionada.").pack(pady=5)
        else:
            # Exibe os dados no frame
            tk.Label(historico_frame, text=f"Histórico de {propriedade_selecionada.capitalize()} em {data_selecionada}:", font=("Helvetica", 10)).pack(pady=5)
            for item in historico:
                descricao = item["Alimentos"]["descricao"]
                valor = item[propriedade_selecionada]
                tk.Label(historico_frame, text=f"- {descricao}: {valor}g").pack(pady=2)

    def voltar():
        mudar_tela(Tela_Consumo1, root, usuario_email)

    tk.Button(frame, text="Exibir Histórico", width=20, command=exibir_historico).pack(pady=10)
    tk.Button(frame, text="Limpar", width=20, command=limpar_frame).pack(pady=10)
    tk.Button(frame, text="Voltar", width=20, command=voltar).pack(pady=10)


#######################################################################
def Tela_Historico_Insulina(root, usuario):
    frame = tk.Frame(root)
    frame.place(relwidth=1, relheight=1)
    configurar_fundo_liso(frame)

    email_usuario = usuario.email
    
    error_label = tk.Label(frame, text="", fg="red")
    error_label.pack(pady=5)

    # Obter informações do perfil médico
    resposta_usuario = supabase.table('Usuarios').select('*').eq('email', email_usuario).execute()
    if resposta_usuario.data and len(resposta_usuario.data) > 0:
        perfil_usuario = resposta_usuario.data[0]
        perfil_medico = PerfilMedico(
            email=perfil_usuario['email'],
            sexo=perfil_usuario['sexo'],
            altura=perfil_usuario['altura'],
            peso=perfil_usuario['peso'],
            idade=perfil_usuario['idade'],
            atividade=perfil_usuario['atividade'],
            tipo_diabetes=perfil_usuario['tipo_diabetes'],
            toma_insulina=perfil_usuario['toma_insulina'],
            tipo_insulina=perfil_usuario['tipo_insulina'],
            dosagem_max=perfil_usuario['dosagem_max']
        )
    else:
        error_label.config(text="Usuário não encontrado.", fg="red")
        return

    tk.Label(frame, text="Histórico de Consumos", font=("Helvetica", 16)).pack(pady=20)
    tk.Label(frame, text="Selecione a data:").pack(pady=5)

    data_entry = DateEntry(frame, width=12, background='darkblue', foreground='white', borderwidth=2)
    data_entry.pack(pady=5)

    tk.Label(frame, text="Selecione a refeição:").pack(pady=5)
    refeicao_var = StringVar(value="Selecione uma refeição")
    refeicoes_disponiveis = ["Café da Manhã", "Almoço", "Jantar"]  # Exemplo de refeições disponíveis
    OptionMenu(frame, refeicao_var, *refeicoes_disponiveis).pack(pady=5)

    historico_frame = tk.Frame(frame)
    historico_frame.pack(pady=10, fill="both", expand=True)

    nutrientes = Nutrientes()

    def limpar_frame():
        for widget in historico_frame.winfo_children():
            widget.destroy()

    def exibir_historico():
        limpar_frame()
        data_selecionada = data_entry.get_date().strftime('%Y-%m-%d')
        refeicao_selecionada = refeicao_var.get()

        if refeicao_selecionada == "Selecione uma refeição":
            
            ("Erro", "Por favor, selecione uma refeição.")
            return

        historico = HistoricoRefeicao().mostraHistorico(data=data_selecionada, refeicao=refeicao_selecionada)
        print(f"Histórico obtido para {data_selecionada}: {historico}")

        if not historico:
            tk.Label(historico_frame, text="Nenhum dado encontrado para a data selecionada.").pack(pady=5)
        else:
            for item in historico:
                alimento = type('Alimento', (object,), {'nutrientes': [
                    item['energia'], item['proteina'], item['lipideo'], item['carboidrato'], item['fibra']]})()
                nutrientes.adicionaNutrientes(alimento)

            totais = nutrientes.obter_totais()
            carboidratos = totais['carboidratos']
            proteinas = totais['proteina']

            insulina_tipo = perfil_medico.tipo_insulina
            peso = perfil_medico.peso
            tipo_diabetes = perfil_medico.tipo_diabetes
            dosagem_max = perfil_medico.dosagem_max

            if insulina_tipo == "Asparge":
                dosagem = Asparge().calculaDosagem(peso, tipo_diabetes, dosagem_max, carboidratos, proteinas)
            elif insulina_tipo == "Humalog":
                dosagem = Humalog().calculaDosagem(peso, tipo_diabetes, carboidratos, proteinas, dosagem_max)
            else:
                error_label.config(text="Tipo de insulina desconhecido.", fg="green")
                return

            tk.Label(historico_frame, text=f"Quantidade de carboidratos: {carboidratos} g").pack(pady=5)
            tk.Label(historico_frame, text=f"Quantidade de proteínas: {proteinas} g").pack(pady=5)
            tk.Label(historico_frame, text=f"Dose de insulina calculada: {dosagem} unidades").pack(pady=5)

    tk.Button(frame, text="Exibir Histórico e Calcular Insulina", width=25, command=exibir_historico).pack(pady=10)
    tk.Button(frame, text="Limpar", width=20, command=limpar_frame).pack(pady=10)
    tk.Button(frame, text="Voltar", width=20, command=lambda: Tela_Consumo1(root)).pack(pady=10)


###############################################################################

root = tk.Tk()
root.title("Contagem de Carboidratos")
root.geometry("360x640")
mudar_tela(Tela_Inicial, root)
root.mainloop()