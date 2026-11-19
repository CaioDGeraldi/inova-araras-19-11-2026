# Tasks | Spec 008 - Comunidade e avaliações

## Decisões e preparação
- [ ] Formalizar política de retenção, exclusão e anonimização antes da produção, sem presumir prazo legal.
- [ ] Publicar política da comunidade antes de habilitar avaliações públicas.
- [ ] Usar somente nome de exibição escolhido pelo usuário na identificação pública; nunca nome legal, telefone, e-mail ou ID interno.

## Domínio e autorização
- [ ] Modelar Review com alvo, autor interno, nota inteira de 1 a 5, comentário opcional até 1.000 caracteres e estado.
- [ ] Garantir uma avaliação ativa por conta/alvo e versionamento das edições.
- [ ] Implementar exclusão lógica com trilha mínima e respeito à política de retenção/direitos do titular.
- [ ] Modelar ReviewResponse vinculada à avaliação e ao estabelecimento.
- [ ] Modelar Report com denunciante, alvo, motivo, estado e instante.
- [ ] Modelar registro imutável/auditável de decisão de moderação.
- [ ] Garantir que anonimato afete somente a apresentação pública.
- [ ] Garantir autorização de resposta por responsável principal do estabelecimento.
- [ ] Restringir autoria interna, denúncias e fila de moderação a perfis autorizados.

## Experiência pública e do consumidor
- [ ] Exibir avaliações e respostas públicas no detalhe do estabelecimento/experiência.
- [ ] Implementar criação de avaliação autenticada.
- [ ] Implementar escolha entre exibição identificada e anônima.
- [ ] Implementar denúncia autenticada para spam/fraude, assédio/discriminação, conteúdo ilegal, exposição de dados pessoais, conflito de interesse ou outro com justificativa.
- [ ] Limitar denúncias repetidas e aplicar rate limit sem ocultação automática.
- [ ] Exibir confirmação de denúncia sem remoção automática.
- [ ] Implementar estados vazios, erros e conteúdo moderado.

## Experiência do estabelecimento
- [ ] Exibir avaliações recebidas no painel do estabelecimento.
- [ ] Permitir resposta oficial pelo responsável autorizado.
- [ ] Permitir edição e remoção da resposta pelo responsável, com auditoria e sem alterar a avaliação original.
- [ ] Impedir resposta ou alteração em estabelecimento de terceiro.
- [ ] Preservar avaliação original e nota após resposta.

## Administração e moderação
- [ ] Criar fila restrita de denúncias.
- [ ] Permitir análise e decisão de manter, ocultar ou remover conforme política.
- [ ] Exigir motivo e registrar moderador/instante em cada decisão.
- [ ] Implementar comunicação de resultado conforme mecanismo aprovado.
- [ ] Definir e implementar fluxo de revisão/contestação.
- [ ] Preservar histórico e autoria interna conforme retenção.

## Segurança e qualidade
- [ ] Testar acesso anônimo versus identificado na resposta pública.
- [ ] Testar que IDs de autor enviados pelo cliente são ignorados.
- [ ] Testar autorização cruzada de respostas entre estabelecimentos.
- [ ] Testar abuso de denúncias, duplicidade e rate limit.
- [ ] Testar que denúncia não remove conteúdo automaticamente.
- [ ] Testar que crítica negativa legítima permanece publicada.
- [ ] Testar conteúdo com dados pessoais e tratamento de moderação.
- [ ] Testar acessibilidade por teclado e leitor de tela.

## Encerramento
- [ ] Atualizar CURRENT_STATE com evidências reais.
- [ ] Vincular PR, testes e evidências à spec.
- [ ] Não marcar tarefas concluídas sem implementação e validação.
