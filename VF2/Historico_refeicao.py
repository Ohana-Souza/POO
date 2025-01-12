from supabase import create_client, Client
from Chaves_banco import SUPABASE_KEY, SUPABASE_URL
from datetime import datetime
from Alimento import Alimento

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


class HistoricoRefeicao:
    
    def salvaRefeicao(self, usuario, refeicao, nutrientes, insulina):
        
        resposta_refeicao = supabase.table('Refeicao').select('id').eq('refeicao', refeicao).execute()

        if resposta_refeicao.data and len(resposta_refeicao.data) > 0:
            id_refeicao = resposta_refeicao.data[0]['id']

        resposta_usuario = supabase.table('Usuarios').select('id').eq('email', usuario).execute()

        if resposta_usuario.data and len(resposta_usuario.data) > 0:
            id_usuario = resposta_usuario.data[0]['id']
        
        dia_refeicao = datetime.today().strftime('%Y-%m-%d')

        response = supabase.table('Historico').insert({
            'dia': dia_refeicao,
            'id_refeicao': id_refeicao,
            'energia' : nutrientes[0],
            'proteina': nutrientes[1],
            'lipideo': nutrientes[2],
            'carboidrato': nutrientes[3],
            'fibra': nutrientes[4],
            'insulina': insulina,
            'id_usuario': id_usuario
        }).execute()


        if not response.data:  
            print("Nenhum dado encontrado para o alimento selecionado.")
            return False

        if 'error' in response:  
            print("Erro ao buscar dados:", response['error'])
            return False

    def mostraHistorico(self, data, refeicao, usuario):

        resposta_refeicao = supabase.table('Refeicao').select('id').eq('refeicao', refeicao).execute()

        if resposta_refeicao.data and len(resposta_refeicao.data) > 0:
            id_refeicao = resposta_refeicao.data[0]['id']


        resposta_usuario = supabase.table('Usuarios').select('id').eq('email', usuario).execute()

        if resposta_usuario.data and len(resposta_usuario.data) > 0:
            id_usuario = resposta_usuario.data[0]['id']

        response = supabase.table("Historico").select("dia, Refeicao(refeicao), proteina, carboidrato, fibra, lipideo, energia, insulina").match({"dia": data, "id_refeicao": id_refeicao, "id_usuario":id_usuario}).execute()
        dados = response.data

        linhas_formatadas = []

        for i, item in enumerate(dados, 1):
            linhas_formatadas.append(f"Refeição {i}:")
            linhas_formatadas.append(f"  Dia: {item['dia']}")
            linhas_formatadas.append(f"  Refeição: {item['Refeicao']['refeicao']}")
            linhas_formatadas.append(f"  Proteína: {item['proteina']} g")
            linhas_formatadas.append(f"  Carboidrato: {item['carboidrato']} g")
            linhas_formatadas.append(f"  Fibra: {item['fibra']} g")
            linhas_formatadas.append(f"  Lipídeo: {item['lipideo']} g")
            linhas_formatadas.append(f"  Energia: {item['energia']} kcal")
            linhas_formatadas.append(f"  Insulina: {item['insulina']} U")
            linhas_formatadas.append("-" * 40)
        

        if not response.data:  
            print("Nenhum dado encontrado no histórico")
            return False

        if 'error' in response:  
            print("Erro ao buscar dados:", response['error'])
            return False

        return "\n".join(linhas_formatadas)
        


from Alimento import Alimento
from Calculadora_Insulina import Calculadora_Insulina
from Insulina import Humalog 
from Usuario import Usuario
from Perfil_Medico import PerfilMedico
from Nutrientes import Nutrientes

Usuario_teste = Usuario("juliateste@gmail.com")
Usuario_teste.autenticacao_usuario("senha")
Perfil_teste = PerfilMedico(Usuario_teste.email,"Feminino",153,43,19,"Leve","Tipo 1","Sim","Asperge",15)
alimento1 = Alimento()
alimento1.adicionaAlimento(200,"Arroz, integral, cozido")
alimento2 = Alimento()
alimento2.adicionaAlimento(500,"Bolo, mistura para")
nutrientes_teste = Nutrientes()
nutrientes_teste.adicionaNutrientes(alimento1)
nutrientes_teste.adicionaNutrientes(alimento2)
nutrientes_teste.mostraTotais()
insulina_teste = Humalog(Perfil_teste.peso, Perfil_teste.tipo_diabetes, nutrientes_teste.total_carboidratos,nutrientes_teste.total_proteina, Perfil_teste.dosagem_max)
calculadora = Calculadora_Insulina() 
dose_calculada = calculadora.fazCalculoDosagem(insulina_teste)
alarme = calculadora.fazVerificacaoAlarme(insulina_teste, dose_calculada)
historico = HistoricoRefeicao()
nutrientes_lista = nutrientes_teste.obterLista()
historico.salvaRefeicao(Perfil_teste._email, "Café da manhã", nutrientes_lista, dose_calculada)
diaHoje = datetime.today().strftime('%Y-%m-%d')
mostra = historico.mostraHistorico(diaHoje, "Café da manhã", Perfil_teste.email)
print(mostra)


