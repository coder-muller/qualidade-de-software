# Aula 5 - Testes funcionais e estruturais no Local Eats

> Disciplina: Qualidade de Software  
> Estudo de caso: Local Eats

---

## 1. Funcionalidade escolhida

### Busca e filtragem de restaurantes

Essa funcionalidade permite localizar restaurantes por termo digitado e por filtros como culinaria, preco e localizacao. Ela e central para o produto porque conecta a necessidade do usuario ao conteudo disponivel na plataforma.

### O que o usuario espera

Do ponto de vista de uso, a expectativa e simples:

- receber resultados coerentes com o criterio informado
- combinar filtros sem comportamento contraditorio
- obter retorno rapido e previsivel
- entender claramente quando nao houver resultados

---

## 2. Testes funcionais (caixa-preta)

Nos testes funcionais, a avaliacao e feita apenas pelo comportamento visivel do sistema. O codigo nao entra na analise; importa apenas o que o usuario informa e o que o sistema devolve.

### Cenarios recomendados

| ID | Cenario | Resultado esperado |
|---|---|---|
| CP-01 | buscar por uma culinaria especifica | listar apenas restaurantes compativeis com a culinaria selecionada |
| CP-02 | buscar por termo parcial em letras minusculas | retornar resultados relevantes mesmo com variacoes de escrita |
| CP-03 | combinar filtros de culinaria e faixa de preco | considerar os dois filtros ao mesmo tempo |
| CP-04 | remover filtros apos uma busca refinada | atualizar a listagem de acordo com o novo estado |
| CP-05 | pesquisar um termo sem correspondencia | exibir mensagem clara de ausencia de resultados |

### Defeitos que essa abordagem ajuda a encontrar

- restaurantes fora do criterio retornado
- filtros ignorados parcial ou totalmente
- ausencia de resultados validos quando ha dados compativeis
- mensagens confusas em situacoes de lista vazia
- lentidao perceptivel no uso normal

### Por que caixa-preta e importante aqui

O proprio problema norteador informa que a busca retorna resultados incorretos. Portanto, a primeira pergunta a responder e objetiva: o usuario encontra ou nao encontra o que procura?

---

## 3. Testes estruturais (caixa-branca)

Nos testes estruturais, o foco muda da experiencia percebida para a logica interna. A ideia e verificar como o sistema trata condicoes, caminhos e combinacoes de dados.

### Fluxo logico esperado

```text
receber termo de busca
normalizar a entrada do usuario
receber filtros ativos
validar parametros
montar consulta
executar busca
ordenar ou ranquear resultados
retornar lista final
```

### Pontos internos que precisam de cobertura

- caminho sem termo digitado
- caminho com apenas um filtro ativo
- caminho com multiplos filtros ativos
- tratamento de campos vazios ou nulos
- normalizacao de letras maiusculas e minusculas
- remocao de resultados duplicados
- prioridade entre busca textual e filtros combinados
- comportamento quando parte dos dados do restaurante esta incompleta

### Defeitos que essa abordagem ajuda a encontrar

- condicoes mal implementadas na combinacao de filtros
- falha na validacao de parametros vazios
- erro de normalizacao de texto
- duplicidade por unificacao incorreta de resultados
- problema no algoritmo de ordenacao ou ranqueamento

### Por que caixa-branca e importante aqui

Mesmo quando um caso simples funciona, a logica pode falhar nas bordas. A abordagem estrutural ajuda a localizar a causa raiz do erro e evita que a equipe corrija apenas o sintoma visivel.

---

## 4. Comparacao entre as abordagens

| Aspecto | Caixa-preta | Caixa-branca |
|---|---|---|
| Foco | comportamento observado | logica interna e caminhos de decisao |
| Referencia principal | expectativa do usuario | implementacao da funcionalidade |
| Pergunta central | o sistema faz o que deveria fazer? | o sistema foi construido corretamente? |
| Tipo de defeito mais visivel | erro funcional, inconsistencias de retorno, falha de UX | condicao incorreta, cobertura insuficiente, tratamento inadequado de excecao |

As duas abordagens se complementam. Uma mostra o defeito no uso real. A outra explica por que ele acontece.

---

## 5. Aplicacao ao caso Local Eats

No contexto do Local Eats, a abordagem funcional e a mais urgente porque o problema ja se manifesta para o usuario final. Ainda assim, ela nao resolve sozinha a origem da falha.

Se a busca entrega resultado errado, a equipe precisa confirmar tanto o impacto funcional quanto os caminhos internos envolvidos em filtros, normalizacao, consulta e ordenacao. Sem isso, ha risco alto de correcao parcial e reincidencia do defeito.

---

## 6. Conclusao

Testes funcionais e estruturais nao sao alternativas excludentes. Eles tratam perspectivas diferentes do mesmo problema.

Para o Local Eats, o melhor resultado vem da combinacao das duas abordagens: caixa-preta para validar o comportamento que o usuario percebe e caixa-branca para corrigir a causa tecnica com mais seguranca.
