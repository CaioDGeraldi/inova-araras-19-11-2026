# Requisitos não funcionais | Vem pro Centro

Metas numéricas são objetivos iniciais de engenharia a medir em ambiente documentado; não representam desempenho já comprovado.

| ID | Categoria | Requisito / critério |
|---|---|---|
| RNF-001 | Acessibilidade | Atender WCAG 2.2 AA nos fluxos essenciais. |
| RNF-002 | Acessibilidade | Contraste mínimo 4.5:1 para texto normal e 3:1 para texto grande/componentes aplicáveis. |
| RNF-003 | Acessibilidade | Fluxos essenciais operáveis por teclado, com foco visível e ordem lógica. |
| RNF-004 | Acessibilidade | Campos com labels; erros identificam problema e correção; semântica compatível com leitores de tela. |
| RNF-005 | Acessibilidade | Zoom/reflow sem perda de função; respeitar prefers-reduced-motion. |
| RNF-006 | Responsividade | Fluxos essenciais funcionam em celular, tablet e desktop sem rolagem horizontal indevida. |
| RNF-007 | Usabilidade | Descoberta de lojas, atividades e rotas funciona sem login. |
| RNF-008 | Usabilidade | Formulários solicitam apenas dados necessários e apresentam erros próximos aos campos. |
| RNF-009 | Desempenho | Meta inicial: LCP p75 até 2,5 s em páginas públicas sob perfil de teste documentado. |
| RNF-010 | Desempenho | Meta inicial: INP p75 até 200 ms e CLS p75 até 0,1, quando mensuráveis. |
| RNF-011 | Desempenho | Imagens otimizadas, lazy loading fora da primeira dobra e limites de upload. |
| RNF-012 | Compatibilidade | Suportar versões estáveis recentes de Chrome, Edge, Firefox e Safari e navegadores móveis representativos. |
| RNF-013 | Segurança | Senhas usam hash seguro do Django; nunca texto puro. |
| RNF-014 | Segurança | Toda autorização é verificada no servidor, inclusive acesso a objetos por identificador. |
| RNF-015 | Segurança | Formulários autenticados mantêm CSRF; saída escapada; entrada validada. |
| RNF-016 | Segurança | Uploads validam extensão, MIME, conteúdo e tamanho; arquivos não confiáveis não são executados. |
| RNF-017 | Segurança | Segredos e credenciais ficam fora do repositório e dos logs. |
| RNF-018 | Segurança | Login, check-in, emissão/resgate e formulários expostos têm proteção proporcional contra abuso. |
| RNF-019 | Integridade | Check-ins e resgates usam transações e restrições contra duplicidade. |
| RNF-020 | Integridade | Confirmação de compra e concessão de benefício são idempotentes. |
| RNF-021 | Integridade | Operações críticas registram ator, instante, recurso e resultado sem dados sensíveis desnecessários. |
| RNF-022 | Privacidade | Coletar somente dados necessários para finalidade declarada. |
| RNF-023 | Privacidade | Não realizar rastreamento contínuo de localização. |
| RNF-024 | Privacidade | Dados privados, CNPJ protegido e contato pessoal não aparecem em páginas públicas. |
| RNF-025 | Privacidade | Definir retenção, canal de titular, transparência e processo de exclusão/anonimização aplicável. |
| RNF-026 | Disponibilidade | Falhas externas não corrompem transações locais; integrações falham de forma controlada. |
| RNF-027 | Manutenibilidade | Domínios modularizados, dependências explícitas e sem abstrações sem uso. |
| RNF-028 | Testabilidade | Regras, autorização, transações, concorrência e jornadas essenciais possuem testes automatizados. |
| RNF-029 | Observabilidade | Erros e operações críticas são registráveis sem dados secretos. |
| RNF-030 | SEO | Páginas públicas possuem URLs estáveis, títulos e metadados apropriados. |
| RNF-031 | Fuso horário | Exibir datas no fuso America/Sao_Paulo e armazenar instantes de forma consistente. |
| RNF-032 | Reprodutibilidade | Instalação reproduzível com versões/dependências fixadas e uv.lock. |
| RNF-033 | Backup | Antes de dados reais, definir backup e testar restauração conforme infraestrutura. |
| RNF-034 | Conteúdo | Cancelamentos, validade, disponibilidade declarada e atualização do catálogo são claros. |
| RNF-035 | Privacidade analítica | Eventos usados para inteligência comercial são minimizados e não formam histórico individual de consumo. |
| RNF-036 | Privacidade analítica | Painéis e exportações aplicam agregação, limiar mínimo de grupo e supressão de células pequenas. |
| RNF-037 | Governança | Acesso institucional exige finalidade, perfil autorizado, registro de auditoria e revisão periódica. |
| RNF-038 | Transparência estatística | Indicadores e pesquisas exibem período, cobertura, tamanho de amostra, método e limitações relevantes. |

A inteligência comercial deve ser testada contra tentativas de reidentificação por filtros sucessivos, grupos pequenos, exportações e comparação de períodos. Dados brutos devem ter retenção definida e acesso mais restrito que indicadores agregados.

## Verificação mínima

- Auditoria automatizada de acessibilidade complementada por inspeção manual.
- Testes de teclado, foco, zoom, reflow e leitor de tela.
- Medição de Core Web Vitals em perfil documentado.
- Testes de autorização horizontal/vertical e acesso a objetos de terceiros.
- Testes concorrentes para check-in, resgate e confirmação de compra.
- Verificação de uploads e segredos.
- Teste de restauração de backup antes de produção com dados reais.

WCAG 2.2 AA não é garantida apenas por Bootstrap ou ferramenta automática. LCP/INP/CLS são metas a medir, não promessas sem medição. SLA/RTO/RPO serão definidos quando houver ambiente de produção e operação contínua.