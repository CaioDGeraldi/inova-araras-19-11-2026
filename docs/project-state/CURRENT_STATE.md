# Estado atual do projeto

**Atualizado:** 19/11/2026, auditoria do backlog, PRs integrados e riscos da demonstração.

## Contexto

1º Inova Araras, 19/11/2026. Iniciativa: Centro em Movimento. Plataforma: Vem pro Centro. Desenvolvimento individual.

## Repositório e PRs

- Branch padrão: `main`.
- PR #2: modelos de Issue e Pull Request, mergeado.
- PR #4: fundação Django, mergeado. A validação inicial pendente foi concluída posteriormente e registrada no PR #18.
- PR #5: baseline documental do produto, requisitos, domínio, plano, fluxos e Specs, mergeado.
- PR #6: proposta institucional Centro em Movimento, mergeado.
- PR #18: corte funcional de duas horas para a demonstração integrada, mergeado. Não representa entrega nem conclusão do MVP.
- PR #20: Bootstrap, navegação móvel e acessibilidade básica da demonstração, mergeado.
- PR #22: complementos P0 de endereço, imagens, estados da loja, evento na rota e período, mergeado.
- PR #24: identidade visual e interface de consumo do Vem pro Centro, mergeado.
- PR #25: preparação de demonstração no Heroku, mergeado. O `Procfile` ainda executa `seed_demo` em cada inicialização; o risco está registrado na Issue #15.
- No snapshot de implementação até o PR #25, não havia Pull Requests abertos. O PR #26 contém apenas esta sincronização documental do backlog e do estado do projeto.

## Backlog de implementação

As Issues abaixo representam entregas verticais, não arquivos individuais. Cada uma referencia suas Specs, tasks e fluxos. O desenvolvimento é individual; dependências indicam a ordem lógica, não divisão de equipe.

| Identificador | Issue | Entrega | Estado em 19/11/2026 | Evidência / dependências |
|---|---:|---|---|---|
| F0.01 | [#3](https://github.com/CaioDGeraldi/inova-araras-19-11-2026/issues/3) | Fundação Django | Concluída | PR #4 + validações posteriores no PR #18 |
| F0.02 | [#7](https://github.com/CaioDGeraldi/inova-araras-19-11-2026/issues/7) | Leitor QR em navegador móvel | Encerrada: não planejada | O dispositivo usa a câmera nativa para abrir a URL do QR |
| F0.03 | [#8](https://github.com/CaioDGeraldi/inova-araras-19-11-2026/issues/8) | Comércio e descoberta pública | Aberta, parcial | PRs #18, #22 e #24; faltam critérios completos da Spec 002 |
| F0.04 | [#9](https://github.com/CaioDGeraldi/inova-araras-19-11-2026/issues/9) | Cronograma do Centro | Aberta, parcial | PRs #18 e #22; faltam ocorrências/Place e recursos P1 |
| F0.05 | [#10](https://github.com/CaioDGeraldi/inova-araras-19-11-2026/issues/10) | Rotas de Descoberta e check-ins | Aberta, parcial | PRs #18 e #22; faltam rotação/revogação, fallback e múltiplas execuções |
| F0.06 | [#11](https://github.com/CaioDGeraldi/inova-araras-19-11-2026/issues/11) | Confirmação de compra por Meu QR | Aberta, parcial | PR #18 usa código fixo; token temporário, idempotência e auditoria ainda pendentes |
| F0.07 | [#12](https://github.com/CaioDGeraldi/inova-araras-19-11-2026/issues/12) | Campanhas, Fidelidade ao Centro e cupons | Aberta, parcial | PR #18 entrega campanha simples; validade, limites e compensações pendentes |
| F0.08 | [#13](https://github.com/CaioDGeraldi/inova-araras-19-11-2026/issues/13) | Comunidade, avaliações e moderação | Aberta | Implementação pendente |
| F0.09 | [#14](https://github.com/CaioDGeraldi/inova-araras-19-11-2026/issues/14) | Administração e auditoria da plataforma | Aberta, parcial | Operações iniciais usam Django Admin; auditoria e consulta operacional pendentes |
| F0.10 | [#15](https://github.com/CaioDGeraldi/inova-araras-19-11-2026/issues/15) | Seed e cenário integrado de demonstração seguro | Aberta, parcial | O comando existe; segurança de credenciais, isolamento e execução em deploy precisam ser corrigidos |
| F0.11 | [#16](https://github.com/CaioDGeraldi/inova-araras-19-11-2026/issues/16) | Política de privacidade e retenção pré-produção | Aberta | Obrigatória antes de produção com dados reais e avaliações públicas |

A Issue [#17](https://github.com/CaioDGeraldi/inova-araras-19-11-2026/issues/17) foi renomeada para `[DEMO-2H]` e registra somente o corte temporário de duas horas implementado no PR #18. Ela não entrega nem encerra o MVP. A definição oficial do MVP permanece em `docs/product/MVP.md`. A Issue [#19](https://github.com/CaioDGeraldi/inova-araras-19-11-2026/issues/19) também foi identificada como tarefa de interface da demo. As Issues #21 e #23 foram concluídas, respectivamente, pelos PRs #22 e #24.

A Issue #3 foi concluída após a validação posterior da fundação; a Issue #7 foi encerrada como não planejada porque não há leitor QR embutido no navegador. As Issues #8 a #12 permanecem abertas de propósito: os PRs integraram cortes parciais e não satisfazem todo o escopo das Specs.

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

## Pendências e próximos passos

1. Continuar as Issues #8 a #12 até atender os critérios completos das Specs 002 a 005 e 007; os PRs da demo contam como entregas parciais.
2. Implementar comunidade/moderação (#13) e consolidar administração/auditoria (#14) conforme prioridade P1 e capacidade.
3. Endurecer `seed_demo` (#15): remover senha fixa e saída de credenciais, impedir colisões com dados reais, recusar uso em produção e retirar a execução automática do Procfile. Separar restauração de imagens da criação/atualização de dados.
4. Formalizar política de privacidade, retenção, exclusão, anonimização e descarte (#16) antes de produção com dados reais e antes de habilitar avaliações públicas.
5. Identificar estabelecimentos, locais e atividades reais disponíveis para o piloto; marcar todo dado fictício como demonstração.
6. Confirmar responsável, validade, limites e regras comerciais de cada benefício antes de ativar campanhas.
7. Manter Issues vinculadas às Specs e tasks, sem criar uma Issue de “entrega do MVP” que duplique a definição em `docs/product/MVP.md`.

Não há mais dependência F0.02: o fluxo usa câmera nativa do dispositivo para abrir a URL do QR.

## Validação registrada nos PRs integrados

- PR #18: `manage.py check`, `makemigrations --check`, `migrate`, `pytest` (1 teste), Ruff, duas execuções do `seed_demo` com contagens iguais e smoke tests HTTP 200 foram registrados como aprovados.
- PR #20: Django check, pytest (1 teste), Ruff e HTTP 200 nas telas capturadas foram registrados como aprovados.
- PR #22: check, migrations, migrate, pytest (1 teste), Ruff e validações de imagem/período foram registrados como aprovados.
- PR #24: check, pytest (1 teste), Ruff, seed repetido e HTTP 200 foram registrados como aprovados.
- PR #25: check e Ruff foram registrados como aprovados.
- `uv.lock` está versionado e `compose.yaml` configura PostgreSQL 16.

Esses resultados são evidências relatadas nos PRs integrados, não uma nova execução de testes nesta atualização documental. A cobertura automatizada continua pequena; os critérios completos das Issues abertas não devem ser considerados concluídos por causa dos smoke tests da demonstração.

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

- O comando `python manage.py seed_demo` existe e foi executado duas vezes com contagens iguais, conforme evidência do PR #18.
- A Issue #15 permanece aberta: o comando usa senha fixa, redefine senhas e imprime credenciais; o `Procfile` executa o seed a cada inicialização do serviço; a rotina ainda precisa de proteção contra colisões com registros reais e transação.
- `docs/demo/DEMO_SCENARIO.md` descreve o cenário pretendido, mas não comprova que todos os fluxos P1 estão implementados.
- A demonstração deve usar exclusivamente contas, contatos, estabelecimentos, produtos e transações fictícias e claramente identificadas.

## Atalhos e limitações da demonstração

- Cupom sem validade; a Issue #12 continua aberta para completar as regras da Spec 005.
- Meu QR fixo por conta, não o token temporário rotativo da Spec 007; Issue #11.
- Check-in por GET, com a limitação registrada no PR #18; Issue #10.
- WhatsApp usa DDI 55 fixo no estado atual.
- Cobertura automatizada mínima: PRs registram 1 teste pytest, além de smoke tests; não equivale à validação completa das regras de negócio.
- `ALLOWED_HOSTS` local exige incluir o IP da rede para testar QR em outro dispositivo.
- `Procfile` executa `seed_demo` na inicialização e o comando usa credencial fixa; risco conhecido acompanhado pela Issue #15.
