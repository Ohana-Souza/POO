from abc import ABC, abstractmethod 

class InterfaceInsulina(ABC):
    @abstractmethod
    def calculaDosagem(self):
        pass

    def verificaAlarme(self, dose_calculada, dosagem_maxima):
    
        if dose_calculada > dosagem_maxima:
            return (f"\n⚠️  ALERTA: A dose calculada excede a dose máxima do perfil médico!\n"
                    f"Dose calculada: {dose_calculada} unidades\n"
                    f"Dose máxima permitida: {dosagem_maxima} unidades\n"
                    "Consulte seu médico ou profissional de saúde antes de administrar essa dose.\n")
            
        else:
            return ("\n✅ A dose calculada está dentro dos limites seguros.\n")


