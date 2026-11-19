# Estado atual do projeto

**Atualizado:** 19/11/2026, sincronização das decisões funcionais e criação do backlog de implementação.

## Contexto

1º Inova Araras, 19/11/2026. Iniciativa: Centro em Movimento. Plataforma: Vem pro Centro. Desenvolvimento individual.

## Repositório e PRs

- Branch padrão: main.
- Issue #3: fundação Django.
- PR #4: fundação Django, mergeado.
- PR #5: preparação documental, branch `001/docs/project-readiness`, alvo main. Reúne baseline de produto, requisitos, domínio, plano de entrega, fluxos e specs. Última sincronização: commit `583f9e5` e commit subsequente de rastreabilidade do backlog.
- PR #6: proposta institucional Centro em Movimento, aberta e não mesclada segundo a última verificação registrada.
- PR #18: demo funcional (corte da Issue #17), mergeado.
- Não foi feito merge automático de PRs.

## Backlog de implementação

As Issues abaixo representam entregas verticais, não arquivos individuais. Cada uma referencia suas Specs, tasks e fluxos. O desenvolvimento é individual; dependências indicam a ordem lógica, não divisão de equipe.

| Identificador | Issue | Entrega | Dependências |
|---|---:|---|---|
| F0.01 | [#3](https://github.com/CaioDGeraldi/inova-araras-19-11-2026/issues/3) | Fundação Django | Nenhuma |
| F0.02 | [#7](https://github.com/CaioDGeraldi/inova-araras-19-11-2026/issues/7) | Spike de leitura QR em navegadores móveis | F0.01 |
| F0.03 | [#8](https://github.com/CaioDGeraldi/inova-araras-19-11-2026/issues/8) | Comércio e descoberta pública | F0.01 |
| F0.04 | [#9](https://github.com/CaioDGeraldi/inova-araras-19-11-2026/issues/9) | Cronograma do Centro | F0.01; associação com lojas depende de F0.03 |
| F0.05 | [#10](https://github.com/CaioDGeraldi/inova-araras-19-11-2026/issues/10) | Rotas de Descoberta e check-ins | F0.01 a F0.04 e spike F0.02 |
| F0.06 | [#11](https://github.com/CaioDGeraldi/inova-araras-19-11-2026/issues/11) | Confirmação de compra por Meu QR | F0.01, F0.02, F0.03 |
| F0.07 | [#12](https://github.com/CaioDGeraldi/inova-araras-19-11-2026/issues/12) | Campanhas, Fidelidade ao Centro e cupons | F0.01, F0.02, F0.05, F0.06 |
| F0.08 | [#13](https://github.com/CaioDGeraldi/inova-araras-19-11-2026/issues/13) | Comunidade, avaliações e moderação | F0.01, F0.03; integração administrativa F0.09 |
| F0.09 | [#14](https://github.com/CaioDGeraldi/inova-araras-19-11-2026/issues/14) | Administração e auditoria da plataforma | F0.01; integração por domínio F0.03 a F0.08 |
| F0.10 | [#15](https://github.com/CaioDGeraldi/inova-araras-19-11-2026/issues/15) | Seed e cenário integrado de demonstração | Núcleo F0.03/F0.04; P1 conforme entrega |
| F0.11 | [#16](https://github.com/CaioDGeraldi/inova-araras-19-11-2026/issues/16) | Política de privacidade e retenção pré-produção | Em paralelo; obrigatória antes de produção |

A Issue [#17](https://github.com/CaioDGeraldi/inova-araras-19-11-2026/issues/17) foi entregue como corte da demo (PR #18), cobrindo parte das entregas F0.03 a F0.10; o restante de cada uma segue no backlog.

Issue #3 foi reaproveitada e renomeada como F0.01. Não foi criada uma segunda Issue para a fundação. As Issues não foram atribuídas a uma equipe; o responsável pelo desenvolvimento é único.

## Documentação consolidada nesta branch

- PRD e MVP com escopo P0/P1/P2.
- Requisitos funcionais e não funcionais.
- Modelo de domínio, relações, estados e invariantes.
- Arquitetura e decisões.
- Plano de entrega por fatias verticais, atualizado para incluir os recursos P1 de calendário, comunidade e operação administrativa.
- Guia SDD e template de especificação.
- Specs 001 a 009, com a Spec 006 reservada à inteligência comercial P2.
- Arquivos de tasks para Specs 001, 002, 003, 004, 005, 007, 008 e 009. A Spec 006 é P2 e permanece sem tasks de implementação do MVP.

## Baseline de produto

A jornada central é: descobrir → planejar → visitar → registrar participação → acompanhar progresso → desbloquear benefício elegível → continuar explorando e retornar.

Rotas combinam descoberta temática, progresso e recompensas condicionadas a campanhas. Benefícios cruzados devem incentivar novas visitas a outros estabelecimentos; não há compra obrigatória em cada parada.

A jornada comercial conecta descoberta digital, conversa direta com o estabelecimento e compra presencial. O pedido de reserva abre o WhatsApp com mensagem contextualizada; Instagram é canal alternativo com texto para copiar. Consumidor e loja combinam confirmação e prazo na conversa externa. A plataforma não mantém registros ou status de reserva, não processa pagamentos nem opera estoque em tempo real.

Campanhas e cupons P1 possuem resgate presencial: consumidor apresenta código ou QR Code associado à conta; responsável autenticado da loja receptora valida no painel, aplica o benefício e confirma. A consulta preliminar não consome o cupom; a confirmação revalida regras e registra o resgate atomicamente.

O núcleo de diferenciação é a integração de Vitrine Digital, Cronograma do Centro e Rotas de Descoberta. Campanhas/cupons simples complementam a jornada. Comunidade e operação administrativa são P1, podendo ser cortadas do primeiro release se o tempo ameaçar a jornada central. Inteligência comercial, pesquisas de lacunas e painel institucional são evolução P2, sujeita a governança e validação de privacidade. Carteira de pontos complexa, pagamentos, GPS contínuo, integração Vaga Legal e aplicativo nativo ficam fora do núcleo inicial.

## Decisões funcionais fechadas

As decisões consolidadas em 19/11/2026 estão refletidas nas Specs 002, 003, 004, 005, 008 e 009 e nos fluxos correspondentes: cadastro pendente e validado; ocorrências de atividade explícitas; QR estático revogável por parada com fallback assistido; campanhas centralizadas; regras de avaliação/moderação; provisionamento administrativo e auditoria. Não tratar essas decisões como pendências de produto.

## Pendências antes da implementação

1. Revisar e validar PR #4 e a fundação técnica.
2. Confirmar a ordem final dos slices conforme o tempo e as exigências do desafio.
3. Identificar estabelecimentos, locais e atividades reais disponíveis para o piloto; marcar dados fictícios como demonstração.
4. Executar spike de compatibilidade de leitura QR em navegadores móveis reais e selecionar a estratégia técnica.
5. Formalizar política de privacidade, retenção, exclusão, anonimização e descarte antes da produção.
6. Confirmar responsável e regras comerciais de cada benefício antes de ativar campanhas.
7. Identificar estabelecimentos, locais e atividades reais disponíveis para o piloto; marcar dados fictícios como demonstração.
8. Gerar e manter Issues por fatia vertical, vinculadas às Specs e tasks, sem duplicar o workflow do motor SDD.

## Validação

Esta atualização é documental. Nenhum teste de aplicação foi executado. Não declarar fundação, banco, migrations, endpoints ou testes como validados.

## Fluxos documentados

1. `docs/flows/CONSUMER_NAVIGATION.md`: navegação principal do consumidor, cinco destinos, descoberta pública, Agenda, Rotas de Descoberta, Perfil e autenticação contextual.
2. `docs/flows/COMMERCE_DISCOVERY.md`: busca e categorias, resultados, páginas públicas de estabelecimento e produto/serviço, canais de contato, orientação de visita e atalhos externos de reserva.
3. `docs/flows/CUSTOMER_TO_PURCHASE.md`: descoberta, avaliação, mensagem de reserva pelo WhatsApp ou Instagram, confirmação combinada na conversa externa, visita, compra presencial e fidelidade condicionada à confirmação da compra.
4. `docs/flows/DISCOVERY_ROUTES.md`: consulta de rotas, detalhe, autenticação contextual, participação, QR check-in, progresso, conclusão e recompensas condicionadas a campanhas elegíveis.
5. `docs/flows/OWNER_PANEL.md`: entrada com a mesma conta, cadastro e seleção de estabelecimentos, aprovação, edição de informações, catálogo, configuração de canais públicos, resgate de cupons e registro de compra presencial.
6. `docs/flows/COUPON_REDEMPTION.md`: apresentação pelo consumidor, validação online pelo responsável da loja, confirmação presencial e consumo único do cupom.
7. `docs/flows/PURCHASE_CONFIRMATION.md`: Meu QR temporário, leitura pelo responsável, declaração de compra concluída, avaliação de campanhas, idempotência, auditoria, privacidade e limites antifraude.
8. `docs/flows/CAMPAIGNS_AND_LOYALTY.md`: criação e publicação de campanhas, origem da elegibilidade por compra confirmada ou conclusão de rota, emissão de cupons, benefícios cruzados, responsabilidade pelo custo e integração com resgate.
9. `docs/flows/PLATFORM_ADMINISTRATION.md`: acesso administrativo, categorias, aprovação/suspensão de estabelecimentos, publicação de atividades e rotas, moderação P1 e operações/auditoria.
10. `docs/flows/CENTER_CALENDAR.md`: consulta pública, detalhe, navegação relacionada, salvamento P1, sugestões P1 e administração do cronograma.
11. `docs/flows/COMMUNITY_AND_REVIEWS.md`: consulta e criação de avaliações, anonimato público, respostas de estabelecimentos, denúncias e moderação.

O cenário integrado de apresentação está em `docs/demo/DEMO_SCENARIO.md`.

## Rastreabilidade entre fluxos, requisitos, specs e tasks

- Comércio e descoberta: RF-001, RF-004, RF-005, RF-010 a RF-028; Spec 002 e tasks correspondentes.
- Cronograma: RF-030 a RF-041; Spec 003 e tasks correspondentes. RF-037/RF-038/RF-040 são P1 e foram incorporados à spec. RF-039 foi ajustado para P2, alinhado ao corte de capacidade e período de inscrição no MVP.
- Rotas: RF-050 a RF-066; Spec 004 e tasks correspondentes.
- Campanhas e cupons: RF-070 a RF-084; Spec 005 e tasks correspondentes.
- Reserva externa: RF-090 a RF-093, descritos nos fluxos de descoberta e compra e na Spec 002.
- Confirmação de compra: RF-094 a RF-099; Spec 007 e tasks existentes.
- Comunidade: RF-100 a RF-106; nova Spec 008 e tasks correspondentes.
- Administração: RF-110 a RF-114; nova Spec 009 e tasks correspondentes. Gestão de cada domínio continua detalhada nas Specs 002 a 004.
- Inteligência comercial: RF-120 a RF-133; Spec 006, P2 e fora da implementação prioritária do MVP.

## Decisões e limites da confirmação de compra

A confirmação de compra presencial por Meu QR integra o P1 junto às campanhas e cupons simples. O consumidor autenticado apresenta token temporário, opaco, rotativo e sem dados pessoais. O responsável principal da loja escaneia, confere a conta e declara explicitamente a venda concluída. A leitura isolada não confirma compra.

O servidor registra a operação de forma auditável e idempotente, avalia campanhas ativas e elegíveis para a loja e emite benefícios somente após validação. Uma confirmação pode avaliar várias campanhas; o valor total só é solicitado quando uma regra exigir. Compras espontâneas são aceitas. QR identifica conta, não comprova pagamento. Não há integração com caixa/PDV/fiscal e não se exigem documentos ou comprovantes por padrão.

## Preparação da demonstração

- Seed demonstrativo documentado; implementação do comando `python manage.py seed_demo` ainda pendente.
- Dados do seed devem ser fictícios, determinísticos, identificáveis como demonstração e isolados de dados reais.
- Demonstração prevista em duas perspectivas: consumidor e proprietário de estabelecimento.
- Os fluxos são definições funcionais, não protótipos nem implementação de telas.

## Pendências deixadas pelo corte da #17

- Cupom sem validade.
- Meu QR fixo, sem token temporário rotativo.
- Check-in por GET.
- WhatsApp com DDI 55 fixo.
- Regras de negócio sem teste automatizado.
- `ALLOWED_HOSTS` exige o IP da rede para testar o QR no celular.
