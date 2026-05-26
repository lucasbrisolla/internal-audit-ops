# domain: internal audit

## Papel

Mapa leve de consulta para o agente de auditoria interna.

Este arquivo não é a base técnica completa. Use-o para decidir qual módulo carregar sob demanda. A base metodológica principal de auditoria interna vive em `_method-wiki/`; a trilha de auditoria externa / ICFR / SOX vive em `_method-wiki-external-audit/`; workflows, skills e contextos específicos só devem ser carregados quando a tarefa pedir.

## Regra de contexto

- Não carregar todos os módulos por padrão.
- Começar pelo problema do usuário e pelo workflow aplicável.
- Consultar apenas os conceitos, processos, heurísticas ou checklists necessários para a tarefa atual.
- Preferir contexto pequeno, específico e verificável a notas monolíticas.

## Consultas principais

| Necessidade                                                                   | Consultar                                                                          |
| ----------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| Fundamentos de auditoria externa, ICFR, COSO e relação management/auditor     | `_method-wiki-external-audit/concepts/sox-and-icfr-foundations.md`                 |
| Atividades de controle, tipos de controle, SoD, ITGC e controles de aplicação | `_method-wiki/concepts/control-activities-framework.md`                            |
| Tipologia de controles e reliance                                             | `_method-wiki/concepts/control-types-and-reliance.md`                              |
| Objetivos de controle e asserções por processo                                | `_method-wiki/concepts/control-objectives-assertions.md`                           |
| SCOT, caminho crítico e WCGW em auditoria externa                             | `_method-wiki-external-audit/concepts/scot-and-wcgw-foundations-external-audit.md` |
| Mapeamento de processo para auditoria interna                                 | `_method-wiki/concepts/process-mapping-internal-audit.md`                          |
| Scoping, risco inerente, localizações, SOC e M&A                              | `_method-wiki/concepts/scoping-strategy.md`                                        |
| Scoring de risco, impacto, probabilidade e calibração                         | `_method-wiki/concepts/risk-scoring-foundations.md`                                |
| Maturidade de controles                                                       | `_method-wiki/concepts/control-maturity-rubrics.md`                                |
| Glossário técnico de auditoria interna e controle                             | `_method-wiki/concepts/internal-audit-glossary.md`                                 |
| Qualidade de documentação, failure modes e critérios de saída                 | `_method-wiki/heuristics/documentation-quality.md`                                 |
| Status de testes, seleção, REF e IPE                                          | `_method-wiki/processes/testing-status-and-selection.md`                           |
| Confiabilidade de IPE                                                         | `_method-wiki/processes/ipe-reliability-assessment.md`                             |
| ELCs e controles de nível de entidade                                         | `_method-wiki/processes/entity-level-controls.md`                                  |
| GBS, SSC, FBP e transformações operacionais                                   | `_method-wiki/processes/gbs-ssc-control-model.md`                                  |
| Definição de pronto de walkthrough, RCM, teste, achado e plano de ação        | `_method-wiki/checklists/audit-artifacts-definition-of-done.md`                    |

## Heuristica de escolha

- Se a pergunta for conceitual, carregar `concepts/`.
- Se a pergunta for de execução de trabalho, carregar `workflows/`, `processes/` ou `checklists/`.
- Se a pergunta for de julgamento, qualidade ou revisão, carregar `heuristics/` e `patterns/`.
- Se envolver cliente, processo, política ou evidência específica, carregar primeiro o insumo do caso e depois a metodologia mínima necessária.
- Se o problema depender de `SCOT`, `WCGW`, `ICFR`, `SOX`, `material weakness` ou `significant deficiency`, migrar da trilha interna para `_method-wiki-external-audit/`.

## Guardrail

Quando a informação metodológica for insuficiente, sinalizar a lacuna e propor a consulta específica. Não compensar falta de contexto com inferência escondida.
