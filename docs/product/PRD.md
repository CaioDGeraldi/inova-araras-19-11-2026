# Centro em Movimento | PRD

## 1. Visão
Centro em Movimento é uma iniciativa de revitalização do comércio central de Araras apoiada por digitalização, descoberta, campanhas e incentivos para circulação entre estabelecimentos. O aplicativo chama-se **Vem pro Centro**.

> Não queremos apenas levar o comércio local para o digital. Queremos usar a tecnologia para trazer pessoas de volta ao comércio local.

## 2. Problema e hipóteses
O projeto parte da percepção de que o comércio central enfrenta desafios de visibilidade, descoberta e atração de consumidores, especialmente diante de experiências digitais de compra. Não há, neste documento, linha de base local suficiente para quantificar fechamento de lojas ou atribuir causalidade.

Hipóteses a validar: catálogo digital aumenta descoberta; campanhas colaborativas incentivam circulação; benefícios cruzados ajudam consumidores a conhecer outros estabelecimentos; ferramentas simples reduzem barreiras à digitalização.

## 3. Público e atores
- Consumidores e visitantes do Centro.
- Comerciantes e responsáveis pelos estabelecimentos.
- Administração do projeto e potenciais parceiros institucionais, sem presumir acordos.

## 4. Produto
Vem pro Centro oferece vitrine pesquisável, páginas de estabelecimentos e produtos, informações declaradas pelos lojistas, solicitações/reservas quando disponíveis, campanhas e programa coletivo de fidelidade.

## 5. Identidade e contas
Uma conta individual pode atuar como consumidor e responsável por uma ou mais lojas. Não há login separado por papel. No MVP, cada Store tem owner principal. Não implementar memberships, convites ou RBAC granular sem necessidade aprovada.

## 6. Estabelecimentos
Cadastro simples: nome, categorias múltiplas, endereço, contato público, dados necessários de identificação e responsável. CNPJ, se coletado, deve ser protegido e não exposto publicamente. Evitar burocracia e coleta excessiva.

## 7. Catálogo e descoberta
Lojistas gerenciam produtos, fotos, descrições, preços e estoque declarado. Consumidores descobrem lojas e produtos por busca, categorias e filtros. Exibir atualização do catálogo; não prometer estoque em tempo real.

## 8. Experiência do consumidor
Descoberta pública sem login. Login é exigido para ações transacionais ou associadas à identidade, como reservas, fidelidade e avaliações. Experiência mobile-first.

## 9. Painel do comerciante
Dashboard enxuto, sidebar retrátil, área de usuário/configurações, cadastro e manutenção de loja, catálogo, campanhas permitidas e gestão de solicitações. Priorizar baixa fricção e clareza.

## 10. Campanhas e Fidelidade ao Centro
Campanhas podem ser institucionais, coletivas ou de estabelecimento. Programa Fidelidade ao Centro estimula circulação, inclusive por benefício/cupom cruzado: uma compra pode habilitar benefício em outra loja. Regras, elegibilidade, período, limites, resgate, cancelamento e responsável pelo custo precisam ser transparentes. Não presumir subsídio.

## 11. Pontos e confirmação de compra
No MVP, uma reserva/solicitação elegível pode ser marcada como compra concluída pelo responsável da loja. Essa confirmação é o gatilho para pontuação, se a campanha estiver habilitada. Operação idempotente e auditável. Compras espontâneas sem vinculação ficam fora do fluxo inicial.

Taxa de 1 ponto por real e validade de 12 meses são parâmetros de piloto propostos, não decisões fixas. Não converter pontos em dinheiro. Recompensas devem ter financiador definido. Saldo não pode ficar negativo. Se implementado, histórico deve ser ledger e correções devem usar lançamentos compensatórios; FEFO pode ser aplicado a lotes expiráveis conforme spec.

## 12. Avaliações
Avaliações de experiência, atendimento, produtos e campanhas. Publicação pode ser identificada ou anônima publicamente, permanecendo vinculada internamente à conta. Denúncia e moderação são necessárias se incluídas no MVP. Não remover crítica legítima apenas por ser negativa.

## 13. Vaga Legal
Nome correto: Vaga Legal. Inicialmente informação e direcionamento a canais oficiais. Integrações só com API/dados autorizados e viabilidade confirmada. O produto não depende dessa integração.

## 14. Digitalização e incentivo
Propostas de cadastro assistido, fotografia/organização de catálogo, capacitação, divulgação e apoio institucional são propostas, não compromissos firmados. Não afirmar subsídio, redução de aluguel ou parceria confirmada.

## 15. Design e acessibilidade
Mobile-first, interface familiar, simples e profissional. Paleta sóbria inspirada nas cores de uma arara: azul profundo, turquesa discreto, âmbar, grafite e tons claros. WCAG 2.2 AA: contraste, teclado, foco visível, labels, mensagens, reflow, zoom, redução de movimento e alvos adequados.

## 16. Privacidade e segurança
Aplicar LGPD: finalidade, necessidade, transparência, segurança, retenção e direitos do titular. Coletar somente dados necessários. Não expor dados privados de responsáveis ou usuários. Segredos fora do Git.

## 17. Métricas
Operacionais: estabelecimentos cadastrados/ativos, catálogo preenchido e atualizado, buscas, visualizações, ações de contato/reserva, reservas concluídas, participação em campanhas, pontos emitidos e resgatados, distribuição de uso entre lojas, retenção e falhas. Impacto econômico exige linha de base e avaliação; não atribuir causalidade apenas a métricas de uso.

## 18. Limites
Não pressupor integração externa, parceria, dados em tempo real, financiamento, redução de aluguel ou evidência quantitativa local. Distinguir proposta, hipótese, parâmetro configurável e decisão aprovada.
