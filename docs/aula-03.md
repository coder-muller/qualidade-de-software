# Aula 3 - Diagnostico de QA da startup Local Eats

> Disciplina: Qualidade de Software  
> Estudo de caso: Local Eats

---

## 1. Diagnostico da situacao atual

### 1.1 Papeis que provavelmente ja existem

Pelo cenario, a operacao atual deve contar com uma estrutura enxuta, composta por:

- desenvolvimento
- lideranca de produto ou negocio
- apoio pontual de analise de requisitos
- algum nivel de coordenacao tecnica

O ponto mais fraco nao parece ser a ausencia total de pessoas, e sim a falta de definicao de responsabilidades ligadas a qualidade.

### 1.2 Como a qualidade esta sendo tratada hoje

Tudo indica que a qualidade esta distribuida de forma informal. Desenvolvedores corrigem defeitos quando eles aparecem, produto pressiona por entrega e nao existe uma etapa clara de validacao antes da publicacao. Esse modelo e comum em startups, mas cobra um preco alto quando o volume de usuarios cresce.

### 1.3 Principais lacunas identificadas

- nao ha ownership claro sobre qualidade
- criterios de aceitacao parecem pouco definidos
- testes sao insuficientes para os fluxos mais criticos
- defeitos chegam a producao sem rastreabilidade adequada
- web e mobile aparentam evoluir sem alinhamento consistente
- a equipe reage a incidentes, mas previne pouco

### 1.4 Impactos dessas lacunas

Os efeitos praticos sao previsiveis:

- aumento de retrabalho
- correcao tardia de defeitos
- baixa previsibilidade nas entregas
- perda de confianca dos usuarios e parceiros
- custo maior de suporte e manutencao

### 1.5 Quem deve responder pela qualidade

Qualidade nao deve ficar isolada em uma unica funcao. Ela precisa ser responsabilidade compartilhada entre produto, analise, desenvolvimento e QA. Ainda assim, e importante existir um papel que organize a estrategia de testes, registre riscos e garanta disciplina no processo de validacao.

---

## 2. Estrutura minima recomendada

| Papel | Responsabilidade principal | Contribuicao para a qualidade |
|---|---|---|
| Product Manager | priorizar backlog, definir valor e aprovar escopo | evita entregas mal definidas e reduz ambiguidade de negocio |
| Analista de sistemas ou negocio | detalhar regras, fluxos e criterios de aceitacao | melhora testabilidade e reduz erro de interpretacao |
| Desenvolvedor | implementar funcionalidades, revisar codigo e criar testes tecnicos | previne defeitos desde a construcao |
| Analista de QA | planejar cenarios, executar testes, registrar bugs e apoiar regressao | organiza a validacao do produto com foco em risco |
| DevOps | publicar versoes, monitorar ambiente e apoiar observabilidade | reduz falhas operacionais e acelera a resposta a incidentes |

Essa estrutura ja seria suficiente para sair de um modelo reativo e chegar a um processo minimo de qualidade.

---

## 3. Responsabilidades relacionadas a qualidade

| Atividade | Responsavel principal | Apoio |
|---|---|---|
| Definir criterios de aceitacao | Product Manager / Analista | QA e desenvolvimento |
| Revisar requisitos antes do desenvolvimento | Analista de sistemas | Product Manager e QA |
| Planejar cenarios de teste | QA | Analista e desenvolvimento |
| Criar testes unitarios e de integracao | Desenvolvimento | QA |
| Executar testes funcionais e exploratorios | QA | Desenvolvimento |
| Registrar e classificar defeitos | QA | Product Manager |
| Validar correcao e regressao | QA | Desenvolvimento |
| Aprovar prontidao da entrega | Product Manager | QA e DevOps |
| Monitorar incidentes em producao | DevOps | QA e desenvolvimento |

---

## 4. Praticas de QA recomendadas

### 4.1 Qualidade orientada por risco

Busca, login, pedido, pagamento e persistencia de avaliacoes devem receber prioridade de validacao. Sao fluxos com impacto direto no negocio e na confianca do usuario.

### 4.2 Criterios de aceitacao antes de desenvolver

Cada historia precisa sair da analise com comportamento esperado, regra de negocio e condicoes de aceite claras. Isso reduz retrabalho e facilita o teste.

### 4.3 Registro formal de defeitos

Todo bug relevante deve ter descricao, severidade, passos para reproducao, ambiente afetado e status. Sem esse controle, a equipe corrige no curto prazo, mas perde historico e rastreabilidade.

### 4.4 Smoke test antes de publicar

Antes de cada release, a equipe deve validar rapidamente os fluxos que nao podem quebrar: autenticacao, busca, abertura de restaurante, pedido e avaliacao.

### 4.5 Revisao tecnica e alinhamento entre plataformas

Como o cenario aponta inconsistencias entre web e mobile, a equipe precisa revisar criterios comuns e evitar evolucao separada das duas frentes.

---

## 5. Contratacoes recomendadas

### 5.1 Vaga - Analista de Qualidade de Software

**Objetivo da posicao**  
Estruturar a validacao do produto, reduzir escape de defeitos e melhorar a confiabilidade das entregas.

**Responsabilidades**

- planejar e executar testes manuais e exploratorios
- registrar defeitos com clareza e prioridade
- revisar criterios de aceitacao junto a produto e analise
- apoiar smoke tests e regressao antes de release
- acompanhar os principais riscos de qualidade do produto

**Requisitos obrigatorios**

- conhecimento de fundamentos de teste de software
- boa escrita para documentar cenarios e defeitos
- capacidade de analisar fluxos web e mobile
- comunicacao objetiva para atuar com times pequenos

**Diferenciais**

- experiencia com bug tracking
- nocao de automacao de testes
- familiaridade com Git e ferramentas de apoio ao desenvolvimento

**Certificacao desejavel**

- ISTQB CTFL

### 5.2 Vaga - Desenvolvedor Full Stack

**Objetivo da posicao**  
Evoluir o produto com foco em estabilidade, manutenibilidade e correcao tecnica dos fluxos criticos.

**Responsabilidades**

- implementar novas funcionalidades
- corrigir defeitos identificados em homologacao e producao
- criar testes tecnicos para regras de negocio relevantes
- participar de revisao de codigo
- atuar em alinhamento com QA e produto

**Requisitos obrigatorios**

- experiencia em desenvolvimento web
- conhecimento de front-end e back-end
- dominio basico de Git
- capacidade de depuracao e analise de falhas

**Diferenciais**

- experiencia com APIs REST
- nocao de CI/CD
- familiaridade com testes automatizados
- vivencia em times ageis

---

## 6. Conclusao

O diagnostico mostra uma startup com produto promissor, mas com maturidade limitada em processo de qualidade. O maior risco nao esta apenas no defeito tecnico, e sim na ausencia de um fluxo que previna defeitos antes da entrega.

Com papeis mais claros, praticas basicas de QA e um dono explicito para a validacao, a equipe tende a reduzir retrabalho, acelerar aprendizado e entregar com muito mais previsibilidade.
