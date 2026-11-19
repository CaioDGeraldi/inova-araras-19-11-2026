# Tasks | Spec 001

- [x] Inspecionar PR #4 e diff antes de alterar.
- [x] Verificar Python 3.12 e uv no ambiente.
- [x] Resolver e versionar uv.lock.
- [x] Configurar .env a partir de .env.example.
- [x] Subir PostgreSQL e verificar conexão.
- [x] Aplicar migrations e validar CustomUser.
- [x] Executar Django check.
- [x] Verificar healthcheck e template base.
- [x] Executar Ruff.
- [x] Executar pytest.
- [x] Corrigir problemas comprovados.
- [x] Atualizar README se necessário.
- [x] Registrar evidências e abrir/atualizar PR.
- [x] Revisar sem merge automático.


## Evidência de conclusão

A fundação foi introduzida no PR #4 e validada posteriormente no PR #18: lockfile presente, PostgreSQL via Compose, migrations, Django check, healthcheck/smoke HTTP, Ruff e pytest (1 teste). A Issue #3 foi encerrada após essa validação.