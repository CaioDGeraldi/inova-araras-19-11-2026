# Modelo de domínio | Vem pro Centro

Modelo conceitual do MVP. Não obriga implementação imediata de todas as entidades nem define todas as colunas físicas. A modelagem deve ser refinada em specs.

## Contextos

- **Identidade:** pessoas e autenticação.
- **Comércio:** estabelecimentos, categorias e catálogo.
- **Programação:** atividades e locais.
- **Circulação:** rotas, paradas, participações e check-ins.
- **Incentivos:** campanhas, cupons e resgates.
- **Contato comercial:** canais públicos e encaminhamento de pedidos de reserva para conversas externas.
- **Comunidade:** avaliações e denúncias, após política de moderação.
- **Inteligência comercial:** sinais agregados de busca, cobertura de oferta, pesquisas e relatórios institucionais.

## Entidades

**User:** pessoa autenticada. Pode descobrir como visitante e participar de rotas, solicitar contato, resgatar benefícios e avaliar. Pode ser responsável por vários estabelecimentos.

**Store:** estabelecimento participante, responsável principal, nome público, descrição, endereço, canais públicos de contato (WhatsApp e Instagram inicialmente), categorias, estado de aprovação e auditoria. Os contatos públicos são declarados pelo responsável e separados de seus dados privados.

**Category:** classificação reutilizável de estabelecimento, produto/serviço ou atividade. Evitar taxonomia excessivamente rígida.

**Product:** produto ou serviço de Store. Preço e disponibilidade são declarados; imagem opcional; catálogo guarda data de atualização.

**Place:** local físico de atividade ou parada que não seja necessariamente loja, como praça ou espaço cultural. Não duplicar se Store já representar o local.

**Event:** atividade programada, com organizador, local, início, término opcional, categoria, estado, gratuidade/preço e indicação de inscrição. Pode relacionar-se a Store e DiscoveryRoute.

**DiscoveryRoute:** percurso temático publicado pela administração, com período opcional, regra de participação/conclusão, estado e paradas.

**RouteStop:** parada de DiscoveryRoute, com ordem sugerida, obrigatoriedade, instruções e referência a Store, Event ou Place. Deve possuir exatamente um alvo válido no MVP.

**RouteParticipation:** participação de User em DiscoveryRoute ou ocorrência da rota. Controla início, estado e conclusão.

**CheckIn:** registro de tentativa/aceite de visita em RouteStop, associado à participação. Guarda instante, resultado e referência segura ao token. Política de repetição explícita.

**Campaign:** ação promocional com responsável, período, estado, elegibilidade, benefício, limites, lojas envolvidas e responsável pelo custo.

**Coupon:** benefício emitido conforme Campaign, com identificador não previsível, destinatário quando individual, validade e estado.

**CouponRedemption:** registro de resgate, com cupom, consumidor, estabelecimento receptor, instante e operador. Resgate atômico.

**Review / Report (P1):** opinião de consumidor e denúncia/moderação. Anonimato apenas na apresentação pública; autoria permanece vinculada internamente.

**SearchSignal (P2):** evento minimizado de busca sem resultado ou com baixa cobertura. Deve evitar identidade, identificadores persistentes, localização precisa e armazenamento desnecessário de texto livre. Os eventos brutos têm acesso restrito e retenção limitada.

**DemandAggregate (P2):** indicador agregado por categoria e período, calculado a partir de sinais de busca, cobertura do catálogo, disponibilidade declarada e pesquisas. Armazena período, metodologia, cobertura, limiar aplicado e nível de confiança; não contém linhas individuais.

**FieldSurvey (P2):** definição de pesquisa voluntária, com finalidade, público, método, período, questionário, responsável e política de retenção.

**SurveyResult (P2):** resultado agregado de pesquisa, com tamanho de amostra, método de recrutamento, período, limitações e supressão de grupos pequenos. Respostas individuais não são disponibilizadas no painel institucional.

**InstitutionalAccess / AuditEntry (P2):** autorização de acesso ao painel por finalidade e perfil, com trilha de auditoria de visualização, exportação e alteração de permissões.

## Relacionamentos

- User 1:N Store como owner.
- Store N:M Category.
- Store 1:N Product.
- Event N:1 Place e organizador; pode relacionar-se a Store e DiscoveryRoute.
- DiscoveryRoute 1:N RouteStop.
- RouteStop aponta para Store, Event ou Place.
- User 1:N RouteParticipation; DiscoveryRoute 1:N RouteParticipation.
- RouteParticipation 1:N CheckIn; CheckIn referencia RouteStop.
- Campaign N:M Store; Campaign 1:N Coupon.
- Coupon 0..N CouponRedemption conforme regra; cupom de uso único tem no máximo um resgate.
- O encaminhamento de reserva gera apenas um link de contato externo com contexto de Store/Product; não cria entidade transacional nem estado de reserva na plataforma.
- SearchSignal alimenta agregações sem expor evento individual; DemandAggregate pode ser contextualizado por FieldSurvey/SurveyResult.
- Acesso institucional consulta somente DemandAggregate e SurveyResult agregados, com AuditEntry.

## Estados e transições

**Store:** draft → pending_review → approved; pending_review → rejected; approved → suspended; suspended → approved após revisão. Rejected/suspended não aparece como participante público.

**Event:** draft → published → completed/archived; published → cancelled. Cancelamento preserva histórico e é exibido claramente.

**DiscoveryRoute:** draft → published → active → archived; published/active pode ser cancelled. Participações existentes preservam contexto histórico mínimo.

**RouteParticipation:** active → completed ou cancelled. Completed é terminal, salvo correção administrativa auditada.

**CheckIn:** submitted → accepted ou rejected. Check-in aceito não é apagado silenciosamente.

**Campaign:** draft → scheduled → active → ended; active pode ser paused/cancelled.

**Coupon:** issued → redeemed, expired ou cancelled. Cupom resgatado não volta a issued sem operação compensatória auditada.

## Invariantes

1. User representa pessoa, não papel.
2. Apenas owner autorizado ou admin altera dados privados de Store.
3. Store não aprovado/suspenso não é apresentado como participante oficial.
4. Product não representa estoque transacional; disponibilidade é declarada.
5. Toda RouteStop publicada possui alvo físico ou atividade definido.
6. CheckIn aceito pertence a participação válida e parada do mesma rota.
7. Duplicidade de check-in é bloqueada conforme política explícita.
8. Participação conclui somente quando a regra da rota é satisfeita.
9. Nenhuma parada exige compra por padrão.
10. Campaign ativa possui período, regra, elegibilidade, limites e responsável pelo custo.
11. CouponRedemption é atômico conforme política do cupom.
12. Compra confirmada não gera benefício duplicado.
13. Cancelamentos e correções críticas deixam trilha de auditoria.
14. Dados privados não podem ser inferidos por endpoints públicos.
15. Indicadores institucionais não permitem reidentificar consumidores ou estabelecimentos por filtros, períodos ou grupos pequenos.
16. Busca sem resultado é sinal de cobertura insuficiente na plataforma, não prova de inexistência da oferta no Centro.
17. Pesquisas voluntárias apresentam método, amostra e limitações; amostras de conveniência não são representativas por padrão.

## Decisões de modelagem em aberto

- Rota recorrente: RouteEdition/Occurrence no MVP ou período simples.
- Check-in repetível por rota, parada ou ocorrência.
- Token QR estático rotacionável ou token curto, conforme operação e ameaça de compartilhamento.
- Place separado ou endereço embutido, conforme reuso real.
- Campanha/cupons P1: confirmar após núcleo.
- Definir política editorial e validação dos canais públicos de contato do estabelecimento.

Não criar todas as entidades de uma vez. Primeira spec deve detalhar Store/Product e Event; próxima DiscoveryRoute/RouteStop/Participation/CheckIn. Campanhas e confirmação de compra entram em specs independentes. Links externos de contato não criam entidade de reserva na plataforma.