# Centro em Movimento | PRD

**Produto digital:** Vem pro Centro  
**Iniciativa:** Centro em Movimento  
**Cidade-piloto:** Araras/SP  
**Status:** baseline de produto para o MVP; hipóteses e dependências externas permanecem identificadas.

## 1. Visão

Centro em Movimento é uma iniciativa de revitalização do Centro de Araras. Vem pro Centro é a plataforma digital que conecta consumidores, comerciantes, estabelecimentos, programação e experiências presenciais.

> Não queremos apenas levar o comércio local para o digital. Queremos usar a tecnologia para trazer pessoas de volta ao comércio local e dar motivos para que explorem, aproveitem e retornem ao Centro.

O produto não é apenas um catálogo nem um marketplace de retirada. Sua proposta combina descoberta comercial, programação presencial, circuitos de visitação e incentivos entre estabelecimentos.

## 2. Estrutura da iniciativa

- **Centro em Movimento:** iniciativa ampla de revitalização, articulação e melhoria da experiência no Centro.
- **Vem pro Centro:** plataforma digital que conecta as iniciativas.
- **Vitrine Digital do Centro:** descoberta de estabelecimentos, produtos e serviços.
- **Circuito Vivo:** percursos e experiências que estimulam circulação e descoberta presencial.
- **Cronograma do Centro:** programação de eventos, atividades e experiências, com data, horário e local.
- **Fidelidade ao Centro:** programa de benefícios que incentiva consumo e relacionamento entre estabelecimentos.
- **Campanhas Colaborativas:** ações individuais, coletivas e cruzadas.
- **Comunidade e Avaliações:** participação e feedback dos consumidores.
- **Vaga Legal:** proposta complementar de informação e direcionamento sobre estacionamento, sem pressupor integração técnica.

Essas são frentes de uma iniciativa integrada, não produtos independentes nem marcas que precisem de aplicativos próprios.

## 3. Problema e hipóteses

O projeto parte da percepção de que o comércio central enfrenta desafios de visibilidade, descoberta, atração e circulação de consumidores. Ainda não há linha de base local suficiente para quantificar fechamento de lojas, vacância ou perda de fluxo, nem para atribuir causalidade.

Hipóteses que o piloto deve testar:
1. Uma vitrine pesquisável facilita descobrir estabelecimentos e produtos desconhecidos.
2. Uma programação centralizada oferece motivos concretos para visitar o Centro em dias e horários específicos.
3. Circuitos que conectam lojas, espaços e atividades aumentam a diversidade de locais visitados.
4. Benefícios cruzados podem incentivar a descoberta de outros estabelecimentos.
5. Ferramentas simples e apoio assistido reduzem a barreira de entrada digital de pequenos comerciantes.
6. A combinação de comércio, cultura, convivência e informação pode melhorar a experiência de frequentar o Centro.

Não afirmar que essas hipóteses já foram comprovadas em Araras. O piloto deve produzir evidências.

## 4. Objetivos

- Facilitar a descoberta de estabelecimentos, produtos e serviços.
- Tornar visível a programação do Centro.
- Conectar atividades e estabelecimentos por circuitos presenciais.
- Permitir registro de participação e progresso em circuitos.
- Viabilizar campanhas e cupons com regras transparentes.
- Facilitar a presença digital dos comerciantes.
- Gerar indicadores operacionais para avaliar adoção e circulação.

O MVP não garante revitalização econômica, aumento de faturamento, redução de vacância ou permanência física. Esses impactos dependem de adesão, programação, condições urbanas, segurança, mobilidade, parceiros e avaliação longitudinal.

## 5. Públicos e atores

- **Visitante/consumidor:** descobre lojas, produtos, atividades, circuitos e benefícios.
- **Comerciante/responsável:** mantém perfil do estabelecimento, catálogo e campanhas autorizadas.
- **Organizador:** propõe ou mantém informações de atividade, conforme permissão.
- **Administração:** aprova estabelecimentos, publica programação, configura circuitos e campanhas, modera conteúdo e acompanha indicadores.
- **Parceiros potenciais:** Prefeitura, ACIA, SEBRAE, instituições de ensino, organizações culturais e proprietários. Nenhuma parceria é presumida como firmada.

## 6. Princípios

1. Presença física como resultado: recursos centrais conectam descoberta digital a experiências presenciais.
2. Descoberta pública: consultar lojas, produtos, atividades e circuitos não exige conta.
3. Baixa fricção para pequenos negócios.
4. Transparência sobre disponibilidade, regras, custos, datas e cancelamentos.
5. A plataforma direciona ao estabelecimento; não precisa operar checkout ou entrega.
6. Catálogo e estoque são declarados pelo lojista, não dados em tempo real.
7. Privacidade por padrão; sem rastreamento contínuo de localização.
8. WCAG 2.2 AA como referência de conformidade.
9. Evolução por evidência; sem integrações ou complexidade sem necessidade validada.

## 7. Identidade, contas e autorização

- Uma pessoa possui uma conta individual.
- A mesma conta pode atuar como consumidor e responsável por um ou mais estabelecimentos.
- Não haverá login separado por papel.
- No MVP, cada estabelecimento possui um responsável principal.
- Não implementar convites, equipe, memberships ou RBAC granular sem necessidade demonstrada.
- Ações administrativas e comerciais são verificadas no servidor.

## 8. Estabelecimentos e catálogo

Cada estabelecimento deve conter nome público, descrição, endereço, uma ou mais categorias, contato público, situação de publicação e responsável privado. Dados fiscais, se coletados, não serão públicos e só serão solicitados quando houver finalidade definida.

O responsável mantém produtos ou serviços com nome, descrição, preço quando aplicável, imagem opcional e disponibilidade declarada. O sistema exibe a data de atualização do catálogo. Não prometer estoque em tempo real.

Estabelecimentos não aprovados ou suspensos não aparecem como participantes oficiais. O fluxo de aprovação deve ser simples.

## 9. Vitrine e descoberta

A vitrine é pública e mobile-first. Permite explorar estabelecimentos, produtos e serviços por busca e categoria. Páginas públicas apresentam endereço, contato, horário quando informado, catálogo e data de atualização.

Não incluir checkout, pagamento, entrega ou logística no MVP. Solicitação/reserva pode existir como contato prévio, sem converter o produto em marketplace transacional.

## 10. Circuito Vivo

Circuito Vivo é o mecanismo de circulação presencial. Um circuito conecta estabelecimentos, espaços públicos ou atividades em um percurso temático. Pode ter ordem sugerida, paradas obrigatórias/opcionais, período de validade, regras de conclusão e benefício associado.

O consumidor consulta o circuito sem login. Login é necessário para iniciar participação, registrar check-ins e acompanhar progresso individual.

O MVP pode usar QR Code por parada como registro de visita. Check-in não é prova antifraude absoluta: códigos podem ser compartilhados. O produto deve descrevê-lo como registro de participação, aplicar controles de duplicidade e permitir substituição/rotação dos códigos. Não usar GPS contínuo.

Circuitos não devem exigir compra em todas as paradas. Participação pode envolver visita, presença em atividade, descoberta ou interação definida na regra.

## 11. Cronograma do Centro

O cronograma centraliza atividades que dão motivos para visitar o Centro: eventos culturais, feiras, oficinas, apresentações, ações comerciais, experiências e iniciativas comunitárias.

Cada atividade publicada informa título, descrição, data, horário de início e término quando aplicável, local, organizador, categoria, situação e condições de participação. Deve indicar se é gratuita ou paga e se exige inscrição. Atividades canceladas permanecem identificáveis como canceladas, com informação atualizada.

A administração publica e mantém o cronograma no MVP. Estabelecimentos podem sugerir atividades em evolução posterior. Inscrição, lista de presença e notificações não são pré-requisitos para o valor inicial.

Uma atividade pode estar vinculada a circuito e/ou estabelecimento, mas também pode ocorrer em praça ou espaço público.

## 12. Campanhas e Fidelidade ao Centro

Campanhas podem ser individuais, coletivas ou institucionais. Cada campanha informa responsável, período, elegibilidade, benefício, limites, estabelecimentos participantes, regras de resgate, cancelamento e responsável pelo custo.

A primeira versão deve priorizar cupons simples, controlados e auditáveis. Benefício cruzado é importante: uma compra ou participação em um estabelecimento pode habilitar benefício em outro.

Não emitir benefício sem responsável financeiro/comercial identificado. Não converter pontos em dinheiro. Carteira de pontos, lotes, expiração, FEFO e regras configuráveis ficam para evolução específica, salvo exigência expressa e tempo para implementar com segurança.

Se a concessão depender de compra, a compra deve ser confirmada pelo responsável. A confirmação é idempotente e auditável. Compras espontâneas sem vínculo com solicitação não entram automaticamente no fluxo inicial.

Taxa de 1 ponto por real e validade de 12 meses são parâmetros de piloto discutidos anteriormente, não regras aprovadas nem hardcoded. Só entram em vigor após validação comercial e definição de financiamento.

## 13. Reservas e contato

A plataforma pode permitir solicitação de reserva/interesse. Isso não é checkout nem garantia de disponibilidade. A loja precisa confirmar ou recusar. A confirmação de compra, quando aplicável a campanha, é ação posterior do responsável.

O MVP não processa pagamento, entrega ou logística. Se a janela apertar, manter contato direto e adiar solicitação sem comprometer vitrine, cronograma e Circuito Vivo.

## 14. Comunidade e avaliações

A evolução de comunidade pode permitir avaliações sobre atendimento, produtos, acessibilidade, atividades e experiências. O usuário escolhe exibição identificada ou anônima publicamente. O anonimato público não elimina a associação interna à conta para moderação e denúncias.

Avaliações negativas legítimas não devem ser removidas apenas por serem desfavoráveis. Denúncia, política de conteúdo, moderação e resposta do estabelecimento são necessárias antes de ativar publicação aberta.

## 15. Vaga Legal e iniciativas institucionais

Vaga Legal começa como informação e direcionamento a canais oficiais. Integração depende de fonte autorizada, acordo, segurança e viabilidade. O MVP mantém valor sem integração.

Cadastro assistido, fotografia de produtos, capacitação e divulgação coletiva são propostas, não compromissos firmados. Não afirmar subsídios, redução de aluguel, benefícios tributários ou parcerias sem aprovação formal. SEBRAE é entidade privada de apoio, não órgão governamental.

## 16. Experiências

**Consumidor:** Início, Explorar, Circuito Vivo, Cronograma, Campanhas e Minha conta. A página inicial prioriza programação, circuitos ativos, estabelecimentos e campanhas, sem esconder a busca.

**Comerciante:** dashboard simples com sidebar retrátil e topbar de usuário/configurações. Áreas de visão geral, estabelecimento, produtos/serviços, solicitações, campanhas e participação em circuitos.

**Administração:** Django Admin pode cobrir operações internas inicialmente. Interfaces próprias só quando o fluxo exigir melhor experiência.

## 17. Métricas

- Oferta: estabelecimentos cadastrados/aprovados/ativos; catálogo preenchido e atualizado; atividades, circuitos e campanhas ativos.
- Descoberta: visualizações, buscas sem resultado, cliques em contato/como chegar, circuitos iniciados.
- Circulação: check-ins válidos, estabelecimentos distintos visitados, circuitos concluídos, participação em atividades, cupons resgatados.
- Retenção: participantes que retornam, recorrência de visita registrada, comerciantes que atualizam catálogo.

Check-in não mede tempo de permanência. Para estimar permanência, usar pesquisa voluntária ou metodologia específica, sem rastreamento contínuo. Impacto econômico exige linha de base e avaliação; métricas de uso isoladas não demonstram aumento de faturamento ou causalidade.

## 18. Privacidade, segurança e acessibilidade

Aplicar LGPD: finalidade, adequação, necessidade, transparência, segurança, prevenção e direitos do titular. Não coletar localização contínua. Não expor dados privados do responsável, telefone pessoal ou CNPJ por padrão. Definir retenção e canal de contato.

A interface deve atender WCAG 2.2 AA: contraste, teclado, foco visível, rótulos, mensagens de erro, zoom/reflow, leitores de tela, alvos adequados e respeito a prefers-reduced-motion.

## 19. Restrições e dependências

Não presumir parceria institucional, API de estacionamento, estoque em tempo real, financiamento de cupons, agenda oficial de eventos, subsídios ou dados quantitativos locais de fechamento de lojas. O produto deve funcionar com conteúdo mantido pela administração e comerciantes participantes.

## 20. Critério de sucesso

O MVP valida sua proposta quando uma pessoa consegue descobrir uma atividade ou estabelecimento, planejar uma visita, participar de circuito presencial e registrar uma experiência/benefício, enquanto comerciante/administração mantêm informações sem operação excessivamente complexa. A demonstração deve mostrar jornada conectada, não telas independentes.