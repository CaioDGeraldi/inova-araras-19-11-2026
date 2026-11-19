# Cenário de demonstração | Vem pro Centro

## Objetivo

Demonstrar, em uma narrativa curta e reproduzível, como o Vem pro Centro conecta a descoberta do consumidor à presença digital mantida pelo proprietário do estabelecimento.

Este cenário é exclusivamente demonstrativo. Todos os nomes, pessoas, estabelecimentos, produtos, preços, atividades e benefícios devem ser fictícios. Não copiar identidade, endereço, contato ou catálogo de empresas reais.

## Perspectiva do consumidor

1. Abrir a experiência pública sem precisar criar uma conta.
2. Encontrar estabelecimentos e produtos por descoberta ou busca.
3. Abrir a página de um estabelecimento e consultar descrição, preço, disponibilidade declarada e data de atualização.
4. Consultar uma atividade do Cronograma do Centro.
5. Abrir uma Rota de Descoberta, entender suas paradas obrigatórias e opcionais e iniciar participação quando autenticado.
6. Consultar uma campanha demonstrativa, se estiver habilitada e tiver regras e responsável pelo custo claramente definidos.

## Perspectiva do proprietário

1. Entrar com uma conta demonstrativa de proprietário.
2. Acessar o painel do estabelecimento sob sua responsabilidade.
3. Atualizar informações de apresentação da loja.
4. Criar ou editar produto, preço, imagem e disponibilidade declarada.
5. Conferir como a atualização aparece na vitrine pública.
6. Conferir e manter o WhatsApp público da loja e, opcionalmente, o perfil público do Instagram.
7. Testar a geração do link de WhatsApp com dados demonstrativos e mensagem contextualizada, sem enviar mensagens para números reais.
8. Conferir a alternativa do Instagram com texto para copiar.

## Conjunto mínimo de dados

- 1 conta de consumidor fictícia.
- 2 contas de proprietários fictícias, com canais de contato demonstrativos não operacionais ou claramente identificados como teste.
- 2 estabelecimentos fictícios, de categorias distintas.
- Categorias reutilizáveis e produtos variados, com preço e disponibilidade declarada.
- 2 ou 3 atividades fictícias no Cronograma do Centro.
- 1 Rota de Descoberta com paradas vinculadas a estabelecimentos, atividades ou locais fictícios, incluindo paradas obrigatórias e opcionais.
- 1 campanha demonstrativa opcional, somente se emissor, receptor, elegibilidade, período, benefício, limites e responsável pelo custo estiverem definidos.

## Requisitos do comando

Comando esperado: `python manage.py seed_demo`.

- Determinístico: os mesmos dados são criados em toda execução.
- Idempotente: reexecutar não duplica registros e reconcilia os dados pertencentes ao seed.
- Isolado: todos os registros criados possuem marcador inequívoco de demonstração ou pertencem a um conjunto de IDs estáveis reservado ao seed.
- Seguro: recusa execução em produção; não altera nem apaga registros sem marcador demonstrativo.
- Explícito: não roda automaticamente em migrations, startup, deploy ou comandos genéricos.
- Configurável: credenciais são fornecidas por variáveis de ambiente/configuração local; nenhuma senha real ou reutilizável fica versionada.
- Transacional: falha parcial não deve deixar o cenário em estado inconsistente.
- Auditável: a saída informa quantos registros foram criados/atualizados, sem imprimir senhas ou tokens secretos.

## Critérios de aceitação

- [ ] Uma execução cria todo o cenário mínimo.
- [ ] Reexecuções não criam duplicatas.
- [ ] Os dados são identificados visualmente como fictícios na demonstração e não são confundidos com participantes reais.
- [ ] As duas contas de proprietário acessam somente seus respectivos estabelecimentos.
- [ ] A conta de consumidor consegue percorrer a jornada pública prevista.
- [ ] O botão de WhatsApp gera mensagem contextualizada com número demonstrativo e não envia automaticamente.
- [ ] O perfil de Instagram demonstrativo permite visualizar o texto sugerido para cópia.
- [ ] Rotas exibem paradas obrigatórias e opcionais de forma inequívoca.
- [ ] O comando recusa ambiente de produção.
- [ ] Nenhum registro real é alterado ou apagado pelo seed.
- [ ] Credenciais não são armazenadas no Git nem exibidas nos logs.
- [ ] A narrativa pode ser repetida após reset do ambiente demonstrativo.

## Fora do escopo

- Dados ou contas de estabelecimentos reais.
- Importação de catálogo de empresas existentes.
- Integrações externas, pagamentos ou estoque em tempo real.
- Garantia de que toda funcionalidade planejada estará implementada no dia do pitch.
- Execução automática do seed em ambientes de produção.
