from Usuario import Usuario 
from Perfil_Medico import PerfilMedico

            
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
    
