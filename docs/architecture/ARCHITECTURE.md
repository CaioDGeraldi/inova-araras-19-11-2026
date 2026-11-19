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
- apps/reservations/: solicitações e confirmação de compra, somente se aprovadas.
- apps/community/: avaliações, denúncias e moderação, quando priorizadas.
- apps/dashboard/: composição de experiências operacionais, não dono das regras.

Os diretórios são limites conceituais, não ordem obrigatória de criação. Não criar app loyalty separado até carteira de pontos entrar no escopo; cupons simples podem ficar em campaigns.

## Relações de domínio

- User pode ser responsável por várias Stores.
- Store possui categorias e produtos/serviços.
- Event possui local e organizador; pode relacionar-se opcionalmente a Store ou DiscoveryRoute.
- DiscoveryRoute possui RouteStops ordenadas; uma parada referencia Store, Event ou Place.
- User participa de DiscoveryRoute por RouteParticipation.
- CheckIn pertence a uma participação e parada.
- Campaign pode envolver uma ou mais Stores.
- Coupon pertence a Campaign; Redemption registra uso por consumidor e estabelecimento elegível.
- Reservation, se implementada, pertence a User e Store; conclusão pode originar compra elegível.

Evitar duplicar endereço/local em entidades relacionadas sem regra clara. Place pode ser entidade própria ou value object conforme reutilização real.

## Estados e integridade

- Estabelecimento: draft/pending, approved, rejected, suspended.
- Atividade: draft, published, cancelled, completed/archived.
- DiscoveryRouteo: draft, published, active, completed, archived.
- Participação: active, completed, cancelled.
- Check-in: accepted ou rejected, com motivo interno.
- Campanha: draft, scheduled, active, paused, ended, cancelled.
- Cupom: issued, redeemed, expired, cancelled.
- Solicitação: pending, accepted, declined, cancelled, completed.

Transições devem ser explícitas e autorizadas no servidor. Não permitir edição silenciosa de registros históricos críticos.

## Transações e concorrência

- Check-in deve possuir restrição única conforme política de repetição (ex.: participação + parada + ocorrência).
- Resgate de cupom deve validar elegibilidade e gravar consumo atomicamente.
- Confirmação de compra deve ser idempotente.
- Benefícios e saldos não podem ser calculados apenas no cliente.
- Pontos futuros exigem ledger imutável, Decimal, lançamentos compensatórios, concorrência e expiração por lote; não implementar saldo editável diretamente.
- Integridade deve ser garantida no banco quando possível, além da validação de aplicação.

## QR Code e presença

QR contém token opaco/não sequencial, não dados pessoais. Validar no servidor, controlar validade/rotação e duplicidade. Check-in é registro de participação, não prova infalível de presença. Não coletar GPS continuamente. Para benefício de maior valor, exigir validação adicional pelo estabelecimento.

## Interface

- Vitrine e cronograma públicos, mobile-first.
- Dashboard do comerciante com sidebar retrátil e topbar.
- Administração pode começar com Django Admin.
- HTMX para interações incrementais; evitar SPA sem necessidade.
- Animações discretas, respeitando prefers-reduced-motion.
- WCAG 2.2 AA como baseline.
- SEO em páginas públicas de lojas, produtos, atividades e rotas.

## Segurança e privacidade

Autorização no servidor e por objeto/estabelecimento. Manter CSRF, validação de entrada e escaping de saída. Uploads validam tipo, tamanho e conteúdo. Segredos ficam fora do Git. Dados privados não aparecem em serializers, templates ou logs públicos. Auditoria para publicação, cancelamento, confirmação de compra, emissão e resgate de benefícios. Minimização, finalidade, retenção e direitos conforme LGPD.

## Testes

- Unitários para regras e transições.
- Integração para transações, autorização e restrições únicas.
- Testes HTTP para jornadas públicas e autenticadas.
- Testes de concorrência/idempotência em check-in, compra e resgate.
- Verificação manual de teclado, foco, zoom, leitor de tela e responsividade.
- Não declarar teste executado sem execução e evidência.

## Evolução

Adicionar novos apps ou integrações apenas após spec e decisão. A arquitetura deve permitir extração futura, mas não pagar hoje o custo de uma distribuição que ainda não existe.