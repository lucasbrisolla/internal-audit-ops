# Achado de Auditoria — 5 Cs

> Template da trilha interna. Se o caso exigir classificação `Control Deficiency`, `Significant Deficiency` ou `Material Weakness`, usar `_method-wiki-external-audit/templates/output-achado-5c-external-audit.md`.
> Referência: workflow `finding-drafting.md` + `finding-rating.md`. Preencher na sequência: Condition → Criteria → Cause → Consequence → Corrective Action.
> Para achados que vão para comunicação com gestão, verificar nível **Forte** na Rubric de Qualidade antes de encaminhar → `_method-wiki/checklists/audit-artifacts-definition-of-done.md`.
>
> **Persistência:** salvar em arquivo consolidado por processo `templates/achados/achados-<processo>.md`. Múltiplos achados no mesmo arquivo, separados por `---\n---`, com Resumo Consolidado ao final. Referência interna: `REC-01`, `FAT-01` etc. Proibido criar arquivos individuais por achado. Modelo: `templates/achados/achados-faturamento.md`.

---

## Identificação

| Campo | Valor |
|---|---|
| Cliente / Entidade | |
| Processo | |
| Referência do achado | ex: ACH-2025-001 |
| Data | |
| Auditor responsável | |

---

## Rating

| Dimensão | Avaliação |
|---|---|
| Severidade | `[ ] Crítico` `[ ] Alto` `[ ] Médio` `[ ] Baixo` |
| Probabilidade de ocorrência | `[ ] Alta` `[ ] Média` `[ ] Baixa` |
| Impacto financeiro estimado | |
| Tipo de risco | `[ ] Controle` `[ ] Fraude` `[ ] Operacional` `[ ] Compliance` `[ ] Financeiro` |
| Maturidade do controle associado | Nível: ___ / Score: ___ — ref. `control-maturity-rubrics.md` (opcional) |

**Racional de severidade:**
> Documentar impacto × probabilidade. Se severidade = Crítico ou tipo = Fraude: aplicar Prudent Official Test (`patterns/control-deficiency-severity.md`) e registrar conclusão aqui. Verificar se há outros achados no mesmo componente COSO — se sim, avaliar severidade agregada antes de fechar rating individual.

---

## 1. Condition (Condição)

> O que foi observado? Descrever o fato concreto identificado — sem julgamento, sem causa, sem consequência. Evidência direta.

**Observação:**

**Evidência de suporte:**
- Tipo: `[ ] Documental` `[ ] Entrevista` `[ ] Analítica` `[ ] Reperformance`
- Referência / path:
- Amostra (se aplicável): n= / universo=

---

## 2. Criteria (Critério)

> Qual é o padrão que deveria ser seguido? Política, norma, regulamento, contrato ou melhor prática contra o qual a condição é comparada.

**Critério:**

**Fonte:**
- `[ ] Política interna` `[ ] COSO / IIA` `[ ] Norma contábil (CPC/IFRS)` `[ ] Regulamento setorial` `[ ] Contrato` `[ ] Melhor prática`
- Referência específica (artigo, seção, página):

---

## 3. Cause (Causa)

> Por que a condição existe? Causa-raiz — não sintoma. Evitar "falta de controle" como causa única.

**Causa identificada:**

**Categoria:**
- `[ ] Ausência de controle` `[ ] Controle existente mas ineficaz` `[ ] Falha humana` `[ ] Falha de sistema` `[ ] Falta de segregação` `[ ] Falta de treinamento` `[ ] Design inadequado do processo`

---

## 4. Consequence (Consequência)

> Qual é o impacto real ou potencial? Quantificar quando possível. Conectar à asserção afetada.

**Consequência:**

**Dimensão impactada:**
- `[ ] Operacional` `[ ] Compliance` `[ ] Governança` `[ ] Financeira` `[ ] TI / Segurança` `[ ] Fraude`

**Impacto quantificado (se aplicável):**

**Análise de Fraud Triangle (preencher se tipo de risco incluir Fraude):**
- Oportunidade:
- Motivação / Pressão:
- Racionalização:
- Lacunas de investigação (vértices não confirmados — endereçar em execução):

> Ref.: `_method-wiki/processes/fraud-risk-assessment.md`

---

## 5. Corrective Action (Ação Corretiva)

> O que precisa ser feito para resolver? Ação específica, responsável e prazo. Distinguir correção pontual, melhoria estrutural ou roadmap (bloqueada por dependência externa/sistêmica).

| #   | Ação | Responsável (owner único) | Prazo | Tipo                                         | Critério de conclusão |
| --- | ---- | ------------------------- | ----- | -------------------------------------------- | --------------------- |
| 1   |      |                           |       | `[ ] Pontual` `[ ] Estrutural` `[ ] Roadmap` |                       |
| 2   |      |                           |       | `[ ] Pontual` `[ ] Estrutural` `[ ] Roadmap` |                       |
|     |      |                           |       |                                              |                       |

> **Roadmap:** usar quando a ação depende de terceiro (ICT, fornecedor, sistema) e não pode ser concluída no ciclo corrente. Registrar dependência e prazo estimado. Garantir que controles compensatórios cobrem o risco residual enquanto a ação estrutural não é implementada.

**Posição da gestão:**

---

## Gate de Adversarial Review

> Aplicar antes da DoD → `skills/challenge-reasoning.md` modo Advogado do Diabo (Ferramenta 6). Se severidade = Crítico/Alto: aplicar também Prudent Official Challenge (Ferramenta 14).

- `[ ] Gate aplicado`
- Resultado: `[ ] Passou sem alteração` `[ ] C revisado:` _______________

---

## Rascunho de Parágrafo (opcional)

> Texto corrido para inserção no relatório. Gerado pelo workflow `finding-drafting.md`.
