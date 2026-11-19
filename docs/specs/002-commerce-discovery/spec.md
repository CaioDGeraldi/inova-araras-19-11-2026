# Spec 002 | Comércio e descoberta pública

## Contexto
A vitrine digital é a base de descoberta do Vem pro Centro. Sem estabelecimentos e catálogo confiáveis, cronograma e rotas não conseguem direcionar visitantes para o comércio participante.

## Objetivo
Permitir que um responsável mantenha estabelecimento, catálogo e canais de contato e que qualquer visitante descubra lojas e produtos sem autenticação.

## Requisitos relacionados
RF-001, RF-004, RF-005, RF-010 a RF-028; RNF-001 a RNF-008, RNF-013 a RNF-017, RNF-022 a RNF-025, RNF-030.

## Atores e permissões
- Visitante: consultar lojas, categorias e produtos publicados.
- Usuário autenticado: cadastrar estabelecimento e solicitar/assumir responsabilidade conforme fluxo aprovado.
- Owner: editar apenas estabelecimentos sob sua responsabilidade.
- Admin: aprovar, rejeitar, suspender e moderar cadastros.

## Incluído
- Store, Category e Product/Service.
- Relação de responsável principal.
- Estados de aprovação.
- Página pública de estabelecimento e produto.
- Busca por nome e filtro por categoria.
- Preço, descrição, imagem opcional e disponibilidade declarada.
- Cadastro e exibição de WhatsApp público e Instagram opcional.
- Atalho externo de pedido de reserva com mensagem contextualizada.
- Data de atualização do catálogo.

## Excluído
- Checkout, pagamento, entrega e estoque transacional.
- Entidade de reserva, caixa de entrada, histórico ou status de pedidos na plataforma.
- Integração com API do WhatsApp Business, webhooks ou sincronização com Instagram Direct.
- Gestão de equipe/memberships.
- Integração automática de CNPJ ou estoque.
- Avaliações públicas nesta spec.

## Fluxo principal
1. Usuário autenticado envia cadastro de estabelecimento.
2. Sistema valida campos obrigatórios e cria estado pendente.
3. Admin aprova ou rejeita; a decisão fica auditável.
4. Owner aprovado cadastra/edita produtos e serviços.
5. Visitante acessa vitrine, busca e abre página pública.
6. Página exibe somente dados públicos e data de atualização.

## Regras
- Uma pessoa pode ser owner de mais de uma Store.
- Apenas owner autorizado ou admin altera dados privados.
- Store pendente, rejeitada ou suspensa não aparece como participante oficial.
- Store pode possuir várias categorias.
- Preço pode ser ausente quando não fizer sentido para o serviço.
- Disponibilidade é declarada, nunca apresentada como estoque em tempo real.
- Contato público é distinto de contato privado do responsável.
- WhatsApp é o canal prioritário para pedido de reserva por link de clique para conversa com mensagem pré-preenchida; o consumidor precisa enviar manualmente.
- Instagram é opcional: o link abre o perfil/Direct e a interface oferece texto para copiar, sem presumir preenchimento automático.
- A confirmação e as condições de retirada são acordadas na conversa externa; a plataforma não conhece o estado da reserva.
- CNPJ, se coletado, não é público e precisa de finalidade.

## Dados e estados
Store: draft/pending_review, approved, rejected, suspended.  
Product: draft, published, archived.  
Category: active/inactive.

## Segurança e privacidade
- Testar acesso cruzado: owner A não edita Store de owner B.
- Não serializar telefone/e-mail privados, CNPJ ou dados internos em página pública.
- Validar upload por tipo, conteúdo e tamanho.
- Proteger formulários contra CSRF e abuso.
- Não permitir enumeração de recursos privados.

## Critérios de aceitação
- [ ] Visitante acessa vitrine sem login.
- [ ] Busca por nome encontra apenas estabelecimentos/produtos publicados.
- [ ] Filtro por categoria funciona.
- [ ] Owner cadastra e atualiza sua loja e catálogo.
- [ ] Owner não altera loja de terceiro.
- [ ] Admin aprova/rejeita/suspende e a visibilidade acompanha o estado.
- [ ] Catálogo exibe data da última atualização.
- [ ] Responsável mantém número público de WhatsApp separado de seus dados privados.
- [ ] Consumidor abre WhatsApp com mensagem contextualizada e precisa enviá-la manualmente.
- [ ] Perfil público do Instagram pode ser cadastrado e aberto pelo link do perfil/Direct com texto copiável.
- [ ] A interface não apresenta estado de reserva nem presume confirmação de conversa externa.
- [ ] Dados privados não aparecem na resposta pública.
- [ ] Testes cobrem permissões, estados e busca.

## Decisões em aberto
- Campos obrigatórios finais de cadastro e validação de endereço.
- Se cadastro entra automaticamente como pendente ou precisa convite.
- Limites de quantidade/tamanho de imagens.
