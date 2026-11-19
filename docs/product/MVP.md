# MVP | Vem pro Centro

## Objetivo

Entregar uma primeira versão demonstrável que conecte descoberta digital a experiências presenciais no Centro de Araras. O MVP deve provar uma jornada entre vitrine, cronograma e Circuito Vivo, com campanha simples como incentivo complementar.

**Princípio de corte:** preservar a jornada presencial integrada; reduzir funcionalidades periféricas antes de comprometer segurança, acessibilidade ou integridade.

## P0 | Núcleo obrigatório

### Identidade e operação
- Conta individual, autenticação e autorização.
- Uma conta pode atuar como consumidor e responsável por estabelecimentos.
- Administração aprova estabelecimentos, publica atividades e gerencia circuitos.

### Vitrine Digital
- Cadastro e edição de estabelecimento.
- Uma ou mais categorias por estabelecimento.
- Página pública da loja.
- Cadastro/edição de produtos ou serviços com descrição, preço quando aplicável, imagem opcional e disponibilidade declarada.
- Busca por estabelecimento/produto e filtro por categoria.
- Endereço, contato e data de atualização visíveis.

### Cronograma do Centro
- Administração cadastra, publica, edita e cancela atividades.
- Listagem pública por data e detalhe da atividade.
- Data, horário, local, descrição, categoria, organizador e condição gratuita/paga.
- Indicação clara de cancelamento e necessidade de inscrição.
- Atividade pode ser associada a estabelecimento ou circuito.

### Circuito Vivo
- Administração cria circuito, define descrição, período e paradas.
- Paradas podem representar estabelecimento, atividade ou local.
- Circuito define ordem sugerida e paradas obrigatórias/opcionais.
- Visitante consulta circuito sem login.
- Usuário autenticado inicia participação e registra check-in por QR Code.
- Sistema controla duplicidade e apresenta progresso.
- Regra de conclusão é explícita e testada.
- Não exigir compra em cada parada.

### Demonstração integrada
- Dados de demonstração identificados como tais.
- Pelo menos um circuito com paradas reais ou claramente demonstrativas.
- Pelo menos uma atividade publicada no cronograma.
- Jornada de visitante parte da descoberta e chega ao check-in presencial.
- Painel administrativo mantém o conteúdo.

## P0 condicionado à jornada comercial

Solicitação de reserva/interesse pode entrar no P0 se necessária para demonstrar contato com a loja e confirmação de compra. Não é checkout nem reserva garantida. Se o tempo apertar, usar contato direto e preservar vitrine + cronograma + circuito.

Quando uma solicitação existir, o responsável pode registrar conclusão como compra. A operação deve ser autorizada, idempotente e auditável. Só gera benefício se houver campanha ativa com regra explícita.

## P1 | Após o núcleo estável

- Campanhas simples e cupons de uso único.
- Benefício cruzado entre estabelecimentos com emissor, receptor, financiador, validade e limites explícitos.
- Resgate de cupom com proteção transacional contra duplicidade.
- Estabelecimentos sugerem atividades para aprovação administrativa.
- Consumidor salva atividades.
- Avaliações com anonimato público, denúncia e moderação básica.
- Histórico de circuitos e participação.
- Filtros por proximidade sem rastreamento contínuo.
- Métricas operacionais em painel simples.

## P2 | Evolução posterior

- Carteira de pontos, lotes, expiração, FEFO, estorno e regras configuráveis.
- Inscrição completa, lista de presença e notificações de eventos.
- Notificações push.
- Geolocalização opcional e pontual, se houver justificativa e consentimento.
- Integração Vaga Legal.
- Pagamentos, checkout, entrega e logística.
- Equipes/memberships por estabelecimento.
- Integrações institucionais e dados em tempo real.
- Analytics de impacto econômico com linha de base.
- Aplicativo nativo.

## Fora do MVP

- Checkout e processamento de pagamento.
- Rastreamento GPS contínuo.
- Conversão de pontos em dinheiro.
- Promessa de estoque em tempo real.
- Integração não autorizada com sistemas públicos/privados.
- Recompensas sem responsável financeiro.
- Chat interno.
- Recomendação por IA.
- Permissões complexas por equipe.
- Venda de ingressos.

## Critérios globais de aceite

- [ ] Visitante consulta lojas, produtos, atividades e circuitos sem login.
- [ ] Comerciante autorizado mantém estabelecimento e catálogo.
- [ ] Administração publica e cancela atividades.
- [ ] Administração cria circuito com diferentes tipos de parada.
- [ ] Usuário autenticado inicia circuito e registra check-in.
- [ ] Check-in duplicado é tratado conforme regra da parada.
- [ ] Progresso e conclusão correspondem às regras do circuito.
- [ ] Circuito não exige compra em todas as paradas.
- [ ] QR Code não é apresentado como prova absoluta de presença.
- [ ] Dados privados não aparecem em páginas públicas.
- [ ] Operações críticas possuem testes e auditoria.
- [ ] Fluxos principais funcionam em celular e teclado.
- [ ] Setup e execução são reproduzíveis conforme README.

## Critério de demonstrabilidade

1. Consumidor descobre atividade no cronograma.
2. Consulta circuito associado e suas paradas.
3. Encontra estabelecimentos e produtos participantes.
4. Visita parada e registra check-in.
5. Visualiza progresso e regra de conclusão.
6. Consulta campanha/benefício elegível, se incluído na versão demonstrada.
7. Comerciante/administração atualiza conteúdo.

Não demonstrar integrações, parcerias, dados ou transações não implementados e validados.

## Regra de priorização

O projeto será desenvolvido por uma pessoa. Planejar uma entrega vertical de cada vez. Cada slice deve ter spec, critérios verificáveis, testes e evidência.