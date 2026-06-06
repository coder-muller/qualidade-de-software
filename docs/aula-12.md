# Aula 12 - BDD e automacao orientada a comportamento do Local Eats

> Disciplina: Qualidade de Software  
> Estudo de caso: Local Eats  
> PBL 8 - Entrega 2

---

## Integrantes

- Guilherme Coelho Muller
- Arthur Ortiz Fonseca
- Joao Pedro da Silva Caldeira

---

## 1. Fluxos escolhidos

### Guilherme Coelho Muller - Historico de pedidos

Validar se os pedidos realizados pelo usuario sao exibidos corretamente na pagina de transacoes.

### Arthur Ortiz Fonseca / Joao Pedro da Silva Caldeira - Perfil do usuario

Validar o acesso ao perfil autenticado e a exibicao da secao de restaurantes favoritos.

---

## 2. Cenarios BDD

### Historico de pedidos

Arquivo: [`features/historico_pedidos.feature`](../features/historico_pedidos.feature)

```gherkin
Funcionalidade: Historico de pedidos
  Como usuario autenticado do Local Eats
  Quero visualizar meus pedidos anteriores
  Para acompanhar o historico de transacoes

  Cenario: Visualizar pedidos realizados
    Dado que o usuario esta autenticado no sistema
    Quando acessa a pagina de pedidos
    Entao o sistema deve exibir o historico de transacoes

  Cenario: Validar valor total do pedido
    Dado que o usuario esta autenticado no sistema
    Quando visualiza um pedido realizado
    Entao o sistema deve exibir o valor total do pedido
```

### Perfil do usuario

Arquivo: [`features/perfil_usuario.feature`](../features/perfil_usuario.feature)

```gherkin
Funcionalidade: Perfil do usuario
  Como usuario autenticado do Local Eats
  Quero acessar meu perfil
  Para visualizar meus dados e favoritos

  Cenario: Acessar pagina de perfil
    Dado que o usuario esta autenticado no sistema
    Quando acessa a pagina de perfil
    Entao o sistema deve exibir o nome do usuario

  Cenario: Visualizar secao de favoritos
    Dado que o usuario esta autenticado no sistema
    Quando acessa a pagina de perfil
    Entao o sistema deve exibir a secao de restaurantes favoritos
```

---

## 3. Automacao com pytest-bdd

### Estrutura

```
features/
├── historico_pedidos.feature
└── perfil_usuario.feature
tests/bdd/
├── steps_comuns.py
├── test_historico_pedidos.py
└── test_perfil_usuario.py
pages/
├── orders_page.py
└── profile_page.py
```

### Step definitions compartilhados

O passo de autenticacao foi centralizado em [`tests/bdd/steps_comuns.py`](../tests/bdd/steps_comuns.py) para evitar duplicacao entre features:

```python
@given("que o usuario esta autenticado no sistema")
def usuario_autenticado_no_sistema(page, credenciais):
    login = LoginPage(page)
    login.acessar()
    login.realizar_login(credenciais["email"], credenciais["password"])
    assert login.usuario_logado()
```

### Vinculo entre linguagem natural e codigo

- os cenarios em Gherkin descrevem o comportamento esperado em portugues
- os step definitions traduzem cada passo em acoes Playwright reutilizando Page Objects
- a separacao permite que mudancas de interface afetem apenas `pages/` e os steps, nao os cenarios

---

## 4. Execucao dos testes

### Comando

```bash
pytest tests/bdd/ -v --browser chromium
```

### Resultado

- total de cenarios: 4
- passaram: 4
- falharam: 0
- tempo: ~11s

```
tests/bdd/test_historico_pedidos.py::test_visualizar_pedidos_realizados PASSED
tests/bdd/test_historico_pedidos.py::test_validar_valor_total_do_pedido PASSED
tests/bdd/test_perfil_usuario.py::test_acessar_pagina_de_perfil PASSED
tests/bdd/test_perfil_usuario.py::test_visualizar_secao_de_favoritos PASSED

============================== 4 passed in 11.42s ==============================
```

### Evidencias

- log de execucao: [`artefatos/evidencias/pbl8-execucao-bdd.log`](../artefatos/evidencias/pbl8-execucao-bdd.log)
- screenshot da pagina de pedidos: [`artefatos/evidencias/pbl8-pagina-pedidos.png`](../artefatos/evidencias/pbl8-pagina-pedidos.png)

---

## 5. Reflexao

### O BDD melhorou a comunicacao entre requisito e teste?

Sim. Os cenarios em Gherkin deixam explicito o comportamento esperado sem detalhes de implementacao, o que aproxima PO, QA e desenvolvimento.

### A automacao ficou mais legivel que os testes e2e puros?

Em parte. A legibilidade dos cenarios melhorou, mas os step definitions ainda exigem manutencao tecnica quando a interface muda.

### O que melhorariam?

- reduzir passos duplicados entre features com um modulo de steps mais amplo
- adicionar tags (`@smoke`, `@pedidos`) para execucao seletiva
- preparar massa de dados com pedidos garantidos para o cenario de valor total

### Como o BDD contribui para o Local Eats?

Ajuda a documentar e validar fluxos de confianca do usuario (pedidos e perfil) de forma que qualquer integrante do grupo entenda o que esta sendo testado antes de ler o codigo.

---

## Conclusao

O BDD complementou os testes unitarios e funcionais ao colocar o comportamento do usuario no centro da automacao. Para o Local Eats, isso e especialmente util em fluxos que dependem de autenticacao e persistencia de dados.
