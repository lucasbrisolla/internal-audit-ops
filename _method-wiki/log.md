# Method Wiki - Log

## [2026-04-28] coso-erm-distillation | Cap. 7 — Strategy & Objective-Setting (P7/P9)

MDs editados:
- `concepts/scoping-strategy.md` — seção 12 adicionada
- `modes/risk-assessment.md` — seção 4f adicionada

Conteúdo adicionado em `scoping-strategy.md` (seção 12):
- Apetite de risco: 5 formas de expressão (qualitativa, alvo, faixa, teto, piso); como o auditor usa como calibrador de escopo; apetite sem mecanismo de monitoramento = gap de ERM
- Tolerância: distinção de apetite (estratégico vs. operacional/mensurável); tabela comparativa; quando performance fora da tolerância é desvio documentável mesmo sem falha de controle
- Armadilhas: apetite como documento de gaveta, confusão apetite vs. limites de controle, apetite acima da capacidade real

Conteúdo adicionado em `risk-assessment.md` (seção 4f):
- Tabela de ação por situação de apetite: acima do apetite → P1 automático; ausente → usar padrão e documentar
- Cascata apetite → tolerância: desvio de tolerância como critério de inclusão no plano independente de falha de controle

Descartado de Cap. 7:
- P6 (Business Context) — já coberto em `modes/business-understanding.md`
- P8 (Alternative Strategies) — implementação de ERM pela gestão, não avaliação pelo auditor
- Exemplos numéricos de cascata de objetivos — ilustrativos, sem valor reutilizável
- Risk capacity (detalhe de gestão de portfólio além do escopo de interna)

---

## [2026-04-28] coso-erm-distillation | Cap. 8 — Performance (P10-P14)

MDs editados:
- `concepts/risk-scoring-foundations.md`
- `modes/risk-assessment.md`

Conteúdo adicionado em `risk-scoring-foundations.md`:
- Inherent / Target residual / Actual residual: distinção dos 3 estados de risco (COSO ERM P11); implicações quando actual residual > target; respostas redundantes
- Quinta dimensão Recovery (P12): distinto de persistence — mede capacidade de resposta da organização, não duração do impacto
- Seção de bias na avaliação: confidence bias, framing bias, overconfidence — com exemplos e mitigações

Conteúdo adicionado em `modes/risk-assessment.md`:
- Seção 4c: quando cliente tem ERM ativo — consumir inventário existente, avaliar completude, gaps de cobertura vs. mapa de riscos; precisão na descrição de risco (estrutura padrão de frase P10, tabela impreciso vs. preciso)
- Seção 4d: 5 respostas a risco (accept/avoid/pursue/reduce/share) com critério de aplicação; quando resposta "accept" sem aprovação de governança = deficiência de P13
- Seção 4e: portfolio view para o auditor — concentração, correlação positiva, hedge natural, escalada por agregação; 4 níveis de integração COSO ERM; como apresentar ao comitê

Descartado de Cap. 8:
- Modelos quantitativos específicos (Monte Carlo, VaR, cash flow at risk) — implementação de ERM, não avaliação pelo auditor
- Exemplos numéricos de stress testing — muito específicos, sem valor reutilizável sem contexto
- Discussão de risk-adjusted capital — métricas financeiras de gestão de portfólio, fora do escopo de interna

---

## [2026-04-28] coso-erm-distillation | Three Lines Model (IIA 2020 + GIAS 2024)

MD criado: `concepts/three-lines-model.md`

Conteúdo:
- Estrutura do modelo: tabela de 5 papéis (órgão de governança, 1ª, 2ª, 3ª linha, prestadores externos)
- Primeira linha: responsabilidade pelo risco não transferida para segunda linha
- Segunda linha: o que é e o que não é; reliance possível mas condicionado à avaliação de qualidade
- Terceira linha: independência como diferencial; armadilha CAE com funções de segunda linha (ex: CAE = CRO)
- Relacionamentos entre papéis: governança → gestão, gestão → auditoria interna, auditoria interna → órgão de governança
- Implicações para planejamento: tabela de avaliação quando cliente tem CRO ativa; critérios de reliance no trabalho de segunda linha
- Avaliação de maturidade da função de auditoria interna: 6 dimensões
- Red flags consolidados

Fonte: IIA Three Lines Model (EN, atualizado setembro 2024 / GIAS 2024) + versão PT-BR julho 2020
Trigger: cliente piloto do setor industrial tem CRO ativa e ERM em estruturação

Descartado:
- Histórico da transição "Three Lines of Defense" → "Three Lines Model" — sem valor operacional
- Detalhes de aplicação em instituições financeiras reguladas — escopo específico não coberto ainda

---

## [2026-04-28] consistency-review | Back-references para information-and-communication.md e monitoring.md

MDs editados (adição de referências em `Artefatos relacionados`):
- `processes/entity-level-controls.md` — adicionados links para `information-and-communication.md` (P14↔P1/P3/P5) e `monitoring.md` (P5↔P17)
- `processes/inquiry-planning-and-follow-up.md` — adicionado link para `information-and-communication.md` (hotline/surveys como evidência de P14)
- `concepts/control-activities-framework.md` — adicionado link para `monitoring.md` (armadilha monitoring como substituto; critérios de mitigação real)
- `modes/risk-assessment.md` — adicionado link para `monitoring.md` (P9 e P16 compartilham gatilhos)

MDs já consistentes (sem alteração necessária):
- `patterns/control-deficiency-severity.md` — já referenciava `monitoring.md`
- `processes/ipe-reliability-assessment.md` — já tinha seção "Vínculo com COSO P13–P15"

---

## [2026-04-28] method-distillation | Cap. 7 — Monitoring

MD criado: `processes/monitoring.md`
MD editado: `patterns/control-deficiency-severity.md`

Conteúdo do novo MD `monitoring.md`:
- Papel do componente: responsabilidade da entidade, não do auditor; princípio de imprevisibilidade
- P16 — 7 pontos de foco; tabela de exemplos de avaliações contínuas com perguntas críticas; avaliações separadas e uso de aleatoriedade como deterrente
- Baseline problem: risco de dados corrompidos desde o início tornando analytics inúteis; caso real de localidade com operações paralelas não reportadas
- Dashboard: força vs. armadilha (pontos não reavaliados, falsa segurança, ausência de tie-in)
- Service organizations no monitoramento: gap de cobertura temporal de SOC reports, "inquiry plus"
- Deficiências de Monitoring como controles pervasivos (Chart 4): amplificam severidade de outros achados
- Red flags consolidados

Conteúdo adicionado em `control-deficiency-severity.md` — seção "Comunicação de Deficiências (P17)":
- Cadeia obrigatória: responsável direto → nível acima → governança
- Dado empírico: 70% das deficiências subestimadas pela gestão (estudo empírico de referência 2004-2005)
- Protocolo especial para fraude: tabela comparativa rotina vs. fraude, risco de destruição de evidência
- Requisitos legais/regulatórios de disclosure externo

Descartado de Cap. 7:
- Coordenação com auditor externo na comunicação de deficiências — escopo de externa
- Implicações PCAOB/SEC para comunicação de MW — externo
- Histórico COSO 2006 → 2013 para Monitoring — histórico sem valor operacional

## [2026-04-28] method-distillation | Cap. 6 — Information and Communication

MD criado: `processes/information-and-communication.md`

Conteúdo do novo MD:
- Papel do componente I&C no COSO: pervasividade — deficiências aqui contaminam múltiplos componentes
- P13 (Gera Informação Relevante): 5 pontos de foco, perguntas críticas de avaliação, importância de dados não-financeiros em estimativas, inventário de relatórios, relação com IPE como evidência de P13
- P14 (Comunica Internamente): 5 elementos obrigatórios de comunicação de responsabilidades de controle; hotline como linha separada com critérios de avaliação de efetividade e armadilha de volume zero; comunicação informal e necessidade de mecanismo de escalada; feedback loop governance ↔ gestão ↔ auditoria; relação com P16/P17
- P15 (Comunica Externamente): fontes externas como evidência de deficiências internas (reclamações, reports de reguladores, management letter); processo de triagem e escalada; foco de interna em canais de entrada
- Seção de pervasividade: como identificar impacto em outros componentes ao achar deficiência de I&C
- Red flags consolidados

Descartado de Cap. 6:
- External reporting financeiro (SEC, public company disclosures) — escopo de externa
- Histórico de transição 1992→2013 para atributos de I&C — histórico sem valor operacional
- Exemplo Enron — ilustrativo, sem conteúdo metodológico novo além do que o conceito já cobre

## [2026-04-28] method-distillation | Cap. 1 — What We All Share

MDs editados:
- `heuristics/documentation-quality.md` — seção "Controls vs. Processes" adicionada: distinção entre documentar processo e documentar controle, exemplos práticos, implicações para walkthrough e atualização de documentação; failure mode correspondente adicionado à lista
- `processes/audit-engagement-execution.md` — seção 8 adicionada: Triangle of Efficiency (referencial metodológico Cap. 1) — 3 vértices (requisitos, COSO/framework, empresa), lógica de retrabalho por deficit em cada vértice, aplicação prática no kickoff

Descartado de Cap. 1:
- História COSO 1992→2013 e transição para 2013 — histórico sem valor operacional
- Debate SOX cost-benefit, public vs. nonpublic reporting — escopo de externa
- Reasonable assurance, limitações de controle interno — já cobertos em `context/standards/sox.md`
- COSO 17 Principles (Appendix 1A) — já coberto

## [2026-04-28] method-distillation | Cap. 13 — Forms and Templates (revisão após leitura completa)

MDs editados após leitura integral dos Appendices 13A–13H:
- `concepts/sample-size.md` — seção 14 adicionada: campos obrigatórios de documentação por teste amostral (completude da população, definição de exceção antes da execução, reliance em terceiros, controle "unusually important", avaliação qualitativa, X-Ref ao deficiency summary); nota sobre viés de confirmação na definição tardia de exceção
- `patterns/control-deficiency-severity.md` — seção "Deficiency Summary" adicionada: 13 campos de registro por deficiência para avaliação agregada (ID, componente, princípio, severidade, Present/Functioning, dono, remediação, princípios relacionados); nota sobre por que summary centralizado é necessário para avaliação de MW por agregação
- `checklists/itgc-inquiry-guide.md` — 3 perguntas adicionadas em "Segurança e autenticação": acceptable use policy (formalização, comunicação, aplicação) e penetration tests (quando, por quem, resultados, ações)

Conteúdo descartado de Cap. 13:
- Templates 13A/13B (work papers principle-focused e revenue): formulários de formato, sem conteúdo metodológico novo
- Histórico de evolução de matriz 1992→2013: irrelevante para interna

## [2026-04-28] method-distillation | Cap. 12 e 13 — Project Management e Templates

MD editado: `processes/audit-engagement-execution.md`

Conteúdo adicionado (Cap. 12):
- Seção 5: Estrutura do time — seniority/autoridade necessária, papel de IA (work product vs. membro ativo), limitação de objetividade em auto-avaliação, tabela de especialistas técnicos com gatilhos de acionamento (IT, valuation, tax)
- Seção 6: Projeto piloto — quando vale, como selecionar área, 5 perguntas de debriefing pós-piloto
- Seção 7: Critérios para ferramentas de documentação — tabela de 8 critérios (acesso, rede, one-write, cross-referencing, status, work paper discipline, rollover, arquivamento); nota sobre eficiência de documentação+teste pela mesma equipe

Não adicionado:
- Coordenação com auditor externo (independência, PCAOB AS No. 5, seção 302/404) — escopo de externa
- Cap. 13 inteiro (Appendix 13A–13H): templates SOX; walk-through e deficiency summary já cobertos em `evidence-and-testing-foundations.md` e `control-deficiency-severity.md`

## [2026-04-28] method-distillation | Cap. 2 — Scoping

MD reescrito: `concepts/scoping-strategy.md`

Conteúdo adicionado (Cap. 2 + Appendix 2A):
- Direção correta de scoping: partir do amplo e excluir com evidência, não o inverso
- Técnica de mapeamento financeiro FS × segmentos para identificar core (planilha com % por conta/localidade)
- Escala de cobertura por nível de risco (core → trivial)
- Armadilha RI vs. risco de controle no scoping: não dar pass a área de alto RI por assumir controles não testados
- Overstatement vs. understatement: risco de completude invisível em valores não registrados (skimming, receita subdeclarada)
- Múltiplas localidades: 3 tipos de risco (centralizado, específico de local, baixo risco) com abordagem por tipo
- Organizações de serviço no scoping: grau de interação como critério, SOC 1 Type 1/2, quando não há report
- Reliance no trabalho de outros: 3 critérios (escopo, timing, qualidade de documentação)
- Sinais de alarme que forçam revisão de escopo durante o trabalho
- Viés SALY no scoping: perguntas anuais obrigatórias antes de replicar
- Tabela de perguntas operacionais de scoping (Appendix 2A adaptado): 9 áreas com pergunta + finalidade

Não adicionado:
- Disclosure committee (SOX/SEC) — externo irrelevante para interna
- Histórico AS No. 2 vs. AS No. 5 — histórico regulatório sem valor operacional
- Requisitos nonaccelerated filers — idem

## [2026-04-28] method-distillation | Cap. 5 — Control Activities

MDs editados:
- `concepts/control-activities-framework.md`
- `concepts/control-types-and-reliance.md`

Conteúdo adicionado em `control-activities-framework.md`:
- Seção 7 (P10): elementos de matriz risco→controle (8 campos), gaps sem controle como deficiência de design, abordagem para riscos não mapeáveis a asserções (override gerencial)
- Seção 8: service organizations — SOC 1 Type 1 vs. Type 2, checklist de 5 pontos de avaliação do report, handoff boundary, alternativas quando não há SOC report
- Seção 9: armadilha monitoring como substituto de controles transacionais — por que falha, tabela de 4 critérios para aceitar monitoring como mitigação real
- Seção 10 (P12): 5 pontos de foco COSO, rastreabilidade P3→P12, flowchart vs. narrativa, quando P12 gera deficiência
- Conexão interna adicionada: `control-types-and-reliance.md`

Conteúdo do `control-types-and-reliance.md` (reescrito — estava raso):
- Tabela manual/IT-dependent/application com implicação para teste
- Controles híbridos e ponto de falha mais comum (exceção gerada sem resolução)
- Tabela prev/detect com trade-offs reais: custo, timing, exposição a distorção de reporting intermediário
- Princípio detecção+correção: dois elementos obrigatórios para eficácia
- Redundância como princípio deliberado
- Tabela automatizados vs. manuais com dependência de ITGCs
- Tabela de implicações para reliance por condição
- Perguntas de classificação para walkthrough
- Red flags incluindo remissão à armadilha de monitoring

Não adicionado:
- Appendix 5A (assertions × ciclos) → já coberto em `concepts/control-objectives-assertions.md`
- Appendix 5B (interrelações entre princípios) → conteúdo de context/design, não operacional
- Discussão de transição 1992→2013 framework → irrelevante para interna

## [2026-04-21] scaffold | Estrutura inicial

- Criada a árvore `_method-wiki/` em `3. Recursos/ok`
- Pastas-base criadas: concepts, heuristics, workflows, checklists, patterns, examples, postmortems, processes e sectors
- Arquivos iniciais criados: README.md, index.md e log.md

## [2026-04-28] sync | index.md atualizado e _method-wiki-external-audit scaffolded

- `index.md` corrigido: removidas entradas de arquivos movidos para `_method-wiki-external-audit/` (reporting-requirements, sox-and-icfr-foundations, engagement-critical-close-checklist, engagement-lifecycle-checklist, misstatement-discussion-questions, work-paper-guide, Nível de Evidência)
- `index.md` corrigido: adicionadas entradas faltantes de heuristics (9 arquivos), patterns (6), postmortems (2) e processes (12)
- `index.md` corrigido: descrição de scoping-strategy ajustada para escopo de auditoria interna
- `_method-wiki-external-audit/` ganhou README.md, index.md e log.md

## [2026-04-28] method-distillation | Cap. 3 — Fraud Risk (gap adicional)

MD editado: `processes/fraud-risk-assessment.md`

Conteúdo adicionado (Cap. 3 + Appendix 3A/3B):
- COSO Princípio 8: 4 pontos de foco obrigatórios
- Fraud Triangle completo: motivação, oportunidade, racionalização — com exemplos reais de racionalização
- Dados ACFE: tipos de fraude × frequência × impacto mediano
- Fontes de detecção: denúncia (42%), auditoria interna (14–16%), auditoria externa (3%)
- Antifraud controls com % de redução de perda documentadas (data analytics −60%, hotline −41%)
- Esquemas comuns por processo: OTC, P2P, H2R, estoque
- Checklist de avaliação de programa antifraud existente
- Override gerencial como fator de ambiente de controle — sinais de alerta

## [2026-04-28] method-distillation | Cap. 3 — Risk Assessment

MDs editados:
- `concepts/risk-scoring-foundations.md`
- `modes/risk-assessment.md`

Conteúdo adicionado do referencial metodológico (Cap. 3):
- Separação obrigatória RI vs. risco de controle — erro comum de avaliação conjunta
- Quatro dimensões de risco COSO 2013: likelihood, magnitude, velocity, persistence — com analogia e casos de uso
- Princípio 9 (significant change): fontes internas e externas de mudança, viés SALY, armadilha de documentação vaga

Não adicionado (coberto em MD separado ou externo):
- Princípio 8 (fraud risk) → `processes/fraud-risk-assessment.md` — verificar gap em sessão própria
- Assertions (13 + simplificações) → já coberto em `concepts/control-objectives-assertions.md`
- Dados empíricos de fraude (ACFE survey) → escopo de `processes/fraud-risk-assessment.md`

## [2026-04-28] method-distillation | Cap. 10 — Deficiency Severity

MD editado: `patterns/control-deficiency-severity.md`

Conteúdo adicionado do referencial metodológico (Cap. 10 + Appendix 10A/10B):
- Framework de 4 Charts (exceções → processo → ITGC → pervasivos) com lógica step-by-step
- Definições precisas: gross exposure, adjusted exposure, upper limit deviation rate
- Tabela de upper limit a 90% de confiança (N=25 a 50, desvios 0 a 2)
- Prudent Official Test — como aplicar e exemplos de falha
- Agregação de deficiências — regras e condições de MW por acumulação
- Deficiências especiais presumidamente mais severas (lista completa)
- Controles compensatórios — critérios de efetividade real e armadilhas comuns
- Dados empíricos: tipos de MW mais comuns ao longo do tempo (estudo empírico de referência study)

Conflito marcado:
- ITGC: referencial metodológico (prática prevalecente) trata severidade como condicional à aplicação. COSO 2013 Princípio 11 sugere avaliação independente. Validar com contexto regulatório do cliente.

## [2026-04-28] method-distillation | Cap. 8 — Evidence and Testing

MDs editados:
- `concepts/sample-size.md`
- `processes/ipe-reliability-assessment.md`

MD criado:
- `concepts/evidence-and-testing-foundations.md`

Conteúdo adicionado em `sample-size.md`:
- Seção 13: top-down concept aplicado ao dimensionamento de testes (sequência: CE → ITGCs → shared controls → transacionais)
- Impacto de ITGC deficiente no N de controles automatizados
- Alerta sobre confusão 25/40/60 (guidance A-133 não se aplica a controles de reporte financeiro)

Conteúdo adicionado em `ipe-reliability-assessment.md`:
- Seção "Vínculo com Books and Records": tie-in a registros oficiais como requisito, não opção
- Documento original vs. cópia: preferência por live data em áreas de maior risco
- Seção "Vínculo com COSO P13–P15": confiabilidade de IPE como evidência de Information & Communication

Conteúdo do novo MD `evidence-and-testing-foundations.md`:
- Tabela de tipos e hierarquia de evidência (reperformance → inquiry)
- Condições que aumentam força de evidência (externa > interna, original > cópia, direta > oral)
- Walkthrough: definição correta (foco nos controles, não no documento), diferença de "seguir o processo"
- Critérios de qualidade de documentação de walkthrough (8 itens)
- Erro de stovepipe: avaliar teste isoladamente sem referenciar procedimentos correlatos
- Top-down concept: sequência CE → ITGC → shared controls → transacionais com lógica de custo de descoberta tardia
- Tabela de situações sem amostragem (SoD, ELC, governança, controles automatizados, código de conduta)
- Seção de documentação de julgamentos de evidência

Não adicionado:
- Testing Security and Access detalhado → já coberto em `checklists/itgc-inquiry-guide.md` e processos ITGC
- Program Modifications e New System Development → já cobertos em `processes/vendor-supplied-change-management.md` e `processes/entity-programmed-changes.md`
- Discussão SOX/PCAOB/acelerados → escopo de `_method-wiki-external-audit/`

## [2026-04-28] method-distillation | Cap. 4 — Control Environment

MD reescrito: `processes/entity-level-controls.md`

Conteúdo adicionado (Cap. 4 + Appendix 4A):
- Papel do CE como componente "trump card" do COSO e relação com management override
- P1: quatro pontos de foco, tabela incentivos vs. tentações, sinais de problema por filosofia gerencial, evidências úteis, organismos de serviço como extensão do CE
- P2: critérios de avaliação do comitê de auditoria (5 dimensões), tratamento de entidades sem independência estrutural possível
- P3: sinais de risco estrutural (complexidade desnecessária, partes relacionadas, delegação sem monitoramento)
- P4: sinais de deficiência de competência, padrão de mitigação documentada, relação com P1 e P3
- P5: paper-tiger mentality, sinais de falha de accountability, interação com Monitoring P17
- Tabela de interações entre princípios com exemplos de root cause
- Tabela de responsabilidades por cargo (Appendix 4A): CEO, gestão, diretores financeiros, conselho, comitê de auditoria, auditoria interna, demais colaboradores
- Checklist de avaliação rápida por princípio (pergunta-chave)
- Red flags consolidados de ambiente de controle

Não adicionado:
- Conteúdo sobre independência Blue Ribbon Commission → escopo de externa/SOX
- Transição de 1992 → 2013 Framework → irrelevante para interna
- Guidance SEC/PCAOB sobre comitê de auditoria → já coberto em `_method-wiki-external-audit/`

Novo MD: não criado — conteúdo conceitual incorporado no próprio MD operacional

## [2026-04-28] method-distillation | Cap. 9 — Interviews & Questionnaires

MD editado: `processes/inquiry-planning-and-follow-up.md`

Conteúdo adicionado (Cap. 9 + Appendix 9A):
- Seção "Modalidades de Coleta": entrevista individual, survey e focus group — quando usar cada um
- Survey: problemas comuns que reduzem confiabilidade, timing no ciclo, proporção mínima de amostra (5–10%)
- Focus group: limitações por cultura e hierarquia, uso em alternância com surveys
- Tabela Inquiry + Observation: papel de cada modalidade, quando priorizar documentos
- Dado empírico referencial metodológico: 55% comunicação via sinais não-verbais, 38% tom, 7% conteúdo verbal
- Regras de condução: perguntas pessoais > perguntas sobre "a empresa"; não revelar o que já se sabe; pedir exemplos concretos
- Seção "Escalada de fraude durante entrevista": 5 passos operacionais, citação referencial metodológico sobre não improvisar investigação
- Armadilhas adicionais: mesmas pessoas todo ciclo, júnior entrevistando executivo, formato repetido

Não adicionado:
- Banco de perguntas por princípio COSO → já coberto em `checklists/inquiry-question-bank.md`
- Perguntas específicas de ITGC → já cobertas em `checklists/itgc-inquiry-guide.md`
- Survey template completo → Appendix 9A já estava incorporado nos checklists anteriores

## [2026-04-26] cleanup | Mapas de migração arquivados

- `_maps/` deixou de ser área viva da wiki.
- Mapas de migração foram movidos para `archive/ey-migration-maps/`.
- `athena-architecture.md` foi preservado em `archive/review-later/` para revisão futura.
