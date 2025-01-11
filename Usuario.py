import bcrypt
import re
from supabase import create_client, Client
from Chaves_banco import SUPABASE_KEY, SUPABASE_URL

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


class Usuario:
    def __init__(self, email):
        self._email = email
        
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, novo_email):
        email = novo_email.strip().lower()
        padrao_email = r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$'
        if not re.match(padrao_email, email):
            print("Formato de e-mail inválido.")
        self._email = email


    def autenticacao_usuario(self, senha_inserida):
        response = supabase.table('Usuarios').select('senha').eq('email', self._email).execute()

        if response.data:  
            senha_armazenada = response.data[0]['senha']
        
            if bcrypt.checkpw(senha_inserida.encode('utf-8'), senha_armazenada.encode('utf-8')):
                print("Login realizado com sucesso!")
                return True 
            else:
                print("Senha Inválida")
                return False 
        else:
            print("Usuário não encontrado!")
            return False
       
            
    def insere_usuario(self, senha):
        
        padrao_email = r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$'
        if not re.match(padrao_email, self._email):
            print("Formato de e-mail inválido.")
            return
            
        response = supabase.table('Usuarios').select('email').eq('email', self._email).execute()

        if response.data and len(response.data) > 0:
            print("Erro: Este email já está em uso.")
            return  False

        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(senha.encode('utf-8'), salt)
        hashed_senha = hashed.decode('utf-8')

        response = supabase.table('Usuarios').insert({
            'email': self._email,
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
            

