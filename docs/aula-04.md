# Aula 4 - Estrategia inicial de testes do Local Eats

> Disciplina: Qualidade de Software  
> Estudo de caso: Local Eats

---

## 1. Funcionalidades priorizadas

As funcionalidades abaixo representam a jornada principal do usuario e concentram os riscos mais relevantes do produto:

| Funcionalidade | Relevancia para o negocio | Risco principal |
|---|---|---|
| Login e autenticacao | permite acesso a recursos personalizados | bloqueio de acesso ou sessao instavel |
| Busca e filtros de restaurantes | sustenta a proposta central da plataforma | retorno incorreto ou irrelevante |
| Visualizacao de restaurante e cardapio | apoia a decisao do usuario | dados incompletos ou navegacao quebrada |
| Pedido e pagamento | converte uso em operacao de negocio | erro de registro, cobranca ou confirmacao |
| Avaliacoes | reforca confianca e prova social | perda de dados ou exibicao inconsistente |
| Favoritos | melhora recorrencia de uso | falha de persistencia por usuario |

---

## 2. Niveis de teste por funcionalidade

| Funcionalidade | Testes unitarios | Testes de integracao | Testes de sistema / aceitacao |
|---|---|---|---|
| Login e autenticacao | validacao de campos, formato de email e regras de senha | formulario, servico de autenticacao e sessao | acesso completo com credenciais validas e tratamento de erro |
| Busca e filtros | regras de filtro, normalizacao e ordenacao | interface, API de busca e base de restaurantes | usuario encontra restaurantes coerentes com o criterio informado |
| Visualizacao de restaurante | montagem de dados de cardapio, nota e endereco | recuperacao conjunta de detalhes, fotos e avaliacoes | pagina carrega com informacoes corretas e navegacao estavel |
| Pedido e pagamento | calculo de subtotal, total e validacoes do carrinho | carrinho, checkout, persistencia do pedido e retorno de pagamento | usuario conclui o pedido e recebe confirmacao consistente |
| Avaliacoes | validacao de nota, texto e campos obrigatorios | envio, persistencia e leitura da avaliacao | avaliacao continua visivel apos envio e nova carga da pagina |
| Favoritos | adicionar, remover e evitar duplicidade | persistencia vinculada ao usuario autenticado | lista de favoritos reflete o estado correto da conta |

---

## 3. Prioridades e riscos

### Prioridade alta

- busca e filtros
- pedido e pagamento
- login e autenticacao
- persistencia de avaliacoes

### Prioridade media

- visualizacao de restaurante e cardapio
- favoritos

### Justificativa

Busca e filtros precisam vir primeiro porque a descoberta de restaurantes e a funcao mais importante do produto. Pedido e pagamento tambem estao no topo porque qualquer erro nesse fluxo afeta diretamente operacao, receita e confianca.

Login e autenticacao entram como prioridade alta por sustentarem recursos personalizados e trilhas de uso autenticadas. Ja as avaliacoes merecem destaque porque o cenario relata perda de informacao apos atualizacao, o que caracteriza risco real de confiabilidade.

---

## 4. Aplicacao da piramide de testes

### Maior volume

- testes unitarios

### Volume intermediario

- testes de integracao

### Menor volume

- testes de sistema e ponta a ponta

### Racional da distribuicao

Os testes unitarios devem concentrar a maior cobertura porque sao mais baratos, mais rapidos e ajudam a proteger regras de negocio antes que o defeito avance no fluxo.

Os testes de integracao sao especialmente importantes no Local Eats, ja que muitos riscos surgem da combinacao entre interface, API, persistencia e comportamento por plataforma.

Os testes de sistema precisam existir, mas focados em jornadas criticas. Sao mais lentos, mais caros e devem validar o que realmente nao pode quebrar em uma release.

---

## 5. Testes em producao

O uso de verificacoes em producao faz sentido, desde que seja controlado e nunca substitua a validacao anterior.

Casos em que isso agrega valor:

- monitoramento de desempenho em horarios de pico
- analise de erros reais por dispositivo e navegador
- rollout gradual com feature flags
- observacao de comportamento apos release em fluxos sensiveis

No contexto do Local Eats, esse cuidado e relevante porque parte dos defeitos relatados depende de ambiente, volume de uso e diversidade de aparelhos. Ainda assim, testes em producao devem ser encarados como camada complementar de seguranca, nao como etapa principal de validacao.

---

## 6. Conclusao

A estrategia inicial de testes do Local Eats deve ser orientada por risco, com foco nos fluxos que sustentam descoberta, conversao e confianca. Isso significa concentrar cobertura em busca, autenticacao, pedido e persistencia de avaliacoes.

Com uma base forte de testes unitarios e de integracao, e validacao de sistema focada no essencial, a equipe consegue reduzir escape de defeitos sem tornar o processo pesado demais para uma operacao enxuta.
