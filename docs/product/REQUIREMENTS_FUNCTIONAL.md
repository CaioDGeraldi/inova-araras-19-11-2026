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
| RF-011 | P0 | Estabelecimento possui nome público, descrição, endereço, contato e situação. |
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
| RF-039 | P1 | Atividade pode definir capacidade e período de inscrição. |
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
| RF-064 | P1 | Administração revoga/rotaciona token de parada. |
| RF-065 | P1 | Rota pode possuir edições/ocorrências em períodos diferentes. |

## F. Campanhas e benefícios

| ID | Prioridade | Requisito |
|---|---|---|
| RF-070 | P1 | Administração ou responsável autorizado cria campanha conforme permissão. |
| RF-071 | P1 | Campanha define período, responsável, benefício, elegibilidade, limites, lojas e regras. |
| RF-072 | P1 | Campanha identifica responsável pelo custo. |
| RF-073 | P1 | Consumidor consulta campanhas ativas e regras. |
| RF-074 | P1 | Emitir cupom elegível com identificador não previsível. |
| RF-075 | P1 | Estabelecimento autorizado valida e resgata cupom. |
| RF-076 | P1 | Resgate é atômico e não pode ser concluído duas vezes. |
| RF-077 | P1 | Registrar emissor, destinatário, estabelecimento de resgate e instante. |
| RF-078 | P1 | Campanha pode envolver benefício cruzado entre estabelecimentos. |
| RF-079 | P1 | Campanha pode estar associada à participação/conclusão de rota. |
| RF-080 | P2 | Manter carteira de pontos, lotes, expiração e ledger. |
| RF-081 | P2 | Compra confirmada pode gerar pontos conforme regra versionada e financiada. |

## G. Solicitações e compras

| ID | Prioridade | Requisito |
|---|---|---|
| RF-090 | P1 | Consumidor autenticado pode enviar solicitação de interesse/reserva. |
| RF-091 | P1 | Responsável pode aceitar, recusar ou cancelar solicitação. |
| RF-092 | P1 | Solicitação não representa pagamento nem garantia automática de disponibilidade. |
| RF-093 | P1 | Responsável pode marcar solicitação como compra concluída. |
| RF-094 | P1 | Confirmação de compra é autorizada, idempotente e auditável. |
| RF-095 | P1 | Compra confirmada só gera benefício quando houver campanha elegível. |

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

