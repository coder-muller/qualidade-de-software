# Qualidade de Software

## Integrantes

- Guilherme Coelho Muller
- Arthur Ortiz Fonseca
- Joao Pedro da Silva Caldeira

## Objetivo do repositorio

Este repositorio organiza as atividades da disciplina de Qualidade de Software dentro da metodologia PBL, usando o estudo de caso Local Eats como base para analise, diagnostico e planejamento de testes.

## Organizacao do repositorio

- `docs/` -> documentacao e entregas do projeto
- `artefatos/` -> evidencias, relatorios e diagramas
- `referencias/` -> materiais de apoio
- `src/` -> regras de negocio do Local Eats (pedido, desconto, entrega)
- `tests/` -> testes unitarios, funcionais (e2e) e BDD
- `pages/` -> Page Objects para automacao Playwright
- `features/` -> cenarios Gherkin (BDD)
- `codegen/` -> scripts gerados com Playwright Codegen

## Entrega 1

Atividades de analise e planejamento de testes manuais:

- [Aula 2 - Atributos de qualidade](docs/aula-02.md)
- [Aula 3 - Diagnostico de QA](docs/aula-03.md)
- [Aula 4 - Estrategia inicial de testes](docs/aula-04.md)
- [Aula 5 - Testes funcionais e estruturais](docs/aula-05.md)
- [Aula 6 - Planejamento e execucao de testes](docs/aula-06.md)

## Entrega 2

Atividades de automacao de testes (PBL 6, 7 e 8):

| PBL | Documento | Conteudo |
|-----|-----------|----------|
| PBL 6 - Testes unitarios e TDD | [docs/aula-09.md](docs/aula-09.md) | `src/` + `tests/unit/` |
| PBL 7 - Testes funcionais automatizados | [docs/aula-10.md](docs/aula-10.md) | Playwright + POM |
| PBL 8 - BDD | [docs/aula-12.md](docs/aula-12.md) | Gherkin + pytest-bdd |

**App testado:** https://local-eats-unisenac.vercel.app/

## Como executar os testes

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install chromium
```

Credenciais (opcional — padrao do seed: `teste@teste.com` / `123`):

```bash
cp .env.example .env
# edite LOCAL_EATS_EMAIL e LOCAL_EATS_PASSWORD se necessario
```

Executar por tipo:

```bash
pytest tests/unit/ -v
pytest tests/e2e/ -v --browser chromium
pytest tests/bdd/ -v --browser chromium
```

Executar toda a suite:

```bash
pytest tests/ -v --browser chromium
```
