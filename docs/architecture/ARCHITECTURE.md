# Arquitetura inicial

## Stack definida pela fundação
- Python 3.12
- Django 5.2 LTS
- uv
- Django REST Framework
- Django Templates + django-htmx
- Bootstrap 5.3
- PostgreSQL 16
- WhiteNoise + Gunicorn
- Ruff, pytest, pytest-django

## Estrutura
- `config/`: configuração e entrypoints.
- `apps/core/`: identidade e abstrações transversais.
- Domínios em apps Django independentes, criados conforme specs.
- Templates e estáticos compartilhados, sem acoplamento de domínio.

## Diretrizes
1. Modularidade por domínio, sem abstrações prematuras.
2. Django monolith para o MVP, sem microserviços.
3. HTML server-rendered e HTMX como caminho primário; DRF para endpoints que justifiquem API.
4. Não criar services/selectors/serializers vazios ou camadas obrigatórias sem caso de uso.
5. Responsabilidades e regras de negócio não devem depender de UI.
6. Integridade financeira/pontos: decimal, transações, idempotência, rastreabilidade e concorrência, se o domínio de fidelidade entrar.
7. Dados privados minimizados e protegidos.
8. Testar regras de domínio, fluxos críticos e integração.

## Fundação existente
PR #4 propõe configuração Django, User customizado, UUIDModel, TimeStampedModel, healthcheck, Templates/HTMX, PostgreSQL, estáticos, Ruff e pytest. Antes de expandir, auditar e validar essa base. Não presumir lockfile, migrations, banco ou testes validados.

## UI
Mobile-first, acessível WCAG 2.2 AA, design consistente, animações discretas, sem sacrificar performance. Dashboard de lojista e vitrine pública são experiências distintas, mas compartilham identidade visual.
