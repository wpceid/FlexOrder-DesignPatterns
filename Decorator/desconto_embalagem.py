from abc import ABC, abstractmethod

# Componente Base (Interface)
class Pedido(ABC):
    @abstractmethod
    def calcular_valor(self) -> float:
        pass

# Componente Concreto
class PedidoBase(Pedido):
    def __init__(self, itens: list):
        self.itens = itens

    def calcular_valor(self) -> float:
        valor_base = sum(item['valor'] for item in self.itens)
        print(f"Valor base do pedido: R${valor_base:.2f}")
        return valor_base

# Decorator Base
class PedidoDecorator(Pedido):
    def __init__(self, pedido: Pedido):
        self._pedido = pedido

    def calcular_valor(self) -> float:
        return self._pedido.calcular_valor()

# Decorators Concretos
class DescontoPix(PedidoDecorator):
    def calcular_valor(self) -> float:
        valor_original = super().calcular_valor()
        desconto = valor_original * 0.05
        print(f"Aplicando desconto PIX de R${desconto:.2f}")
        return valor_original - desconto

class DescontoPedidoGrande(PedidoDecorator):
    def calcular_valor(self) -> float:
        valor_original = super().calcular_valor()
        if valor_original > 500:
            desconto = valor_original * 0.10
            print(f"Aplicando desconto pedido grande de R${desconto:.2f}")
            return valor_original - desconto
        return valor_original

class TaxaEmbalagemPresente(PedidoDecorator):
    def calcular_valor(self) -> float:
        valor_original = super().calcular_valor()
        taxa = 5.00
        print(f"Adicionando taxa de embalagem presente: R${taxa:.2f}")
        return valor_original + taxa