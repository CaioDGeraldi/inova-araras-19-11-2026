# Spec 005 | Campanhas e cupons simples

## Contexto

Fidelidade ao Centro e Campanhas Colaborativas conectam estabelecimentos por benefícios. O primeiro passo deve ser um cupom simples, transparente e controlado, sem criar uma carteira financeira de pontos antes da validação comercial.

## Objetivo

Permitir campanhas com regras e responsável definidos, emissão de cupons elegíveis e resgate presencial de uso único pelo estabelecimento autorizado, com validação online no servidor.

## Requisitos relacionados

RF-070 a RF-079, RF-082 a RF-084; RF-094 a RF-099 quando compra confirmada for fonte de elegibilidade; RNF-013 a RNF-025, RNF-028, RNF-029, RNF-039 a RNF-041. A mecânica de identificação e confirmação da compra é especificada em `docs/specs/007-purchase-confirmation/spec.md`.

## Atores e permissões

- **Admin:** cria e administra campanhas coletivas, define lojas, regras e responsável pelo custo.
- **Responsável da loja:** consulta e resgata cupons somente em estabelecimento sob sua responsabilidade e participante da campanha.
- **Consumidor:** consulta campanhas e cupons próprios, apresenta o benefício no estabelecimento.
- **Operador:** no MVP, é o responsável principal autenticado pela loja; não criar contas de equipe ou permissões granulares.

## Incluído

- Campaign com período, estado, descrição, benefício, elegibilidade, limites, lojas participantes e responsável pelo custo.
- Coupon individual com identificador opaco e não previsível, destinatário, validade e estado.
- Código textual e QR Code como duas representações do mesmo identificador.
- Consulta de cupons na conta do consumidor.
- Validação preliminar pelo painel do estabelecimento, por leitura do QR Code ou digitação do código.
- Confirmação explícita do resgate após aplicação presencial do benefício.
- CouponRedemption imutável e atômico, com consumidor, campanha/regra, loja receptora, operador e instante.
- Integração com PurchaseConfirmation como origem possível de elegibilidade; os detalhes do QR de consumidor, declaração de venda, idempotência e auditoria pertencem à Spec 007.

## Excluído

- Carteira de pontos e conversão monetária.
- Regras complexas de níveis, cashback ou crédito.
- Subsídio presumido pela plataforma ou governo.
- Benefício sem responsável financeiro/comercial.
- Checkout e pagamento.
- Validação por WhatsApp, Instagram, captura de tela ou conferência offline.
- Contas de funcionários, equipe ou permissões granulares no MVP.
- Verificação de identidade por CPF, documento ou dado sensível como regra geral.

## Origem por compra presencial

Quando a condição da campanha for compra, o consumidor apresenta **Meu QR** e o responsável principal autenticado confirma a venda presencial concluída no painel. O mecanismo completo, inclusive token temporário, validação server-side, campos mínimos, chave de idempotência, concorrência e limites antifraude, está definido na Spec 007 e no fluxo `docs/flows/PURCHASE_CONFIRMATION.md`.

A campanha não trata a leitura do QR como venda. A concessão ocorre somente após a declaração explícita do responsável e a validação da regra. Uma confirmação pode avaliar mais de uma campanha elegível. Compra espontânea também é aceita; reserva externa não é requisito.

## Fluxo principal

1. Admin cria campanha e informa regras, lojas emissoras/receptoras, benefício, período, limites, elegibilidade e responsável pelo custo.
2. Campanha é publicada após validação.
3. Consumidor autenticado consulta as regras e obtém cupom quando elegível.
4. O cupom aparece em Fidelidade ao Centro, associado à conta, com benefício, loja receptora, validade, estado e código/QR.
5. Consumidor comparece ao estabelecimento receptor e apresenta o código ou QR Code.
6. Responsável da loja entra no painel autenticado e abre **Cupons e resgates**.
7. Operador lê o QR Code com a câmera ou digita o código textual.
8. Servidor valida existência, estado, validade, campanha, elegibilidade, limites, loja receptora e autorização do operador.
9. Se válido, o painel mostra benefício, campanha, validade, loja receptora e dados mínimos para conferência. Essa consulta não consome o cupom.
10. O estabelecimento aplica o benefício na venda presencial.
11. O operador confirma **Concluir resgate** no painel.
12. O servidor repete as verificações e registra CouponRedemption e estado redeemed em uma única transação.
13. O consumidor vê o cupom como utilizado após a confirmação do servidor.
14. Tentativas posteriores são recusadas e informam que o cupom já foi utilizado.

## Regras

- Campanha ativa possui período, regra de elegibilidade, limites e responsável pelo custo.
- Benefício informa claramente o que é concedido e suas restrições.
- Campanha identifica emissor, estabelecimento receptor e responsável pelo custo.
- Benefício cruzado indica qual loja origina a elegibilidade e qual loja aceita o cupom.
- Cupom de uso único tem no máximo um resgate.
- Código textual e QR Code representam o mesmo identificador; não criar duas credenciais independentes.
- Identificador é aleatório, opaco e não sequencial. QR Code não inclui dados pessoais.
- Cupom individual fica associado ao consumidor elegível. O código é necessário para apresentação, mas não prova de forma absoluta a identidade de quem o apresenta.
- O operador vê somente dados mínimos necessários para conferir o benefício; não vê telefone, e-mail ou dados privados do consumidor.
- A consulta preliminar não reserva nem consome o cupom. Se o consumidor desistir antes da confirmação, o cupom permanece emitido, desde que válido.
- A confirmação ocorre depois de o benefício ser aplicado na venda presencial. O servidor revalida as condições e consome o cupom atomicamente.
- Captura de tela não comprova validade. O painel consulta o servidor no momento do resgate.
- Loja não participante ou operador sem autorização não pode consultar detalhes nem resgatar o cupom.
- Cupom expirado, cancelado, já resgatado ou incompatível com a loja é recusado.
- Pausar/cancelar campanha impede operações futuras conforme regra publicada, preservando cupons emitidos segundo política explícita.
- Regras não podem ser alteradas retroativamente para invalidar cupom emitido sem política de migração/comunicação.
- Nenhuma recompensa pode ser emitida sem financiador ou responsável comercial.
- Correções e compensações após resgate exigem operação administrativa auditada; não reabrir o cupom silenciosamente.

## Estados

Campaign: draft, scheduled, active, paused, ended, cancelled.  
Coupon: issued, redeemed, expired, cancelled.  
Redemption é registro histórico, não estado editável. A validação preliminar não cria estado intermediário persistente.

## Concorrência e segurança

- Confirmação de resgate é transacional e protegida por unicidade/lock apropriado.
- Revalidação e gravação de CouponRedemption/estado redeemed acontecem na mesma transação.
- Identificadores não são sequenciais nem previsíveis.
- Validar operador, loja receptora, campanha, validade e elegibilidade no servidor.
- Aplicar limitação de tentativas para códigos inválidos e evitar respostas que permitam enumerar cupons.
- Auditar emissão, alteração de regras, pausa, cancelamento e resgate.
- Não registrar segredo completo do cupom em logs.
- Falha de conexão não pode ser apresentada como resgate concluído; consultar estado do servidor antes de repetir.
- O código pode ser compartilhado; validação online e uso único reduzem risco, mas não provam a identidade física do portador. Benefícios de alto valor podem exigir verificação adicional definida pela campanha, sem documento por padrão.

## Critérios de aceitação
- [ ] Apenas administração cria e publica campanhas no primeiro release.
- [ ] Correção de resgate indevido usa evento compensatório vinculado ao original, com motivo, operador e instante; original permanece intacto.
- [ ] Campanha pode exigir validação adicional para benefício de alto valor sem exigir documento pessoal por padrão.
- [ ] Leitura QR é testada em navegadores móveis reais antes da escolha da biblioteca/estratégia técnica.


- [ ] Admin cria campanha com período, regra, lojas e responsável pelo custo.
- [ ] Campanha incompleta ou sem responsável não pode ser ativada.
- [ ] Consumidor consulta regras antes de aderir.
- [ ] Responsável autorizado escaneia Meu QR, confere a conta e confirma explicitamente a compra concluída.
- [ ] Token expirado, revogado, inválido ou consumido é recusado; leitura isolada não registra venda.
- [ ] Compra espontânea pode ser confirmada sem reserva prévia.
- [ ] Uma confirmação avalia todas as campanhas aplicáveis e não duplica concessões.
- [ ] Cupom é emitido apenas para usuário elegível e associado à sua conta.
- [ ] Consumidor consulta o cupom e apresenta código ou QR Code no estabelecimento.
- [ ] QR Code e código textual representam o mesmo identificador.
- [ ] Responsável autenticado abre Cupons e resgates no painel da loja elegível.
- [ ] Operador lê QR Code ou digita o código.
- [ ] Validação preliminar consulta o servidor e não consome o cupom.
- [ ] Benefício, validade e loja receptora são apresentados antes da confirmação.
- [ ] Loja não participante ou operador sem autorização não consegue consultar detalhes nem resgatar.
- [ ] Cupom expirado, cancelado, inexistente, incompatível ou já resgatado é recusado.
- [ ] Confirmação após aplicação presencial consome o cupom e cria um registro de resgate.
- [ ] Duas tentativas simultâneas não geram dois resgates.
- [ ] Falha técnica não é apresentada como sucesso.
- [ ] Emissor, consumidor, receptor, operador e instante ficam auditáveis.
- [ ] Dados privados e segredo completo não aparecem em logs.
- [ ] Pausar/cancelar campanha impede operações futuras conforme regra.
- [ ] Testes cobrem autorização, validade, elegibilidade, rate limit e concorrência.

## Decisões consolidadas

- Resgate presencial e validado pelo painel autenticado do estabelecimento receptor.
- Código textual e QR Code são duas representações do mesmo identificador.
- Validação preliminar não consome o cupom; confirmação posterior à aplicação do benefício consome atomicamente.
- No MVP, o operador é o responsável principal autenticado pela loja.
- WhatsApp e Instagram não validam cupons.

## Decisões consolidadas

- No primeiro release, campanhas são criadas e publicadas pela administração. Criação individual por proprietários fica fora do MVP.
- Resgate indevido é corrigido por operação/evento compensatório vinculado ao resgate original, com motivo, operador autorizado e instante. O registro original nunca é editado ou excluído.
- Campanha pode exigir validação adicional para benefício de alto valor, mas não exige documento pessoal por padrão.
- Leitura de QR deve ser testada em navegadores móveis reais. Escolha de biblioteca e estratégia técnica é decisão de implementação após spike, não decisão de produto.
- Toda campanha declara emissor, receptor, responsável pelo custo, período, elegibilidade e limites.
- A confirmação de compra presencial da Spec 007 é a fonte de elegibilidade por compra. Uma confirmação avalia todas as campanhas elegíveis para a loja.
