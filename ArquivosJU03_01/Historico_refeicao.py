from supabase import create_client, Client
from Chaves_banco import SUPABASE_KEY, SUPABASE_URL
from datetime import datetime
from Alimento import Alimento

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

class HistoricoRefeicao:

    def salvaRefeicao(self, refeicao, descricao, nutrientes):
        try:
            resposta_refeicao = supabase.table('Refeicao').select('id').eq('refeicao', refeicao).execute()
            if not resposta_refeicao.data:
                print("Refeição não encontrada.")
                return False

            id_refeicao = resposta_refeicao.data[0]['id']
            print(f"ID da Refeição: {id_refeicao}")

            resposta_alimento = supabase.table('Alimentos').select('id').eq('descricao', descricao).execute()
            if not resposta_alimento.data:
                print("Alimento não encontrado.")
                return False

            id_alimento = resposta_alimento.data[0]['id']
            print(f"ID do Alimento: {id_alimento}")

            dia_refeicao = datetime.today().strftime('%Y-%m-%d')
            dados_historico = {
                'dia': dia_refeicao,
                'id_refeicao': id_refeicao,
                'id_alimento': id_alimento,
                'energia': nutrientes[0],
                'proteina': nutrientes[1],
                'lipideo': nutrientes[2],
                'carboidrato': nutrientes[3],
                'fibra': nutrientes[4],
            }
            print(f"Dados a serem inseridos: {dados_historico}")

            response = supabase.table('Historico').insert(dados_historico).execute()
            print(f"Response ao inserir na tabela 'Historico': {response}")

            if not response.data:
                print("Nenhum dado encontrado para o alimento selecionado.")
                return False

            return True

        except Exception as e:
            print(f"Erro ao salvar a refeição: {e}")
            return False

    
    def mostraHistorico(self, data):
        try:
            response = supabase.table('Historico').select(
                'dia', 'id_refeicao(refeicao)', 'id_alimento(descricao)', 'energia', 'proteina', 'lipideo', 'carboidrato', 'fibra'
            ).eq('dia', data).execute()

            print(f"Response ao buscar dados da tabela 'Historico': {response}")

            if not response.data:
                print("Nenhum dado encontrado no histórico.")
                return []

            historico = []
            for item in response.data:
                historico.append(
                    f"Data: {item['dia']}, Refeição: {item['id_refeicao']['refeicao']}, "
                    f"Alimento: {item['id_alimento']['descricao']}, Energia: {item['energia']}kcal, "
                    f"Proteína: {item['proteina']}g, Lipídeo: {item['lipideo']}g, "
                    f"Carboidrato: {item['carboidrato']}g, Fibra: {item['fibra']}g"
                )
            return historico

        except Exception as e:
            print(f"Erro ao buscar histórico: {e}")
            return []

testeAl = Alimento()
testeAl.adicionaAlimento(1, 200)
teste = HistoricoRefeicao()
if teste.salvaRefeicao("Café da manhã", testeAl.descricao, testeAl.nutrientes):
    print("Refeição salva com sucesso!")
else:
    print("Erro ao salvar a refeição.")
printar = teste.mostraHistorico(datetime.today().strftime('%Y-%m-%d'))
print(printar)
