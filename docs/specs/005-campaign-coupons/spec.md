# Spec 005 | Campanhas e cupons simples

## Contexto
Fidelidade ao Centro e Campanhas Colaborativas conectam estabelecimentos por benefícios. O primeiro passo deve ser um cupom simples, transparente e controlado, sem criar uma carteira financeira de pontos antes da validação comercial.

## Objetivo
Permitir campanhas com regras e responsável definidos, emissão de cupons elegíveis e resgate único por estabelecimento autorizado.

## Requisitos relacionados
RF-070 a RF-079; RF-094 a RF-095 quando compra confirmada for fonte de elegibilidade; RNF-013 a RNF-025, RNF-028, RNF-029.

## Atores e permissões
- Admin: cria e administra campanhas coletivas.
- Owner: cria campanhas limitadas ao próprio estabelecimento, se habilitado.
- Consumidor: consulta campanha e recebe/resgata cupom elegível.
- Operador autorizado da loja: valida resgate.

## Incluído
- Campaign com período, estado, descrição, benefício, elegibilidade, limites, lojas participantes e responsável pelo custo.
- Coupon individual com identificador não previsível e validade.
- Emissão manual ou por evento de negócio definido na campanha.
- Resgate único com confirmação no servidor.
- Histórico de emissão e resgate.

## Excluído
- Carteira de pontos e conversão monetária.
- Regras complexas de níveis, cashback ou crédito.
- Subsídio presumido pela plataforma ou governo.
- Benefício sem responsável financeiro.
- Checkout e pagamento.

## Fluxo principal
1. Admin cria campanha e informa regras, lojas, benefício, período e responsável pelo custo.
2. Campanha é publicada após validação.
3. Consumidor consulta campanha e obtém cupom quando elegível.
4. No estabelecimento receptor, consumidor apresenta o cupom.
5. Operador autorizado solicita validação.
6. Servidor verifica estado, validade, elegibilidade, estabelecimento e limite.
7. Servidor registra resgate atomicamente e retorna confirmação.
8. Tentativa repetida informa que o cupom já foi utilizado.

## Regras
- Campanha ativa possui período e regra de elegibilidade.
- Benefício informa claramente o que é concedido e suas restrições.
- Campanha identifica emissor, estabelecimento receptor e responsável pelo custo.
- Benefício cruzado precisa indicar qual loja concede e qual loja aceita, sem ambiguidade.
- Cupom de uso único tem no máximo um resgate.
- Resgate não pode depender apenas de validação no cliente.
- Cancelamento/pausa impede novas emissões/resgates conforme regra explícita.
- Regras não podem ser alteradas retroativamente para invalidar cupom emitido sem política de migração/comunicação.
- Nenhuma recompensa pode ser emitida sem financiador ou responsável comercial.

## Estados
Campaign: draft, scheduled, active, paused, ended, cancelled.  
Coupon: issued, redeemed, expired, cancelled.  
Redemption é registro histórico, não estado editável.

## Concorrência e segurança
- Resgate é transacional e protegido por unicidade/lock apropriado.
- Identificadores não são sequenciais nem previsíveis.
- Validar operador, loja receptora e elegibilidade no servidor.
- Auditar emissão, alteração de regras, pausa, cancelamento e resgate.
- Não registrar segredo completo do cupom em logs.

## Critérios de aceitação
- [ ] Admin cria campanha com período, regra, lojas e responsável pelo custo.
- [ ] Campanha incompleta ou sem responsável não pode ser ativada.
- [ ] Consumidor consulta regras antes de aderir.
- [ ] Cupom é emitido apenas para usuário elegível.
- [ ] Loja não participante não consegue resgatar cupom.
- [ ] Cupom expirado/cancelado/resgatado é recusado.
- [ ] Duas tentativas simultâneas não geram dois resgates.
- [ ] Emissor, consumidor, receptor e instante ficam auditáveis.
- [ ] Pausar/cancelar campanha impede operações futuras conforme regra.
- [ ] Testes cobrem autorização, validade, elegibilidade e concorrência.

## Decisões em aberto
- Se campanhas/cupons entram no primeiro piloto ou após Rotas de Descoberta.
- Modelo de código apresentado: QR dinâmico, código curto ou ambos.
- Quem pode emitir campanhas individuais no primeiro release.
- Política de compensação quando cupom é resgatado indevidamente.
