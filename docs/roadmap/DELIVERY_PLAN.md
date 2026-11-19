# Plano de entrega | Vem pro Centro

## Princípio

Desenvolvimento individual, orientado por fatias verticais. A ordem representa dependências, não promessa de duração. A data do evento não justifica afirmar que funcionalidades estarão prontas sem implementação e validação.

## Estado das fases após a demonstração de 19/11/2026

- **Fase 0 — concluída:** base criada no PR #4 e validada posteriormente no PR #18. A Issue #3 foi encerrada. A Issue #7 foi encerrada como não planejada, pois o QR abre pela câmera nativa do dispositivo.
- **Fase 1 — parcial:** cadastro, painel, catálogo, busca, contatos externos e complementos P0 integrados nos PRs #18, #22 e #24. Issue #8 permanece aberta para os critérios completos da Spec 002.
- **Fase 2 — parcial:** consulta pública de eventos e associação evento/rota integradas nos PRs #18 e #22. Ocorrências/Place e recursos P1 permanecem pendentes na Issue #9.
- **Fase 3 — parcial:** rotas, QR por URL, check-in e progresso integrados nos PRs #18 e #22. Rotação/revogação, fallback assistido e múltiplas execuções permanecem pendentes na Issue #10.
- **Fase 4 — parcial:** campanha simples, confirmação manual simplificada e cupom cruzado integrados no PR #18. Token temporário, validade, limites e auditoria permanecem pendentes nas Issues #11 e #12.
- **Fase 5 — pendente:** comunidade/moderação e camada completa de administração/auditoria continuam nas Issues #13 e #14.
- **Fase 6 — parcial:** WhatsApp com mensagem contextualizada e Instagram como alternativa já aparecem na demo; não há estado local de reserva nem sincronização de conversa.
- **Fase 7 — pendente:** inteligência comercial continua P2, sem implementação declarada.
- **Demonstração:** `seed_demo` existe, mas não está pronto para produção. Credencial fixa, saída da senha, colisões potenciais e execução automática no `Procfile` estão acompanhadas pela Issue #15.

O PR #18 e a Issue #17 correspondem a um corte temporário de demo de duas horas. Não significam entrega nem conclusão do MVP definido em `docs/product/MVP.md`.

## Fase 0 — Fundação confiável

- Auditar PR #4.
- Confirmar Python 3.12 e uv.
- Gerar e versionar uv.lock.
- Configurar ambiente local e PostgreSQL.
- Executar migrations, Django check, Ruff e pytest.
- Confirmar CustomUser, healthcheck e template base.
- Registrar evidências no CURRENT_STATE.

**Saída:** baseline reproduzível. Não iniciar domínios sobre fundação não verificada.

## Fase 1 — Comércio mínimo e operação administrativa P0

- Identidade e autorização.
- Acesso protegido ao painel administrativo.
- Categorias, Store e aprovação.
- Product/Service.
- Painel mínimo do comerciante.
- Cadastro de canais públicos, com WhatsApp separado de dados privados.
- Vitrine pública, busca, páginas e contato externo.
- Navegação administrativa para categorias e estabelecimentos.
- Testes de autorização e exposição de dados.

**Saída:** comerciante mantém loja/catálogo, administração controla elegibilidade e visitante descobre sem login.

## Fase 2 — Cronograma do Centro

- Place/organizador.
- Event e categorias.
- Administração de publicação/cancelamento.
- Calendário/listagem por data e detalhe público.
- Datas no fuso America/Sao_Paulo.
- P1: sugestões de atividades sujeitas à aprovação.
- P1: salvar/remover atividades na conta, sem criar inscrição.
- Testes de visibilidade, autorização, ordenação e cancelamento.

**Saída:** administração publica atividades e visitante planeja a visita; recursos P1 permitem contribuição moderada e salvamento pessoal.

## Fase 3 — Rotas de Descoberta

- DiscoveryRoute e DiscoveryRouteStop.
- Administração de rotas e paradas.
- Participação do consumidor.
- QR Code e validação server-side.
- Revogação imediata de token comprometido (P0).
- CheckIn, duplicidade e auditoria.
- Progresso e conclusão.
- Vincular Event/Store/Place a paradas.
- Testes de token, concorrência, repetição e autorização.

**Saída:** visitante consulta rota, visita parada, registra participação e acompanha progresso.

## Fase 4 — Incentivos simples

- Campaign e Coupon.
- Regras, elegibilidade, período e responsável pelo custo.
- Meu QR temporário, opaco, rotativo e de uso único.
- PurchaseConfirmation e confirmação explícita pelo responsável autenticado.
- Avaliação de todas as campanhas elegíveis na mesma confirmação.
- Emissão e resgate de cupom único.
- Transação, idempotência e unicidade de concessão por confirmação/campanha.
- Testes concorrentes, autorização, auditoria e recuperação de falhas.

**Saída:** compra presencial registrada por declaração auditável do responsável; benefícios emitidos conforme campanhas elegíveis e resgatados uma única vez.

## Fase 5 — Comunidade e operação P1

- Avaliações de estabelecimentos/experiências com autoria identificada ou anônima publicamente.
- Respostas oficiais de responsáveis autorizados.
- Denúncias e fila de moderação.
- Política de comunidade, decisão fundamentada e trilha de auditoria.
- Consulta operacional de check-ins, campanhas e resgates.
- Indicadores operacionais agregados com período, unidade e fonte.
- Separação explícita entre dados demonstrativos e reais.
- Testes de autorização, anonimato público, moderação e auditoria.

**Saída:** consumidores podem compartilhar experiências e a operação consegue moderar e acompanhar indicadores básicos sem expor dados individuais.

## Fase 6 — Pedido de reserva por contato externo e consolidação do piloto

- Gerar link de clique para conversa no WhatsApp com mensagem contextualizada e texto codificado para URL.
- Exigir revisão e envio manual da mensagem pelo consumidor.
- Disponibilizar Instagram como alternativa: abrir perfil/Direct e fornecer mensagem para cópia.
- Não criar estado local de reserva, caixa de entrada, histórico ou sincronização de conversas.
- Testar número ausente/inválido, falha de abertura e fallback para cópia.
- Conteúdo real ou dados demonstrativos claramente marcados.
- Revisão de acessibilidade e responsividade.
- Segurança, logs e backup.
- Teste ponta a ponta e roteiro de demonstração.

**Saída:** consumidor prepara pedido de reserva e combina a retirada diretamente com a loja; piloto demonstrável sem depender de dados reais ou operações manuais durante o pitch.

## Fase 7 — Inteligência comercial e diagnóstico institucional (P2)

- Definir taxonomia de buscas e categorias.
- Instrumentar eventos minimizados de busca sem resultado.
- Calcular cobertura de catálogo e sinais de demanda não atendida.
- Conduzir pesquisas voluntárias com consumidores e comerciantes.
- Validar sinais por levantamento de campo.
- Disponibilizar painel institucional restrito, somente com dados agregados, metodologia e limitações.
- Testar limiares, supressão de grupos pequenos, filtros sucessivos, exportações e risco de reidentificação.
- Definir retenção, governança, finalidade e auditoria.

**Saída:** diagnóstico exploratório que apoia campanhas de digitalização e planejamento, sem expor dados individuais e sem afirmar causalidade ou demanda comprovada sem validação.

## Cortes se o tempo apertar

1. Remover avaliações e comunidade do primeiro corte.
2. Adiar carteira de pontos; manter cupom simples ou remover campanha.
3. Adiar o botão de mensagem contextualizada, mantendo canais públicos e contato direto.
4. Adiar filtros por proximidade, notificações e inscrições.
5. Preservar vitrine, cronograma e Rotas de Descoberta em jornada demonstrável.
6. Não cortar autorização, integridade de check-in, segurança, acessibilidade essencial ou testes críticos.

## Dependências externas

- Estabelecimentos precisam aceitar participar e manter dados.
- Atividades precisam de organizadores e locais confirmados.
- Benefícios exigem acordo sobre elegibilidade e custo.
- Eventos públicos dependem das autorizações aplicáveis.
- Vaga Legal depende de dados e autorização.
- Painel institucional depende de governança, finalidade, autorização de acesso e avaliação de privacidade.
- Pesquisas dependem de método, participação voluntária e divulgação responsável dos limites da amostra.
- Nenhuma dependência deve ser simulada como compromisso confirmado.

## Evidências por fase

Cada fase só é concluída com spec aprovada, implementação, testes executados e registrados, critérios de aceite verificados, revisão de segurança/autorização, atualização de CURRENT_STATE e PR revisável sem merge automático.

## Preparação da demonstração do pitch

- Implementar o comando `python manage.py seed_demo` após os modelos necessários estarem estáveis.
- Criar cenário fictício coerente para consumidor e dois proprietários/estabelecimentos.
- Popular catálogo, disponibilidade declarada, Cronograma do Centro e uma Rota de Descoberta com paradas obrigatórias e opcionais.
- Garantir determinismo, idempotência, marcação dos registros e proteção contra execução em produção.
- Configurar credenciais demonstrativas por ambiente local, sem segredos versionados.
- Ensaiar a narrativa nas duas perspectivas e registrar limitações do que ainda não estiver implementado.

**Saída:** ambiente de demonstração reproduzível, sem dependência de dados reais ou operações manuais durante o pitch.
