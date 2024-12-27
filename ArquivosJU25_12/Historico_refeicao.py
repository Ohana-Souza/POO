from supabase import create_client, Client
from Chaves_banco import SUPABASE_KEY, SUPABASE_URL

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


class HistoricoRefeicao:
    
    def salvaRefeicao(self):
        pass 