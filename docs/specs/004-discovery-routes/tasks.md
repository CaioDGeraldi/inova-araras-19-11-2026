# Tasks | Spec 004 - Rotas de Descoberta

## Preparação e decisões

## Domínio e administração P0
- [ ] Modelar DiscoveryRoute e RouteStop.
- [ ] Modelar vínculos exclusivos da parada com Store, Event ou Place.
- [ ] Implementar criação/edição de rota em rascunho.
- [ ] Implementar ordem sugerida, obrigatoriedade/opcionalidade e instruções.
- [ ] Validar ao menos uma parada e regra explícita de conclusão antes de publicar.
- [ ] Implementar publicação, ativação, cancelamento e arquivamento.
- [ ] Gerar token QR estático, aleatório, opaco e não sequencial por parada, sem PII.
- [ ] Implementar revogação e rotação atômica do token, invalidando o anterior.
- [ ] Implementar revogação imediata de token comprometido (P0).

## Participação e check-in P0
- [ ] Implementar consulta pública de lista, detalhe e paradas.
- [ ] Implementar início autenticado de participação.
- [ ] Implementar validação server-side de token, rota, parada, período e participação.
- [ ] Implementar gravação transacional de CheckIn com unicidade por participação e parada.
- [ ] Modelar cada RouteParticipation como uma execução da rota; nova execução cria nova participação.
- [ ] Implementar check-in assistido por operador autorizado como fallback, registrando operador, participante, parada, instante e motivo.
- [ ] Impedir duplicidade conforme política definida e restrições do banco.
- [ ] Calcular progresso somente com check-ins aceitos.
- [ ] Concluir participação conforme regra explícita.
- [ ] Preservar histórico em cancelamentos e correções.

## Recursos P1
- [ ] Implementar histórico de rotas e check-ins da conta.
- [ ] Implementar rotação atômica de token quando a política P1 for aprovada.
- [ ] Manter edições/ocorrências programadas e DiscoveryRouteEdition fora do MVP.

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
