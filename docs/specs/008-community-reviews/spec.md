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

## Decisões em aberto antes da implementação
- Escala da nota e se comentário será opcional.
- Limite de tamanho e política de conteúdo.
- Uma avaliação por usuário/estabelecimento ou por experiência/ocorrência.
- Política de edição e exclusão pelo autor.
- Política de edição e exclusão de respostas pelo responsável.
- Motivos de denúncia, limites de frequência e prevenção de abuso.
- Critérios objetivos, prazo e mecanismo de contestação da moderação.
- Política de retenção e atendimento a solicitações de titulares.
- Forma de identificação pública permitida para avaliações identificadas.
