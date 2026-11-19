# MVP | Vem pro Centro

## Objetivo

Entregar uma primeira versão demonstrável que conecte descoberta digital a experiências presenciais no Centro de Araras. O MVP deve provar uma jornada entre vitrine, cronograma e Rotas de Descoberta, com campanha simples como incentivo complementar.

**Princípio de corte:** preservar a jornada presencial integrada; reduzir funcionalidades periféricas antes de comprometer segurança, acessibilidade ou integridade.

## P0 | Núcleo obrigatório

### Identidade e operação
- Conta individual, autenticação e autorização.
- Uma conta pode atuar como consumidor e responsável por estabelecimentos.
- Administração aprova estabelecimentos, publica atividades e gerencia rotas.

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
- Atividade pode ser associada a estabelecimento ou rota.

### Rotas de Descoberta
- Administração cria rota, define descrição, período e paradas.
- Paradas podem representar estabelecimento, atividade ou local.
- Rota define ordem sugerida e paradas obrigatórias/opcionais.
- Visitante consulta rota sem login.
- Usuário autenticado inicia participação e registra check-in por QR Code.
- Sistema controla duplicidade e apresenta progresso.
- Regra de conclusão é explícita e testada.
- Não exigir compra em cada parada.

### Demonstração integrada
- Dados de demonstração identificados como tais.
- Pelo menos uma rota com paradas reais ou claramente demonstrativas.
- Pelo menos uma atividade publicada no cronograma.
- Jornada de visitante parte da descoberta e chega ao check-in presencial.
- Painel administrativo mantém o conteúdo.

## Reserva para retirada presencial | P1 do MVP

A reserva integra o MVP após a estabilidade do núcleo de vitrine, cronograma e Rotas de Descoberta. O consumidor autenticado solicita a reserva de um produto publicado, informa quantidade e aguarda decisão do responsável. A solicitação pendente não garante nem separa o produto.

O responsável aceita ou recusa. Ao aceitar, confirma a quantidade que será separada e define prazo de retirada. Pode marcar como pronta para retirada, confirmar a retirada presencial ou cancelar antes da retirada com justificativa. Reservas não retiradas expiram no prazo definido. O consumidor acompanha os estados pelo Perfil.

A reserva não é compra, checkout ou garantia automática de estoque. O catálogo mantém disponibilidade declarada; o aceite representa o compromisso da loja de separar a quantidade confirmada até o prazo. Pagamento e conclusão da venda ocorrem presencialmente. Não há integração com PDV, baixa automática de estoque, entrega ou logística. A retirada e a compra são eventos distintos para fins de fidelidade.

## P1 | Após o núcleo estável

- Campanhas simples e cupons de uso único.
- Benefício cruzado entre estabelecimentos com emissor, receptor, financiador, validade e limites explícitos.
- Resgate de cupom com proteção transacional contra duplicidade.
- Estabelecimentos sugerem atividades para aprovação administrativa.
- Consumidor salva atividades.
- Avaliações com anonimato público, denúncia e moderação básica.
- Histórico de rotas e participação.
- Filtros por proximidade sem rastreamento contínuo.
- Métricas operacionais em painel simples.

## P2 | Evolução posterior

### Inteligência comercial e planejamento institucional
- Agregar buscas sem resultados por termo normalizado, categoria e período, sem histórico individual.
- Diferenciar ausência de resultado, poucos resultados e indisponibilidade declarada.
- Cruzar sinais de busca com cobertura do catálogo e categorias dos estabelecimentos.
- Disponibilizar painel restrito com tendências agregadas, cobertura, metodologia, período e limitações.
- Conduzir pesquisas voluntárias com consumidores e comerciantes para validar lacunas percebidas.
- Gerar relatórios agregados para orientar campanhas de digitalização, capacitação e articulação institucional.
- Aplicar limiar mínimo de grupo, supressão de células pequenas, controle de acesso, auditoria e retenção limitada.



- Carteira de pontos, lotes, expiração, FEFO, estorno e regras configuráveis.
- Inscrição completa, lista de presença e notificações de eventos.
- Notificações push.
- Geolocalização opcional e pontual, se houver justificativa e consentimento.
- Integração Vaga Legal.
- Pagamentos, checkout, entrega e logística.
- Equipes/memberships por estabelecimento.
- Integrações institucionais e dados em tempo real.
- Analytics de impacto econômico com linha de base.
- Inteligência comercial institucional conforme a spec 006, após validação de privacidade, metodologia e governança.
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

- [ ] Visitante consulta lojas, produtos, atividades e rotas sem login.
- [ ] Comerciante autorizado mantém estabelecimento e catálogo.
- [ ] Consumidor autenticado solicita reserva e acompanha a decisão da loja.
- [ ] Responsável aceita/recusa, define prazo, marca como pronta e confirma retirada ou cancela com motivo.
- [ ] Reservas não retiradas expiram e não são tratadas como compras.
- [ ] Administração publica e cancela atividades.
- [ ] Administração cria rota com diferentes tipos de parada.
- [ ] Usuário autenticado inicia rota e registra check-in.
- [ ] Check-in duplicado é tratado conforme regra da parada.
- [ ] Progresso e conclusão correspondem às regras da rota.
- [ ] Rota não exige compra em todas as paradas.
- [ ] QR Code não é apresentado como prova absoluta de presença.
- [ ] Dados privados não aparecem em páginas públicas.
- [ ] Indicadores institucionais, quando habilitados, exibem apenas agregações protegidas e não permitem consultar buscas ou respostas individuais.
- [ ] Operações críticas possuem testes e auditoria.
- [ ] Fluxos principais funcionam em celular e teclado.
- [ ] Setup e execução são reproduzíveis conforme README.

## Critério de demonstrabilidade

1. Consumidor descobre atividade no cronograma.
2. Consulta a rota associada e suas paradas.
3. Encontra estabelecimentos e produtos participantes.
4. Visita parada e registra check-in.
5. Visualiza progresso e regra de conclusão.
6. Consulta campanha/benefício elegível, se incluído na versão demonstrada.
7. Comerciante/administração atualiza conteúdo.

Não demonstrar integrações, parcerias, dados ou transações não implementados e validados.

## Regra de priorização

O projeto será desenvolvido por uma pessoa. Planejar uma entrega vertical de cada vez. Cada slice deve ter spec, critérios verificáveis, testes e evidência.

## Seed demonstrativo

A demonstração do pitch deve ser reproduzível sem depender de cadastros manuais feitos durante a apresentação.

- Disponibilizar comando dedicado `python manage.py seed_demo`.
- Criar dados inteiramente fictícios e claramente identificados como demonstração, sem reproduzir nomes ou dados de estabelecimentos reais.
- O cenário deve incluir um consumidor, pelo menos dois proprietários, dois estabelecimentos de categorias diferentes, produtos com preços e disponibilidade declarada, atividades no Cronograma do Centro e uma Rota de Descoberta com paradas obrigatórias e opcionais.
- Incluir campanha demonstrativa somente se as regras e o responsável pelo benefício estiverem definidos no próprio cenário.
- O seed deve ser determinístico e idempotente: execuções repetidas atualizam/reutilizam os registros de demonstração sem duplicá-los.
- Todos os registros devem possuir identificação inequívoca de origem demonstrativa para permitir manutenção e limpeza seletiva.
- O comando deve recusar execução em produção e nunca apagar ou alterar registros que não pertençam ao conjunto demonstrativo.
- Senhas de contas demonstrativas devem ser fornecidas por configuração local/variáveis de ambiente, nunca publicadas no repositório ou impressas em logs.
- O seed não substitui fixtures de teste nem deve ser executado automaticamente em deploy.
