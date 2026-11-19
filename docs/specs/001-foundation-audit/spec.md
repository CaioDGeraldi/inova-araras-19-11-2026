# Spec 001 | Auditoria e conclusão da fundação Django

## Contexto
PR #4 forneceu a base do projeto, mas a validação inicial ficou incompleta. Posteriormente, o PR #18 registrou a geração/versionamento de `uv.lock`, migrações, Django check, pytest, Ruff e smoke tests com a aplicação conectada à configuração PostgreSQL. A Issue #3 foi encerrada após essa validação posterior.

## Objetivo
Verificar a base no ambiente de desenvolvimento, corrigir problemas que impeçam o uso e deixar um baseline confiável para desenvolver o domínio.

## Incluído
- Conferir dependências e gerar/validar uv.lock.
- Instalar dependências em Python 3.12.
- Configuração .env e PostgreSQL 16 via compose.
- Migrar e verificar CustomUser.
- Django check, healthcheck e renderização base.
- Ruff e pytest.
- README e comandos de setup reproduzíveis.
- Segredos e configuração local protegidos.

## Excluído
- Features de produto.
- Integrações externas.
- Deploy específico de provedor.
- Abstrações não necessárias para a fundação.

## Critérios de aceitação
- [x] Instalação reproduzível com uv e lockfile versionado.
- [x] PostgreSQL local inicia e aplicação conecta.
- [x] Migrations aplicam sem erro e User customizado está ativo.
- [x] manage.py check passa.
- [x] Healthcheck responde.
- [x] Template base renderiza e HTMX está configurado.
- [x] Ruff e pytest passam; PR #18 registrou 1 teste aprovado.
- [x] README permite outra pessoa iniciar o projeto.
- [x] Nenhum segredo real de ambiente está versionado; credenciais demonstrativas inseguras permanecem tratadas separadamente na Issue #15.

## Verificação registrada
PR #18 reporta `manage.py check`, `makemigrations --check`, `migrate`, `pytest` (1 teste), Ruff, seed repetido e smoke tests HTTP 200. `uv.lock` e `compose.yaml` estão versionados. A Issue #3 foi concluída com base nessas evidências posteriores ao PR #4.
