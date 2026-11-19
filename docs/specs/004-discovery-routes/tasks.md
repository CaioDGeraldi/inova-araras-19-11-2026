# Tasks | Spec 004 - Rotas de Descoberta

## Preparação e decisões
- [ ] Definir política de repetição e reentrada de participação.
- [ ] Definir se QR será estático revogável ou token de curta duração no piloto.
- [ ] Definir se haverá fallback assistido para check-in.
- [ ] Definir política para alteração/cancelamento de rota com participações ativas.

## Domínio e administração P0
- [ ] Modelar DiscoveryRoute e RouteStop.
- [ ] Modelar vínculos exclusivos da parada com Store, Event ou Place.
- [ ] Implementar criação/edição de rota em rascunho.
- [ ] Implementar ordem sugerida, obrigatoriedade/opcionalidade e instruções.
- [ ] Validar ao menos uma parada e regra explícita de conclusão antes de publicar.
- [ ] Implementar publicação, ativação, cancelamento e arquivamento.
- [ ] Gerar token de check-in por parada sem PII ou identificador sequencial.
- [ ] Implementar revogação imediata de token comprometido (P0).

## Participação e check-in P0
- [ ] Implementar consulta pública de lista, detalhe e paradas.
- [ ] Implementar início autenticado de participação.
- [ ] Implementar validação server-side de token, rota, parada, período e participação.
- [ ] Implementar gravação transacional de CheckIn.
- [ ] Impedir duplicidade conforme política definida e restrições do banco.
- [ ] Calcular progresso somente com check-ins aceitos.
- [ ] Concluir participação conforme regra explícita.
- [ ] Preservar histórico em cancelamentos e correções.

## Recursos P1
- [ ] Implementar histórico de rotas e check-ins da conta.
- [ ] Implementar rotação atômica de token quando a política P1 for aprovada.
- [ ] Avaliar suporte a edições/ocorrências de rota sem quebrar participações existentes.

## Segurança e qualidade
- [ ] Testar usuário não autenticado, rota encerrada e participação incompatível.
- [ ] Testar token inválido, expirado e revogado.
- [ ] Testar revogação imediata.
- [ ] Testar reenvio e concorrência sem duplicidade.
- [ ] Testar regras com paradas obrigatórias e opcionais.
- [ ] Testar que check-in não exige compra nem GPS contínuo.
- [ ] Verificar que tokens não aparecem em logs ou mensagens.
- [ ] Testar acessibilidade e feedback de falhas de rede.

## Encerramento
- [ ] Atualizar CURRENT_STATE com evidências reais.
- [ ] Vincular PR, testes e evidências à spec.
- [ ] Não marcar tarefas concluídas sem implementação e validação.
