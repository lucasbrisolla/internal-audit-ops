---
lista: testes-tipicos-por-controle
tipo: master-list
descricao: Procedimentos de teste padrão por tipo de controle para uso principal em auditoria interna, com pré-condições, dependências de IPE/ITGC e evidência aceitável
escopo_auditoria: interna-mista
fonte_base: testes-tipicos-por-controle-external-audit.md
tipos_de_controle:
  - aprovacao-autorizacao
  - reconciliacao
  - revisao-independente
  - contagem-fisica
  - acesso-logico
  - relatorio-de-excecao
  - validacao-automatizada
  - corte
  - analise-analitica
  - confirmacao-externa
uso:
  - test-execution
  - risk-control-mapping
  - audit-planning
nota: tamanho_de_amostra segue orientação de risco — Alta = 25+, Média = 15–25, Baixa = 5–15; ajustar conforme população e CRA
---

# Testes Típicos por Tipo de Controle

Versão de trabalho para **auditoria interna/mista**. A referência-base de origem externa está em `testes-tipicos-por-controle-external-audit.md`.

Catálogo de procedimentos de teste organizados por **tipo de controle**, não por processo. O agente usa esta lista para derivar o teste adequado assim que o controle é identificado no mapeamento.

**Estrutura de cada entrada:**
- **Pré-condição:** quando o teste é válido — o que precisa estar em vigor para o controle existir
- **Procedimento:** o que executar
- **Dependência IPE/ITGC:** qual relatório ou condição sistêmica precisa ser validado antes
- **Evidência aceitável:** o que constitui prova suficiente (forte vs. fraca)
- **Armadilha:** erro comum ao testar esse tipo de controle

---

## 1. Aprovação / Autorização

Controle onde uma pessoa com alçada autoriza formalmente uma transação antes de ela ser executada.

### TT-APR-001 — Aprovação manual documentada

**Pré-condição:** existe política de alçadas com critérios definidos (valor, tipo de transação) e aprovação deixa rastro físico ou eletrônico identificável.

**Procedimento:**
1. Obter tabela de alçadas vigente no período
2. Selecionar amostra de transações aprovadas
3. Para cada item: verificar existência de aprovação, identidade do aprovador, data e se o valor está dentro da alçada do aprovador
4. Verificar se há transações que deveriam ter sido aprovadas por alçada superior mas não foram

**Dependência IPE/ITGC:** relatório de transações aprovadas extraído do sistema (não filtrado pelo auditado). Verificar se o sistema impede aprovação pelo próprio solicitante (controle sistêmico de SoD).

**Evidência aceitável:**
- Forte: aprovação eletrônica no sistema com log de usuário + data + valor
- Média: e-mail de aprovação antes da transação (data anterior ao registro)
- Fraca: aprovação verbal reconstruída a posteriori; assinatura sem data; aprovação após o fato

**Armadilha:** testar se a aprovação existe, mas não testar se o aprovador tinha alçada para aquele valor. Aprovar é necessário mas não suficiente — quem aprovou precisa ter autoridade para tanto.

---

### TT-APR-002 — Aprovação sistêmica (workflow automatizado)

**Pré-condição:** sistema tem workflow configurado que impede avanço da transação sem aprovação eletrônica; ITGC de acesso ao módulo de configuração de workflow está testado.

**Procedimento:**
1. Obter evidência da configuração do workflow no sistema (print de configuração ou relatório de TI)
2. Confirmar que o workflow não pode ser bypassado por usuário padrão (verificar perfis com acesso de bypass)
3. Selecionar amostra de transações e confirmar que todas passaram pelo workflow
4. Verificar se existem transações fora do sistema (offline, planilha) que não passaram pelo workflow

**Dependência IPE/ITGC:** ITGC de acesso ao módulo de configuração de workflow (mudança de configuração = mudança de controle). Se ITGC não testado, tratar como controle manual.

**Evidência aceitável:**
- Forte: print de configuração do workflow + log de transações com status de aprovação
- Fraca: descrição verbal de como o sistema funciona sem evidência da configuração

**Armadilha:** assumir que workflow existe = workflow funciona. Verificar se existem perfis com "bypass" ou se transações urgentes têm caminho alternativo sem aprovação.

---

## 2. Reconciliação

Controle onde dois conjuntos de dados independentes são comparados e diferenças são investigadas e resolvidas.

### TT-REC-001 — Reconciliação entre sistema e suporte externo

**Pré-condição:** dois conjuntos de dados independentes existem para o mesmo saldo (ex: razão contábil vs. extrato bancário; aging vs. razão de clientes). Reconciliação é realizada por pessoa diferente de quem preparou os dados.

**Procedimento:**
1. Obter a reconciliação preparada pela gestão para o período amostrado
2. Confirmar que a base usada foi extraída do sistema (não de relatório gerencial)
3. Verificar se há evidência de revisão e aprovação por pessoa diferente do preparador
4. Amarrar o saldo final da reconciliação ao razão contábil (tie-out)
5. Avaliar itens reconciliantes: idade, natureza, se foram resolvidos em período subsequente
6. Verificar se todos os itens de break acima de threshold têm explicação e prazo de resolução

**Dependência IPE/ITGC:** extrato do razão deve ser extraído diretamente do sistema pelo auditor ou validado como íntegro (completude, sem filtro). Relatório preparado pelo auditado = IPE que precisa de validação.

**Evidência aceitável:**
- Forte: reconciliação assinada pelo preparador e aprovador com datas + extrato do sistema anexo + itens reconciliantes com status
- Fraca: reconciliação sem aprovação documentada; saldo não amarrado ao razão; itens antigos sem explicação

**Armadilha:** reconciliação que "fecha" sem itens reconciliantes pode indicar que foi preparada retroativamente para coincidir com o saldo. Verificar data de preparação vs. data do fechamento.

---

### TT-REC-002 — Reconciliação intercompany

**Pré-condição:** existem transações entre entidades do mesmo grupo registradas por ambas as partes.

**Procedimento:**
1. Obter saldo intercompany declarado por cada parte
2. Confirmar que ambos os saldos foram extraídos dos respectivos sistemas
3. Identificar e quantificar diferenças
4. Para diferenças: verificar se foram investigadas e qual é a explicação (timing, câmbio, erro)
5. Confirmar que a eliminação na consolidação foi feita corretamente e sobre os saldos reconciliados

**Dependência IPE/ITGC:** relatório de transações intercompany por contraparte extraído de cada entidade.

**Evidência aceitável:**
- Forte: confirmação por escrito de ambas as partes antes do fechamento + diferenças resolvidas ou explicadas
- Fraca: apenas o saldo de uma parte sem confirmação da contraparte

---

## 3. Revisão Independente

Controle onde pessoa com conhecimento e autoridade revisa output de outro — sem ser o mesmo que preparou.

### TT-REV-001 — Revisão de demonstrações ou relatórios pelo CFO/Controller

**Pré-condição:** existe processo formal de revisão com entregável claro e responsável identificado.

**Procedimento:**
1. Identificar quem realizou a revisão e qual foi o objeto
2. Verificar evidência da revisão: anotações, e-mail de aprovação, formulário assinado, ata
3. Confirmar que a data da revisão é anterior à publicação ou uso do relatório
4. Verificar se variações significativas foram questionadas e respondidas com documentação
5. Testar se as conclusões da revisão estão documentadas (não apenas "revisado")

**Dependência IPE/ITGC:** nenhuma — controle puramente manual. Risco: evidência fabricada retroativamente.

**Evidência aceitável:**
- Forte: comentários ou anotações do revisor no documento com data + resposta do preparador documentada
- Média: e-mail de aprovação com referência ao conteúdo específico
- Fraca: assinatura sem data; "revisado e aprovado" sem qualquer comentário ou questionamento

**Armadilha:** revisão que nunca encontra problema é sinal de alerta — revisor pode estar assinando sem examinar. Perguntar sobre o último item que foi rejeitado ou questionado.

---

### TT-REV-002 — Revisão analítica de fechamento

**Pré-condição:** existe processo formal de comparação de resultados com período anterior ou orçamento, com explicação de variações relevantes.

**Procedimento:**
1. Obter análise analítica realizada no fechamento
2. Verificar se cobre DRE, BP e DFC comparativos
3. Para cada variação acima do threshold definido: verificar se há explicação documentada e quem a forneceu
4. Avaliar se as explicações são suportadas por evidência (não apenas narrativa da gestão)
5. Identificar variações que deveriam ter sido questionadas mas não foram

**Dependência IPE/ITGC:** relatório comparativo gerado pelo sistema (não montado manualmente em planilha pela gestão).

**Evidência aceitável:**
- Forte: análise analítica formal com threshold definido + explicações com referência cruzada a suporte
- Fraca: análise narrativa sem cálculo de variação ou sem questionamento de itens materiais

---

## 4. Contagem Física / Inventário

Controle onde a existência física de ativos é verificada contra o registro sistêmico.

### TT-FIS-001 — Observação de contagem física de estoque ou imobilizado

**Pré-condição:** empresa realiza contagem física periódica com procedimento documentado e pessoal independente da custódia.

**Procedimento:**
1. Obter procedimento de contagem e lista de locais/itens incluídos
2. Verificar se a contagem foi realizada por equipe independente da custódia
3. Selecionar amostra de itens para teste bidirecional:
   - Registro → físico (existência): confirmar que item no sistema existe no local indicado
   - Físico → registro (completude): confirmar que item físico observado está no sistema
4. Verificar como diferenças entre contagem e sistema foram tratadas (aprovação de ajuste)
5. Amarrar resultado da contagem ao registro contábil

**Dependência IPE/ITGC:** lista de inventário para contagem deve ser extraída do sistema antes da contagem — não preparada após. Verificar data do relatório.

**Evidência aceitável:**
- Forte: atas de contagem assinadas por contador e supervisor independente + conciliação com razão + ajustes aprovados
- Fraca: contagem realizada pela própria custódia sem supervisor; lista preparada após a contagem

**Armadilha:** contar apenas "registro → físico" testa existência mas não completude. O teste bidirecional é obrigatório para cobertura adequada.

---

## 5. Acesso Lógico

Controle que restringe quem pode realizar quais ações nos sistemas de informação.

### TT-ACE-001 — Revisão de lista de usuários ativos e perfis

**Pré-condição:** existe lista de usuários com perfis atribuídos e processo formal de provisão/revogação.

**Procedimento:**
1. Obter lista de usuários ativos com perfis extraída diretamente do sistema (não relatório preparado pela gestão)
2. Cruzar com lista de colaboradores ativos de RH — identificar usuários sem vínculo ativo
3. Para amostra de usuários: verificar se o perfil é compatível com a função exercida (menor privilégio)
4. Identificar perfis privilegiados (admin, super user) e verificar se estão justificados e monitorados
5. Verificar se há usuários compartilhados (contas genéricas) — rastreabilidade comprometida

**Dependência IPE/ITGC:** extração direta do sistema de identidade (AD, ERP) pelo auditor ou com validação de completude. Lista fornecida pela gestão = IPE que precisa de validação.

**Evidência aceitável:**
- Forte: extração direta do sistema com query documentada + cruzamento com RH com diferenças investigadas
- Fraca: lista fornecida pelo auditado sem validação de extração; ausência de cruzamento com RH

**Armadilha:** revisar só usuários ativos. Contas bloqueadas mas não desativadas podem ser reativadas sem processo. Incluir contas inativas na análise.

---

### TT-ACE-002 — Teste de SoD em perfis de sistema

**Pré-condição:** matriz SoD foi definida e há método para verificar se perfis criam conflito.

**Procedimento:**
1. Obter matriz SoD relevante para o sistema (ver `master-lists/sod-matrix.md`)
2. Para cada par de funções incompatíveis: verificar se algum usuário tem ambos os perfis simultaneamente
3. Para conflitos identificados: verificar se existe controle compensatório ativo e testável
4. Confirmar que controles compensatórios são revisados periodicamente (não apenas existem)

**Dependência IPE/ITGC:** extração de perfis do sistema com mapeamento de transações por perfil.

**Evidência aceitável:**
- Forte: análise de SoD com base em extração sistêmica + lista de conflitos + evidência de controles compensatórios testados
- Fraca: declaração da gestão de que "não há conflitos" sem análise formal

---

## 6. Relatório de Exceção

Controle detectivo onde o sistema gera uma lista de transações que violam uma regra pré-definida, e um responsável revisa e resolve cada item.

### TT-EXC-001 — Teste de relatório de exceção

**Pré-condição:** relatório de exceção existe, é gerado automaticamente pelo sistema com base em regra configurada, e há processo formal de revisão e resolução de cada item.

**Procedimento:**
1. Validar que o relatório é gerado pelo sistema (não manualmente) — obter evidência da configuração da regra
2. Verificar se a regra de exceção cobre o risco que o controle pretende mitigar
3. Para período amostrado: obter relatório de exceção e verificar evidência de revisão por responsável
4. Selecionar amostra de exceções: confirmar que cada item foi investigado, resolvido ou aceito com justificativa
5. Verificar se há itens antigos não resolvidos que indicam que a revisão é formal mas não substantiva
6. Testar completude: introduzir transação de teste que deveria aparecer no relatório e confirmar que apareceu

**Dependência IPE/ITGC:** integridade do relatório — completude (todos os itens aparecem) e acurácia (regra funciona como configurada). ITGC de change management garante que a regra não foi alterada.

**Evidência aceitável:**
- Forte: relatório com evidência de revisão item a item + resolução documentada + teste de completude positivo
- Fraca: relatório gerado mas sem evidência de que alguém revisou; itens resolvidos em massa sem análise individual

**Armadilha:** relatório de exceção sem teste de completude não cobre o risco de que a regra está configurada de forma muito estreita e deixa exceções reais de fora.

---

## 7. Validação Automatizada (Edit Checks)

Controle sistêmico que impede ou sinaliza transação que viola uma regra de negócio no momento da entrada de dados.

### TT-AUT-001 — Teste de validação sistêmica

**Pré-condição:** sistema tem regra de validação configurada (ex: bloqueia pagamento sem OC; impede NF sem entrega registrada). ITGC de acesso à configuração do sistema está testado.

**Procedimento:**
1. Obter evidência da configuração da regra no sistema (print de configuração ou documentação de TI)
2. Verificar se existem formas de bypass (perfil de override, campo de exceção manual)
3. Verificar quem tem acesso ao bypass e se uso é monitorado
4. Testar a regra: tentar executar transação que a viola e confirmar que o sistema bloqueia
5. Selecionar amostra de transações que passaram pela validação e confirmar que os pré-requisitos foram atendidos

**Dependência IPE/ITGC:** ITGC de change management (regra pode ter sido alterada) e ITGC de acesso ao módulo de configuração. Sem ITGC testado, confiança no controle automatizado é limitada.

**Evidência aceitável:**
- Forte: configuração documentada + teste de funcionamento da regra + confirmação de que bypass é monitorado
- Fraca: declaração de que "o sistema não deixa passar" sem evidência da configuração ou teste

**Armadilha:** controle automatizado sem ITGC testado tem o mesmo risco que um controle manual — a configuração pode ter sido alterada. Não tratar como "controle forte" sem base nos ITGCs.

---

## 8. Corte (Cutoff)

Controle que garante que transações são registradas no período correto — nem antes nem depois.

### TT-COR-001 — Teste de corte em receita / despesa

**Pré-condição:** empresa tem política de corte documentada com critério de quando registrar (ex: na entrega, na assinatura, na transferência de risco).

**Procedimento:**
1. Identificar a política de corte aplicável (ex: FOB origem vs. destino, percentual de conclusão)
2. Selecionar transações próximas ao fechamento (últimos e primeiros dias do período — mínimo 5 dias antes e depois)
3. Para cada transação: verificar documentação de suporte (romaneio, confirmação de entrega, laudo de conclusão)
4. Confirmar que a data de registro coincide com o evento econômico, não com a data do documento
5. Verificar se há transações registradas no período mas com evidência de entrega/conclusão em período diferente

**Dependência IPE/ITGC:** relatório de transações próximas ao fechamento com datas de documento e de registro — extraído do sistema.

**Evidência aceitável:**
- Forte: documento de suporte com data do evento + data de registro coincidente com política + sem exceções não explicadas
- Fraca: registro baseado na data da nota fiscal, não na data da entrega; ausência de documentação de suporte

**Armadilha:** testar apenas os últimos dias antes do fechamento. Antecipação de receita pode ocorrer em qualquer ponto do período, e postergação de despesa também. Janela de corte deve ser bidirecional.

---

## 9. Análise Analítica

Procedimento substantivo que identifica variações ou relações incomuns nos dados financeiros ou operacionais.

### TT-ANA-001 — Análise de variação horizontal/vertical

**Pré-condição:** dados comparativos de ao menos dois períodos estão disponíveis e são confiáveis.

**Procedimento:**
1. Calcular variação absoluta e percentual entre períodos para contas relevantes
2. Definir threshold de investigação (ex: variação > 10% e > R$ X)
3. Para cada item acima do threshold: obter explicação da gestão com suporte documental
4. Avaliar se a explicação é plausível dado o contexto do negócio e consistente com outros dados
5. Identificar relações esperadas que não se mantêm (ex: receita cresce mas CMV não — margem bruta melhora sem explicação operacional)

**Dependência IPE/ITGC:** dados extraídos do razão contábil, não de relatório gerencial. Verificar se os períodos comparativos foram restated ou reapresentados.

**Evidência aceitável:**
- Forte: análise documentada com threshold definido + explicações suportadas por dados operacionais (volume, preço, headcount)
- Fraca: explicação apenas narrativa sem dados operacionais de suporte; variações ignoradas abaixo de threshold muito alto

**Armadilha:** análise analítica como procedimento final confirma o que você já sabe. O valor está em usá-la para identificar o que testar — não para concluir sem testes adicionais em áreas de risco.

---

### TT-ANA-002 — Análise de indicadores operacionais vs. financeiros

**Pré-condição:** dados operacionais (volume, unidades, headcount, m², contratos) estão disponíveis e são independentes dos dados financeiros.

**Procedimento:**
1. Selecionar dois ou três indicadores operacionais que deveriam estar correlacionados com a conta financeira em análise
2. Construir expectativa: dado o volume operacional, qual seria o valor financeiro esperado?
3. Comparar expectativa com valor real registrado
4. Investigar diferença acima do threshold com suporte documental

**Dependência IPE/ITGC:** dados operacionais de fonte independente (sistema operacional, dados de produção, RH). Não usar dados gerenciais preparados pela mesma área que registra a conta financeira.

**Evidência aceitável:**
- Forte: expectativa construída com premissas documentadas + diferença explicada com suporte
- Fraca: expectativa baseada em dados fornecidos pelo auditado; diferença explicada sem suporte quantitativo

---

## 10. Confirmação Externa

Procedimento que obtém evidência diretamente de terceiro independente, sem intermediação do auditado.

### TT-CON-001 — Confirmação de saldo com cliente ou fornecedor

**Pré-condição:** terceiro tem informação que pode confirmar ou contradizer o saldo registrado pela empresa.

**Procedimento:**
1. Selecionar amostra de saldos a confirmar — priorizar os maiores, os mais antigos e os de partes relacionadas
2. Preparar carta de confirmação com o saldo da empresa (confirmação positiva) ou sem saldo (confirmação em branco)
3. Enviar diretamente ao terceiro sem intermediação do auditado — endereço independente
4. Receber resposta diretamente e comparar com saldo registrado
5. Para diferenças: investigar causa (timing, disputa, erro)
6. Para não respostas: aplicar procedimentos alternativos (pagamentos subsequentes, documentação de suporte)

**Dependência IPE/ITGC:** lista de saldos e endereços extraída do sistema (não fornecida pelo auditado). Confirmação enviada e recebida sem intermediação.

**Evidência aceitável:**
- Forte: confirmação positiva por escrito recebida diretamente do terceiro com saldo concordante
- Média: procedimento alternativo bem documentado (ex: pagamento recebido após data-base que confirma o saldo)
- Fraca: confirmação recebida com intermediação do auditado; não resposta sem procedimento alternativo

**Armadilha:** confirmação em branco (sem saldo) tem maior poder probatório porque o terceiro precisa preencher o valor — não apenas confirmar o que a empresa declarou. Usar quando o risco é superavaliação.

---

## Leitura Rápida — Hierarquia de Evidência

| Tipo de Controle | Natureza | Dependência ITGC | Força Probatória Máxima |
|---|---|---|---|
| Validação automatizada | Preventivo / Automatizado | Alta — sem ITGC, tratar como manual | Alta (se ITGC testado) |
| Confirmação externa | Substantivo | Nenhuma | Alta |
| Relatório de exceção | Detectivo / Híbrido | Média — integridade do relatório | Alta (se completude testada) |
| Aprovação sistêmica | Preventivo / Automatizado | Alta | Alta (se ITGC testado) |
| Reconciliação com revisão | Detectivo / Manual | Média — fonte dos dados | Média-Alta |
| Aprovação manual | Preventivo / Manual | Baixa | Média |
| Revisão independente | Detectivo / Manual | Nenhuma | Média |
| Análise analítica | Substantivo | Média — fonte dos dados | Média (direcional) |
| Contagem física | Detectivo / Manual | Nenhuma | Alta (bidirecional) |
| Corte | Substantivo | Média | Alta (com suporte documental) |
