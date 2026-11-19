# Modelo de domínio | Vem pro Centro

Modelo conceitual do MVP. Não obriga implementação imediata de todas as entidades nem define todas as colunas físicas. A modelagem deve ser refinada em specs.

## Contextos

- **Identidade:** pessoas e autenticação.
- **Comércio:** estabelecimentos, categorias e catálogo.
- **Programação:** atividades e locais.
- **Circulação:** circuitos, paradas, participações e check-ins.
- **Incentivos:** campanhas, cupons e resgates.
- **Solicitações:** interesse/reserva e confirmação de compra, se incluídas.
- **Comunidade:** avaliações e denúncias, após política de moderação.

## Entidades

**User:** pessoa autenticada. Pode descobrir como visitante e participar de circuitos, solicitar contato, resgatar benefícios e avaliar. Pode ser responsável por vários estabelecimentos.

**Store:** estabelecimento participante, responsável principal, nome público, descrição, endereço, contatos públicos, categorias, estado de aprovação e auditoria. Dados privados do responsável não são expostos.

**Category:** classificação reutilizável de estabelecimento, produto/serviço ou atividade. Evitar taxonomia excessivamente rígida.

**Product:** produto ou serviço de Store. Preço e disponibilidade são declarados; imagem opcional; catálogo guarda data de atualização.

**Place:** local físico de atividade ou parada que não seja necessariamente loja, como praça ou espaço cultural. Não duplicar se Store já representar o local.

**Event:** atividade programada, com organizador, local, início, término opcional, categoria, estado, gratuidade/preço e indicação de inscrição. Pode relacionar-se a Store e Circuit.

**Circuit:** percurso temático publicado pela administração, com período opcional, regra de participação/conclusão, estado e paradas.

**CircuitStop:** parada de Circuit, com ordem sugerida, obrigatoriedade, instruções e referência a Store, Event ou Place. Deve possuir exatamente um alvo válido no MVP.

**CircuitParticipation:** participação de User em Circuit ou ocorrência do circuito. Controla início, estado e conclusão.

**CheckIn:** registro de tentativa/aceite de visita em CircuitStop, associado à participação. Guarda instante, resultado e referência segura ao token. Política de repetição explícita.

**Campaign:** ação promocional com responsável, período, estado, elegibilidade, benefício, limites, lojas envolvidas e responsável pelo custo.

**Coupon:** benefício emitido conforme Campaign, com identificador não previsível, destinatário quando individual, validade e estado.

**CouponRedemption:** registro de resgate, com cupom, consumidor, estabelecimento receptor, instante e operador. Resgate atômico.

**Reservation (opcional):** solicitação de interesse/reserva de User para Store. Não é pagamento nem garantia de estoque. Pode evoluir para accepted, declined, cancelled e completed.

**Review / Report (P1):** opinião de consumidor e denúncia/moderação. Anonimato apenas na apresentação pública; autoria permanece vinculada internamente.

## Relacionamentos

- User 1:N Store como owner.
- Store N:M Category.
- Store 1:N Product.
- Event N:1 Place e organizador; pode relacionar-se a Store e Circuit.
- Circuit 1:N CircuitStop.
- CircuitStop aponta para Store, Event ou Place.
- User 1:N CircuitParticipation; Circuit 1:N CircuitParticipation.
- CircuitParticipation 1:N CheckIn; CheckIn referencia CircuitStop.
- Campaign N:M Store; Campaign 1:N Coupon.
- Coupon 0..N CouponRedemption conforme regra; cupom de uso único tem no máximo um resgate.
- Reservation referencia User e Store; conclusão pode originar compra elegível.

## Estados e transições

**Store:** draft → pending_review → approved; pending_review → rejected; approved → suspended; suspended → approved após revisão. Rejected/suspended não aparece como participante público.

**Event:** draft → published → completed/archived; published → cancelled. Cancelamento preserva histórico e é exibido claramente.

**Circuit:** draft → published → active → archived; published/active pode ser cancelled. Participações existentes preservam contexto histórico mínimo.

**CircuitParticipation:** active → completed ou cancelled. Completed é terminal, salvo correção administrativa auditada.

**CheckIn:** submitted → accepted ou rejected. Check-in aceito não é apagado silenciosamente.

**Campaign:** draft → scheduled → active → ended; active pode ser paused/cancelled.

**Coupon:** issued → redeemed, expired ou cancelled. Cupom resgatado não volta a issued sem operação compensatória auditada.

**Reservation:** pending → accepted/declined/cancelled; accepted → completed/cancelled. Confirmação de compra é idempotente.

## Invariantes

1. User representa pessoa, não papel.
2. Apenas owner autorizado ou admin altera dados privados de Store.
3. Store não aprovado/suspenso não é apresentado como participante oficial.
4. Product não representa estoque transacional; disponibilidade é declarada.
5. Toda CircuitStop publicada possui alvo físico ou atividade definido.
6. CheckIn aceito pertence a participação válida e parada do mesmo circuito.
7. Duplicidade de check-in é bloqueada conforme política explícita.
8. Participação conclui somente quando a regra do circuito é satisfeita.
9. Nenhuma parada exige compra por padrão.
10. Campaign ativa possui período, regra, elegibilidade, limites e responsável pelo custo.
11. CouponRedemption é atômico conforme política do cupom.
12. Compra confirmada não gera benefício duplicado.
13. Cancelamentos e correções críticas deixam trilha de auditoria.
14. Dados privados não podem ser inferidos por endpoints públicos.

## Decisões de modelagem em aberto

- Circuito recorrente: CircuitEdition/Occurrence no MVP ou período simples.
- Check-in repetível por circuito, parada ou ocorrência.
- Token QR estático rotacionável ou token curto, conforme operação e ameaça de compartilhamento.
- Place separado ou endereço embutido, conforme reuso real.
- Campanha/cupons P1: confirmar após núcleo.
- Reserva: confirmar prioridade e política de expiração.

Não criar todas as entidades de uma vez. Primeira spec deve detalhar Store/Product e Event; próxima Circuit/CircuitStop/Participation/CheckIn. Campanhas e reservas entram em specs independentes.