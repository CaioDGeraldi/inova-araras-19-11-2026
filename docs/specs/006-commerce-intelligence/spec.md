# Spec 006 | Inteligência comercial e diagnóstico de lacunas

## Contexto

Centro em Movimento pretende fortalecer a atividade comercial e a experiência de frequentar o Centro. O Vem pro Centro pode produzir sinais agregados sobre o que as pessoas procuram, quais categorias possuem baixa cobertura na plataforma e quais necessidades precisam ser investigadas com comerciantes e consumidores.

Essa capacidade não deve se tornar um mecanismo de vigilância. O objetivo é apoiar diagnóstico e planejamento institucional sem expor pessoas, consultas individuais ou desempenho comercial de estabelecimentos específicos.

## Objetivo

Definir como identificar buscas sem resultados, estimar possíveis categorias com demanda não atendida, realizar pesquisas de campo e apresentar indicadores agregados em painel restrito para planejamento público e institucional.

## Prioridade e escopo

- Prioridade: P2, evolução posterior ao núcleo de descoberta e circulação.
- Esta spec documenta comportamento e salvaguardas; não obriga implementação no MVP inicial.
- Nenhuma integração com base governamental, sistema de terceiros ou fonte externa é presumida.
- A funcionalidade deve ser útil mesmo sem dados institucionais externos.

## Requisitos relacionados

RF-120 a RF-133; RNF-022, RNF-025, RNF-035 a RNF-038.

## Conceitos

### 1. Busca sem resultado

Consulta que, após normalização e aplicação dos filtros, não retorna estabelecimento, produto ou serviço relevante na plataforma.

Estados analíticos distintos:
- **zero resultado:** nenhum item relevante encontrado;
- **baixa cobertura:** poucos resultados para a consulta/categoria;
- **indisponibilidade declarada:** resultados existem, mas os itens relevantes estão marcados como indisponíveis;
- **inconclusiva:** consulta ambígua, inválida, fora do domínio comercial ou não classificável.

O sistema não deve tratar esses estados como equivalentes.

### 2. Sinal de demanda não atendida

Hipótese de oportunidade que combina mais de uma fonte:
- recorrência e volume de buscas sem resultado;
- cobertura de lojas e produtos cadastrados por categoria;
- disponibilidade declarada;
- pesquisa voluntária com consumidores;
- consulta a comerciantes e levantamento presencial.

Uma busca isolada ou a falta de cadastro de uma loja não comprova ausência de oferta no Centro.

### 3. Painel de inteligência institucional

Interface de acesso restrito para perfis institucionais autorizados e administração do projeto. Apresenta somente indicadores agregados, tendências, metodologia, cobertura e limitações.

Não é painel de vigilância, CRM de consumidores, ranking de lojas ou ferramenta de decisão automática.

### 4. Pesquisa de lacunas comerciais

Pesquisa voluntária estruturada com consumidores, visitantes e comerciantes para validar:
- produtos e serviços procurados;
- categorias pouco encontradas;
- barreiras para visitar o Centro;
- necessidades de acessibilidade, mobilidade e informação;
- dificuldades de digitalização e divulgação dos estabelecimentos.

## Atores e permissões

- **Visitante/consumidor:** não tem acesso a dados analíticos individuais; pode participar voluntariamente de pesquisas quando disponíveis.
- **Comerciante:** pode responder pesquisas direcionadas e consultar orientações agregadas disponibilizadas a todos em condições equivalentes.
- **Administração do projeto:** configura taxonomia, acompanha indicadores, conduz pesquisas e registra validações de campo.
- **Perfil institucional autorizado:** consulta painéis agregados conforme finalidade e escopo de acesso aprovados.
- **Operador técnico autorizado:** acesso excepcional a dados operacionais minimizados, somente para suporte, segurança e prazo definido, com auditoria.

## Fluxo A — Registrar busca sem resultado

1. Consumidor realiza busca na vitrine.
2. A aplicação executa busca normal e determina o estado do resultado.
3. Se a busca for classificada como zero resultado, baixa cobertura ou indisponibilidade, registra evento minimizado.
4. Antes do armazenamento analítico, normaliza a consulta e remove ou descarta texto livre que possa conter dado pessoal.
5. Associa somente categoria/taxonomia, estado do resultado, filtros não identificáveis e período agregado.
6. Eventos brutos, se tecnicamente indispensáveis, ficam com acesso restrito e retenção curta definida; não entram no painel.
7. Processo periódico produz agregações protegidas.

Não associar o evento a User ID, e-mail, telefone, IP persistente, cookie identificador, localização precisa ou histórico de navegação para o painel analítico.

## Fluxo B — Identificar possível demanda não atendida

1. Agregar volume e recorrência de sinais por categoria e período.
2. Calcular cobertura da plataforma: estabelecimentos ativos e produtos/serviços publicados na categoria.
3. Considerar disponibilidade declarada e data de atualização do catálogo.
4. Cruzar com resultados de pesquisas voluntárias, quando houver.
5. Identificar sinais que merecem investigação, não declarar automaticamente que a categoria inexiste no Centro.
6. Administração registra validação de campo: confirmada, refutada ou inconclusiva.
7. Relatório mostra método, período, cobertura, tamanho da amostra e limitações.

Categorias com poucos estabelecimentos cadastrados podem refletir baixa adesão à plataforma, não falta de oferta real. O painel deve exibir a cobertura da plataforma para evitar essa interpretação.

## Fluxo C — Pesquisa de campo

1. Administração define pergunta de pesquisa, finalidade, público, método, responsável e período.
2. Define campos estritamente necessários e aviso de privacidade.
3. Participação é voluntária; não condicionar benefício essencial à resposta.
4. Respostas são armazenadas com acesso restrito e prazo de retenção definido.
5. Relatórios são publicados somente em forma agregada e com limitações metodológicas.
6. Amostras de conveniência são identificadas como exploratórias, sem alegação de representatividade estatística.

## Fluxo D — Consultar painel institucional

1. Usuário institucional recebe autorização individual, escopo e finalidade.
2. Autentica-se e acessa somente visões agregadas permitidas.
3. Seleciona período e categoria dentro dos filtros aprovados.
4. O painel apresenta indicadores, cobertura, limiar aplicado, data de atualização, método e limitações.
5. Células abaixo do limiar são suprimidas; combinações de filtros que permitam inferência também são bloqueadas.
6. Visualizações e exportações são auditadas.
7. A autorização é revisada periodicamente e revogada quando a finalidade termina.

## Indicadores possíveis

- volume agregado de buscas sem resultado por categoria e período;
- proporção de buscas com zero, poucos ou resultados indisponíveis;
- evolução de buscas por categoria;
- quantidade de estabelecimentos ativos cadastrados por categoria;
- quantidade e atualização de itens publicados por categoria;
- cobertura estimada da vitrine na categoria;
- sinais de demanda recorrentes que aguardam validação;
- resultados agregados de pesquisas com consumidores e comerciantes;
- situação da validação de campo.

Não exibir consultas textuais brutas, listas de pessoas, identificadores, trajetórias, avaliações vinculadas a identidade ou faturamento individual.

## Regras de privacidade e proteção

- Finalidade específica e documentada para cada coleta.
- Minimização desde a captura; evitar coletar identificadores para depois removê-los.
- Não construir histórico individual de consumo para fins institucionais.
- Não exibir linhas individuais nem consultas brutas.
- Aplicar limiar mínimo de volume por célula, definido antes da publicação e revisado conforme risco.
- Suprimir grupos pequenos e bloquear filtros sucessivos que permitam inferência por diferença.
- Evitar granularidade temporal ou geográfica que torne grupos identificáveis.
- Não apresentar métricas de desempenho individual de loja no painel público/institucional.
- Definir retenção e descarte de eventos brutos e respostas de pesquisa.
- Restringir exportações; aplicar a mesma proteção das telas.
- Registrar acesso, exportação, alteração de permissão e operações administrativas.
- Realizar avaliação de risco de reidentificação antes de compartilhar relatórios.
- Não presumir que dados agregados são automaticamente anônimos; avaliar contexto e possibilidade de cruzamento.

O limiar numérico de publicação não é fixado nesta spec. Deve ser definido por avaliação de risco, volume, granularidade e contexto antes de liberar o painel. Até lá, nenhuma célula pequena pode ser exibida.

## Uso institucional dos resultados

Os indicadores podem orientar:
- campanhas de digitalização para categorias pouco representadas;
- capacitação e apoio a comerciantes;
- pesquisas adicionais para confirmar demanda;
- mobilização de estabelecimentos existentes;
- articulação para atrair atividades ou serviços que estejam pouco disponíveis;
- planejamento de eventos, divulgação e experiências no Centro.

O painel oferece subsídios. Não escolhe automaticamente quais negócios devem abrir, não recomenda subsídios individuais e não substitui estudos econômicos ou decisão administrativa.

## Fora do escopo

- Venda ou compartilhamento de dados de consumidores.
- Rastreamento individual ou perfil comportamental.
- Geolocalização contínua.
- Ranking público de lojas por desempenho.
- Exposição de consultas individuais ou respostas de pesquisa.
- Decisão automática de política pública, concessão de benefício ou atração de empreendimento.
- Alegação de demanda comprovada com base somente em buscas digitais.
- Promessa de integração com sistemas públicos ou bases externas.

## Critérios de aceitação

- [ ] Busca sem resultado é distinguida de poucos resultados e indisponibilidade declarada.
- [ ] Evento analítico não contém User ID, contato, identificador persistente ou localização precisa.
- [ ] Texto livre potencialmente pessoal não é exposto nem armazenado sem necessidade.
- [ ] Agregações apresentam categoria, período, cobertura e metodologia.
- [ ] O sistema não classifica ausência de resultados como prova de inexistência de oferta.
- [ ] Sinal de demanda combina mais de uma fonte ou é explicitamente marcado como preliminar.
- [ ] Pesquisa define finalidade, público, método, período, campos e retenção.
- [ ] Resultados de pesquisa apresentam amostra, método e limitações.
- [ ] Painel exige autorização institucional individual e finalidade documentada.
- [ ] Grupos pequenos e filtros que permitam inferência são suprimidos.
- [ ] Painel e exportações não revelam dados individuais ou desempenho comercial de loja.
- [ ] Acessos e exportações são auditados.
- [ ] Administração consegue registrar validação de campo como confirmada, refutada ou inconclusiva.
- [ ] Relatórios não são apresentados como prova de causalidade ou representatividade sem método adequado.

## Testes necessários

- Testes de classificação de zero resultado, poucos resultados e indisponibilidade.
- Testes de normalização e descarte de texto livre com dados pessoais simulados.
- Testes de ausência de identificadores no conjunto analítico.
- Testes de agregação e limiar mínimo.
- Testes de filtros sucessivos e inferência por diferença.
- Testes de autorização e escopo institucional.
- Testes de exportação e auditoria.
- Testes de retenção e descarte.
- Revisão de privacidade e risco de reidentificação antes de qualquer uso com dados reais.

## Decisões pendentes antes da implementação

- Taxonomia comercial inicial e processo de revisão.
- Método de normalização/classificação de buscas.
- Janela temporal e limiar mínimo de agregação.
- Retenção dos eventos operacionais e respostas de pesquisa.
- Modelo de autorização e governança institucional.
- Método de pesquisa de campo e responsável por sua condução.
- Processo de validação presencial das oportunidades.
- Regras de publicação e exportação de relatórios.
