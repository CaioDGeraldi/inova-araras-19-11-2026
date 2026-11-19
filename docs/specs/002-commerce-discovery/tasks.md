# Tasks | Spec 002 - Comércio e descoberta pública

## Preparação
- [ ] Confirmar dependência da fundação e do modelo de usuário da Spec 001.

## Domínio e autorização
- [ ] Implementar Category com estado ativo/inativo.
- [ ] Implementar Store com responsável principal e estados draft/pending_review/approved/rejected/suspended.
- [ ] Implementar Product/Service com estados draft/published/archived.
- [ ] Garantir que um usuário possa possuir mais de um estabelecimento.
- [ ] Implementar autorização server-side por estabelecimento.
- [ ] Implementar aprovação, rejeição e suspensão administrativa com motivo/auditoria.
- [ ] Impedir que estabelecimento pendente/rejeitado/suspenso apareça publicamente.

## Painel do proprietário
- [ ] Implementar cadastro e edição de estabelecimento com nome público, categoria, endereço estruturado e canal público de contato.
- [ ] Criar cadastro espontâneo em `pending_review`, sem publicação automática.
- [ ] Validar CEP, logradouro, número, bairro, município e UF sem depender de API externa; complemento é opcional.
- [ ] Implementar gerenciamento de categorias vinculadas.
- [ ] Implementar cadastro, edição, publicação e arquivamento de produtos/serviços.
- [ ] Implementar cadastro de WhatsApp público separado de contatos privados.
- [ ] Implementar cadastro opcional de Instagram público.
- [ ] Implementar upload com JPEG, PNG e WebP, limite de 5 MB por arquivo e até 5 imagens por estabelecimento e por produto/serviço.
- [ ] Validar tipo real, dimensões e conteúdo dos arquivos no servidor.
- [ ] Exibir estado de aprovação e orientação de correção ao responsável.

## Vitrine pública
- [ ] Implementar listagem e página pública de estabelecimentos elegíveis.
- [ ] Implementar detalhe público de produto/serviço.
- [ ] Implementar busca por nome de estabelecimento e produto/serviço.
- [ ] Implementar filtro por categoria.
- [ ] Exibir preço quando informado, disponibilidade declarada e data de atualização.
- [ ] Garantir que URLs diretas respeitem elegibilidade pública.
- [ ] Garantir que serializadores/endpoints não exponham telefone/e-mail privados ou dados fiscais.

## Contato e reserva externa P1
- [ ] Gerar link de WhatsApp com mensagem contextualizada e codificada para URL.
- [ ] Incluir loja, produto, quantidade e link público, sem dados pessoais do consumidor.
- [ ] Exigir revisão e envio manual pelo consumidor.
- [ ] Disponibilizar Instagram como alternativa com texto copiável e abertura do perfil/Direct.
- [ ] Não criar entidade, status, histórico ou sincronização de reserva.
- [ ] Tratar ausência/invalidade de contato e falha de abertura do canal.

## Segurança e qualidade
- [ ] Testar isolamento entre estabelecimentos de responsáveis diferentes.
- [ ] Testar estados e visibilidade pública.
- [ ] Testar busca e filtros com conteúdo não publicado.
- [ ] Testar upload por tipo real, dimensões, conteúdo, tamanho e limites de quantidade.
- [ ] Testar cadastro pendente e ausência de publicação antes da aprovação.
- [ ] Testar CSRF, abuso e enumeração de recursos privados.
- [ ] Testar links externos e ausência de dados pessoais na mensagem.
- [ ] Verificar acessibilidade e responsividade dos fluxos públicos e privados.

## Encerramento
- [ ] Atualizar CURRENT_STATE com evidências reais.
- [ ] Vincular PR, testes e evidências à spec.
- [ ] Não marcar tarefas concluídas sem implementação e validação.
