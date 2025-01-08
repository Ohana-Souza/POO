from Usuario import Usuario
from supabase import create_client, Client
from Chaves_banco import SUPABASE_KEY, SUPABASE_URL

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

class PerfilMedico(Usuario):
    def __init__(self, email, sexo, altura, peso, idade, atividade, tipo_diabetes, toma_insulina, tipo_insulina, dosagem_max):
        super().__init__(email)
        self.sexo = sexo
        self.altura = altura
        self.peso = peso
        self.idade = idade 
        self.atividade = atividade
        self.tipo_diabetes = tipo_diabetes
        self.toma_insulina = toma_insulina
        self.tipo_insulina = tipo_insulina
        self.dosagem_max = dosagem_max 
        
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
        
        if resposta_tipo_diabetes.data and len(resposta_tipo_diabetes.data) > 0:
            id_tipo_diabetes = resposta_tipo_diabetes.data[0]['id']
        
        resposta_tipo_insulina = supabase.table('Tipos_insulina').select('id').eq('tipo', self.tipo_insulina).execute()
        
        if resposta_tipo_insulina.data and len(resposta_tipo_insulina.data) > 0:
            id_tipo_insulina = resposta_tipo_insulina.data[0]['id']


        if self.toma_insulina == "Sim":
            resposta_toma_insulina = 1
        elif self.toma_insulina == "Não":
            resposta_toma_insulina = 0

        response = supabase.table('Perfil_medico').insert({
            'id_usuario': id_usuario,
            'id_sexo': id_sexo,
            'altura': self.altura,
            'idade': self.idade,
            'id_atividade': id_atividade,
            'id_tipo_diabetes': id_tipo_diabetes,
            'peso': self.peso,
            'toma_insulina': resposta_toma_insulina,
            'id_tipo_insulina': id_tipo_insulina,
            'dosagem_max': self.dosagem_max
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
    
#teste = PerfilMedico("juliateste@gmail.com", "Feminino",153,43,19,"Leve","Tipo 1","Sim","Asperge",40)
#teste.cria_perfil_medico()