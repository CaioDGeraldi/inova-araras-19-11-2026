# Especificação e SDD do projeto

Este repositório guarda a fonte de verdade do produto Inova Araras: visão, MVP, requisitos, domínio, arquitetura, decisões e estado. Orquestração, agentes, workflow de Issues/PRs e regras gerais de execução ficam no FractawProjects. Não duplicar o motor SDD aqui.

## Hierarquia de fontes

1. Decisões aprovadas pelo responsável do produto.
2. PRD: visão, problema, atores e objetivos.
3. MVP: escopo e prioridades.
4. Requisitos funcionais e não funcionais: comportamento e qualidade verificáveis.
5. Modelo de domínio: entidades, relações, estados e invariantes.
6. Arquitetura e decisões: restrições e escolhas técnicas.
7. Specs: comportamento de uma mudança específica e critérios de aceite.
8. CURRENT_STATE: fotografia operacional, nunca substitui decisões normativas.

Em conflito, decisão aprovada mais recente prevalece; atualizar os documentos afetados para remover divergência.

## Fluxo esperado

Contexto/Issue → spec e critérios de aceitação → plano/tasks pelo FractawProjects → implementação → testes e evidências → revisão → PR → atualização do estado.

## Regras

- Usar MVP como filtro de escopo.
- Entregar fatias verticais demonstráveis.
- Distinguir decisão, recomendação, hipótese e dependência externa.
- Mudança de produto, dados sensíveis, arquitetura fundamental ou expansão de escopo exige aprovação.
- Decisões técnicas reversíveis podem ser propostas pelo agente, justificadas e registradas.
- Testes só podem ser declarados como executados com evidência.
- Atualizar CURRENT_STATE após trabalho significativo.
- Não criar Issue por requisito individual sem agrupar por slice coerente.
- Não duplicar templates, papéis ou workflows já mantidos pelo FractawProjects.
- Nunca fazer merge sem autorização explícita.

## Estrutura

- docs/product/PRD.md
- docs/product/MVP.md
- docs/product/REQUIREMENTS_FUNCTIONAL.md
- docs/product/REQUIREMENTS_NON_FUNCTIONAL.md
- docs/product/DOMAIN_MODEL.md
- docs/architecture/ARCHITECTURE.md
- docs/architecture/DECISIONS.md
- docs/roadmap/DELIVERY_PLAN.md
- docs/specs/NNN-slug/spec.md
- docs/project-state/CURRENT_STATE.md

## Como usar specs

Toda mudança relevante deve possuir spec em docs/specs/NNN-slug/spec.md. A spec deve apontar requisitos afetados, escopo incluído/excluído, atores, regras, dados/estados, segurança/privacidade/acessibilidade, dependências e critérios de aceite.

Plan/tasks não precisam ser duplicados no repositório se FractawProjects já os administra; persistir apenas quando forem artefatos úteis ou exigidos.