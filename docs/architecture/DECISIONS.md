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

## Baseline funcional consolidada

- Priorizar jornada integrada: vitrine → cronograma → rota → check-in → progresso → retorno.
- Cronograma público é administrado centralmente; sugestões P1 passam por revisão e nunca publicam automaticamente.
- Rotas usam QR estático por parada, revogável e rotacionável atomicamente. Participação representa uma execução; check-in é único por participação/parada. Há fallback assistido por operador autorizado.
- Campanhas do primeiro release são criadas/publicadas pela administração; correções de resgate usam eventos compensatórios.
- Comunidade usa nota 1–5, comentário opcional até 1.000 caracteres, uma avaliação ativa por conta/alvo, moderação fundamentada e anonimato apenas público.
- Administração usa provisionamento privilegiado, auditoria de ações críticas, correções compensatórias e indicadores operacionais somente leitura.
- Django Admin pode atender operações internas iniciais; não duplicar regras de domínio no painel.
- Não implementar checkout, pagamento, entrega ou GPS contínuo.
- Desenvolvimento individual por fatias verticais.
- Se o prazo apertar, cortar funcionalidades periféricas antes do núcleo presencial.

## Dependências pré-produção

- Testar leitura de QR em navegadores móveis reais e escolher biblioteca/estratégia após spike.
- Formalizar política de retenção, exclusão, anonimização, acesso e descarte de dados/auditoria antes da produção.
- Confirmar estabelecimentos, atividades, locais e campanhas reais do piloto; marcar dados fictícios como demonstração.

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
