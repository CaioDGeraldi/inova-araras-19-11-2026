# Tasks | Spec 009 - Administração e operação da plataforma

## Preparação e decisões
- [ ] Formalizar política de retenção, acesso restrito e descarte de auditoria antes da produção.
- [ ] Mapear permissões administrativas já existentes nas Specs 002 a 008 para evitar duplicação.

## Acesso e navegação P0
- [ ] Criar entrada protegida para o painel administrativo.
- [ ] Implementar autorização server-side para páginas, ações e endpoints.
- [ ] Provisionar administradores por bootstrap de superusuário ou comando privilegiado protegido; impedir autoelevação por cadastro público.
- [ ] Implementar recuperação segura de credenciais e revogação que desative a conta e invalide sessões/tokens ativos.
- [ ] Criar navegação para categorias, estabelecimentos, cronograma e rotas.
- [ ] Integrar as telas aos fluxos das Specs 002, 003 e 004 sem duplicar regras de domínio.
- [ ] Testar acesso direto por URL e chamadas sem permissão.

## Auditoria P0/P1
- [ ] Definir serviço/abstração de auditoria reutilizável.
- [ ] Registrar provisionamento/revogação administrativa; aprovação/rejeição/suspensão; publicação/edição relevante/cancelamento de atividades e rotas; alterações de campanha; confirmação/correção de compra e resgate; moderação/revisões; revogação/rotação QR.
- [ ] Registrar ações de moderação conforme Spec 008.
- [ ] Registrar alterações administrativas de campanhas conforme Spec 005.
- [ ] Registrar autor, recurso, ação, instante, resultado e motivo quando aplicável.
- [ ] Excluir tokens completos, segredos e dados pessoais desnecessários dos registros.
- [ ] Implementar correções por evento compensatório vinculado ao original, com motivo, operador e instante; nunca editar/apagar o evento original.
- [ ] Testar integridade e acesso restrito à trilha.

## Consulta operacional P1
- [ ] Criar consulta somente leitura de check-ins.
- [ ] Criar consulta somente leitura de campanhas e resgates.
- [ ] Exibir filtros por período e estabelecimento quando pertinente, respeitando permissões.
- [ ] Restringir dados globais a administradores autorizados e dados de loja ao responsável da própria loja, quando a interface existir.
- [ ] Criar indicadores agregados de estabelecimentos por estado, atividades publicadas/canceladas, rotas/participações/check-ins aceitos, campanhas ativas, cupons emitidos/resgatados e compras declaradas, sempre com período, unidade e fonte.
- [ ] Identificar compras como declarações dos responsáveis, não faturamento auditado.
- [ ] Não incluir consultas de busca, sessões ou dados de inteligência institucional P2.

## Dados demonstrativos P1
- [ ] Definir marcador de origem demonstrativa reutilizável.
- [ ] Garantir que seed e fixtures identifiquem registros demonstrativos.
- [ ] Permitir filtrar/separar dados demonstrativos e reais nos indicadores.
- [ ] Testar que rotinas demonstrativas não alteram registros reais.
- [ ] Garantir que relatórios indiquem claramente quando incluem dados fictícios.

## Qualidade e encerramento
- [ ] Testar autorização em cada domínio administrativo.
- [ ] Testar auditoria de ações críticas e acesso restrito.
- [ ] Testar indicadores agregados e separação demonstrativo/real.
- [ ] Atualizar CURRENT_STATE com evidências reais.
- [ ] Vincular PR, testes e evidências à spec.
- [ ] Não marcar tarefas concluídas sem implementação e validação.
