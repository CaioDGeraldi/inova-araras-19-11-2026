# Plano de entrega | Vem pro Centro

## Princípio

Desenvolvimento individual, orientado por fatias verticais. A ordem representa dependências, não promessa de duração. A data do evento não justifica afirmar que funcionalidades estarão prontas sem implementação e validação.

## Fase 0 — Fundação confiável

- Auditar PR #4.
- Confirmar Python 3.12 e uv.
- Gerar e versionar uv.lock.
- Configurar ambiente local e PostgreSQL.
- Executar migrations, Django check, Ruff e pytest.
- Confirmar CustomUser, healthcheck e template base.
- Registrar evidências no CURRENT_STATE.

**Saída:** baseline reproduzível. Não iniciar domínios sobre fundação não verificada.

## Fase 1 — Comércio mínimo

- Identidade e autorização.
- Store, categorias e aprovação.
- Product/Service.
- Painel mínimo do comerciante.
- Vitrine pública, busca e páginas.
- Testes de autorização e exposição de dados.

**Saída:** comerciante mantém loja/catálogo e visitante descobre sem login.

## Fase 2 — Cronograma

- Place/organizador.
- Event e categorias.
- Administração de publicação/cancelamento.
- Calendário/listagem por data e detalhe público.
- Datas no fuso America/Sao_Paulo.
- Testes de visibilidade e cancelamento.

**Saída:** administrador publica atividade e visitante planeja visita.

## Fase 3 — Circuito Vivo

- Circuit e CircuitStop.
- Participação do consumidor.
- QR Code e validação server-side.
- CheckIn, duplicidade e auditoria.
- Progresso e conclusão.
- Vincular Event/Store/Place a paradas.
- Testes de token, concorrência, repetição e autorização.

**Saída:** visitante consulta circuito, visita parada, registra participação e acompanha progresso.

## Fase 4 — Incentivos simples

- Campaign e Coupon.
- Regras, elegibilidade, período e responsável pelo custo.
- Emissão e resgate de cupom único.
- Transação e idempotência.
- Campanha associada a loja/circuito.
- Testes concorrentes e auditoria.

**Saída:** benefício emitido por campanha e resgatado uma única vez em estabelecimento elegível.

## Fase 5 — Consolidação do piloto

- Conteúdo real ou dados demonstrativos claramente marcados.
- Revisão de acessibilidade e responsividade.
- Segurança, logs e backup.
- Métricas operacionais.
- Documentação de operação e moderação.
- Teste ponta a ponta e roteiro de demonstração.

## Cortes se o tempo apertar

1. Remover avaliações e comunidade do primeiro corte.
2. Adiar carteira de pontos; manter cupom simples ou remover campanha.
3. Adiar reservas e usar contato direto.
4. Adiar filtros por proximidade, notificações e inscrições.
5. Preservar vitrine, cronograma e Circuito Vivo em jornada demonstrável.
6. Não cortar autorização, integridade de check-in, segurança, acessibilidade essencial ou testes críticos.

## Dependências externas

- Estabelecimentos precisam aceitar participar e manter dados.
- Atividades precisam de organizadores e locais confirmados.
- Benefícios exigem acordo sobre elegibilidade e custo.
- Eventos públicos dependem das autorizações aplicáveis.
- Vaga Legal depende de dados e autorização.
- Nenhuma dependência deve ser simulada como compromisso confirmado.

## Evidências por fase

Cada fase só é concluída com spec aprovada, implementação, testes executados e registrados, critérios de aceite verificados, revisão de segurança/autorização, atualização de CURRENT_STATE e PR revisável sem merge automático.