# Requisitos funcionais | Vem pro Centro

IDs estáveis para rastreabilidade entre PRD, specs, Issues, implementação e testes. P0 = obrigatório para a jornada do MVP; P1 = após o núcleo estável; P2 = evolução.

## A. Identidade e autorização

| ID | Prioridade | Requisito |
|---|---|---|
| RF-001 | P0 | Permitir cadastro de conta individual com dados mínimos. |
| RF-002 | P0 | Permitir autenticação e encerramento de sessão. |
| RF-003 | P1 | Permitir recuperação de senha. |
| RF-004 | P0 | Uma conta pode atuar como consumidor e responsável por estabelecimentos. |
| RF-005 | P0 | Autorizar ações privadas no servidor, verificando usuário e recurso. |
| RF-006 | P1 | Permitir atualização de dados e solicitação de exclusão conforme retenção. |

## B. Estabelecimentos

| ID | Prioridade | Requisito |
|---|---|---|
| RF-010 | P0 | Responsável autenticado pode cadastrar estabelecimento. |
| RF-011 | P0 | Estabelecimento possui nome público, descrição, endereço, canais de contato públicos e situação. |
| RF-018 | P0 | Responsável pode cadastrar e atualizar o número público de WhatsApp do estabelecimento, separado de seus contatos privados. |
| RF-012 | P0 | Estabelecimento pode possuir múltiplas categorias. |
| RF-013 | P0 | Estabelecimento possui responsável principal. |
| RF-014 | P0 | Responsável pode editar o próprio estabelecimento. |
| RF-015 | P0 | Administração pode aprovar, rejeitar ou suspender estabelecimento. |
| RF-016 | P0 | Apenas estabelecimentos aprovados e ativos aparecem como participantes oficiais. |
| RF-017 | P1 | Estabelecimento pode manter imagens e horário de funcionamento. |

## C. Catálogo e descoberta

| ID | Prioridade | Requisito |
|---|---|---|
| RF-020 | P0 | Responsável pode cadastrar, editar, publicar e arquivar produtos/serviços. |
| RF-021 | P0 | Produto/serviço pode conter nome, descrição, preço opcional, imagem opcional e disponibilidade declarada. |
| RF-022 | P0 | Exibir data de atualização do catálogo. |
| RF-023 | P0 | Visitante consulta vitrine sem autenticação. |
| RF-024 | P0 | Pesquisar estabelecimentos por nome. |
| RF-025 | P0 | Pesquisar produtos/serviços por nome. |
| RF-026 | P0 | Filtrar estabelecimentos por categoria. |
| RF-027 | P0 | Acessar página pública do estabelecimento e produtos/serviços. |
| RF-028 | P1 | Filtrar por região/proximidade sem rastreamento contínuo. |

## D. Cronograma do Centro

| ID | Prioridade | Requisito |
|---|---|---|
| RF-030 | P0 | Administração cria, edita, publica e cancela atividades. |
| RF-031 | P0 | Atividade contém título, descrição, data, horário, local, categoria e organizador. |
| RF-032 | P0 | Atividade informa se é gratuita/paga e se exige inscrição. |
| RF-033 | P0 | Visitante consulta cronograma sem autenticação. |
| RF-034 | P0 | Consultar atividades por data. |
| RF-035 | P0 | Acessar detalhes de atividade. |
| RF-036 | P0 | Atividade cancelada permanece identificável e informa cancelamento. |
| RF-037 | P1 | Estabelecimento/organizador pode sugerir atividade para aprovação. |
| RF-038 | P1 | Usuário autenticado pode salvar atividade. |
| RF-039 | P2 | Atividade pode definir capacidade e período de inscrição. |
| RF-040 | P1 | Atividade pode ser vinculada a estabelecimento e/ou rota. |
| RF-041 | P2 | Enviar lembretes/notificações de atividades salvas. |

## E. Rotas de Descoberta

| ID | Prioridade | Requisito |
|---|---|---|
| RF-050 | P0 | Administração cria, edita, publica, ativa e arquiva rotas de descoberta. |
| RF-051 | P0 | Rota possui nome, descrição, período opcional, imagem opcional e regra de conclusão. |
| RF-052 | P0 | Rota possui paradas ordenadas ou ordem sugerida. |
| RF-053 | P0 | Parada referencia estabelecimento, atividade ou local. |
| RF-054 | P0 | Parada pode ser obrigatória ou opcional. |
| RF-055 | P0 | Visitante consulta rota e paradas sem autenticação. |
| RF-056 | P0 | Usuário autenticado inicia participação em rota elegível. |
| RF-057 | P0 | Usuário registra check-in em parada por QR Code válido. |
| RF-058 | P0 | Validar token e elegibilidade da parada no servidor. |
| RF-059 | P0 | Impedir duplicidade conforme política configurada. |
| RF-060 | P0 | Apresentar progresso e estado da participação. |
| RF-061 | P0 | Concluir participação quando regra da rota for satisfeita. |
| RF-062 | P0 | Rota não exige compra em cada parada por padrão. |
| RF-063 | P1 | Consultar histórico de rotas e check-ins. |
| RF-064 | P0 | Administração pode revogar imediatamente o token de uma parada comprometida ou inválida. |
| RF-065 | P1 | Rota pode possuir edições/ocorrências em períodos diferentes. |
| RF-066 | P1 | Administração pode rotacionar o token de uma parada, substituindo o anterior. |

## F. Campanhas e benefícios

| ID | Prioridade | Requisito |
|---|---|---|
| RF-070 | P1 | Administração ou responsável autorizado cria campanha conforme permissão. |
| RF-071 | P1 | Campanha define período, responsável, benefício, elegibilidade, limites, lojas e regras. |
| RF-072 | P1 | Campanha identifica responsável pelo custo. |
| RF-073 | P1 | Consumidor consulta campanhas ativas e regras. |
| RF-074 | P1 | Emitir cupom elegível com identificador não previsível. |
| RF-075 | P1 | Responsável autenticado pela loja receptora valida cupom por QR Code ou código textual no painel; o servidor verifica campanha, validade, elegibilidade, limites, loja e autorização do operador. |
| RF-076 | P1 | A validação preliminar não consome o cupom; após aplicar o benefício presencialmente, o operador confirma e o servidor revalida e consome atomicamente, impedindo duplicidade inclusive em concorrência. |
| RF-077 | P1 | Registrar consumidor, campanha/regra, estabelecimento receptor, operador autorizado e instante, sem armazenar o código secreto completo em logs. |
| RF-082 | P1 | Consumidor autenticado consulta seus cupons e apresenta o código ou QR Code associado à sua conta; o estado só muda após confirmação do servidor. |
| RF-083 | P1 | A validação informa benefício, validade e loja elegível, além de dados mínimos para conferência, sem expor contatos ou dados privados do consumidor. |
| RF-084 | P1 | Recusar cupom inexistente, expirado, cancelado, já resgatado, incompatível com a loja ou sem elegibilidade vigente. |
| RF-078 | P1 | Campanha pode envolver benefício cruzado entre estabelecimentos. |
| RF-079 | P1 | Campanha pode estar associada à participação/conclusão de rota. |
| RF-080 | P2 | Manter carteira de pontos, lotes, expiração e ledger. |
| RF-081 | P2 | Compra confirmada pode gerar pontos conforme regra versionada e financiada. |

## G. Solicitações e compras

| ID | Prioridade | Requisito |
|---|---|---|
| RF-090 | P1 | Consumidor pode abrir uma conversa de WhatsApp com mensagem contextualizada para pedir reserva de produto publicado, sem exigir conta no Vem pro Centro. |
| RF-091 | P0 | Responsável pode cadastrar e atualizar o número público de WhatsApp que receberá os contatos da loja. |
| RF-092 | P1 | A mensagem preparada apresenta loja, produto, quantidade e link público; o consumidor precisa revisar e enviar manualmente. A plataforma não registra envio, resposta ou confirmação da reserva. |
| RF-093 | P1 | Responsável pode cadastrar um perfil público de Instagram como canal alternativo; a plataforma abre o perfil/Direct e disponibiliza mensagem para cópia, sem presumir pré-preenchimento. |
| RF-094 | P1 | Responsável principal autenticado seleciona um estabelecimento sob sua responsabilidade, lê o QR temporário de identificação apresentado pelo consumidor e associa a conta à operação; a leitura não confirma a compra. |
| RF-095 | P1 | Após a venda presencial, o responsável confirma explicitamente a compra concluída; o servidor valida token, autorização, loja, campanhas, período, limites e elegibilidade, registra a operação de forma auditável e idempotente e só emite benefícios elegíveis. |
| RF-096 | P1 | Consumidor autenticado pode gerar e apresentar **Meu QR**, token temporário, opaco, rotativo e sem dados pessoais; token expirado, revogado ou consumido é recusado. |
| RF-097 | P1 | Uma confirmação pode avaliar todas as campanhas de compra ativas e elegíveis para a loja; o valor total só é solicitado quando uma regra exigir. |
| RF-098 | P1 | A mesma requisição não duplica confirmação ou benefício; compras legítimas distintas não podem ser bloqueadas apenas por compartilharem consumidor e estabelecimento. |
| RF-099 | P1 | Confirmação de compra é declaração do responsável, não prova de pagamento ou integração com PDV; QR de consumidor, QR de rota e QR de cupom são mecanismos distintos. |

## H. Comunidade

| ID | Prioridade | Requisito |
|---|---|---|
| RF-100 | P1 | Usuário autenticado pode avaliar estabelecimento ou experiência. |
| RF-101 | P1 | Usuário escolhe exibição identificada ou anônima publicamente. |
| RF-102 | P1 | Autoria permanece internamente vinculada para moderação. |
| RF-103 | P1 | Estabelecimento pode responder à avaliação. |
| RF-104 | P1 | Usuário pode denunciar conteúdo. |
| RF-105 | P1 | Administração modera conteúdo e registra motivo. |
| RF-106 | P1 | Crítica legítima não é removida apenas por ser negativa. |

## I. Administração e indicadores

| ID | Prioridade | Requisito |
|---|---|---|
| RF-110 | P0 | Administração gerencia categorias, estabelecimentos, cronograma e rotas. |
| RF-111 | P1 | Administração consulta registros de check-in, campanhas e resgates. |
| RF-112 | P1 | Sistema apresenta indicadores operacionais agregados. |
| RF-113 | P1 | Ações críticas geram trilha de auditoria. |
| RF-114 | P1 | Dados demonstrativos podem ser identificados e separados de dados reais. |

## Regras transversais

- Visitante não precisa de conta para descoberta.
- Conta representa pessoa, não papel.
- Estoque é declaração do comerciante.
- Abertura de canal externo não comprova mensagem enviada nem reserva confirmada.
- QR Code registra participação, não garante presença antifraude.
- Benefício exige regra, elegibilidade, limites e responsável pelo custo.
- Dados demonstrativos não podem ser apresentados como reais.
- Nenhuma integração ou parceria pode ser presumida.

Cada spec deve listar os RFs afetados. Testes de aceitação devem referenciar os IDs. Mudanças de escopo atualizam MVP e este documento.

## J. Inteligência comercial e diagnóstico de lacunas

| ID | Prioridade | Requisito |
|---|---|---|
| RF-120 | P2 | Registrar de forma minimizada eventos de busca sem resultado, sem associá-los a identidade ou histórico individual para fins analíticos. |
| RF-121 | P2 | Normalizar e agrupar consultas por categoria, período e intenção provável, preservando limitações e evitando armazenar texto livre desnecessário. |
| RF-122 | P2 | Distinguir buscas sem resultados, com poucos resultados, com resultados indisponíveis e consultas inconclusivas. |
| RF-123 | P2 | Calcular indicadores de cobertura da oferta cadastrada por categoria e período. |
| RF-124 | P2 | Identificar sinais de possível demanda não atendida combinando buscas, cobertura de catálogo, disponibilidade declarada e pesquisas. |
| RF-125 | P2 | Exibir nível de confiança, período, cobertura e limitações metodológicas de cada sinal. |
| RF-126 | P2 | Disponibilizar painel restrito a perfis institucionais autorizados com indicadores exclusivamente agregados. |
| RF-127 | P2 | Impedir consulta ou exportação de buscas brutas, sessões, trajetórias, respostas individuais ou dados pessoais no painel. |
| RF-128 | P2 | Suprimir grupos pequenos e combinações de filtros que possam permitir reidentificação. |
| RF-129 | P2 | Registrar acesso, exportação e alterações de permissões do painel em trilha de auditoria. |
| RF-130 | P2 | Permitir estruturar pesquisas voluntárias com finalidade, público, método, período, campos e retenção definidos. |
| RF-131 | P2 | Apresentar resultados de pesquisas de forma agregada, acompanhados de tamanho da amostra, método e limitações. |
| RF-132 | P2 | Permitir que administração registre validação de campo de sinais de demanda, incluindo confirmação, refutação ou necessidade de investigação adicional. |
| RF-133 | P2 | Produzir relatórios agregados que apoiem campanhas de digitalização, capacitação e articulação institucional, sem decisão automática. |

