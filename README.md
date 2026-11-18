# Inova Araras 2026

Repositório do projeto desenvolvido para o 1º Inova Araras, em 19 de novembro de 2026.

## Requisitos

- Python 3.12
- [uv](https://docs.astral.sh/uv/)
- Docker com Docker Compose

## Configuração local

No Windows CMD:

```cmd
copy .env.example .env
docker compose up -d db
uv lock
uv sync
uv run python manage.py migrate
uv run python manage.py runserver
```

A aplicação ficará disponível em http://127.0.0.1:8000.

## Comandos úteis

```cmd
uv run python manage.py createsuperuser
uv run python manage.py check
uv run pytest
uv run ruff check .
uv run python manage.py collectstatic
```

O arquivo `.env` contém configurações locais e não deve ser versionado. Em produção, defina uma `SECRET_KEY` própria, `DEBUG=false`, os hosts permitidos e as origens confiáveis de CSRF.

## Estrutura

- `config/`: configuração do Django.
- `apps/core/`: usuário principal, modelos abstratos e healthcheck.
- `templates/`: templates compartilhados.
- `static/`: arquivos estáticos próprios.

O endpoint de verificação está disponível em `/api/v1/health/`.
