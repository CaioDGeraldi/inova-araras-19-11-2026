# Spec 003 | Cronograma do Centro

## Contexto
A programação é um motivo explícito para escolher quando visitar o Centro. O cronograma deve reunir eventos culturais, feiras, oficinas, apresentações, ações comerciais e experiências comunitárias em um local público e consultável.

## Objetivo
Permitir que a administração publique atividades e que visitantes consultem programação por data, horário, local e categoria sem criar conta.

## Requisitos relacionados
RF-030 a RF-041; RNF-001 a RNF-012, RNF-022 a RNF-025, RNF-030, RNF-031, RNF-034.

## Atores e permissões
- Visitante: consultar atividades publicadas.
- Admin: criar, editar, publicar e cancelar atividades.
- Organizador/estabelecimento: pode sugerir atividades em evolução posterior, sujeitas à aprovação.

## Incluído
- Cadastro administrativo de atividade.
- Título, descrição, categoria, organizador, data, início, término opcional, local e condição gratuita/paga.
- Indicação de inscrição obrigatória/opcional.
- Listagem pública por data e detalhe da atividade.
- Estados draft, published, cancelled, completed/archived.
- Associação opcional com estabelecimento e circuito.

## Excluído
- Venda de ingressos e pagamento.
- Inscrição completa e controle de vagas no primeiro corte.
- Notificações push.
- Integração com agenda externa sem autorização.

## Fluxo principal
1. Admin cria atividade em rascunho.
2. Informa dados obrigatórios e local.
3. Publica a atividade.
4. Visitante consulta cronograma e abre detalhes.
5. Se houver alteração, a página apresenta informação atualizada.
6. Se cancelada, atividade permanece identificada como cancelada.

## Regras
- Atividade publicada precisa ter título, descrição resumida, início e local.
- Horário é interpretado no fuso America/Sao_Paulo.
- Término, quando informado, deve ser posterior ao início.
- Cancelamento não apaga registros de participação nem desaparece silenciosamente.
- Atividade passada pode ser arquivada, preservando histórico.
- Gratuidade/preço e necessidade de inscrição devem ser explícitos.
- Não publicar atividade sem confirmação operacional do organizador/local.

## Dados e estados
Event: draft → published → cancelled ou completed/archived.  
Place: nome, endereço e instruções públicas suficientes para encontrar o local.  
Organizer: referência a usuário/organização responsável, com contato público opcional.

## Segurança, privacidade e acessibilidade
- Apenas admin publica no primeiro MVP.
- Não expor contato privado do organizador.
- Datas devem ser legíveis e consistentes em mobile.
- Cancelamento deve ser comunicado visualmente e por texto, não apenas por cor.
- Navegação por teclado e leitores de tela.

## Critérios de aceitação
- [ ] Admin cria, edita, publica e cancela atividade.
- [ ] Visitante consulta atividades sem login.
- [ ] Filtro/listagem por data apresenta atividades na ordem correta.
- [ ] Detalhe exibe data, horário, local, organizador, gratuidade/preço e inscrição.
- [ ] Atividade cancelada continua visível com estado claro.
- [ ] Data/hora respeita America/Sao_Paulo.
- [ ] Término inválido é recusado.
- [ ] Testes cobrem permissão, publicação, cancelamento e ordenação.

## Decisões em aberto
- Se atividades recorrentes serão representadas por ocorrências separadas.
- Quais categorias iniciais serão oferecidas.
- Se endereço será Place separado ou campo reutilizável no Event.
