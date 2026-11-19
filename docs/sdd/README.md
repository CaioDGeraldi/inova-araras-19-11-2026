# Guia de especificação do projeto

Este repositório contém contexto e especificações do produto Inova Araras. O processo, orquestração, papéis dos agentes, workflow de Issues/PRs e regras gerais SDD são delegados ao FractawProjects. Este documento não replica o sistema de agentes.

## Fonte de verdade
1. Decisões aprovadas e registradas.
2. PRD: visão e requisitos de produto.
3. MVP: prioridade e limite da entrega.
4. Arquitetura e decisões: restrições técnicas.
5. Specs: requisitos e critérios de aceitação de cada mudança.
6. CURRENT_STATE: fotografia do estado operacional, não substitui documentos normativos.

## Fluxo esperado
Contexto/Issue → spec e critérios de aceitação → plano e tasks gerados conforme workflow do FractawProjects → implementação → testes/evidências → revisão → PR → atualizar estado.

## Specs
Cada mudança relevante deve possuir spec em `docs/specs/NNN-slug/spec.md`. Critérios podem estar na spec ou em `acceptance.md`. Plan/tasks não precisam ser duplicados no repositório se o FractawProjects já os administra; registrar apenas quando exigido ou quando forem artefatos úteis e persistentes.

## Regras específicas
- Usar MVP como filtro de escopo.
- Entregar slices verticais demonstráveis.
- Distinguir proposta, decisão e hipótese.
- Decisões reversíveis dentro da arquitetura podem ser tomadas pelo agente e documentadas. Mudança de produto, dados sensíveis, arquitetura fundamental ou expansão de escopo exige aprovação.
- Testes reportados devem ser realmente executados.
- Atualizar `docs/project-state/CURRENT_STATE.md` ao finalizar trabalho significativo.
- Nunca fazer merge sem autorização explícita do responsável.
