# Tasks | Spec 003 - Cronograma do Centro

## Preparação
- [ ] Definir categorias iniciais de atividade.
- [ ] Definir representação de Place e Organizer.
- [ ] Decidir como atividades recorrentes serão representadas.
- [ ] Definir campos obrigatórios e política de correção de sugestões P1.

## Domínio e administração P0
- [ ] Modelar Event e seus estados draft/published/cancelled/completed/archived.
- [ ] Implementar formulário administrativo de criação e edição.
- [ ] Validar título, descrição, início, término e local.
- [ ] Aplicar fuso America/Sao_Paulo na persistência e apresentação.
- [ ] Implementar publicação somente por administrador.
- [ ] Implementar cancelamento explícito sem apagar histórico.
- [ ] Implementar conclusão/arquivamento de atividades passadas.
- [ ] Implementar associação explícita opcional com Store e DiscoveryRoute.

## Consulta pública P0
- [ ] Implementar listagem por data e ordenação por horário.
- [ ] Implementar detalhe público com dados e condições da atividade.
- [ ] Exibir estado cancelado de forma textual e acessível.
- [ ] Ocultar rascunhos e sugestões não publicadas.
- [ ] Diferenciar agenda vazia de falha técnica.

## Recursos P1
- [ ] Modelar EventSuggestion e estados de revisão.
- [ ] Permitir envio de sugestão por responsável/organizador autenticado.
- [ ] Implementar fila de revisão administrativa para sugestões.
- [ ] Impedir publicação automática após aprovação da sugestão.
- [ ] Modelar SavedEvent com unicidade por conta/atividade.
- [ ] Permitir salvar/remover atividade com autenticação.
- [ ] Disponibilizar consulta pessoal de atividades salvas.
- [ ] Refletir alterações e cancelamentos na consulta de atividades salvas.
- [ ] Garantir que salvar não crie inscrição ou reserva de vaga.

## Segurança e qualidade
- [ ] Testar permissões administrativas e titularidade das atividades salvas.
- [ ] Testar transições de estado e publicação/cancelamento.
- [ ] Testar fuso horário, ordenação e término inválido.
- [ ] Testar sugestões privadas até publicação.
- [ ] Testar duplicidade de atividades salvas.
- [ ] Testar responsividade, teclado e leitor de tela.

## Encerramento
- [ ] Atualizar CURRENT_STATE com evidências reais.
- [ ] Vincular PR, testes e evidências à spec.
- [ ] Não marcar tarefas concluídas sem implementação e validação.
