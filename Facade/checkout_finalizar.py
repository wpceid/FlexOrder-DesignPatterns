from dataclasses import dataclass
from typing import List, Dict, Any

# === Subsistemas ===
class SistemaEstoque:
    def registrar_saida(self, itens: List[Dict[str, Any]]) -> bool:
        print("\nRegistrando saída no estoque...")
        for item in itens:
            print(f"- {item['nome']}: Registrado")
        return True

class GeradorNotaFiscal:
    def emitir_nf(self, dados_pedido: Dict[str, Any]) -> str:
        print("\nGerando nota fiscal...")
        return "NF-e 123456789"

class RegistroTransacao:
    def salvar(self, dados_pedido: Dict[str, Any], status: str) -> bool:
        print(f"\nRegistrando transação - Status: {status}")
        return True

# === Data Classes ===
@dataclass
class DadosPedido:
    itens: List[Dict[str, Any]]
    metodo_pagamento: str
    tipo_frete: str
    tem_embalagem_presente: bool = False

# === Facade ===
class CheckoutFacade:
    def __init__(self):
        self.estoque = SistemaEstoque()
        self.nota_fiscal = GeradorNotaFiscal()
        self.registro = RegistroTransacao()

    def processar_checkout(self, pedido: DadosPedido) -> bool:
        """Interface simplificada para todo o processo de checkout"""
        print("\n=== Iniciando Checkout Modernizado ===")
        
        try:
            # 1. Validação inicial
            if not self._validar_pedido(pedido):
                return False

            # 2. Cálculo de valores
            valor_final = self._calcular_valor_final(pedido)
            
            # 3. Processamento principal
            if self._processar_pagamento(pedido.metodo_pagamento, valor_final):
                # 4. Processos auxiliares
                self.estoque.registrar_saida(pedido.itens)
                self.nota_fiscal.emitir_nf(vars(pedido))
                self.registro.salvar(vars(pedido), "CONCLUIDO")
                
                print("\n=== Checkout Finalizado com Sucesso ===")
                print(f"Valor Final: R${valor_final:.2f}")
                return True
            
            return False

        except Exception as e:
            print(f"\nErro no checkout: {str(e)}")
            self.registro.salvar(vars(pedido), "ERRO")
            return False

    def _validar_pedido(self, pedido: DadosPedido) -> bool:
        """Validação básica dos dados do pedido"""
        return len(pedido.itens) > 0

    def _calcular_valor_final(self, pedido: DadosPedido) -> float:
        """Calcula o valor final considerando descontos e taxas"""
        valor_base = sum(item['valor'] for item in pedido.itens)
        print(f"\nValor base: R${valor_base:.2f}")
        
        # Cálculo do desconto
        valor_com_desconto = self._aplicar_desconto(valor_base, pedido)
        
        # Cálculo do frete
        valor_frete = self._calcular_frete(valor_com_desconto, pedido.tipo_frete)
        
        # Taxa de embalagem
        valor_final = valor_com_desconto + valor_frete
        if pedido.tem_embalagem_presente:
            valor_final += 5.00
            print("Taxa de embalagem presente: R$5.00")
            
        return valor_final

    def _aplicar_desconto(self, valor_base: float, pedido: DadosPedido) -> float:
        """Aplica descontos conforme regras de negócio"""
        if pedido.metodo_pagamento == 'Pix':
            desconto = valor_base * 0.05
            print(f"Desconto PIX (5%): R${desconto:.2f}")
            return valor_base - desconto
        elif valor_base > 500:
            desconto = valor_base * 0.10
            print(f"Desconto pedido grande (10%): R${desconto:.2f}")
            return valor_base - desconto
        return valor_base

    def _calcular_frete(self, valor: float, tipo_frete: str) -> float:
        """Calcula o frete baseado no tipo selecionado"""
        if tipo_frete == 'Normal':
            frete = valor * 0.05
        elif tipo_frete == 'Expresso':
            frete = valor * 0.10 + 15.00
        else:  # Teletransporte
            frete = 50.00
        
        print(f"Frete {tipo_frete}: R${frete:.2f}")
        return frete

    def _processar_pagamento(self, metodo: str, valor: float) -> bool:
        """Processa o pagamento usando o método selecionado"""
        print(f"\nProcessando pagamento via {metodo}")
        print(f"Valor: R${valor:.2f}")
        
        if metodo == 'Credito' and valor >= 1000:
            print("Pagamento rejeitado: Limite excedido")
            return False
            
        print("Pagamento aprovado!")
        return True

# === Exemplo de Uso ===
def main():
    # Exemplo 1: Pedido simples com PIX
    pedido1 = DadosPedido(
        itens=[
            {'nome': 'Capa da Invisibilidade', 'valor': 150.0},
            {'nome': 'Poção de Voo', 'valor': 80.0}
        ],
        metodo_pagamento='Pix',
        tipo_frete='Normal'
    )

    # Exemplo 2: Pedido grande com presente
    pedido2 = DadosPedido(
        itens=[{'nome': 'Cristal Mágico', 'valor': 600.0}],
        metodo_pagamento='Credito',
        tipo_frete='Expresso',
        tem_embalagem_presente=True
    )

    # Processando os pedidos
    checkout = CheckoutFacade()
    
    print("\nProcessando Pedido 1:")
    checkout.processar_checkout(pedido1)
    
    print("\nProcessando Pedido 2:")
    checkout.processar_checkout(pedido2)

if __name__ == "__main__":
    main()