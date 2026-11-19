# Spec 004 | Circuito Vivo

## Contexto
Circuito Vivo conecta estabelecimentos, atividades e espaços do Centro em percursos de descoberta. Seu propósito é estimular circulação física e experiências, não obrigar uma sequência de compras.

## Objetivo
Permitir que a administração monte circuitos, que visitantes conheçam suas paradas e que usuários autenticados registrem participação presencial por check-in e acompanhem progresso.

## Requisitos relacionados
RF-050 a RF-065; RNF-001 a RNF-008, RNF-013 a RNF-025, RNF-027 a RNF-029, RNF-031.

## Atores e permissões
- Visitante: consulta circuitos e paradas.
- Participante autenticado: inicia participação e registra check-in.
- Admin: cria, publica, ativa, cancela e arquiva circuitos; administra tokens.
- Owner de estabelecimento: não altera circuito global no primeiro MVP.

## Incluído
- Circuit e CircuitStop.
- Paradas vinculadas a Store, Event ou Place.
- Ordem sugerida, obrigatoriedade e instruções.
- Regra explícita de conclusão.
- CircuitParticipation.
- QR Code por parada com token opaco.
- CheckIn validado no servidor.
- Progresso e estado da participação.

## Excluído
- GPS contínuo ou geofencing obrigatório.
- Compra obrigatória em cada parada.
- Ranking competitivo e gamificação complexa.
- Pontos financeiros automáticos no primeiro corte.
- Prova antifraude absoluta de presença.

## Fluxo principal
1. Admin cria circuito em rascunho e adiciona paradas.
2. Admin define período, regra de conclusão e quais paradas são obrigatórias/opcionais.
3. Admin publica circuito e gera/ativa token de check-in por parada.
4. Visitante consulta circuito e decide participar.
5. Usuário autenticado inicia participação.
6. No local, usuário lê QR Code; aplicação envia token ao servidor.
7. Servidor valida token, período, estado do circuito, parada, participação e política de repetição.
8. Servidor grava CheckIn atomicamente e recalcula progresso.
9. Quando regra é satisfeita, participação passa a completed.

## Regras e invariantes
- Circuito publicado possui ao menos uma parada.
- Cada parada possui exatamente um alvo válido no MVP: Store, Event ou Place.
- Circuito pode definir ordem sugerida sem exigir sequência, salvo configuração explícita.
- Paradas opcionais não bloqueiam conclusão.
- Nenhuma parada exige compra por padrão.
- Check-in exige usuário autenticado e participação ativa.
- Check-in aceito pertence à participação e circuito corretos.
- Duplicidade é bloqueada pela política configurada e também por restrição no banco.
- Token não contém dados pessoais nem identificadores sequenciais.
- Token revogado/expirado não gera check-in.
- QR Code compartilhado pode gerar fraude; o sistema não deve prometer prova absoluta de presença.
- Check-in aceito não é apagado silenciosamente; correção é auditada.

## Estados
Circuit: draft, published, active, cancelled, archived.  
Participation: active, completed, cancelled.  
CheckIn: submitted, accepted, rejected.

## Concorrência e segurança
- Validar no servidor; nunca confiar em estado enviado pelo navegador.
- Operação de check-in transacional.
- Impedir duas gravações concorrentes para a mesma chave de unicidade.
- Limitar tentativas e registrar rejeições relevantes sem guardar token secreto em logs.
- Permitir rotação/revogação de token.
- QR deve ser exibido no estabelecimento e o operador precisa de procedimento simples para substituí-lo.
- Não coletar localização contínua.

## Critérios de aceitação
- [ ] Admin cria circuito e adiciona Store/Event/Place como paradas.
- [ ] Circuito público exibe paradas, ordem sugerida e regra de conclusão.
- [ ] Visitante consulta sem login.
- [ ] Usuário autenticado inicia participação.
- [ ] Check-in válido registra participação uma única vez conforme regra.
- [ ] Token inválido, revogado, expirado ou fora do período é recusado.
- [ ] Check-in de circuito/parada incompatível é recusado.
- [ ] Tentativas concorrentes não duplicam participação.
- [ ] Progresso considera apenas check-ins aceitos e paradas obrigatórias.
- [ ] Conclusão acontece somente quando regra é satisfeita.
- [ ] Circuito pode ser concluído sem compra em cada parada.
- [ ] Correções e cancelamentos preservam auditoria.
- [ ] Testes cobrem autorização, token, duplicidade, concorrência e transições.

## Decisões em aberto
- Política exata de repetição: uma vez por participação, por parada ou por ocorrência.
- QR estático rotacionável versus token de curta duração; avaliar viabilidade operacional.
- Se CircuitEdition/Occurrence é necessária no piloto.
- Se parada aceita check-in pelo comerciante como fallback de acessibilidade/tecnologia.
