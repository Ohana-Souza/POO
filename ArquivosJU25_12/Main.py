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