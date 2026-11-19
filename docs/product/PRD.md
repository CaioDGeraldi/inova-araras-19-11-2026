# Centro em Movimento | PRD

**Produto digital:** Vem pro Centro  
**Iniciativa:** Centro em Movimento  
**Cidade-piloto:** Araras/SP  
**Status:** baseline de produto para o MVP; hipóteses e dependências externas permanecem identificadas.

## 1. Visão

Centro em Movimento é uma iniciativa de revitalização do Centro de Araras. Vem pro Centro é a plataforma digital que conecta consumidores, comerciantes, estabelecimentos, programação e experiências presenciais.

> Não queremos apenas levar o comércio local para o digital. Queremos usar a tecnologia para trazer pessoas de volta ao comércio local e dar motivos para que explorem, aproveitem e retornem ao Centro.

O produto não é apenas um catálogo nem um marketplace de retirada. Sua proposta combina descoberta comercial, programação presencial, rotas de visitação e incentivos entre estabelecimentos.

## 2. Estrutura da iniciativa

- **Centro em Movimento:** iniciativa ampla de revitalização, articulação e melhoria da experiência no Centro.
- **Vem pro Centro:** plataforma digital que conecta as iniciativas.
- **Vitrine Digital do Centro:** descoberta de estabelecimentos, produtos e serviços.
- **Rotas de Descoberta:** percursos e experiências que estimulam circulação e descoberta presencial.
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
3. Rotas que conectam lojas, espaços e atividades aumentam a diversidade de locais visitados.
4. Benefícios cruzados podem incentivar a descoberta de outros estabelecimentos.
5. Ferramentas simples e apoio assistido reduzem a barreira de entrada digital de pequenos comerciantes.
6. A combinação de comércio, cultura, convivência e informação pode melhorar a experiência de frequentar o Centro.

Não afirmar que essas hipóteses já foram comprovadas em Araras. O piloto deve produzir evidências.

## 4. Objetivos

- Facilitar a descoberta de estabelecimentos, produtos e serviços.
- Tornar visível a programação do Centro.
- Conectar atividades e estabelecimentos por rotas presenciais.
- Permitir registro de participação e progresso em rotas.
- Viabilizar campanhas e cupons com regras transparentes.
- Facilitar a presença digital dos comerciantes.
- Gerar indicadores operacionais para avaliar adoção e circulação.
- Identificar sinais agregados de interesse não atendido e lacunas de oferta, com validação por pesquisas e levantamento local.
- Apoiar o planejamento institucional com dados agregados, transparentes e protegidos.

O MVP não garante revitalização econômica, aumento de faturamento, redução de vacância ou permanência física. Esses impactos dependem de adesão, programação, condições urbanas, segurança, mobilidade, parceiros e avaliação longitudinal.

## 5. Públicos e atores

- **Visitante/consumidor:** descobre lojas, produtos, atividades, rotas e benefícios.
- **Comerciante/responsável:** mantém perfil do estabelecimento, catálogo e campanhas autorizadas.
- **Organizador:** propõe ou mantém informações de atividade, conforme permissão.
- **Administração:** aprova estabelecimentos, publica programação, configura rotas e campanhas, modera conteúdo e acompanha indicadores.
- **Parceiros potenciais:** Prefeitura, ACIA, SEBRAE, instituições de ensino, organizações culturais e proprietários. Nenhuma parceria é presumida como firmada.

## 6. Princípios

1. Presença física como resultado: recursos centrais conectam descoberta digital a experiências presenciais.
2. Descoberta pública: consultar lojas, produtos, atividades e rotas não exige conta.
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

Não incluir checkout, pagamento, entrega ou logística no MVP. A reserva de produto para retirada presencial integra o MVP como compromisso operacional confirmado pela loja, sem converter o produto em marketplace transacional.

## 10. Rotas de Descoberta

Rotas de Descoberta são experiências presenciais temáticas que conectam estabelecimentos, espaços públicos e atividades em um percurso. Podem ser gastronômicas, culturais, históricas, comerciais ou mistas. Uma rota pode definir ordem sugerida, paradas obrigatórias/opcionais, período de validade, regra de conclusão e benefício associado.

A motivação combina três elementos:
- **Descoberta:** apresentar lugares, produtos, atividades e experiências que a pessoa talvez não conhecesse.
- **Progresso:** permitir acompanhar as paradas visitadas e entender o que falta para concluir.
- **Recompensa:** campanhas podem oferecer pontos, cupons, brindes ou experiências após participação elegível, criando um motivo adicional para continuar explorando e retornar ao Centro.

Exemplo ilustrativo: uma rota gastronômica pode conectar uma cafeteria, uma hamburgueria e uma sorveteria. A pessoa consulta o percurso, visita os locais e lê o QR Code disponibilizado em cada parada. Cada check-in aceito registra a parada como visitada e atualiza o progresso. Ao cumprir a regra de conclusão, pode desbloquear um benefício previsto em uma campanha. Gastronomia é apenas um exemplo; não limita os temas possíveis.

O consumidor consulta rotas e detalhes sem login. Login é necessário para iniciar participação, registrar check-ins e acompanhar progresso individual. O detalhe deve apresentar previamente tema, paradas, período, obrigatoriedade, regra de conclusão e eventual recompensa, incluindo suas condições.

O MVP pode usar QR Code por parada como registro de visita. A leitura de um código válido registra a parada na participação e atualiza o progresso. Check-in não é prova antifraude absoluta de presença: códigos podem ser compartilhados. O produto deve descrevê-lo como registro de participação, aplicar controles de duplicidade e permitir revogação/rotação dos códigos. Não usar GPS contínuo.

Rotas não devem exigir compra em todas as paradas. Participação pode envolver visita, presença em atividade, descoberta ou interação definida na regra. O check-in comprova somente que a conta apresentou um código válido associado à parada, não que permaneceu no local ou realizou uma compra.

Benefícios não são automáticos nem inerentes a qualquer rota. Quando houver recompensa, ela deve estar vinculada a uma campanha com responsável identificado, elegibilidade, período, limites, benefício e regras de resgate/cancelamento explícitas. Priorizar incentivos que conectem estabelecimentos: por exemplo, concluir uma rota em uma cafeteria pode habilitar um cupom para uso em uma sorveteria participante. Não emitir pontos ou cupons sem regra e responsável pelo custo definidos.


## 11. Inteligência comercial e oportunidades do Centro

O Vem pro Centro pode produzir indicadores agregados para apoiar o planejamento do comércio e políticas públicas, sem expor consumidores individualmente. Essa capacidade é uma evolução posterior e não deve ser confundida com analytics individual ou monitoramento de pessoas.

### Identificação de buscas sem resultados

Registrar eventos mínimos de busca quando a consulta não retorna resultados relevantes. O registro deve priorizar termo normalizado, categoria/filtros aplicados, período e resultado agregado. Não armazenar identidade do consumidor, identificadores persistentes, localização precisa ou histórico individual para essa finalidade.

Os indicadores devem distinguir:
- busca sem qualquer resultado;
- busca com resultados, mas sem disponibilidade declarada;
- busca com poucos resultados;
- busca potencialmente ambígua, inválida ou sem intenção comercial clara.

Termos livres podem conter dados pessoais. A aplicação deve reduzir esse risco antes de armazenar ou agregar consultas, limitar acesso aos dados operacionais e aplicar retenção curta. O painel não deve exibir consultas individuais.

### Identificação de categorias com demanda não atendida

Uma busca sem resultado não prova que a cidade não oferece aquele produto ou serviço. A oferta pode existir em loja não cadastrada, catálogo incompleto, produto sem nome equivalente ou disponibilidade desatualizada.

Uma oportunidade comercial deve ser classificada somente pela combinação de sinais, como:
- volume e recorrência de buscas normalizadas sem resultado;
- quantidade e cobertura de estabelecimentos/catálogos cadastrados na categoria;
- buscas com poucos resultados ou indisponibilidade declarada;
- resultados de pesquisas voluntárias com consumidores;
- confirmação por levantamento de campo e consulta aos comerciantes.

O sistema deve apresentar nível de confiança, período analisado, cobertura da plataforma e limitações dos dados. Não deve rotular uma categoria como ausente no Centro com base apenas em buscas digitais.

### Painel de inteligência para gestão pública e planejamento

Painel restrito a perfis institucionais autorizados e à administração do projeto, com indicadores agregados por categoria e período, tendências, cobertura do catálogo, sinais de demanda não atendida e resultados de pesquisas de campo.

Regras:
- não apresentar dados pessoais, sessões, trajetórias ou histórico individual;
- não expor consultas em nível de linha;
- suprimir grupos pequenos e combinações que permitam inferir pessoas ou negócios;
- aplicar limiar mínimo de volume e agregação temporal antes de exibir métricas;
- não ranquear publicamente estabelecimentos nem divulgar desempenho comercial individual;
- distinguir dados observados, estimativas, respostas de pesquisa e hipóteses;
- exibir data, cobertura, metodologia e limitações;
- acesso institucional depende de finalidade, autorização, controle de acesso e registro de auditoria.

O painel é instrumento de diagnóstico e planejamento. Não substitui pesquisa econômica, decisão pública ou validação presencial.

### Pesquisas para identificar lacunas comerciais

A iniciativa pode conduzir pesquisas voluntárias com consumidores, comerciantes e visitantes para entender categorias procuradas, necessidades não atendidas, barreiras de acesso, hábitos de visita e dificuldades de digitalização.

Cada pesquisa deve declarar finalidade, público, método, período, responsável, campos coletados, retenção e forma de divulgação. Coletar o mínimo necessário; evitar dados sensíveis e identificação desnecessária. Resultados publicados devem ser agregados e acompanhados de tamanho da amostra, método de recrutamento e limitações. Amostras de conveniência não podem ser apresentadas como representativas de toda a população.

### Uso dos resultados

Os sinais podem orientar campanhas de digitalização, capacitação, mobilização de comerciantes, pesquisas complementares e articulação para atrair categorias ausentes ou pouco representadas. Nenhuma recomendação deve ser tratada como decisão automática de política pública.

## 12. Cronograma do Centro

O cronograma centraliza atividades que dão motivos para visitar o Centro: eventos culturais, feiras, oficinas, apresentações, ações comerciais, experiências e iniciativas comunitárias.

Cada atividade publicada informa título, descrição, data, horário de início e término quando aplicável, local, organizador, categoria, situação e condições de participação. Deve indicar se é gratuita ou paga e se exige inscrição. Atividades canceladas permanecem identificáveis como canceladas, com informação atualizada.

A administração publica e mantém o cronograma no MVP. Estabelecimentos podem sugerir atividades em evolução posterior. Inscrição, lista de presença e notificações não são pré-requisitos para o valor inicial.

Uma atividade pode estar vinculada a rota e/ou estabelecimento, mas também pode ocorrer em praça ou espaço público.

## 13. Campanhas e Fidelidade ao Centro

Campanhas podem ser individuais, coletivas ou institucionais. Cada campanha informa responsável, período, elegibilidade, benefício, limites, estabelecimentos participantes, regras de resgate, cancelamento e responsável pelo custo.

A primeira versão deve priorizar cupons simples, controlados e auditáveis. Benefício cruzado é importante: uma compra ou participação elegível em um estabelecimento pode habilitar benefício em outro. Uma rota pode estar associada a uma campanha para recompensar sua conclusão, desde que a elegibilidade, o período, os limites, o benefício e o responsável pelo custo estejam definidos. A recompensa deve incentivar novas visitas, não exigir compra em todas as paradas.

Não emitir benefício sem responsável financeiro/comercial identificado. Não converter pontos em dinheiro. Carteira de pontos, lotes, expiração, FEFO e regras configuráveis ficam para evolução específica, salvo exigência expressa e tempo para implementar com segurança.

Se a concessão depender de compra, a compra deve ser confirmada pelo responsável. A confirmação é idempotente e auditável. Compras espontâneas sem vínculo com solicitação não entram automaticamente no fluxo inicial.

Taxa de 1 ponto por real e validade de 12 meses são parâmetros de piloto discutidos anteriormente, não regras aprovadas nem hardcoded. Só entram em vigor após validação comercial e definição de financiamento.

## 14. Reservas e contato

Solicitação de reserva/interesse é uma capacidade P1, posterior ao núcleo de descoberta e circulação. Não é checkout nem garantia de disponibilidade. A loja precisa confirmar ou recusar. Até sua implementação, o consumidor pode usar os canais públicos de contato. A confirmação de compra, quando aplicável a campanha, é ação posterior do responsável.

O MVP não processa pagamento, entrega ou logística. Se a janela apertar, manter contato direto e adiar solicitação sem comprometer vitrine, cronograma e Rotas de Descoberta.

## 15. Comunidade e avaliações

A evolução de comunidade pode permitir avaliações sobre atendimento, produtos, acessibilidade, atividades e experiências. O usuário escolhe exibição identificada ou anônima publicamente. O anonimato público não elimina a associação interna à conta para moderação e denúncias.

Avaliações negativas legítimas não devem ser removidas apenas por serem desfavoráveis. Denúncia, política de conteúdo, moderação e resposta do estabelecimento são necessárias antes de ativar publicação aberta.

## 16. Vaga Legal e iniciativas institucionais

Vaga Legal começa como informação e direcionamento a canais oficiais. Integração depende de fonte autorizada, acordo, segurança e viabilidade. O MVP mantém valor sem integração.

Cadastro assistido, fotografia de produtos, capacitação e divulgação coletiva são propostas, não compromissos firmados. Não afirmar subsídios, redução de aluguel, benefícios tributários ou parcerias sem aprovação formal. SEBRAE é entidade privada de apoio, não órgão governamental.

## 17. Experiências

**Consumidor:** Início, Explorar, Rotas, Agenda e Perfil. A barra inferior fixa mantém esses cinco destinos; campanhas e Fidelidade ao Centro são acessadas a partir das seções correspondentes. A composição do feed e os atalhos serão definidos nos fluxos.

**Comerciante:** dashboard simples com sidebar retrátil e topbar de usuário/configurações. Áreas de visão geral, estabelecimento, produtos/serviços, solicitações, campanhas e participação em rotas.

**Administração:** Django Admin pode cobrir operações internas inicialmente. Interfaces próprias só quando o fluxo exigir melhor experiência.

## 18. Métricas

Além das métricas operacionais, a evolução de inteligência comercial poderá acompanhar:
- buscas sem resultado por categoria e período;
- buscas com poucos resultados ou sem disponibilidade declarada;
- cobertura de estabelecimentos e catálogos por categoria;
- recorrência de sinais de demanda não atendida;
- resultados agregados de pesquisas voluntárias;
- oportunidades confirmadas ou descartadas após validação de campo.

Esses indicadores não demonstram, isoladamente, demanda econômica suficiente para abertura de negócio. Devem ser interpretados com cobertura, amostra, sazonalidade e limitações metodológicas.



- Oferta: estabelecimentos cadastrados/aprovados/ativos; catálogo preenchido e atualizado; atividades, rotas e campanhas ativos.
- Descoberta: visualizações, buscas sem resultado, cliques em contato/como chegar, rotas iniciadas.
- Circulação: check-ins válidos, estabelecimentos distintos visitados, rotas concluídas, participação em atividades, cupons resgatados.
- Retenção: participantes que retornam, recorrência de visita registrada, comerciantes que atualizam catálogo.

Check-in não mede tempo de permanência. Para estimar permanência, usar pesquisa voluntária ou metodologia específica, sem rastreamento contínuo. Impacto econômico exige linha de base e avaliação; métricas de uso isoladas não demonstram aumento de faturamento ou causalidade.

### Inteligência e pesquisas: salvaguardas específicas

- Não construir perfil individual de consumo para o painel institucional.
- Não disponibilizar consultas brutas ou respostas individuais.
- Aplicar agregação, limiar mínimo de grupo e supressão de células pequenas.
- Impedir filtros cruzados que permitam reidentificação por diferença entre consultas.
- Separar dados operacionais identificáveis, quando estritamente necessários, dos conjuntos analíticos.
- Definir prazo de retenção e descarte dos eventos brutos.
- Pesquisas devem ser voluntárias, transparentes e limitadas à finalidade declarada.
- Revisar risco de reidentificação antes de compartilhar relatórios ou exportações.

## 19. Privacidade, segurança e acessibilidade

Aplicar LGPD: finalidade, adequação, necessidade, transparência, segurança, prevenção e direitos do titular. Não coletar localização contínua. Não expor dados privados do responsável, telefone pessoal ou CNPJ por padrão. Definir retenção e canal de contato.

A interface deve atender WCAG 2.2 AA: contraste, teclado, foco visível, rótulos, mensagens de erro, zoom/reflow, leitores de tela, alvos adequados e respeito a prefers-reduced-motion.

## 20. Restrições e dependências

Não presumir parceria institucional, API de estacionamento, estoque em tempo real, financiamento de cupons, agenda oficial de eventos, subsídios ou dados quantitativos locais de fechamento de lojas. O produto deve funcionar com conteúdo mantido pela administração e comerciantes participantes.

## 21. Critério de sucesso

O MVP valida sua proposta quando uma pessoa consegue descobrir uma atividade ou estabelecimento, planejar uma visita, participar de rota presencial e registrar uma experiência/benefício, enquanto comerciante/administração mantêm informações sem operação excessivamente complexa. A demonstração deve mostrar jornada conectada, não telas independentes.

## Experiência e navegação do consumidor

A interface do consumidor deve adotar padrões familiares de aplicativos móveis de descoberta e comércio, reduzindo a necessidade de aprendizado. A referência de familiaridade é a navegação de aplicativos como Instagram; não se deve copiar sua identidade visual.

Em dispositivos móveis, a navegação principal utiliza uma barra inferior fixa com cinco seções:

- **Início:** ponto de entrada e descoberta.
- **Explorar:** busca por estabelecimentos, produtos, serviços e categorias.
- **Rotas:** Rotas de Descoberta, paradas e progresso.
- **Agenda:** Cronograma do Centro e atividades.
- **Perfil:** dados da conta, favoritos, Fidelidade ao Centro, avaliações e solicitações quando disponíveis.

A estrutura é uma decisão de navegação. A composição do feed, os atalhos internos e os detalhes de cada tela serão definidos nos fluxos antes da implementação visual. A experiência do proprietário permanece em painel operacional próprio, com sidebar retrátil e topbar, usando a mesma identidade e autenticação da pessoa.

A interface deve ser mobile-first, previsível, consistente, acessível e responsiva. Em telas maiores, a navegação pode adaptar sua apresentação sem alterar a hierarquia das seções. Não exigir login para descoberta pública.
