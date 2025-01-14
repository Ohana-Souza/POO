from supabase import create_client, Client
from Chaves_banco import SUPABASE_KEY, SUPABASE_URL
from datetime import datetime

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

class HistoricoAlimentos:
    def salvaAlimento(self, usuario, refeicao, descricao, nutrientes):
        try:
            resposta_refeicao = supabase.table('Refeicao').select('id').eq('refeicao', refeicao).execute()
            
            if resposta_refeicao.data and len(resposta_refeicao.data) > 0:
                id_refeicao = resposta_refeicao.data[0]['id']
            else:
                print("Erro: Refeição não encontrada.")
                return False
            
            resposta_alimento = supabase.table('Alimentos').select('id').eq('descricao', descricao).execute()
            
            if resposta_alimento.data and len(resposta_alimento.data) > 0:
                id_alimento = resposta_alimento.data[0]['id']
            else:
                print("Erro: Alimento não encontrado.")
                return False
            
            resposta_usuario = supabase.table('Usuarios').select('id').eq('email', usuario).execute()
            
            if resposta_usuario.data and len(resposta_usuario.data) > 0:
                id_usuario = resposta_usuario.data[0]['id']
            else:
                print("Erro: Usuário não encontrado.")
                return False
            
            dia_refeicao = datetime.today().strftime('%Y-%m-%d')
            
            response = supabase.table('Historico_Alimentos').insert({
                'dia': dia_refeicao,
                'id_refeicao': id_refeicao,
                'id_alimento': id_alimento,
                'energia': nutrientes[0],
                'proteina': nutrientes[1],
                'lipideo': nutrientes[2],
                'carboidrato': nutrientes[3],
                'fibra': nutrientes[4],
                'id_usuario': id_usuario
            }).execute()
            
            if response.data:
                print("Alimento salvo com sucesso.")
                return True
            else:
                print("Erro ao salvar alimento.")
                return False

        except Exception as e:
            print(f"Erro inesperado ao salvar alimento: {e}")
            return False


    def mostraHistorico(self, data, refeicao, usuario):

        resposta_refeicao = supabase.table('Refeicao').select('id').eq('refeicao', refeicao).execute()

        if resposta_refeicao.data and len(resposta_refeicao.data) > 0:
            id_refeicao = resposta_refeicao.data[0]['id']


        resposta_usuario = supabase.table('Usuarios').select('id').eq('email', usuario).execute()

        if resposta_usuario.data and len(resposta_usuario.data) > 0:
            id_usuario = resposta_usuario.data[0]['id']

        response = supabase.table("Historico_Alimentos").select("dia, Refeicao(refeicao),Alimentos(descricao), proteina, carboidrato, fibra, lipideo, energia").match({"dia": data, "id_refeicao": id_refeicao, "id_usuario":id_usuario}).execute()
        dados = response.data

        linhas_formatadas = []

        for i, item in enumerate(dados, 1):
            linhas_formatadas.append(f"Alimento {i}:")
            linhas_formatadas.append(f"  Descrição: {item['Alimentos']['descricao']}")
            linhas_formatadas.append(f"  Proteína: {item['proteina']} g")
            linhas_formatadas.append(f"  Carboidrato: {item['carboidrato']} g")
            linhas_formatadas.append(f"  Fibra: {item['fibra']} g")
            linhas_formatadas.append(f"  Lipídeo: {item['lipideo']} g")
            linhas_formatadas.append(f"  Energia: {item['energia']} kcal")
            linhas_formatadas.append("-" * 40)
        

        if not response.data:  
            print("Nenhum dado encontrado no histórico")
            return False

        if 'error' in response:  
            print("Erro ao buscar dados:", response['error'])
            return False

        return "\n".join(linhas_formatadas)


#Testessss
from Alimento import Alimento
from Calculadora_Insulina import Calculadora_Insulina
from Insulina import Humalog 
from Usuario import Usuario
from Perfil_Medico import PerfilMedico
from Nutrientes import Nutrientes
from Historico_refeicao import HistoricoRefeicao


#Usuario_teste = Usuario("julia4@gmail.com")
#Usuario_teste.autenticacao_usuario("senha")
#Perfil_teste = PerfilMedico(Usuario_teste.email,"Feminino",153,43,19,"Leve","Tipo 1","Sim","Asperge",15)
#alimento1 = Alimento()
#alimento1.adicionaAlimento(200,"Arroz, integral, cozido")
#alimento2 = Alimento()
#alimento2.adicionaAlimento(500,"Bolo, mistura para")
#historico_alimentos = HistoricoAlimentos()
#historico_alimentos.salvaAlimento("julia4@gmail.com", "Café da manhã", alimento1.descricao, alimento1.nutrientes)
#historico_alimentos.salvaAlimento("julia4@gmail.com", "Café da manhã", alimento2.descricao, alimento2.nutrientes)
#nutrientes_teste = Nutrientes()
#nutrientes_teste.adicionaNutrientes(alimento1)
#nutrientes_teste.adicionaNutrientes(alimento2)
#nutrientes_teste.mostraTotais()
#insulina_teste = Humalog(Perfil_teste.peso, Perfil_teste.tipo_diabetes, nutrientes_teste.total_carboidratos,nutrientes_teste.total_proteina, Perfil_teste.dosagem_max)
#calculadora = Calculadora_Insulina() 
#dose_calculada = calculadora.fazCalculoDosagem(insulina_teste)
#alarme = calculadora.fazVerificacaoAlarme(insulina_teste, dose_calculada)
#historico_refeicao = HistoricoRefeicao()
#nutrientes_lista = nutrientes_teste.obterLista()
#historico_refeicao.salvaRefeicao(Perfil_teste._email, "Café da manhã", nutrientes_lista, dose_calculada)
#diaHoje = datetime.today().strftime('%Y-%m-%d')
#historico_alimentos = HistoricoAlimentos()
#mostra = historico_alimentos.mostraHistorico(diaHoje, "Café da manhã", "julia4@gmail.com")
#print(mostra)
