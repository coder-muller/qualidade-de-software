# Aula 9 - Testes unitarios automatizados e TDD do Local Eats

> Disciplina: Qualidade de Software  
> Estudo de caso: Local Eats  
> PBL 6 - Entrega 2

---

## Integrantes

- Guilherme Coelho Muller
- Arthur Ortiz Fonseca
- Joao Pedro da Silva Caldeira

---

## 1. Estrutura do projeto

```
.
├── src/
│   ├── pedido.py
│   ├── desconto.py
│   └── entrega.py
└── tests/
    └── unit/
        ├── test_pedido.py
        ├── test_desconto.py
        └── test_entrega.py
```

---

## 2. Funcionalidades escolhidas

Cada integrante ficou responsavel por uma regra de negocio do dominio Local Eats.

### Guilherme Coelho Muller - Calculo do total do pedido

**Arquivo:** `src/pedido.py`  
**Testes:** `tests/unit/test_pedido.py`

Soma os valores dos itens e valida se o pedido atinge o valor minimo exigido.

**Regras de negocio:**

- a soma dos itens define o total
- pedido abaixo do valor minimo gera erro
- lista vazia, preco ausente ou negativo geram erro

### Arthur Ortiz Fonseca - Aplicacao de desconto percentual

**Arquivo:** `src/desconto.py`  
**Testes:** `tests/unit/test_desconto.py`

Aplica desconto percentual sobre o valor total do pedido.

**Regras de negocio:**

- percentual deve estar entre 0 e 100
- valor final nao pode ser negativo

### Joao Pedro da Silva Caldeira - Calculo de taxa de entrega

**Arquivo:** `src/entrega.py`  
**Testes:** `tests/unit/test_entrega.py`

Calcula a taxa de entrega com base na distancia em quilometros.

**Regras de negocio:**

- ate 3 km: taxa fixa de R$ 5,00
- acima de 3 km: taxa fixa + R$ 2,00 por km adicional
- distancia negativa gera erro

---

## 3. Testes unitarios e ciclo TDD

### Guilherme - Pedido

#### Teste 1 - Total valido acima do minimo

- **Cenario:** pedido com dois itens somando R$ 35,00 e minimo de R$ 30,00
- **Resultado esperado:** retorna 35.0

**TDD:**

- **Red:** teste criado antes da implementacao; falhou por funcao inexistente
- **Green:** implementacao minima com soma dos precos
- **Refactor:** inclusao de validacao de valor minimo

**Execucao:** passou

#### Teste 2 - Total abaixo do minimo

- **Cenario:** pedido de R$ 5,00 com minimo de R$ 20,00
- **Resultado esperado:** `ValueError`

**TDD:**

- **Red:** teste esperando excecao
- **Green:** validacao do valor minimo adicionada
- **Refactor:** mensagem de erro explicita

**Execucao:** passou

#### Testes complementares

- lista vazia: passou
- preco negativo: passou
- item sem preco: passou

### Arthur - Desconto

#### Teste 1 - Desconto parcial de 50%

- **Cenario:** valor de R$ 100,00 com 50% de desconto
- **Resultado esperado:** R$ 50,00

**TDD:**

- **Red:** teste falhou sem funcao implementada
- **Green:** calculo percentual basico
- **Refactor:** arredondamento e validacao de limites

**Execucao:** passou

#### Teste 2 - Percentual acima de 100%

- **Cenario:** desconto de 110%
- **Resultado esperado:** `ValueError`

**TDD:**

- **Red:** teste de entrada invalida
- **Green:** validacao de faixa do percentual
- **Refactor:** mensagem padronizada de erro

**Execucao:** passou

#### Testes complementares

- sem desconto (0%): passou
- desconto total (100%): passou
- percentual negativo: passou

### Joao Pedro - Entrega

#### Teste 1 - Distancia de 2 km

- **Cenario:** entrega a 2 km
- **Resultado esperado:** taxa fixa de R$ 5,00

**TDD:**

- **Red:** teste sem implementacao
- **Green:** retorno fixo para distancias curtas
- **Refactor:** constantes nomeadas para taxas

**Execucao:** passou

#### Teste 2 - Distancia negativa

- **Cenario:** distancia de -1 km
- **Resultado esperado:** `ValueError`

**TDD:**

- **Red:** teste de validacao de entrada
- **Green:** verificacao de distancia negativa
- **Refactor:** regra condicional para km adicionais mantida

**Execucao:** passou

#### Testes complementares

- exatamente 3 km (limite da taxa fixa): passou
- 5 km com adicional: passou

---

## 4. Execucao dos testes

Comando:

```bash
pytest tests/unit/ -v
```

Resultado:

```
============================= test session starts ==============================
platform darwin -- Python 3.14.3, pytest-9.0.3, pluggy-1.6.0
collected 14 items

tests/unit/test_desconto.py::test_sem_desconto PASSED
tests/unit/test_desconto.py::test_desconto_parcial PASSED
tests/unit/test_desconto.py::test_desconto_total PASSED
tests/unit/test_desconto.py::test_percentual_acima_de_cem_deve_falhar PASSED
tests/unit/test_desconto.py::test_percentual_negativo_deve_falhar PASSED
tests/unit/test_entrega.py::test_distancia_ate_tres_km_taxa_fixa PASSED
tests/unit/test_entrega.py::test_distancia_exatamente_tres_km_taxa_fixa PASSED
tests/unit/test_entrega.py::test_distancia_acima_de_tres_km_com_adicional PASSED
tests/unit/test_entrega.py::test_distancia_negativa_deve_falhar PASSED
tests/unit/test_pedido.py::test_total_valido_acima_do_minimo PASSED
tests/unit/test_pedido.py::test_total_abaixo_do_minimo_deve_falhar PASSED
tests/unit/test_pedido.py::test_lista_vazia_deve_falhar PASSED
tests/unit/test_pedido.py::test_preco_negativo_deve_falhar PASSED
tests/unit/test_pedido.py::test_item_sem_preco_deve_falhar PASSED

============================== 14 passed in 0.02s ==============================
```

---

## 5. Reflexao

### Foi dificil escrever testes antes do codigo?

Sim, no inicio. O TDD exige pensar no comportamento esperado antes da implementacao, o que muda o habito de codificar primeiro e testar depois.

### O TDD ajudou no desenvolvimento?

Sim. Os testes guiaram a implementacao e evitaram regras incompletas, especialmente nas validacoes de entrada invalida.

### Os testes aumentaram a confianca no codigo?

Sim. Qualquer alteracao nas regras de negocio pode ser verificada rapidamente com a suite de 14 testes.

### O que melhorariam?

- cobrir mais cenarios de borda, como valores decimais com muitas casas
- agrupar constantes de negocio em um modulo de configuracao compartilhado

### Como isso ajuda no projeto Local Eats?

Permite evoluir regras de pedido, desconto e entrega com mais seguranca, reduzindo o risco de regressao em funcionalidades centrais do sistema.
