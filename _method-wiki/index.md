# Method Wiki - Index

## Entradas principais

- [README](README.md)
- [Guide](guide.md) — navegação por fase do trabalho e por situação
- [Log](log.md)

## Áreas

- [Concepts](concepts)
- [Heuristics](heuristics)
- [Checklists](checklists)
- [Patterns](patterns)
- [Postmortems](postmortems)
- [Processes](processes)

---

## Concepts

| Arquivo                                                                             | Descrição                                                                                                                                                                                                                                                  | Fonte                   |
| ----------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| [control-activities-framework.md](concepts/control-activities-framework.md)         | COSO Princípios 10–12: tipos de controle, SoD, ITGCs por domínio, controles de aplicação, planilhas, SOC reports, fechamento; P10 matriz risco→controle, service orgs (SOC 1 Type 1/2), armadilha monitoring como substituto, P12 deployment via políticas | referencial metodológico Cap. 5           |
| [evidence-and-testing-foundations.md](concepts/evidence-and-testing-foundations.md) | Fundamentos de evidência: hierarquia de tipos, walkthrough (definição, qualidade, stovepipe error), top-down concept, situações sem amostragem                                                                                                             | referencial metodológico Cap. 8           |
| [control-maturity-rubrics.md](concepts/control-maturity-rubrics.md)                 | Escala de maturidade de controles — 5 níveis, critérios e exemplos por dimensão                                                                                                                                                                            | —                       |
| [control-objectives-assertions.md](concepts/control-objectives-assertions.md)       | Objetivos de controle × asserções PCAOB por processo: OTC, P2P, INV, H2R, FA, Goodwill, TAX, Contingências, Equity, TRE, RTR, Loans                                                                                                                        | referencial metodológico Appendix 5A      |
| [control-types-and-reliance.md](concepts/control-types-and-reliance.md)             | Tipologia de controles e implicações para reliance: controles híbridos, princípio detecção+correção, trade-offs prev/detect, vantagens e riscos de automatizados, red flags de classificação incorreta                                                     | referencial metodológico Cap. 5           |
| [internal-audit-glossary.md](concepts/internal-audit-glossary.md)                   | Vocabulário técnico de auditoria interna: termos de controle, asserções, ToD/ToE e REF                                                                                                                                                                     | domain.md               |
| [process-mapping-internal-audit.md](concepts/process-mapping-internal-audit.md)     | Como mapear processos de negócio para fins de auditoria interna — fluxo, atores, pontos de controle                                                                                                                                                        | —                       |
| [risk-scoring-foundations.md](concepts/risk-scoring-foundations.md)                 | Fundamentos de scoring de risco: conceito de risco (upside, evento vs. condição), separação RI vs. risco de controle, 5 dimensões (likelihood, magnitude, velocity, persistence, recovery), inherent/target/residual, heat map, bias de avaliação, apetite padrão | referencial metodológico Cap. 3 + COSO ERM 2017 |
| [sample-size.md](concepts/sample-size.md)                                           | Tamanho de amostra para testes de controle: fórmula N=F/T, tabelas AICPA, controles infrequentes, sequencial dois estágios, controles automatizados, top-down e confusão 25/40/60                                                                          | referencial metodológico Cap. 8 + App. 8A |
| [scoping-strategy.md](concepts/scoping-strategy.md)                                 | Estratégia de escopo: mapeamento FS×segmentos para identificar core, RI antes de controle, armadilha overstatement/understatement, múltiplas localidades (3 tipos), service orgs, reliance em trabalho de outros, SALY, perguntas operacionais de scoping; apetite de risco e tolerância como calibradores de escopo | referencial metodológico Cap. 2 + COSO ERM 2017 |
| [scot-and-wcgw-foundations.md](concepts/scot-and-wcgw-foundations.md)               | Página-ponte: explica que SCOT pertence primariamente à trilha externa e como fazer interface sem usar SCOT como default interno                                                                                                                            | —                       |
| [three-lines-model.md](concepts/three-lines-model.md)                               | Modelo das Três Linhas (IIA 2020): papéis por linha, relacionamentos, reliance na segunda linha, independência da terceira, avaliação de maturidade da função de auditoria interna, red flags; CRO rubrica de avaliação, ERM committee, comitês do board por foco de oversight, segunda linha responsabilidades esperadas (COSO Appendix C) | IIA 2020 + GIAS 2024 + COSO ERM 2017 |

---

## Heuristics

| Arquivo | Descrição | Fonte |
|---|---|---|
| [audit-bias-and-judgment-calibration.md](heuristics/audit-bias-and-judgment-calibration.md) | Calibração de julgamento para reduzir vieses cognitivos, fortalecer ceticismo profissional e melhorar consistência de decisão | — |
| [coaching-and-development-conversations.md](heuristics/coaching-and-development-conversations.md) | Conversas de coaching orientadas a progresso, clareza de desafio e suporte explícito | — |
| [documentation-quality.md](heuristics/documentation-quality.md) | Heurísticas, failure modes e critérios de qualidade para documentação técnica de auditoria | domain.md |
| [ethical-influence-and-feedback.md](heuristics/ethical-influence-and-feedback.md) | Influência com clareza e ética, reforço de compromisso real e espaço de feedback útil em colaboração remota | — |
| [execution-focus-and-throughput.md](heuristics/execution-focus-and-throughput.md) | Preservar foco, cadência de execução e qualidade de coordenação em trabalhos com múltiplas frentes | — |
| [lean-collaboration-technology.md](heuristics/lean-collaboration-technology.md) | Escolha de tecnologia de colaboração com foco em simplicidade operacional e adoção real | — |
| [planning-and-scope-discipline.md](heuristics/planning-and-scope-discipline.md) | Disciplina de escopo, comunicação e alocação técnica em trabalhos de auditoria | — |
| [remote-communication-clarity.md](heuristics/remote-communication-clarity.md) | Comunicação clara em times virtuais, reduzindo ruído, mal-entendido e retrabalho | — |
| [scope-and-sufficiency-discipline.md](heuristics/scope-and-sufficiency-discipline.md) | Equilíbrio entre escopo, suficiência de evidência e proporcionalidade, evitando overauditing e subcobertura | — |
| [virtual-team-accountability.md](heuristics/virtual-team-accountability.md) | Responsabilização clara em times virtuais: deadline, dono único, especificidade de pedido e registro escrito | — |

---

## Patterns

| Arquivo | Descrição | Fonte |
|---|---|---|
| [control-deficiency-severity.md](patterns/control-deficiency-severity.md) | Avaliação de severidade de falhas de controle: 4 Charts, upper limit deviation, Prudent Official Test, agregação de deficiências, compensatórios e dados empíricos | referencial metodológico Cap. 10 |
| [control-design-and-operating-effectiveness.md](patterns/control-design-and-operating-effectiveness.md) | Avaliação de desenho e efetividade operacional de controles — cobertura temporal, completude e confiabilidade da informação | — |
| [documentation-and-deliverable-governance.md](patterns/documentation-and-deliverable-governance.md) | Governança de documentação: composições, de-para de entregáveis e prevenção de retrabalho em versões | — |
| [ratio-analysis.md](patterns/ratio-analysis.md) | Relações entre contas como evidência substantiva ou suporte analítico à avaliação de saldos | — |
| [test-of-details.md](patterns/test-of-details.md) | Teste de detalhe: adições, baixas, documentação suporte e risco de dupla contagem | — |
| [trend-analysis.md](patterns/trend-analysis.md) | Comparação temporal como evidência substantiva, especialmente quando teste de detalhe é pouco eficiente | — |

---

## Postmortems

| Arquivo | Descrição | Fonte |
|---|---|---|
| [post-project-review-template.md](postmortems/post-project-review-template.md) | Template para retrospectiva pós-projeto: aprendizado reutilizável, causa-raiz e prevenção de recorrência | — |
| [project-execution-risk-patterns.md](postmortems/project-execution-risk-patterns.md) | Padrões recorrentes de falha em execução, coordenação, qualidade técnica e governança de trabalhos | — |

---

## Processes

| Arquivo                                                                                          | Descrição                                                                                                                                                                                       | Fonte                      |
| ------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| [audit-engagement-execution.md](processes/audit-engagement-execution.md)                         | Hub de execução de trabalhos: planejamento operacional, controle de pendências, escalonamento, anti-retrabalho; estrutura de time e especialistas, projeto piloto, critérios para ferramentas de documentação | referencial metodológico Cap. 12             |
| [entity-level-controls.md](processes/entity-level-controls.md)                                   | Avaliação de ambiente de controle: COSO P1–P5 (integridade, governança, estrutura, competência, accountability), tabela de responsabilidades por cargo, red flags e interações entre princípios; board como avaliador do ERM, bias organizacional, comunicação e reporte de risco ao board — tipologia, key indicators vs. KPIs, cascata, reporte de cultura (COSO ERM P1/P3/P19/P20) | referencial metodológico Cap. 4 + COSO ERM 2017 |
| [erp-transition-and-control-remediation.md](processes/erp-transition-and-control-remediation.md) | Hub de transição de ERP: integridade de dados, conciliações críticas, ITGC e remediação de deficiências antes do fechamento                                                                     | —                          |
| [fraud-risk-assessment.md](processes/fraud-risk-assessment.md)                                   | Hub de risco de fraude: COSO P8, Fraud Triangle, dados ACFE, esquemas por processo, programa antifraud e override gerencial                                                                     | referencial metodológico Cap. 3 + App. 3A/3B |
| [gbs-ssc-control-model.md](processes/gbs-ssc-control-model.md)                                   | Modelo de controle para GBS, SSC, FBP, três linhas e transformação operacional                                                                                                                  | domain.md                  |
| [inquiry-planning-and-follow-up.md](processes/inquiry-planning-and-follow-up.md)                 | Hub de indagações: entrevistas, surveys e focus groups — modalidades, evidência inquiry + observation, escalada de fraude e regras de condução                                                  | referencial metodológico Cap. 9              |
| [inventory-observation-and-counting.md](processes/inventory-observation-and-counting.md)         | Hub de inventário físico: estratégia de amostragem, recontagem, evidência e limitações operacionais                                                                                             | —                          |
| [information-and-communication.md](processes/information-and-communication.md)                   | COSO P13–P15: qualidade de informação gerada (P13), comunicação interna e hotline (P14), comunicação externa e escalada de issues (P15); pervasividade de deficiências de I&C                   | referencial metodológico Cap. 6              |
| [monitoring.md](processes/monitoring.md)                                                          | COSO P16–P17: avaliações contínuas e separadas, baseline problem, dashboard trap, service orgs no monitoramento; P17 coberto em `patterns/control-deficiency-severity.md`                        | referencial metodológico Cap. 7              |
| [ipe-reliability-assessment.md](processes/ipe-reliability-assessment.md)                         | Hub de confiabilidade de IPE: completude, precisão, extração, parâmetros, tie-in a books and records, original vs. cópia, vínculo com COSO P13–P15                                              | referencial metodológico Cap. 8              |
| [job-scheduling-and-monitoring.md](processes/job-scheduling-and-monitoring.md)                   | Hub de rotinas automatizadas: agendamentos e monitoramento de jobs em aplicações e ERPs relevantes                                                                                              | —                          |
| [journal-entry-testing.md](processes/journal-entry-testing.md)                                   | Hub de journal entries: management override, população, seleção baseada em risco, data analytics e julgamento                                                                                   | —                          |
| [procure-to-pay.md](processes/procure-to-pay.md)                                                 | Hub de compras e contas a pagar: fluxo operacional, integrações sistêmicas, alçadas, cadastro de fornecedor e controles                                                                         | —                          |
| [security-settings-and-authentication.md](processes/security-settings-and-authentication.md)     | Hub de segurança: configuração, requisitos de senha e mecanismos de autenticação em aplicações e TI                                                                                             | —                          |
| [user-access-management.md](processes/user-access-management.md)                                 | Hub de gestão de acessos: solicitação, aprovação, concessão, revogação, acessos privilegiados e revisão periódica                                                                               | —                          |
| [virtual-team-setup-and-trust.md](processes/virtual-team-setup-and-trust.md)                     | Hub de times virtuais: setup, propósito, expectativas, onboarding, confiança e tratamento de baixo desempenho                                                                                   | —                          |

---

## Checklists

| Arquivo                                                                                         | Descrição                                                                                                               | Fonte                   |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| [audit-artifacts-definition-of-done.md](checklists/audit-artifacts-definition-of-done.md)       | DoD específica de auditoria: walkthrough, RCM, papel de teste, achado e plano de ação                                   | —                       |
| [deficiency-aggregation-gate.md](checklists/deficiency-aggregation-gate.md)                     | Gate de agregação de deficiências: avaliar se deficiências individuais formam SD ou MW quando combinadas                 | —                       |
| [ipe-validation-before-test.md](checklists/ipe-validation-before-test.md)                       | Validação de IPE antes de executar teste: completude, precisão e autoridade da informação produzida pela entidade        | —                       |
| [control-attribute-design.md](checklists/control-attribute-design.md)                           | Atributos de design de controle: gatilho, executor, frequência, evidência, critério de falha                            | —                       |
| [email-and-phone-escalation-checklist.md](checklists/email-and-phone-escalation-checklist.md)   | Checklist de escalação por e-mail e telefone durante o engagement                                                       | —                       |
| [footing-and-casting-checks.md](checklists/footing-and-casting-checks.md)                       | Verificações aritméticas de cálculo e totalização em papéis de trabalho                                                 | —                       |
| [information-sources-for-planning.md](checklists/information-sources-for-planning.md)           | Fontes de informação para fase de planejamento — internas, externas, regulatórias                                       | —                       |
| [inquiry-question-bank.md](checklists/inquiry-question-bank.md)                                 | Banco de perguntas para walkthrough e entrevistas: design, consistência, qualificação, gestão (por princípio COSO 1–17) | referencial metodológico Cap. 9 + App. 9A |
| [interview-consistency-tests.md](checklists/interview-consistency-tests.md)                     | Testes de consistência entre entrevistados — identificar respostas conflitantes                                         | —                       |
| [itgc-inquiry-guide.md](checklists/itgc-inquiry-guide.md)                                       | Guia de inquérito para ITGCs por domínio                                                                                | —                       |
| [onboarding-and-delegation-for-juniors.md](checklists/onboarding-and-delegation-for-juniors.md) | Checklist de onboarding e delegação de tarefas para membros juniores do time                                            | —                       |
| [virtual-meeting-checklist.md](checklists/virtual-meeting-checklist.md)                         | Checklist de reunião virtual — pré, durante e pós                                                                       | —                       |

---
