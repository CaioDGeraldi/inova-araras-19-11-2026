# Spec 007 | Confirmação de compra presencial

## Contexto

O Vem pro Centro conecta descoberta digital e compra presencial. Campanhas do Fidelidade ao Centro podem usar uma compra concluída como condição de elegibilidade, mas a plataforma não processa pagamentos nem integra caixa, PDV ou sistema fiscal.

Esta spec define como o consumidor associa uma compra à sua conta por **Meu QR** e como o responsável autenticado declara que a venda presencial foi concluída. A jornada detalhada está em `docs/flows/PURCHASE_CONFIRMATION.md`.

## Objetivo

Registrar compras presenciais declaradas pelo responsável da loja, de forma auditável e idempotente, para avaliar campanhas elegíveis e emitir os benefícios previstos. O fluxo deve aceitar compras espontâneas, sem reserva prévia.

## Requisitos relacionados

RF-094 a RF-099; RNF-013 a RNF-025, RNF-028, RNF-029 e RNF-039 a RNF-041.

## Atores e permissões

- **Consumidor:** usuário autenticado que solicita e apresenta seu QR temporário.
- **Responsável da loja:** responsável principal autenticado que seleciona uma loja sob sua responsabilidade, escaneia o QR e confirma explicitamente a compra concluída.
- **Servidor:** emite e valida token, verifica autorização, registra a confirmação e avalia campanhas.
- **Admin:** consulta auditoria e executa correções administrativas rastreáveis.

Não criar contas de funcionários, equipes ou permissões granulares no MVP.

## Incluído

- Emissão de **Meu QR** como token aleatório, opaco, temporário, rotativo e de uso único.
- Associação do token a uma conta autenticada sem expor ID sequencial ou dados pessoais.
- Leitura do QR no painel após seleção explícita do estabelecimento.
- Conferência da identificação mínima do consumidor.
- Confirmação explícita da venda pelo responsável após conclusão presencial.
- Registro de consumidor, estabelecimento, operador, instante, referência segura do token, chave de idempotência, valor opcional e campanhas/regras avaliadas.
- Avaliação de todas as campanhas de compra ativas e elegíveis para o estabelecimento.
- Emissão dos benefícios elegíveis após validação server-side.
- Compras espontâneas, sem necessidade de reserva.
- Tratamento de expiração, revogação, repetição, concorrência e falha de conexão.
- Auditoria e correções administrativas sem alteração silenciosa do histórico.

## Excluído

- Checkout, pagamento, caixa, PDV, ERP, adquirente, sistema fiscal e integração de estoque.
- Comprovação independente de que pagamento ou retirada ocorreu.
- Captura de comprovante, OCR ou armazenamento de itens detalhados.
- Exigência padrão de CPF, documento, telefone, e-mail ou dados de cartão.
- Carteira de pontos, cashback, conversão monetária, lotes e FEFO.
- Detecção antifraude absoluta ou prevenção garantida de duas declarações de uma mesma venda real.
- Contas de funcionários e permissões granulares.
- Reserva, status de reserva ou sincronização de conversas externas.

## Modelo conceitual

### ConsumerIdentificationToken

- Conta do consumidor.
- Hash ou representação segura do token, nunca segredo em texto puro.
- Instante de emissão e expiração.
- Estado de consumo/revogação.
- Referência à confirmação que consumiu o token, quando aplicável.

O token é aleatório, opaco, não sequencial, temporário e não contém PII. A duração inicial de referência é de até 60 segundos, sujeita a teste de usabilidade e segurança. Token expirado, revogado ou consumido é recusado. Leitura preliminar não consome o token; ele é consumido na confirmação bem-sucedida.

### PurchaseConfirmation

- Consumidor identificado.
- Estabelecimento.
- Responsável autenticado que declarou a venda.
- Instante da confirmação.
- Referência segura do token utilizado.
- Chave de idempotência da operação.
- Valor total opcional, solicitado apenas quando uma campanha ativa exigir.
- Campanhas e versões de regras avaliadas.
- Resultado de elegibilidade e referências dos benefícios emitidos.

O registro é histórico e auditável. A confirmação representa uma declaração do responsável, não um pagamento processado ou comprovado pela plataforma.

## Fluxo principal

1. Consumidor autentica-se e abre **Perfil → Meu QR**.
2. Servidor emite token temporário e a interface apresenta o QR com indicação de validade.
3. Após concluir a compra presencial, consumidor apresenta o código ao responsável.
4. Responsável autentica-se, seleciona a loja e abre **Registrar compra**.
5. Responsável escaneia o QR.
6. Servidor valida token, validade, estado, associação à conta e autorização da loja; leitura não confirma a compra.
7. Painel apresenta somente identificação mínima para conferência.
8. Responsável declara explicitamente **Confirmar compra concluída**.
9. Sistema solicita apenas os campos exigidos pelas campanhas aplicáveis, como valor total para uma regra com valor mínimo.
10. Servidor revalida autorização, token, loja, campanha, período, limites e idempotência.
11. Na mesma operação consistente, registra a confirmação, consome o token e avalia todas as campanhas de compra elegíveis.
12. Emite benefícios conforme regras e registra a relação entre confirmação, campanha/regra e concessão.
13. Painel apresenta o resultado somente após confirmação do servidor.

Se nenhuma campanha for elegível, a operação pode ser registrada sem benefício. Não emitir pontos ou cupons genéricos.

## Regras de negócio

- A compra deve ter sido concluída presencialmente antes da declaração do responsável.
- A leitura do QR apenas identifica a conta; não registra venda.
- Somente responsável autenticado pela loja selecionada ou admin autorizado pode confirmar.
- Token precisa estar válido, não consumido e associado a uma conta ativa.
- Uma confirmação pode avaliar várias campanhas de compra para aquela loja.
- Valor total é obrigatório somente quando alguma regra ativa exigir; deve ser declarado pelo responsável e não é verificado por integração externa.
- Campanhas precisam estar ativas, dentro do período, vinculadas à loja e ter regras, limites e responsável pelo custo definidos.
- Benefício é emitido somente após confirmação e avaliação positiva da campanha.
- Reserva por WhatsApp/Instagram, mensagem enviada, clique, visita, retirada isolada ou check-in de rota não substituem a confirmação de compra.
- Compras espontâneas podem ser registradas sem reserva prévia.
- Não exigir CPF, documento, telefone, e-mail, comprovante ou dados de cartão por padrão.
- QR de consumidor, QR de parada de rota e QR de cupom são credenciais distintas e não intercambiáveis.

## Idempotência e concorrência

- Cada tentativa lógica de confirmação possui uma chave de idempotência estável para reenvios técnicos.
- Repetir a mesma requisição retorna o resultado já registrado, sem duplicar confirmação ou benefício.
- A unicidade de concessão é garantida por confirmação e campanha/regra.
- Uma confirmação pode conceder benefícios em várias campanhas diferentes.
- Não usar apenas a combinação consumidor + loja como chave de unicidade: compras legítimas distintas podem ocorrer na mesma loja.
- Tentativas concorrentes com o mesmo token não podem gerar mais de uma confirmação.
- A confirmação, o consumo do token e as concessões devem ser gravados de forma consistente; falhas não podem deixar benefício emitido sem a origem correspondente.
- Após falha de conexão, consultar o resultado pela chave de idempotência antes de repetir.

## Segurança e privacidade

- Validar token e autorização exclusivamente no servidor.
- Token aleatório, opaco, de curta duração, uso único e sem dados pessoais.
- Não armazenar token secreto em logs.
- Aplicar limitação de tentativas e proteção contra replay.
- Painel exibe somente identificação mínima do consumidor.
- Registrar operador, estabelecimento, consumidor, instante, campanhas/regras e resultado.
- Definir retenção e acesso à auditoria antes de operar com dados reais.
- Correções administrativas preservam o evento original e registram autor, motivo e instante.

## Limite antifraude

A chave de idempotência impede repetição técnica da mesma requisição; o token de uso único reduz replay. Sem PDV, recibo ou integração fiscal, a plataforma não prova pagamento nem detecta com certeza que a mesma venda real foi registrada novamente com outro token. A confirmação é uma declaração do responsável autenticado, sujeita a auditoria e limites de campanha. Não prometer antifraude absoluto.

## Estados alternativos

| Situação | Resultado |
|---|---|
| Consumidor não autenticado | Exigir autenticação para emitir Meu QR. |
| Token expirado, inválido, revogado ou consumido | Recusar e permitir emissão de novo token. |
| Loja não aprovada/suspensa ou operador sem autorização | Bloquear no servidor. |
| Consumidor/loja não conferem | Cancelar a operação em conferência; não permitir trocar titular manualmente. |
| Nenhuma campanha elegível | Registrar sem benefício, se a operação foi confirmada. |
| Campanha fora do período/limite atingido | Não emitir benefício daquela campanha e registrar o motivo. |
| Valor exigido não informado | Não avaliar a regra que depende dele. |
| Valor abaixo do mínimo | Confirmar compra sem benefício daquela campanha. |
| Falha antes da confirmação | Não apresentar sucesso nem consumir token. |
| Falha após envio | Consultar chave de idempotência e estado do servidor antes de repetir. |
| Duas requisições concorrentes com o mesmo token | No máximo uma confirmação. |

## Critérios de aceitação

- [ ] Consumidor autenticado gera e apresenta Meu QR.
- [ ] QR é temporário, rotativo, opaco e não contém dados pessoais.
- [ ] Token expirado, revogado, inválido ou consumido é recusado.
- [ ] Responsável seleciona uma loja sob sua responsabilidade.
- [ ] Painel lê QR e exibe somente identificação mínima.
- [ ] Leitura não registra compra automaticamente.
- [ ] Responsável confirma explicitamente venda presencial concluída.
- [ ] Compra espontânea pode ser registrada sem reserva.
- [ ] Valor só é solicitado quando regra ativa exigir.
- [ ] Servidor revalida operador, loja, token, campanhas, período, limites e elegibilidade.
- [ ] Uma confirmação avalia todas as campanhas de compra aplicáveis.
- [ ] Benefício só é emitido após confirmação válida e campanha elegível.
- [ ] Reenvio técnico não duplica confirmação ou benefício.
- [ ] Compras legítimas distintas do mesmo consumidor na mesma loja continuam possíveis.
- [ ] Concorrência com o mesmo token não gera duas confirmações.
- [ ] Falhas técnicas não são apresentadas como sucesso.
- [ ] Auditoria registra consumidor, loja, operador, instante, regras e resultado.
- [ ] QR de consumidor, QR de rota e QR de cupom são independentes.
- [ ] Interface não afirma que o QR comprova pagamento ou elimina fraude.

## Decisões consolidadas

- P1 do MVP, junto a campanhas e cupons simples.
- Token temporário com referência inicial de até 60 segundos; duração final depende de testes.
- Responsável principal autenticado é o operador no MVP.
- Valor total somente quando regra ativa exigir.
- Compra é declaração manual do responsável, sem integração externa de pagamento.
- Pontos e carteira complexa permanecem P2.
