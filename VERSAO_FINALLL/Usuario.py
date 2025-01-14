import bcrypt
import re
from supabase import create_client, Client
from Chaves_banco import SUPABASE_KEY, SUPABASE_URL

# Criação do cliente Supabase
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

class Usuario:
    def __init__(self, email: str) -> None:
        """
        Inicializa um objeto Usuario com o email fornecido.
        """
        self._email = email
        
    @property
    def email(self) -> str:
        """
        Obtém o email do usuário.

        :return: str - Email do usuário.
        """
        return self._email

    @email.setter
    def email(self, novo_email: str) -> None:
        """
        Define um novo email para o usuário após verificar seu formato.
        """
        email = novo_email.strip().lower()
        padrao_email = r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$'
        if not re.match(padrao_email, email):
            print("Formato de e-mail inválido.")
        self._email = email

    def autenticacao_usuario(self, senha_inserida: str) -> bool:
        """
        Autentica o usuário comparando a senha inserida com a senha armazenada no banco de dados.
        """
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

    def insere_usuario(self, senha: str) -> bool:
        """
        Insere um novo usuário no banco de dados após verificar o formato do email e criptografar a senha.
        """
        padrao_email = r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$'
        if not re.match(padrao_email, self._email):
            print("Formato de e-mail inválido.")
            return False
            
        response = supabase.table('Usuarios').select('email').eq('email', self._email).execute()

        if response.data and len(response.data) > 0:
            print("Erro: Este email já está em uso.")
            return False

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
