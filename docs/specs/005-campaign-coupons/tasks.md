# Tasks | Spec 005 - Campanhas e cupons simples

## Preparação e regras comerciais
- [ ] Definir se proprietários podem criar campanhas no primeiro release ou se a autoria permanece centralizada na administração.
- [ ] Definir política para cupons emitidos quando campanha for pausada/cancelada.
- [ ] Definir compensação para resgate indevido e requisitos adicionais para benefícios de alto valor.
- [ ] Confirmar responsável pelo custo e regras de cada campanha demonstrativa.

## Domínio e elegibilidade
- [ ] Modelar Campaign, Coupon e CouponRedemption.
- [ ] Implementar estados e transições de campanha.
- [ ] Implementar regras versionadas de elegibilidade, período, limites, emissor e receptor.
- [ ] Impedir ativação de campanha sem responsável pelo custo.
- [ ] Implementar emissão de cupom individual opaco, não sequencial e associado à conta elegível.
- [ ] Integrar origem de elegibilidade por compra com Spec 007 sem duplicar a confirmação de compra.
- [ ] Integrar elegibilidade por conclusão de rota quando houver campanha configurada.

## Experiência do consumidor
- [ ] Exibir campanhas ativas e suas regras.
- [ ] Exibir cupons próprios com benefício, validade, estado e estabelecimento receptor.
- [ ] Apresentar código e QR como representações do mesmo identificador.
- [ ] Atualizar estado do cupom somente após confirmação do servidor.

## Resgate presencial
- [ ] Implementar tela Cupons e resgates no painel da loja.
- [ ] Permitir leitura de QR ou digitação do código.
- [ ] Implementar consulta preliminar sem consumir o cupom.
- [ ] Exibir somente dados mínimos para conferência.
- [ ] Exigir confirmação explícita após aplicação presencial do benefício.
- [ ] Revalidar regras e consumir cupom atomicamente.
- [ ] Impedir resgate por loja não participante ou operador sem autorização.

## Segurança e qualidade
- [ ] Testar elegibilidade, período, limites e estados de campanha.
- [ ] Testar código inexistente, inválido, expirado, cancelado e já resgatado.
- [ ] Testar duas tentativas concorrentes de resgate.
- [ ] Testar que consulta preliminar não consome cupom.
- [ ] Testar que WhatsApp, Instagram, captura de tela e conferência offline não validam resgate.
- [ ] Testar autorização cruzada entre estabelecimentos.
- [ ] Garantir que segredos de cupom não apareçam em logs.
- [ ] Testar falha de conexão e recuperação do estado do servidor.

## Encerramento
- [ ] Atualizar CURRENT_STATE com evidências reais.
- [ ] Vincular PR, testes e evidências à spec.
- [ ] Não marcar tarefas concluídas sem implementação e validação.
