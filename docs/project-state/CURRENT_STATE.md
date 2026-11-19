# Estado atual do projeto

**Atualizado:** 19/11/2026, documentação dos fluxos de descoberta.

## Contexto

1º Inova Araras, 19/11/2026. Iniciativa: Centro em Movimento. Plataforma: Vem pro Centro. Desenvolvimento individual.

## Repositório e PRs

- Branch padrão: main.
- Issue #3: fundação Django.
- PR #4: fundação Django, aberto e não mesclado segundo a última verificação registrada. Validar uv.lock, Python 3.12, migrations, PostgreSQL, Django check, Ruff e pytest antes de assumir concluído.
- PR #5: preparação documental, branch 001/docs/project-readiness, alvo main. Esta atualização amplia o PR com baseline de produto, requisitos, domínio, plano de entrega e fluxos.
- Não foi feito merge de PR #4 ou #5 nesta etapa.

## Documentação consolidada nesta branch

- PRD revisado: visão, atores, jornadas, Rotas de Descoberta, Cronograma, campanhas, privacidade e métricas.
- MVP revisado: P0/P1/P2, critérios de demonstrabilidade e preparação do seed fictício.
- Requisitos funcionais identificados.
- Requisitos não funcionais e metas verificáveis.
- Modelo de domínio, relações, estados e invariantes.
- Arquitetura e decisões revisadas.
- Plano de entrega e riscos.
- Guia SDD reforça que FractawProjects é o motor do workflow.

## Baseline de produto

A jornada central é: descobrir → planejar → visitar → registrar participação → explorar/benefício → retornar.

O núcleo de diferenciação é a integração de Vitrine Digital, Cronograma do Centro e Rotas de Descoberta. Campanhas/cupons simples complementam a jornada. Inteligência comercial, pesquisas de lacunas e painel institucional são evolução P2, sujeita a governança e validação de privacidade. Carteira de pontos complexa, pagamentos, GPS contínuo, integração Vaga Legal e aplicativo nativo ficam fora do núcleo inicial.

## Pendências antes da implementação

1. Revisar e validar PR #4 e a fundação técnica.
2. Validar ordem final dos slices se o desafio exigir restrição de escopo diferente.
3. Identificar estabelecimentos, locais e atividades reais disponíveis para o piloto; marcar dados fictícios como demonstração.
4. Definir regra operacional de QR por parada/ocorrência e processo de rotação do código.
5. Confirmar se cupons entram no primeiro slice ou após a jornada de rota.
6. Confirmar responsável e regras comerciais de cada benefício antes de ativar campanhas.
7. Definir política de privacidade, retenção e contato antes de dados reais.
8. Revisar as specs 002–006 e gerar Issues por fatia vertical via FractawProjects, sem duplicar o workflow.

## Validação

Nenhum teste de aplicação foi executado por esta atualização documental. Não declarar fundação, banco, migrations, endpoints ou testes como validados.

## Fluxos documentados

1. `docs/flows/CONSUMER_NAVIGATION.md`: navegação principal do consumidor, cinco destinos, descoberta pública, Agenda, Rotas de Descoberta, Perfil e autenticação contextual.
2. `docs/flows/COMMERCE_DISCOVERY.md`: busca e categorias, resultados, páginas públicas de estabelecimento e produto/serviço, contato, orientação de visita e estados alternativos.

Próximos fluxos previstos:
- Rotas de Descoberta: consulta, detalhe, participação, paradas, check-in e conclusão.
- Painel do proprietário: acesso com a mesma conta, gestão do estabelecimento e catálogo.
- Demonstração integrada: encadeamento das jornadas de consumidor e proprietário para o pitch.

## Preparação da demonstração

- Seed demonstrativo documentado; implementação do comando `python manage.py seed_demo` ainda pendente.
- Dados do seed devem ser fictícios, determinísticos, identificáveis como demonstração e isolados de dados reais.
- Demonstração prevista em duas perspectivas: consumidor e proprietário de estabelecimento.
- Os fluxos detalhados de navegação são definições funcionais, não protótipos nem implementação de telas.
