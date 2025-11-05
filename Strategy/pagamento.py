from abc import ABC, abstractmethod  # corrigido de abstracmethod

class EstrategiaPagamento(ABC):
    @abstractmethod  # corrigido de abstracmethod
    def processar_pagamento(self, valor_final: float) -> bool:  # corrigido signature
        pass

class PagamentoCredito(EstrategiaPagamento):  # corrigido nome da classe (PascalCase)
    def processar_pagamento(self, valor_final: float) -> bool:
        print(f"Processando R${valor_final:.2f} via Cartão de Crédito...")
        if valor_final < 1000:
            print("   -> Pagamento com Credito APROVADO.")
            return True
        else:
            print("   -> Pagamento com Credito REJEITADO (limite excedido).")
            return False

class PagamentoPix(EstrategiaPagamento):
    def processar_pagamento(self, valor_final: float) -> bool:
        print(f"Processando R${valor_final:.2f} via PIX...")
        print("   -> Pagamento com PIX APROVADO (QR Code gerado).")
        return True

class PagamentoMana(EstrategiaPagamento):
    def processar_pagamento(self, valor_final: float) -> bool:
        print(f"Processando R${valor_final:.2f} via Transferência de Mana...")
        print("   -> Pagamento com Mana APROVADO (requer 10 segundos de espera).")
        return True

# Classe contexto que utiliza as estratégias
class Pagamento:
    def __init__(self, estrategia: EstrategiaPagamento = None):
        self.estrategia = estrategia

    def set_estrategia(self, estrategia: EstrategiaPagamento):
        self.estrategia = estrategia

    def processar(self, valor_final: float) -> bool:
        if not self.estrategia:
            raise ValueError("Estratégia de pagamento não definida")
        return self.estrategia.processar_pagamento(valor_final)

# Dicionário com as estratégias disponíveis
ESTRATEGIAS_PAGAMENTO = {
    "Credito": PagamentoCredito,
    "Pix": PagamentoPix,
    "Mana": PagamentoMana
}