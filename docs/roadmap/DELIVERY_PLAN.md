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
- Cadastro de canais públicos, com WhatsApp separado de dados privados.
- Vitrine pública, busca, páginas e contato externo.
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

## Fase 3 — Rotas de Descoberta

- DiscoveryRoute e DiscoveryRouteStop.
- Participação do consumidor.
- QR Code e validação server-side.
- CheckIn, duplicidade e auditoria.
- Progresso e conclusão.
- Vincular Event/Store/Place a paradas.
- Testes de token, concorrência, repetição e autorização.

**Saída:** visitante consulta rota, visita parada, registra participação e acompanha progresso.

## Fase 4 — Incentivos simples

- Campaign e Coupon.
- Regras, elegibilidade, período e responsável pelo custo.
- Emissão e resgate de cupom único.
- Transação e idempotência.
- Campanha associada a loja/rota.
- Testes concorrentes e auditoria.

**Saída:** benefício emitido por campanha e resgatado uma única vez em estabelecimento elegível.

## Fase 5 — Pedido de reserva por contato externo e consolidação do piloto

- Gerar link de clique para conversa no WhatsApp com mensagem contextualizada e texto codificado para URL.
- Exigir revisão e envio manual da mensagem pelo consumidor.
- Disponibilizar Instagram como alternativa: abrir perfil/Direct e fornecer mensagem para cópia.
- Não criar estado local de reserva, caixa de entrada, histórico ou sincronização de conversas.
- Testar número ausente/inválido, falha de abertura e fallback para cópia.

**Saída:** consumidor prepara pedido de reserva e combina a retirada diretamente com a loja, sem transação ou confirmação controlada pela plataforma.

## Consolidação do piloto

- Conteúdo real ou dados demonstrativos claramente marcados.
- Revisão de acessibilidade e responsividade.
- Segurança, logs e backup.
- Métricas operacionais.
- Documentação de operação e moderação.
- Teste ponta a ponta e roteiro de demonstração.

## Fase 6 — Inteligência comercial e diagnóstico institucional (P2)

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
