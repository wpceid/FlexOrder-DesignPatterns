from abc import ABC, abstractmethod

################################# ESTRATÉGIA #################################  
class EstrategiaFrete(ABC):
    @abstractmethod
    def calcula_frete (self, valor_com_desconto):
        pass
    
class FreteNormal(EstrategiaFrete):
    def calcula_frete (self, valor_com_desconto):
        custo_frete = valor_com_desconto * 0.05
        print(f"Frete Normal: R${custo_frete:.2f}")
        return custo_frete  
        
class FreteExpresso(EstrategiaFrete):
    def calcula_frete (self, valor_com_desconto):
        custo_frete = valor_com_desconto * 0.10 + 15.00  # Taxa extra
        print(f"Frete Expresso (com taxa): R${custo_frete:.2f}")
        return custo_frete
        
class FreteTeletransporte(EstrategiaFrete):
    def calcula_frete(self, valor_com_desconto):
        custo_frete = 50.00
        print(f"Frete Teletransporte: R${custo_frete:.2f}")
        return custo_frete

################################# CONTEXTO ################################# 
class CalculadoraFrete:
    def __init__(self, estrategia: EstrategiaFrete = None):
        self.estrategia = estrategia

    def set_estrategia(self, estrategia: EstrategiaFrete):
        self.estrategia = estrategia

    def calcular(self, valor_com_desconto):
        if not self.estrategia:
            raise ValueError("Estratégia de frete não definida")
        return self.estrategia.calcula_frete(valor_com_desconto)

################################# ESTRATÉGIAS #################################         
ESTRATEGIAS_FRETE = {
    "NORMAL": FreteNormal,
    "EXPRESSO": FreteExpresso,
    "TELETRANSPORTE": FreteTeletransporte
}

################################# "USANDO" A CLASSE REFATORADA ################################# 
def main():

    valor = 200.0
    calculadora = CalculadoraFrete()

    for nome, estrategia in ESTRATEGIAS_FRETE.items():
        calculadora.set_estrategia(estrategia())
        custo = calculadora.calcular(valor)
        print(f"Custo total com {nome}: R${custo:.2f}\n")

if __name__ == "__main__":
    main()