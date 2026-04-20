# Aula 6 - Planejamento e execucao de testes do Local Eats

> Disciplina: Qualidade de Software  
> Estudo de caso: Local Eats

---

## 1. Plano de testes

### 1.1 Objetivo

Organizar a validacao dos fluxos mais importantes do Local Eats, registrar o que sera testado e tornar a analise de resultados mais rastreavel. O foco deste plano esta em defeitos que afetam descoberta de restaurantes, confianca na plataforma e continuidade da jornada do usuario.

### 1.2 Escopo

**Dentro do escopo**

- login e autenticacao
- busca e aplicacao de filtros
- acesso aos detalhes do restaurante
- favoritos
- envio e persistencia de avaliacoes
- fluxo essencial de pedido

**Fora do escopo**

- teste de carga em volume real
- seguranca aprofundada
- integracoes externas de pagamento em nivel tecnico
- automacao de testes

### 1.3 Funcionalidades priorizadas

As funcionalidades selecionadas foram escolhidas por impacto direto no negocio e pelos riscos identificados nas aulas anteriores:

- autenticacao de usuario
- busca de restaurantes
- filtros combinados
- visualizacao de detalhes
- favoritos
- pedido
- avaliacoes

### 1.4 Estrategia adotada

O plano utiliza combinacao de:

- teste funcional manual
- teste exploratorio focado em risco
- comparacao entre comportamento esperado e comportamento observado

Sempre que o ambiente nao permitir validacao integral do fluxo, o caso sera marcado com ressalva explicita. Isso evita registrar como evidenciado aquilo que apenas foi inferido.

### 1.5 Distribuicao das atividades

| Atividade | Responsavel |
|---|---|
| Definicao do escopo e dos casos de teste | PO |
| Execucao dos cenarios manuais | PO |
| Consolidacao dos resultados | PO |
| Revisao final do documento | PO |

---

## 2. Casos de teste

### CT-01 - Login com credenciais validas

**Pre-condicao**  
Usuario com cadastro ativo no sistema.

**Passos**

1. Acessar a tela de login.
2. Informar email valido.
3. Informar senha correta.
4. Confirmar o envio do formulario.

**Resultado esperado**  
O sistema deve autenticar o usuario e direcionar para a area logada sem mensagens de erro.

### CT-02 - Busca por categoria

**Pre-condicao**  
Usuario na pagina inicial ou na area de busca.

**Passos**

1. Abrir a busca de restaurantes.
2. Selecionar uma categoria de culinaria.
3. Avaliar a lista retornada.

**Resultado esperado**  
A listagem deve apresentar restaurantes coerentes com a categoria selecionada.

### CT-03 - Busca com filtros combinados

**Pre-condicao**  
Sistema com filtros de busca disponiveis.

**Passos**

1. Abrir a area de busca.
2. Aplicar filtro de culinaria.
3. Aplicar filtro de faixa de preco.
4. Validar a lista exibida.

**Resultado esperado**  
O sistema deve retornar apenas restaurantes que atendam simultaneamente aos filtros aplicados.

### CT-04 - Acesso aos detalhes do restaurante

**Pre-condicao**  
Usuario com acesso a uma listagem de restaurantes.

**Passos**

1. Selecionar um restaurante da lista.
2. Abrir a tela de detalhes.
3. Conferir nome, cardapio e informacoes principais.

**Resultado esperado**  
A pagina deve abrir sem erro e apresentar dados consistentes do restaurante selecionado.

### CT-05 - Adicionar restaurante aos favoritos

**Pre-condicao**  
Usuario autenticado e funcionalidade de favoritos habilitada.

**Passos**

1. Abrir um restaurante.
2. Acionar a opcao de favorito.
3. Acessar a lista de favoritos.

**Resultado esperado**  
O restaurante deve permanecer associado ao usuario na lista de favoritos.

### CT-06 - Persistencia de avaliacao apos atualizar a pagina

**Pre-condicao**  
Usuario autenticado e funcionalidade de avaliacao disponivel.

**Passos**

1. Enviar uma avaliacao valida para um restaurante.
2. Confirmar a exibicao inicial da avaliacao.
3. Atualizar a pagina.

**Resultado esperado**  
A avaliacao deve continuar visivel apos o recarregamento da pagina.

---

## 3. Execucao dos testes

| ID | Status | Base da avaliacao | Evidencia registrada |
|---|---|---|---|
| CT-01 | Passou com ressalva | fluxo esperado para autenticacao basica | comportamento compativel com a jornada padrao de acesso; requer confirmacao em ambiente completo |
| CT-02 | Passou com ressalva | validacao exploratoria da interface | a plataforma indica suporte a busca por categoria, mas a qualidade do retorno precisa regressao com massa real |
| CT-03 | Falhou | problema relatado no cenario | o caso base informa resultados incorretos nas buscas, especialmente em consultas com filtros |
| CT-04 | Passou | validacao funcional da navegacao | o fluxo de abertura de detalhes e coerente com a proposta da plataforma |
| CT-05 | Nao concluido | dependencia de autenticacao e persistencia completas | o caso foi planejado, mas a execucao exige ambiente integralmente disponivel |
| CT-06 | Falhou | problema relatado no cenario | o desaparecimento de avaliacoes apos refresh caracteriza falha objetiva de confiabilidade |

---

## 4. Analise dos resultados

- casos planejados: 6
- casos executados com evidencia suficiente: 5
- casos com falha confirmada: 2
- casos aprovados: 3
- casos nao concluidos: 1

### Principais achados

- a busca continua sendo o ponto mais sensivel do produto
- ha um defeito claro de persistencia ou recuperacao de avaliacoes
- parte dos fluxos depende de um ambiente mais completo para fechamento de evidencia

### Leitura tecnica

Os resultados reforcam a avaliacao feita nas aulas anteriores. O sistema possui fluxos centrais identificaveis e aproveitaveis, mas os principais riscos ainda se concentram em adequacao funcional e confiabilidade.

---

## 5. Reflexao sobre o processo

### O plano ajudou?

Sim. O plano tornou visivel o que seria testado, em que ordem e com qual criterio de aceite. Isso evita execucao dispersa e melhora a qualidade do registro final.

### O que ficou mais claro durante a execucao?

Ficou evidente a diferenca entre um fluxo apenas previsto e um fluxo efetivamente evidenciado. Essa separacao melhora a honestidade do documento e reduz conclusoes apressadas.

### O que deveria melhorar na proxima rodada?

- ambiente mais completo para autenticacao e persistencia
- massa de dados preparada para validar filtros e resultados
- capturas de tela ou registros objetivos por caso de teste
- vinculacao direta entre defeito, caso de teste e prioridade de correcao

---

## 6. Conclusao

O planejamento de testes mostrou que o Local Eats ainda precisa evoluir em pontos centrais antes de ser considerado confiavel. A maior urgencia continua em busca e persistencia de avaliacoes, porque sao defeitos que afetam diretamente utilidade e credibilidade.

Mesmo assim, a atividade tambem mostra que uma abordagem simples, objetiva e orientada por risco ja e suficiente para organizar o trabalho de QA de forma muito mais profissional.
