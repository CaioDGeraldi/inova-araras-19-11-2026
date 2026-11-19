# Arquitetura | Vem pro Centro

## Stack de referência

- Python 3.12, Django 5.2 LTS e uv.
- Django REST Framework para endpoints que justifiquem API.
- Django Templates + django-htmx como caminho primário.
- Bootstrap 5.3 com tokens e componentes próprios.
- PostgreSQL 16.
- WhiteNoise + Gunicorn.
- Ruff, pytest e pytest-django.

A fundação está proposta no PR #4 e precisa ser validada antes de ser considerada concluída. Consultar CURRENT_STATE.

## Estilo arquitetural

Monólito modular Django. Não iniciar microsserviços, filas, event bus ou frontend SPA separado sem requisito comprovado. O produto tem um desenvolvedor, escopo de validação e domínios que compartilham transações.

Views coordenam HTTP e apresentação. Regras de domínio não ficam em templates ou JavaScript. Serviços de aplicação surgem quando um caso de uso exige coordenação transacional. Selectors/queries dedicados surgem quando consultas complexas ou reutilizadas exigirem. Não criar camadas vazias por convenção.

## Organização lógica sugerida

- config/: settings e entrypoints.
- apps/core/: abstrações transversais realmente compartilhadas.
- apps/accounts/: identidade, sessão e perfil, se não estiverem integrados à fundação.
- apps/establishments/: estabelecimento, responsável, categorias e publicação.
- apps/catalog/: produtos/serviços e disponibilidade declarada.
- apps/events/: programação, local, organizador, publicação e cancelamento.
- apps/discovery_routes/: rota, parada, participação, check-in e conclusão.
- apps/campaigns/: campanha, benefício, cupom, elegibilidade e resgate.
- Os pedidos de reserva são encaminhados por links externos de contato; não há app de reservas no MVP.
- apps/community/: avaliações, denúncias e moderação, quando priorizadas.
- apps/dashboard/: composição de experiências operacionais, não dono das regras.

Os diretórios são limites conceituais, não ordem obrigatória de criação. Não criar app loyalty separado até carteira de pontos entrar no escopo; cupons simples podem ficar em campaigns.

## Relações de domínio

- User pode ser responsável por várias Stores.
- Store possui categorias e produtos/serviços.
- Event representa a atividade principal; EventOccurrence representa cada realização com data, horário, local e estado próprios. Place é reutilizável entre atividades e paradas; Event pode relacionar-se opcionalmente a Store ou DiscoveryRoute.
- DiscoveryRoute possui RouteStops ordenadas; uma parada referencia Store, Event ou Place.
- User participa de DiscoveryRoute por RouteParticipation; cada participação representa uma execução da rota.
- CheckIn pertence a uma participação e parada, com unicidade por participação/parada. QR estático por parada é revogável e rotacionável atomicamente; check-in assistido exige operador autorizado.
- Campaign pode envolver uma ou mais Stores.
- Coupon pertence a Campaign; Redemption registra uso por consumidor e estabelecimento elegível.
- Store mantém os canais públicos de contato; links de reserva contextualizam Store/Product, mas não criam uma entidade de reserva.

Evitar duplicar endereço/local em entidades relacionadas sem regra clara. Place é uma entidade reutilizável compartilhada por EventOccurrence e RouteStop.

## Estados e integridade

- Estabelecimento: draft/pending, approved, rejected, suspended.
- Atividade: draft, published, cancelled, completed/archived.
- Rota: draft, published, active, completed, archived.
- Participação: active, completed, cancelled.
- Check-in: accepted ou rejected, com motivo interno.
- Campanha: draft, scheduled, active, paused, ended, cancelled.
- Cupom: issued, redeemed, expired, cancelled.

Transições devem ser explícitas e autorizadas no servidor. Não permitir edição silenciosa de registros históricos críticos.

## Transações e concorrência

- Não existe transação de reserva no Vem pro Centro; links externos não possuem estados locais.
- Check-in possui restrição única por participação + parada; cada nova execução da rota cria nova RouteParticipation.
- Resgate de cupom deve validar elegibilidade e gravar consumo atomicamente.
- Confirmação de compra deve ser idempotente.
- Benefícios e saldos não podem ser calculados apenas no cliente.
- Pontos futuros exigem ledger imutável, Decimal, lançamentos compensatórios, concorrência e expiração por lote; não implementar saldo editável diretamente.
- Integridade deve ser garantida no banco quando possível, além da validação de aplicação.

## QR Code e presença

QR de parada é estático por parada, com token aleatório, opaco, não sequencial e sem PII. Revogação/rotação invalida o token anterior atomicamente, sem apagar check-ins aceitos. Check-in é único por participação/parada. Fallback assistido registra operador autorizado, participante, parada, instante e motivo, sem autoconfirmação. Check-in é registro de participação declarada, não prova absoluta de presença ou compra. Não coletar GPS continuamente.

## Interface

- Vitrine e cronograma públicos, mobile-first.
- Dashboard do comerciante com sidebar retrátil e topbar.
- Administração pode começar com Django Admin.
- HTMX para interações incrementais; evitar SPA sem necessidade.
- Animações discretas, respeitando prefers-reduced-motion.
- WCAG 2.2 AA como baseline.
- SEO em páginas públicas de lojas, produtos, atividades e rotas.

## Segurança e privacidade

Autorização no servidor e por objeto/estabelecimento. Manter CSRF, validação de entrada e escaping de saída. Uploads validam tipo, tamanho e conteúdo. Segredos ficam fora do Git. Dados privados não aparecem em serializers, templates ou logs públicos. Auditoria para provisionamento administrativo; aprovação/suspensão; publicação/edição relevante/cancelamento; campanhas; confirmação/correção de compra e resgate; moderação; revogação/rotação QR. Correções preservam o evento original e usam eventos compensatórios. Minimização, finalidade, retenção e direitos conforme LGPD.

## Testes

- Unitários para regras e transições.
- Integração para transações, autorização e restrições únicas.
- Testes HTTP para jornadas públicas e autenticadas.
- Testes de concorrência/idempotência em check-in, compra e resgate.
- Verificação manual de teclado, foco, zoom, leitor de tela e responsividade.
- Não declarar teste executado sem execução e evidência.

## Evolução

Adicionar novos apps ou integrações apenas após spec e decisão. A arquitetura deve permitir extração futura, mas não pagar hoje o custo de uma distribuição que ainda não existe.

## Direção visual e navegação do consumidor

A experiência do consumidor é mobile-first e deve reutilizar padrões de interação já familiares em aplicativos de descoberta e comércio. A referência ao Instagram é de familiaridade de navegação, não de cópia de identidade visual, marca ou composição proprietária.

### Navegação principal em dispositivos móveis

Usar uma barra inferior fixa com cinco destinos estáveis:

1. **Início:** entrada principal e superfície de descoberta.
2. **Explorar:** busca e descoberta de estabelecimentos, produtos, serviços e categorias.
3. **Rotas:** Rotas de Descoberta, paradas, participação e progresso.
4. **Agenda:** Cronograma do Centro e detalhes das atividades.
5. **Perfil:** identidade, favoritos, avaliações e Fidelidade ao Centro; pedidos de reserva e suas confirmações permanecem em canais externos.

A barra deve manter posição, ordem, ícones reconhecíveis e rótulos visíveis entre as seções. O conteúdo específico do feed inicial e a distribuição de atalhos serão definidos nos fluxos de navegação, sem antecipar decisões de conteúdo nesta etapa.

### Comportamento responsivo

- Em telas móveis, priorizar navegação inferior e interações confortáveis com uma mão.
- Em telas maiores, adaptar a navegação para um padrão apropriado ao espaço disponível, sem alterar a hierarquia ou os nomes das seções.
- A troca de seção não deve descartar estado de busca, filtros ou progresso sem uma ação explícita.
- O painel do proprietário permanece uma experiência operacional distinta, com sidebar retrátil e topbar, acessível pela conta da pessoa conforme suas permissões.

### Linguagem visual

- Interface familiar, clara e consistente, sem reinventar convenções estabelecidas.
- Identidade própria do Vem pro Centro; não reproduzir logotipo, componentes proprietários ou identidade do Instagram.
- Cards e listas com hierarquia visual simples para lojas, produtos, campanhas, rotas e atividades.
- Evitar excesso de elementos, gestos ocultos e navegação dependente apenas de ícones.
- Manter feedback visível para ações, estados vazios, carregamento, erros e confirmações.

### Acessibilidade

- Rótulos textuais acompanham os ícones da navegação principal.
- Foco visível, ordem lógica, contraste WCAG 2.2 AA e suporte a teclado/leitor de tela.
- Alvos interativos atendem ao mínimo WCAG 2.2 AA e devem ser ampliados quando possível para uso móvel.
- A barra fixa não pode encobrir conteúdo, controles, avisos ou foco de teclado; considerar safe areas dos dispositivos.
- Respeitar `prefers-reduced-motion`.


## Registro de compra presencial e Meu QR

A confirmação de compra é uma operação de domínio separada de reserva, check-in de rota e resgate de cupom. **Meu QR** representa um token temporário, aleatório, opaco, rotativo e de uso único, associado a uma conta autenticada. O servidor valida expiração, revogação e consumo; o QR não contém dados pessoais.

O responsável principal autenticado seleciona uma loja sob sua responsabilidade, escaneia o QR, confere a conta e confirma explicitamente a venda presencial concluída. Ler o código não registra compra. A operação registra consumidor, loja, operador, instante, token referenciado, chave de idempotência, valor total apenas quando exigido por regra, campanhas/regras avaliadas e resultado.

A confirmação e as concessões elegíveis devem ser consistentes e idempotentes. A mesma requisição não duplica a operação; compras distintas legítimas do mesmo consumidor na mesma loja continuam permitidas. A emissão de benefício deve ser única por confirmação e campanha/regra.

Sem integração com caixa, PDV ou sistema fiscal, a confirmação é declaração auditável do responsável e não prova de pagamento. O QR de consumidor não substitui QR de parada nem QR de cupom. O fluxo completo está em `docs/flows/PURCHASE_CONFIRMATION.md` e `docs/specs/007-purchase-confirmation/spec.md`.
