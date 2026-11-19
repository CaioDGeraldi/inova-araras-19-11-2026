# Spec 003 | Cronograma do Centro

## Contexto
A programação é um motivo explícito para escolher quando visitar o Centro. O cronograma deve reunir eventos culturais, feiras, oficinas, apresentações, ações comerciais e experiências comunitárias em um local público e consultável.

## Objetivo
Permitir que a administração publique atividades e que visitantes consultem programação por data, horário, local e categoria sem criar conta. No P1, responsáveis podem sugerir atividades para aprovação e consumidores podem salvar atividades em sua conta, sem que isso se transforme em inscrição.

## Requisitos relacionados
RF-030 a RF-041; RNF-001 a RNF-012, RNF-022 a RNF-025, RNF-030, RNF-031, RNF-034.

## Atores e permissões
- Visitante: consultar atividades publicadas e seus detalhes.
- Usuário autenticado: salvar/remover atividades pessoais (P1).
- Admin: criar, editar, publicar e cancelar atividades.
- Responsável de estabelecimento/organizador autorizado: enviar sugestão de atividade para revisão (P1); não publica diretamente.
- Apenas administrador publica no MVP.

## Incluído
### P0
- Cadastro administrativo de atividade.
- Título, descrição, categoria, organizador, data, início, término opcional, local e condição gratuita/paga.
- Indicação de inscrição obrigatória/opcional.
- Listagem pública por data e detalhe da atividade.
- Estados draft, published, cancelled, completed/archived.

### P1
- Sugestão de atividade por responsável/organizador autenticado, sujeita à aprovação administrativa.
- Salvar e remover atividade na conta do consumidor.
- Consulta pessoal de atividades salvas.
- Atualização do estado da atividade salva quando houver edição ou cancelamento.
- Associação explícita de atividades com estabelecimentos e/ou Rotas de Descoberta.

## Excluído
- Venda de ingressos e pagamento.
- Capacidade e período de inscrição (RF-039, P2), inscrição completa, lista de presença e controle de vagas no primeiro corte.
- Notificações push ou lembretes.
- Publicação direta por estabelecimento/organizador.
- Integração com agenda externa sem autorização.

## Fluxo principal P0
1. Admin cria atividade em rascunho.
2. Informa dados obrigatórios e local.
3. Confirma que organizador e local estão operacionalmente alinhados.
4. Publica a atividade.
5. Visitante consulta cronograma e abre detalhes.
6. Se houver alteração, a página apresenta informação atualizada.
7. Se cancelada, atividade permanece identificada como cancelada.

## Fluxos P1
### Sugestão
1. Responsável/organizador autenticado envia uma sugestão com dados mínimos e referência de responsabilidade.
2. A sugestão permanece privada e pendente; não aparece no cronograma público.
3. Admin revisa dados e confirmação operacional do organizador/local.
4. Admin aprova para edição/publicação, solicita correção ou rejeita.
5. Somente a publicação administrativa torna a atividade visível.

### Salvar atividade
1. Visitante aciona salvar em lista ou detalhe.
2. Se não autenticado, realiza login/cadastro e retorna ao destino.
3. O servidor associa a atividade à conta autenticada.
4. A atividade aparece na área pessoal; o usuário pode removê-la.
5. Salvar não representa inscrição, reserva de vaga ou confirmação de presença.

## Regras
- Atividade publicada precisa ter título, descrição resumida, início e local.
- Horário é interpretado no fuso America/Sao_Paulo.
- Término, quando informado, deve ser posterior ao início.
- Cancelamento não apaga registros de participação nem desaparece silenciosamente.
- Atividade passada pode ser arquivada, preservando histórico.
- Gratuidade/preço e necessidade de inscrição devem ser explícitos.
- Não publicar atividade sem confirmação operacional do organizador/local.
- Sugestão pendente, rejeitada ou em correção não é conteúdo público.
- Responsável só consulta e altera a própria sugestão conforme o estado permitido; não altera atividade publicada diretamente.
- Uma atividade salva não garante vaga nem gera inscrição.
- A mesma conta não deve acumular vínculos duplicados para a mesma atividade.
- Notificações de alteração/cancelamento não fazem parte do primeiro corte; o estado atualizado aparece quando a pessoa consulta a atividade salva.
- Vínculos P1 com estabelecimento/rota são explícitos e não inferidos por proximidade ou nome.

## Dados e estados
Event: draft, published, cancelled, completed/archived.  
EventSuggestion (P1): pending, needs_changes, approved_for_publication, rejected. A aprovação não publica automaticamente.  
SavedEvent (P1): vínculo entre conta e atividade, removível pelo titular.  
Place: nome, endereço e instruções públicas suficientes para encontrar o local.  
Organizer: referência a usuário/organização responsável, com contato público opcional.

## Segurança, privacidade e acessibilidade
- Apenas admin publica no primeiro MVP.
- Sugestões e dados privados do organizador não são públicos.
- Não expor contato privado do organizador.
- Datas devem ser legíveis e consistentes em mobile.
- Cancelamento deve ser comunicado visualmente e por texto, não apenas por cor.
- Navegação por teclado e leitores de tela.
- A autorização de salvar/remover verifica titularidade da conta no servidor.

## Critérios de aceitação
### P0
- [ ] Admin cria, edita, publica e cancela atividade.
- [ ] Visitante consulta atividades sem login.
- [ ] Filtro/listagem por data apresenta atividades na ordem correta.
- [ ] Detalhe exibe data, horário, local, organizador, gratuidade/preço e inscrição.
- [ ] Atividade cancelada continua visível com estado claro.
- [ ] Data/hora respeita America/Sao_Paulo.
- [ ] Término inválido é recusado.
- [ ] Testes cobrem permissão, publicação, cancelamento e ordenação.

### P1
- [ ] Responsável/organizador autenticado pode enviar sugestão.
- [ ] Sugestão não aparece publicamente antes de publicação administrativa.
- [ ] Admin aprova, solicita correção ou rejeita sugestão.
- [ ] Usuário autenticado salva e remove atividade.
- [ ] Atividades salvas são consultáveis pela conta titular sem duplicidade.
- [ ] Salvar atividade não cria inscrição ou reserva de vaga.
- [ ] Alteração/cancelamento aparece no estado consultado da atividade salva.
- [ ] Testes cobrem autorização, duplicidade e estados da sugestão.

## Decisões em aberto
- Se atividades recorrentes serão representadas por ocorrências separadas.
- Quais categorias iniciais serão oferecidas.
- Se endereço será Place separado ou campo reutilizável no Event.
- Campos obrigatórios e política de correção de sugestões.
- Localização da área pessoal de atividades salvas na navegação.
