# Spec 009 | Administração e operação da plataforma

## Contexto
A administração do Vem pro Centro coordena cadastros, categorias, cronograma e Rotas de Descoberta. Esses domínios já possuem regras próprias nas Specs 002, 003 e 004. Esta spec define a camada administrativa transversal, o acesso ao painel e as capacidades operacionais que não devem ser duplicadas em cada domínio.

## Objetivo
Oferecer uma área administrativa protegida para acessar os recursos globais do produto, acompanhar operações P1 e manter trilha de auditoria, sem concentrar no painel dados ou poderes que não sejam necessários à operação.

## Requisitos relacionados
RF-005, RF-015, RF-030, RF-050, RF-064, RF-105, RF-110 a RF-114; RNFs de autenticação, autorização, integridade, privacidade, auditoria e acessibilidade aplicáveis.

## Prioridade
- **P0:** autorização administrativa e acesso às operações de categorias, estabelecimentos, cronograma e Rotas de Descoberta.
- **P1:** consulta operacional de check-ins, campanhas e resgates; indicadores agregados; trilha de auditoria; separação de dados demonstrativos e reais.
- **P2:** inteligência comercial, pesquisas e painel institucional de lacunas de oferta, cobertos pela Spec 006.

## Atores e permissões
- Administrador: usuário explicitamente autorizado a operar recursos globais.
- Moderador: administrador ou perfil autorizado para moderação, conforme política definida na Spec 008.
- Responsável de estabelecimento: acessa somente os recursos da própria loja, conforme Specs 002 e 005.
- Consumidor/visitante: não possui acesso administrativo.

A forma de provisionar e revogar administradores deve ser segura e não pode depender de cadastro público ou de um campo controlado pelo próprio usuário. Não criar RBAC granular ou equipe de estabelecimento no MVP sem necessidade demonstrada.

## Escopo P0
- Acesso protegido à área administrativa.
- Verificação de autorização no servidor em páginas, ações e endpoints.
- Navegação central para categorias, estabelecimentos, Cronograma do Centro e Rotas de Descoberta.
- Integração com os fluxos de domínio existentes, sem duplicar regras de aprovação, publicação, cancelamento, check-in ou revogação.
- Registro das decisões administrativas críticas.

## Escopo P1
- Consulta operacional de registros de check-in, campanhas e resgates.
- Indicadores operacionais agregados, com período e definição explícitos.
- Trilha de auditoria para ações críticas.
- Identificação e separação de dados demonstrativos e reais.

## Fora do escopo
- Painel de inteligência comercial e diagnóstico institucional P2.
- Consulta de buscas individuais, sessões ou trajetórias.
- Alteração direta de registros transacionais sem fluxo específico de correção.
- Impersonação de consumidores ou proprietários.
- Acesso irrestrito a dados pessoais por conveniência.
- Gestão de equipes, convites e permissões granulares por estabelecimento.

## Fluxo administrativo
1. Administrador acessa a rota protegida.
2. Servidor valida autenticação e autorização.
3. Painel apresenta navegação para os domínios administrativos.
4. Administrador opera categorias, estabelecimentos, cronograma e rotas por seus fluxos específicos.
5. Ações críticas registram autor, recurso, ação, instante e motivo quando aplicável.
6. No P1, administrador consulta registros operacionais e indicadores agregados.
7. Registros demonstrativos são identificados e podem ser filtrados/separados dos dados reais.
8. Falhas de consulta ou gravação são apresentadas sem sugerir sucesso inexistente.

## Regras e invariantes
- A autorização é aplicada no servidor; ocultar links na interface não é controle de acesso suficiente.
- Conta comum não pode conceder a si mesma privilégio administrativo.
- O painel mostra apenas dados necessários à tarefa.
- As regras de domínio permanecem nas Specs 002, 003, 004, 005, 007 e 008.
- RF-110 é atendido pela navegação administrativa e pelas capacidades de gestão definidas nessas specs.
- RF-111 permite consulta operacional, não edição arbitrária de check-ins, compras, campanhas ou resgates.
- RF-112 exibe indicadores agregados e não deve ser confundido com inteligência comercial P2.
- RF-113 exige trilha para ações críticas; a lista exata de eventos auditáveis deve ser definida antes da implementação.
- RF-114 exige identificação inequívoca dos registros de demonstração e filtros que impeçam mistura silenciosa.
- Compras confirmadas são declarações dos responsáveis, não faturamento auditado.
- Dados demonstrativos nunca podem ser apresentados como dados reais.
- Nenhuma ação administrativa pode apagar silenciosamente histórico transacional ou de participação.
- Correções exigem operação própria, motivo e autoria auditáveis.

## Auditoria mínima
A trilha deve registrar, conforme o tipo de operação:
- administrador/operador;
- tipo e identificador do recurso;
- ação executada;
- instante;
- resultado;
- motivo, quando a ação exigir justificativa;
- referência segura ao estado anterior/novo quando necessário, sem copiar segredos ou dados pessoais desnecessários.

Não armazenar tokens QR, códigos secretos de cupons ou credenciais em logs de auditoria.

## Indicadores operacionais P1
Indicadores possíveis:
- estabelecimentos por estado de aprovação;
- atividades publicadas/canceladas por período;
- rotas publicadas e participações/check-ins aceitos;
- campanhas ativas e cupons emitidos/resgatados;
- registros de compra confirmada, explicitamente identificados como declarações de responsáveis.

Cada indicador precisa informar período, unidade e fonte. Não expor ranking público de lojas nem inferir faturamento.

## Dados demonstrativos
- Todo registro criado pelo seed de demonstração deve ter marcador inequívoco de origem.
- Filtros e relatórios devem permitir separar registros demonstrativos e reais.
- Dados demonstrativos devem ser fictícios e não reproduzir informações pessoais ou comerciais reais.
- Operações reais não podem ser alteradas ou removidas por rotinas de seed.
- A identificação demonstrativa não substitui o cuidado para evitar exposição de credenciais.

## Segurança e privacidade
- Menor privilégio e autorização por recurso.
- Segregação entre dados administrativos e páginas públicas.
- Auditoria de acesso e ações críticas.
- Proteção contra enumeração e acesso direto a IDs de recursos.
- Não registrar segredos nem dados pessoais desnecessários.
- Indicadores P1 agregados; controles reforçados de privacidade e pesquisas ficam na Spec 006.
- Acessibilidade por teclado e leitor de tela.

## Critérios de aceitação
### P0
- [ ] Usuário sem permissão não acessa o painel nem executa ações administrativas por endpoint.
- [ ] Administrador acessa gestão de categorias, estabelecimentos, cronograma e rotas.
- [ ] Cada domínio mantém sua própria validação e autorização.
- [ ] Ações críticas administrativas registram autor, recurso, ação e instante.
- [ ] Acesso administrativo não permite impersonação de usuários.

### P1
- [ ] Administrador consulta registros operacionais de check-in, campanhas e resgates.
- [ ] Indicadores apresentam período, unidade e fonte.
- [ ] Indicadores não expõem dados individuais nem apresentam compra declarada como faturamento auditado.
- [ ] Auditoria registra ações críticas e motivo quando aplicável.
- [ ] Registros demonstrativos são identificáveis e separáveis dos reais.
- [ ] Relatórios não misturam dados demonstrativos e reais sem indicação explícita.
- [ ] Testes cobrem autorização, auditoria e separação de dados.

## Decisões em aberto
- Processo de provisionamento, recuperação e revogação de administradores.
- Lista final de ações auditáveis e política de retenção.
- Indicadores operacionais exatos do P1.
- Se consulta operacional terá filtros por estabelecimento/período e quais perfis podem usá-los.
- Como representar correções administrativas sem alterar eventos originais.
