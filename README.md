# FlexOrder-DesignPatterns

## Arquitetura Orientada a Objetos

O sistema FlexOrder foi refatorado utilizando padrões de projeto (Design Patterns) para resolver problemas específicos do código legado e melhorar sua manutenibilidade, extensibilidade e organização.

### Padrões Implementados

#### 1. Strategy Pattern (Comportamental)

- **Problema Resolvido**: Código com múltiplos if/else para diferentes tipos de pagamento e frete
- **Solução**:
  - Criação de interfaces `EstrategiaPagamento` e `EstrategiaFrete`
  - Implementações específicas para cada tipo (ex: `PagamentoCredito`, `FreteExpresso`)
  - Eliminação de violações SRP separando as responsabilidades
  - Permite adicionar novos métodos sem modificar código existente (OCP)

#### 2. Decorator Pattern (Estrutural)

- **Problema Resolvido**: Lógica de descontos e taxas adicionais misturada
- **Solução**:
  - Interface base `Pedido` com decoradores
  - Decoradores específicos (`DescontoPix`, `TaxaEmbalagemPresente`)
  - Cada modificador de preço em sua própria classe (SRP)
  - Combinação flexível de modificadores sem alterar classes (OCP)

#### 3. Facade Pattern (Estrutural)

- **Problema Resolvido**: Complexidade do processo de checkout
- **Solução**:
  - Classe `CheckoutFacade` que simplifica a interface
  - Subsistemas independentes (`SistemaEstoque`, `GeradorNotaFiscal`)
  - Separação clara de responsabilidades (SRP)
  - Encapsulamento da complexidade

### Benefícios da Nova Arquitetura

1. **Manutenibilidade**

   - Código mais organizado e modular
   - Responsabilidades bem definidas
   - Fácil identificação e correção de problemas

2. **Extensibilidade**

   - Novos tipos de pagamento/frete sem modificar código existente
   - Decoradores podem ser combinados livremente
   - Subsistemas podem evoluir independentemente

3. **Testabilidade**
   - Classes menores e focadas
   - Interfaces bem definidas
   - Fácil mockar componentes

### Correções de Princípios SOLID

1. **Single Responsibility Principle (SRP)**

   - Antes: Método `finalizar_compra()` fazia tudo
   - Depois: Responsabilidades distribuídas em classes específicas

2. **Open/Closed Principle (OCP)**
   - Antes: Modificações necessárias para novos tipos
   - Depois: Extensão através de novas classes sem modificar existentes

### Estrutura do Projeto

```
FlexOrder-DesignPatterns/
├── Strategy/
│   ├── pagamento.py
│   └── frete.py
├── Decorator/
│   └── desconto_embalagem.py
├── Facade/
│   └── checkout_finalizar.py
└── README.md
```

### Como Executar

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/FlexOrder-DesignPatterns.git

# Entre no diretório
cd FlexOrder-DesignPatterns

# Execute o exemplo principal
python Facade/checkout_finalizar.py
```

### Requisitos

- Python 3.7+
- Não são necessárias dependências externas
