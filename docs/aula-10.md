# Aula 10 - Testes funcionais automatizados do Local Eats

> Disciplina: Qualidade de Software  
> Estudo de caso: Local Eats  
> PBL 7 - Entrega 2

---

## Integrantes

- Guilherme Coelho Muller
- Arthur Ortiz Fonseca
- Joao Pedro da Silva Caldeira

---

## 1. Fluxo funcional escolhido

### Login de usuario

Permite autenticar um usuario no sistema e liberar o acesso aos fluxos protegidos.

**Importancia:** sem login, busca personalizada, favoritos e pedidos nao podem ser validados de forma confiavel.

### Busca e filtro de restaurantes

Complementa o fluxo de login com validacao da funcionalidade mais critica identificada na aula 6: descoberta de restaurantes por termo e por culinaria.

---

## 2. Teste com Codegen

### Comando utilizado

```bash
playwright codegen https://local-eats-unisenac.vercel.app/static/login.html
playwright codegen https://local-eats-unisenac.vercel.app/static/index.html
```

### Codigo gerado

- [`codegen/codegen_login.py`](../codegen/codegen_login.py)
- [`codegen/codegen_busca.py`](../codegen/codegen_busca.py)

### Observacoes

- o Codegen acelerou o primeiro rascunho dos seletores
- o codigo inicial ficou acoplado a placeholders e cliques redundantes
- foi necessario refatorar para IDs estaveis (`#loginEmail`, `#searchInput`, `.rest-card`)

---

## 3. Teste automatizado com Pytest

### Arquivos

- [`tests/e2e/test_login.py`](../tests/e2e/test_login.py)
- [`tests/e2e/test_busca_restaurantes.py`](../tests/e2e/test_busca_restaurantes.py)

### O que os testes fazem

**Login**

- acessa a tela de login
- preenche email e senha
- valida redirecionamento para `index.html`

**Busca**

- autentica o usuario
- busca por termo "Sabor" e valida retorno de cards
- aplica filtro "Italiana" e valida presenca da culinaria na listagem

### Credenciais

As credenciais sao lidas de variaveis de ambiente (`LOCAL_EATS_EMAIL`, `LOCAL_EATS_PASSWORD`). O arquivo [`.env.example`](../.env.example) documenta os valores padrao do seed do sistema.

---

## 4. Refatoracao com Page Object Model (POM)

### Page Objects

- [`pages/login_page.py`](../pages/login_page.py)
- [`pages/home_page.py`](../pages/home_page.py)

### Melhorias realizadas

- separacao entre teste e interacao com a interface
- reutilizacao do fluxo de login nos cenarios de busca
- seletores centralizados por pagina, facilitando manutencao

---

## 5. Execucao dos testes

### Comando

```bash
pytest tests/e2e/ -v --browser chromium
```

### Resultado

- total de testes: 3
- testes passaram: 3
- testes falharam: 0
- tempo: ~10s

```
tests/e2e/test_busca_restaurantes.py::test_busca_por_termo_retorna_restaurantes PASSED
tests/e2e/test_busca_restaurantes.py::test_filtro_por_culinaria_italiana PASSED
tests/e2e/test_login.py::test_login_com_credenciais_validas PASSED

============================== 3 passed in 10.43s ==============================
```

### Evidencias

- log de execucao: [`artefatos/evidencias/pbl7-execucao-pytest.log`](../artefatos/evidencias/pbl7-execucao-pytest.log)
- screenshot da pagina logada: [`artefatos/evidencias/pbl7-pagina-logada.png`](../artefatos/evidencias/pbl7-pagina-logada.png)

---

## 6. Analise critica

- os testes dependem do ambiente publico em Vercel e da disponibilidade da API
- seletores por texto de culinaria podem quebrar se o cardapio de dados mudar
- o primeiro rascunho do Codegen usava classe CSS incorreta (`.restaurant-card`); a classe real e `.rest-card`
- credenciais nao devem ser versionadas no repositorio

---

## 7. Reflexao

Testes automatizados nao substituem a exploracao manual, mas aumentam a confianca em fluxos criticos como login e busca. A refatoracao para POM mostrou que automacao sustentavel exige organizacao desde o inicio, nao apenas gravar scripts.

---

## Conclusao

A automacao funcional do Local Eats permitiu repetir cenarios da aula 6 com mais velocidade e rastreabilidade. O proximo passo natural e ampliar a cobertura para favoritos e pedidos, areas ainda sensiveis no produto.
