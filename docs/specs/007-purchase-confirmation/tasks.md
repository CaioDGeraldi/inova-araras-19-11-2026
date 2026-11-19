# Tasks | Spec 007 - Confirmação de compra presencial

## Preparação
- [ ] Revisar a spec e confirmar dependências com campanhas/cupons.
- [ ] Definir duração final do token após teste de usabilidade e segurança.
- [ ] Definir retenção e acesso aos registros de confirmação/auditoria.

## Domínio e serviços
- [ ] Modelar ConsumerIdentificationToken com hash, expiração, consumo e revogação.
- [ ] Modelar PurchaseConfirmation e relação com consumidor, loja, operador e campanhas avaliadas.
- [ ] Implementar serviço de emissão e validação de Meu QR.
- [ ] Implementar consumo único e invalidação de tokens expirados/revogados.
- [ ] Implementar serviço transacional de confirmação e avaliação de campanhas.
- [ ] Garantir idempotência por operação e unicidade de concessão por confirmação/campanha/regra.
- [ ] Permitir compras legítimas distintas do mesmo consumidor na mesma loja.

## Interfaces
- [ ] Disponibilizar Meu QR na conta do consumidor com validade/renovação visível.
- [ ] Adicionar Registrar compra ao painel do responsável.
- [ ] Exigir seleção/conferência da loja e identificação mínima do consumidor.
- [ ] Solicitar somente os campos requeridos pelas campanhas ativas.
- [ ] Apresentar resultado apenas após confirmação do servidor.

## Segurança e qualidade
- [ ] Testar expiração, revogação, consumo único e replay.
- [ ] Testar autorização por estabelecimento e acesso indevido.
- [ ] Testar reenvio idempotente e requisições concorrentes.
- [ ] Testar concessão em múltiplas campanhas elegíveis sem duplicidade.
- [ ] Testar falhas antes/depois do envio e recuperação pela chave de idempotência.
- [ ] Verificar que tokens e dados privados não aparecem em logs/respostas.
- [ ] Testar que leitura de QR não confirma venda.
- [ ] Testar que reserva, clique, check-in ou retirada isolada não geram benefício por compra.
- [ ] Documentar que a confirmação não comprova pagamento nem oferece antifraude absoluto.

## Encerramento
- [ ] Atualizar CURRENT_STATE com evidências reais de implementação/testes.
- [ ] Vincular PR e evidências à spec.
- [ ] Não marcar tarefas concluídas sem implementação e validação.
