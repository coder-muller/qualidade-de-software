# Aula 2 - Atributos de Qualidade com base na familia ISO/IEC 25000

> Disciplina: Qualidade de Software  
> Estudo de caso: Local Eats

---

## 1. Contexto do produto

O Local Eats e uma plataforma web e mobile voltada a descoberta de restaurantes independentes. O produto combina busca, filtros, favoritos, avaliacoes e jornadas de navegacao que dependem de resposta rapida e comportamento consistente entre dispositivos.

O cenario do PBL deixa claro que a primeira versao foi colocada em operacao com pouca maturacao. O resultado foi a exposicao de defeitos em producao, principalmente em busca, usabilidade, persistencia de dados e compatibilidade entre ambientes.

---

## 2. Problemas observados

Os sintomas descritos no cenario sao:

- lentidao em horarios de pico
- telas confusas e pouco intuitivas
- buscas com resultados incorretos
- falhas em determinados modelos de smartphone
- dificuldade para concluir acoes simples
- avaliacoes que desaparecem apos atualizar a pagina
- inconsistencias entre a versao web e a versao mobile

---

## 3. Relacao entre problemas e atributos de qualidade

| Problema observado | Atributo mais afetado | Analise tecnica | Impacto no negocio |
|---|---|---|---|
| Lentidao em horarios de pico | Eficiencia de desempenho | O sistema perde tempo de resposta e capacidade justamente quando a demanda cresce. Isso indica gargalos de processamento, consulta ou infraestrutura. | Reduz conversao, aumenta abandono e prejudica o uso nos horarios de maior valor comercial. |
| Telas confusas e pouco intuitivas | Usabilidade | A interface nao orienta bem a execucao das tarefas. O esforco cognitivo aumenta e erros de navegacao se tornam mais provaveis. | O usuario demora mais para concluir a jornada e percebe o produto como pouco confiavel. |
| Buscas com resultados incorretos | Adequacao funcional | A funcao central do sistema deixa de retornar resultados coerentes com o criterio informado. O problema afeta corretude e completude funcional. | O usuario nao encontra o restaurante desejado e a proposta principal do produto perde valor. |
| Falhas em determinados smartphones | Compatibilidade | O comportamento nao se mantem estavel em diferentes dispositivos e configuracoes de uso. Isso sugere falhas de adaptacao ou dependencias especificas de ambiente. | Parte do publico pode ficar impedida de usar o servico com regularidade. |
| Dificuldade para concluir acoes simples | Usabilidade | Fluxos basicos deveriam ser claros, curtos e previsiveis. Se acoes simples se tornam confusas, ha problema de operabilidade. | Aumenta frustracao, abandono de tarefa e suporte corretivo. |
| Avaliacoes desaparecem apos atualizar a pagina | Confiabilidade | O sistema nao preserva corretamente um dado que ja foi registrado ou exibido. Isso indica falha de persistencia, sincronizacao ou recuperacao de estado. | Compromete a confianca do usuario e enfraquece a credibilidade da plataforma. |
| Inconsistencias entre web e mobile | Portabilidade | Funcionalidades equivalentes deveriam manter comportamento alinhado entre canais. Diferencas relevantes indicam baixa consistencia entre implementacoes. | A experiencia muda conforme o dispositivo e o produto parece instavel. |

---

## 4. Priorizacao inicial

| Prioridade | Item | Motivo |
|---|---|---|
| Alta | Busca com resultados incorretos | Afeta a principal proposta de valor do sistema e compromete diretamente a jornada do usuario. |
| Alta | Avaliacoes que desaparecem | E um defeito de confiabilidade com impacto direto na credibilidade da plataforma. |
| Alta | Lentidao em horarios de pico | Ocorre no momento de maior uso e pode gerar perda imediata de conversao. |
| Media | Falhas em smartphones especificos | Limita acesso e amplia o risco de exclusao de parte da base de usuarios. |
| Media | Inconsistencias entre web e mobile | Gera percepcao de instabilidade e dificulta suporte e manutencao. |
| Media | Telas confusas e dificuldade em acoes simples | Nao interrompem sempre o uso, mas deterioram a experiencia e ampliam erros operacionais. |

---

## 5. Avaliacao do estado atual do produto

O Local Eats entrega valor de negocio, mas ainda nao apresenta nivel de qualidade suficiente para operar sem monitoramento e correcao prioritarios. O produto esta funcional em partes, porem os problemas identificados atingem atributos essenciais para continuidade sustentavel:

- adequacao funcional
- confiabilidade
- eficiencia de desempenho
- usabilidade
- compatibilidade e portabilidade

Em outras palavras, o sistema nao esta inviabilizado, mas esta exposto a risco tecnico e reputacional acima do aceitavel.

---

## 6. Conclusao

Pela leitura do cenario, o principal problema do Local Eats nao e apenas a existencia de defeitos isolados, e sim a combinacao de falhas em atributos que sustentam a experiencia principal do usuario.

O caminho mais adequado e atacar primeiro os pontos que comprometem busca, persistencia de informacoes e desempenho sob carga. A partir disso, a equipe pode evoluir a usabilidade e a consistencia entre plataformas com menor risco de retrabalho.
