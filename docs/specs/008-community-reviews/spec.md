# Spec 008 | Comunidade e avaliações

## Contexto
A comunidade permite que consumidores compartilhem experiências e que estabelecimentos respondam publicamente. O recurso precisa preservar críticas legítimas e oferecer mecanismos proporcionais para lidar com abuso, spam e exposição de dados pessoais.

## Objetivo
Permitir avaliações de estabelecimentos ou experiências, escolha de identificação pública, respostas oficiais dos estabelecimentos, denúncias e moderação administrativa auditável.

## Requisitos relacionados
RF-100 a RF-106; RNF de autenticação, autorização, privacidade, segurança, auditoria, acessibilidade e integridade aplicáveis.

## Prioridade
P1 do MVP. Pode ser removida do primeiro corte caso o tempo ameace a entrega da jornada P0, conforme a regra de corte do MVP.

## Atores e permissões
- Visitante: consulta avaliações e respostas públicas.
- Usuário autenticado: cria avaliação e denuncia conteúdo.
- Responsável principal: responde avaliações somente em estabelecimento sob sua responsabilidade.
- Administrador/moderador autorizado: consulta denúncias e aplica decisões de moderação.
- A autoria da avaliação permanece vinculada internamente à conta, mesmo quando a exibição pública é anônima.

## Incluído
- Avaliação de estabelecimento ou experiência.
- Nota e comentário conforme campos definidos no produto.
- Opção de exibição identificada ou anônima publicamente.
- Resposta oficial do estabelecimento.
- Denúncia de avaliação ou resposta.
- Fila administrativa de denúncias.
- Moderação com motivo, autor da decisão e instante.
- Preservação de críticas legítimas e histórico de ações.

## Excluído
- Selo de compra verificada ou visita verificada.
- Prova de compra por reserva, clique, check-in ou declaração do lojista.
- Discussões encadeadas, mensagens privadas ou chat.
- Ranking pago, avaliação patrocinada ou alteração comercial de nota.
- Moderação automatizada como decisão final.
- Reputação complexa, níveis ou pontuação de usuários.

## Fluxo principal
1. Visitante consulta avaliações públicas na página do estabelecimento/experiência.
2. Usuário autenticado envia avaliação e escolhe a forma de identificação pública.
3. O servidor associa a autoria à conta e publica conforme validações.
4. Responsável autorizado pode enviar resposta oficial.
5. Usuário autenticado pode denunciar avaliação ou resposta.
6. Denúncia entra em fila restrita; não remove conteúdo automaticamente.
7. Moderador analisa e registra decisão fundamentada.
8. Conteúdo que viola a política recebe medida proporcional; crítica legítima permanece publicada.

## Regras de domínio
- Nota é inteira de 1 a 5 estrelas.
- Comentário é opcional e limitado inicialmente a 1.000 caracteres; deve seguir a política da comunidade e não expor dados pessoais de terceiros.
- Uma conta mantém uma avaliação ativa por alvo (estabelecimento ou ocorrência/experiência). Edição é versionada, sem criar avaliação duplicada.
- Autor pode editar a própria avaliação. Exclusão lógica preserva trilha mínima, sujeita à política de retenção e aos direitos do titular.
- Responsável principal pode editar ou remover a própria resposta oficial; alterações são auditáveis e não alteram a avaliação original.
- Motivos de denúncia: spam/fraude, assédio/discriminação, conteúdo ilegal, exposição de dados pessoais, conflito de interesse e outro com justificativa curta.
- Denúncias repetidas são limitadas e sujeitas a rate limit. Denúncia não oculta automaticamente o conteúdo.
- Moderador decide manter, ocultar ou remover o conteúdo e registra motivo. Usuário afetado pode solicitar uma revisão uma vez pelo canal administrativo.
- Identificação pública usa nome de exibição escolhido pelo usuário. Nome legal, telefone, e-mail e ID interno nunca são publicados.
- Anonimato público preserva autoria interna restrita para moderação e obrigações operacionais.
- Retenção, exclusão e anonimização seguem política de privacidade publicada e solicitações válidas dos titulares. Não presumir prazo legal; aprovar prazo operacional antes da produção.

- RF-100: criar avaliação exige autenticação.
- RF-101: o usuário escolhe exibição identificada ou anônima publicamente.
- RF-102: autoria interna permanece vinculada à conta e acessível somente a perfis autorizados para moderação e obrigações operacionais.
- RF-103: responsável principal pode responder somente avaliações do próprio estabelecimento.
- RF-104: usuário autenticado pode denunciar conteúdo; a denúncia não remove automaticamente a publicação.
- RF-105: administração modera e registra motivo, decisão, moderador e instante.
- RF-106: avaliação negativa não é motivo suficiente para remoção.
- Uma avaliação não comprova compra, pagamento, visita ou presença.
- Não exibir dados pessoais do autor, mesmo quando identificado publicamente; a forma de identificação pública deve usar apenas informação expressamente permitida.
- Resposta do estabelecimento é claramente identificada como manifestação oficial e não altera avaliação ou nota.
- A autoria anônima publicamente não é anonimato perante a plataforma.
- Conteúdo moderado não deve ser apagado silenciosamente; preservar registro e trilha conforme política de retenção.
- Não permitir que estabelecimento denuncie ou remova diretamente avaliação como ação administrativa.
- Denúncias e dados de autoria não são públicos.
- Limites de avaliações, edição, exclusão, denúncia repetida e contestação devem ser definidos antes da implementação.

## Estados propostos
Review: published, hidden, removed.  
ReviewResponse: published, hidden, removed.  
Report: submitted, under_review, dismissed, action_taken.  
A transição de estado deve registrar autor, instante e motivo. Os estados finais e a política de retenção precisam ser validados antes da implementação.

## Privacidade e segurança
- Validar autenticação e autorização no servidor.
- Não confiar em identificadores de autor enviados pelo cliente.
- Restringir autoria interna, denúncias e fila de moderação.
- Proteger contra spam, abuso de denúncias e conteúdo malicioso.
- Não incluir telefone, e-mail ou identificador interno no conteúdo público.
- Definir retenção de avaliações, denúncias e autoria interna antes de produção.
- Registrar decisões sem armazenar dados pessoais desnecessários.
- Permitir acesso por teclado e leitor de tela; estados de moderação devem ser textuais, não apenas por cor.

## Critérios de aceitação
- [ ] Nota é inteira de 1 a 5 estrelas; comentário opcional até 1.000 caracteres.
- [ ] Há uma avaliação ativa por conta e alvo, com edição versionada e sem duplicidade.
- [ ] Autor pode editar; exclusão lógica preserva trilha mínima.
- [ ] Respostas oficiais podem ser editadas/removidas pelo responsável com auditoria, sem alterar a avaliação.
- [ ] Denúncias usam motivos publicados, limite de repetição e rate limit; não ocultam conteúdo automaticamente.
- [ ] Moderador decide manter, ocultar ou remover com motivo; usuário afetado pode solicitar uma revisão uma vez.
- [ ] Identificação pública usa nome de exibição escolhido ou anonimato, nunca nome legal, telefone, e-mail ou ID interno.

- [ ] Visitante consulta avaliações públicas sem login.
- [ ] Usuário autenticado cria avaliação de estabelecimento ou experiência.
- [ ] Usuário escolhe exibição identificada ou anônima publicamente.
- [ ] Avaliação anônima não expõe identidade pública e preserva autoria interna restrita.
- [ ] Responsável responde somente por estabelecimento sob sua responsabilidade.
- [ ] Resposta aparece como manifestação oficial e não altera a avaliação original.
- [ ] Usuário autenticado denuncia avaliação ou resposta.
- [ ] Denúncia não remove conteúdo automaticamente.
- [ ] Moderador autorizado consulta denúncia e registra decisão/motivo.
- [ ] Crítica legítima não é removida apenas por ser negativa.
- [ ] Conteúdo moderado deixa de aparecer publicamente conforme a decisão.
- [ ] Ações de moderação são auditáveis.
- [ ] Dados de autoria interna e denunciantes não aparecem publicamente.
- [ ] Testes cobrem autorização, anonimato público, denúncia, moderação e preservação de críticas legítimas.

