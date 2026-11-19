# Spec 001 | Auditoria e conclusão da fundação Django

## Contexto
PR #4 fornece a base proposta para o projeto. O PR registra validação incompleta: lockfile não gerado e Django, PostgreSQL, Ruff e pytest não executados.

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
- [ ] Instalação reproduzível com uv e lockfile versionado.
- [ ] PostgreSQL local inicia e aplicação conecta.
- [ ] Migrations aplicam sem erro e User customizado está ativo.
- [ ] manage.py check passa.
- [ ] Healthcheck responde.
- [ ] Template base renderiza e HTMX está configurado.
- [ ] Ruff e pytest passam ou falhas restantes estão documentadas e justificadas.
- [ ] README permite outra pessoa iniciar o projeto.
- [ ] Nenhum segredo real versionado.

## Verificação
Registrar comandos executados, resultados, falhas e ambiente. Não declarar critério cumprido sem evidência.
