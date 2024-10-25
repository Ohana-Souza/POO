import bcrypt
import re
from supabase import create_client, Client


SUPABASE_URL = "https://aehobqlgeacrbhbgqrpk.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFlaG9icWxnZWFjcmJoYmdxcnBrIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Mjk2ODI0NjQsImV4cCI6MjA0NTI1ODQ2NH0.8G5nxxAAslmRb0rFqD8G0--ovTettoIV5a5U4OqDnc8"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


class Usuario:
    def __init__(self, email):
        self.email = email
        

    def autenticacao_usuario(self, senha_inserida):
        response = supabase.table('Usuarios').select('senha').eq('email', self.email).execute()

        if response.data:  
            senha_armazenada = response.data[0]['senha']
        
            if bcrypt.checkpw(senha_inserida.encode('utf-8'), senha_armazenada.encode('utf-8')):
                print("Login realizado com sucesso!")
            else:
                print("Senha Inválida")
        else:
            print("Usuário não encontrado!")
       
            
    def insere_usuario(self, senha):
        
        padrao_email = r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$'
        if not re.match(padrao_email, self.email):
            print("Formato de e-mail inválido.")
            return
            
        response = supabase.table('Usuarios').select('email').eq('email', self.email).execute()

        if response.data and len(response.data) > 0:
            print("Erro: Este email já está em uso.")
            return  

        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(senha.encode('utf-8'), salt)
        hashed_senha = hashed.decode('utf-8')

        response = supabase.table('Usuarios').insert({
            'email': self.email,
            'senha': hashed_senha
        }).execute()

        if response.data:  
            print("Usuário cadastrado com sucesso!")
            return True
        elif response.error:  
            print(f"Erro cadastrando o usuário: {response.error.message}")
            return False
        else:
            print("Erro desconhecido.")
            return False
            
        
            
class PerfilMedico(Usuario):
    def __init__(self, email, sexo, altura, peso, idade, atividade, tipo_diabetes):
        super().__init__(email)
        self.sexo = sexo
        self.altura = altura
        self.peso = peso
        self.idade = idade 
        self.atividade = atividade
        self.tipo_diabetes = tipo_diabetes
        
    def cria_perfil_medico(self):
        resposta_usuario = supabase.table('Usuarios').select('id').eq('email', self.email).execute()

        if resposta_usuario.data and len(resposta_usuario.data) > 0:
            id_usuario = resposta_usuario.data[0]['id']

        resposta_sexo = supabase.table('Sexos').select('id').eq('sexo', self.sexo).execute()

        if resposta_sexo.data and len(resposta_sexo.data) > 0:
            id_sexo = resposta_sexo.data[0]['id']

        resposta_atividade = supabase.table('Atividades_fisicas').select('id').eq('nivel', self.atividade).execute()

        if resposta_atividade.data and len(resposta_atividade.data) > 0:
            id_atividade = resposta_atividade.data[0]['id']

        resposta_tipo_diabetes = supabase.table('Tipos_diabetes').select('id').eq('tipo', self.tipo_diabetes).execute()

        if resposta_tipo_diabetes and len(resposta_tipo_diabetes) > 0:
            id_tipo_diabetes = resposta_tipo_diabetes.data[0]['id']


        response = supabase.table('Perfil_medico').insert({
            'id_usuario': id_usuario,
            'id_sexo': id_sexo,
            'altura': self.altura,
            'idade': self.idade,
            'id_atividade': id_atividade,
            'id_tipo_diabetes': id_tipo_diabetes,
            'peso': self.peso
        }).execute()


        if response.data:  
            print("Perfil médico cadastrado com sucesso!")
            return True
        elif response.error:  
            print(f"Erro cadastrando o perfil médico: {response.error.message}")
            return False
        else:
            print("Erro desconhecido.")
            return False
    
    
            
def main():   
    #teste login
    print("Teste login: ")
    email_inserido1 = input("Digite seu e-mail: ")
    senha_inserida1 =  input("Digite sua senha: ")       
    usuario1 = Usuario(email_inserido1)
    usuario1.autenticacao_usuario(senha_inserida1)
    #'john@example.com', 'supersecurepassword'
    
    #teste cadastro
    print("Teste cadastro")
    email_inserido2 = input("Digite seu e-mail: ")
    senha_inserida2 =  input("Digite sua senha: ")       
    usuario2 = Usuario(email_inserido2)
    sucesso_cadastro = usuario2.insere_usuario(senha_inserida2)
    
    #teste perfil médico
    if sucesso_cadastro: 
        print("Teste perfil médico: ")
        email_usuario = usuario2.email
        sexo_inserido = input("Qual seu sexo? ")
        altura_inserida = input("Qual sua altura? ")
        idade_inserida = input("Qual sua idade? ")
        peso_inserido = input("Qual seu peso? ")
        atividade_inserido = input("Qual o nível de atividade física que você pratica por semana? ")
        tipo_diabetes_inserido = input("Qual seu tipo de diabetes? ")
        perfilmedico1 = PerfilMedico(email_usuario, sexo_inserido, altura_inserida, idade_inserida, peso_inserido, atividade_inserido, tipo_diabetes_inserido)
        perfilmedico1.cria_perfil_medico()
    
    
if __name__ == "__main__":
    main()

