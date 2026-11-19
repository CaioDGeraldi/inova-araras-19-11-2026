# Registro de decisões | Centro em Movimento

Este documento separa decisões adotadas, recomendações para o MVP e hipóteses/dependências. Uma recomendação só vira decisão aprovada quando validada pelo responsável do produto.

## Decisões consolidadas

- Iniciativa: **Centro em Movimento**.
- A confirmação manual de compra presencial integra o P1 junto a campanhas e cupons simples.
- Consumidor autenticado apresenta Meu QR, token temporário, opaco, rotativo e sem dados pessoais; o responsável principal autenticado escaneia, confere a conta e declara explicitamente a venda concluída.
- Leitura de QR não confirma compra. A confirmação é declaração auditável do responsável, não prova de pagamento nem integração com PDV/caixa/fiscal.
- Uma confirmação avalia todas as campanhas de compra elegíveis para a loja; valor total só é solicitado quando a regra exigir.
- Compra espontânea pode ser registrada sem reserva prévia. Reserva, clique, visita, retirada isolada e check-in não comprovam compra.
- Idempotência protege contra reenvio técnico sem bloquear compras legítimas distintas do mesmo consumidor na mesma loja.
- Meu QR, QR de rota e QR de cupom são mecanismos separados.

- Plataforma: **Vem pro Centro**.
- Rotas de Descoberta é a proposta de circulação e descoberta presencial, não apenas uma lista de lojas.
- Cronograma do Centro integra a experiência do Vem pro Centro.
- Fidelidade ao Centro conecta campanhas e benefícios entre estabelecimentos.
- Uma identidade individual pode atuar como consumidor e responsável por lojas.
- Descoberta pública não exige login.
- Estoque é declarado, não em tempo real.
- Pedido de reserva acontece por conversa externa iniciada na vitrine, prioritariamente pelo WhatsApp com mensagem pré-preenchida; a plataforma não controla o estado da conversa.
- MVP usa monólito modular Django, sujeito à validação da fundação.
- Vaga Legal é o nome correto.
- PRD define visão; MVP limita escopo; requisitos detalham comportamento; domínio define estados/invariantes; specs orientam mudanças.

## Recomendações como baseline do MVP

- Priorizar jornada integrada: vitrine → cronograma → rota → check-in → progresso → retorno.
- Cronograma público gerenciado inicialmente pela administração.
- DiscoveryRouteos com paradas que podem representar estabelecimento, atividade ou local.
- Check-in por QR Code como registro de participação, sem alegar prova absoluta de presença.
- Não exigir compra em cada parada.
- Campanhas simples/cupom antes de carteira complexa de pontos.
- Django Admin para operações internas iniciais.
- Não implementar checkout, pagamento, entrega ou GPS contínuo.
- Desenvolvimento individual por fatias verticais.
- Se o prazo apertar, cortar funcionalidades periféricas antes do núcleo presencial.

## Recomendações dependentes de confirmação operacional

- Se o botão de mensagem contextualizada pelo WhatsApp entra no primeiro slice executável ou logo após estabilizar a vitrine; o cadastro do número público faz parte dos dados de contato do estabelecimento.
- Se campanhas/cupons entram no primeiro MVP executável ou após rota.
- Se avaliações entram no piloto inicial.
- Se check-in permite repetição por parada, ocorrência ou período.
- Se eventos terão inscrição/limite de participantes no piloto.
- Quais estabelecimentos, atividades, locais e campanhas estarão efetivamente disponíveis.

## Hipóteses e parâmetros não aprovados

- Taxa de 1 ponto por real e validade de 12 meses são parâmetros propostos, não defaults definitivos.
- Benefício cruzado depende de financiador/responsável e regras aceitas pelas lojas.
- Participação institucional, divulgação, capacitação, subsídios e incentivos dependem de acordo formal.
- Integração Vaga Legal depende de fonte autorizada e viabilidade.
- Dados sobre fechamento de lojas e impacto econômico local precisam de baseline.
- Check-in por QR pode ser compartilhado; risco de fraude deve ser comunicado e mitigado.

## Restrições explícitas

- Não presumir API, parceria, subsídio, financiamento ou dado em tempo real.
- Não afirmar causalidade econômica a partir de uso da plataforma.
- Não coletar localização contínua.
- Não conceder benefício sem regra, elegibilidade, limite e responsável pelo custo.
- Não implementar permissões granulares sem caso real.
- Não criar caixa de entrada, entidade de reserva, status local ou integração de mensagens no MVP.
- Não duplicar FractawProjects: o repositório do produto guarda contexto, specs e estado; FractawProjects conduz agentes e workflow.
- Não fazer merge sem autorização explícita.
