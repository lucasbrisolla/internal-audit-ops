# Guia de Navegação — internal-audit-ops

Este guia tem duas entradas. Use a que fizer mais sentido para o seu momento:

- **Por fase do trabalho** — onde você está no ciclo de auditoria
- **Por situação** — o que você precisa fazer agora

O guia não substitui os workflows nem a _method-wiki. Ele aponta para onde ir.

---

## Entrada 1 — Por fase do trabalho

### Fase 1 — Planejamento

O que acontece aqui: entender a entidade, avaliar riscos, definir escopo e montar o programa de trabalho.

**Workflows:**
- `workflows/audit-planning.md` — sequência completa de planejamento

**Modos de apoio:**
- `modes/business-understanding.md` — entender o negócio antes de avaliar risco
- `modes/risk-assessment.md` — avaliar e priorizar riscos organizacionais
- `modes/risk-matrix.md` — formalizar matriz de risco para comitê
- `modes/regulatory-check.md` — verificar conformidade contra normas aplicáveis

**Base metodológica relevante:**
- `concepts/risk-scoring-foundations.md` — como classificar risco inerente e residual
- `concepts/scoping-strategy.md` — como definir escopo de forma defensável
- `processes/entity-level-controls.md` — ambiente de controle como ponto de partida
- `processes/fraud-risk-assessment.md` — risco de fraude como input do planejamento
- `checklists/information-sources-for-planning.md` — fontes de informação para planejamento

**Artefato esperado:** plano de auditoria com escopo, riscos priorizados e programa de trabalho.

---

### Fase 2 — Execução

O que acontece aqui: entender o processo, mapear riscos e controles, desenhar e executar testes, coletar evidência.

**Workflows:**
- `workflows/risk-control-mapping.md` — mapear processo, riscos, controles e testes
- `workflows/test-execution.md` — desenhar e avaliar testes de controle
- `workflows/walkthrough-standardization.md` — padronizar walkthrough
- `workflows/transcript-analysis.md` — aproveitar transcrição de reunião ou entrevista

**Skills auxiliares:**
- `skills/wcgw-mapping.md` — identificar o que pode dar errado por processo
- `skills/control-documentation.md` — expandir controle em descrição testável
- `skills/control-evaluation.md` — avaliar qualidade do controle
- `skills/risk-scoring.md` — calcular score de risco inerente e residual
- `skills/sample-size-calculator.md` — definir tamanho de amostra defensável
- `skills/process-flow-mermaid.md` — gerar fluxograma do processo
- `skills/process-flow-bpmn.md` — gerar fluxograma em BPMN 2.0
- `skills/operating-model-analysis.md` — entender transformações operacionais antes de mapear controles

**Base metodológica relevante:**
- `concepts/evidence-and-testing-foundations.md` — tipos de evidência e hierarquia
- `concepts/control-types-and-reliance.md` — tipos de controle e implicações para teste
- `concepts/control-activities-framework.md` — COSO P10–P12, ITGCs, controles de aplicação
- `concepts/sample-size.md` — lógica de amostragem para testes de controle
- `processes/ipe-reliability-assessment.md` — avaliar confiabilidade de relatórios e dados
- `patterns/control-design-and-operating-effectiveness.md` — avaliar desenho e efetividade
- `checklists/control-attribute-design.md` — atributos de um controle bem documentado
- `checklists/inquiry-question-bank.md` — banco de perguntas para walkthrough e entrevistas
- `checklists/itgc-inquiry-guide.md` — perguntas específicas para ITGCs

**Artefato esperado:** RCM com riscos, controles e testes; papéis de trabalho com evidência documentada.

---

### Fase 3 — Achados

O que acontece aqui: formalizar observações, classificar severidade, estruturar plano de ação.

**Workflows:**
- `workflows/finding-drafting.md` — redigir achado com base nos 5 Cs
- `workflows/finding-rating.md` — classificar severidade do achado

**Skills auxiliares:**
- `skills/challenge-reasoning.md` — questionar julgamento, rating ou conclusão antes de fechar
- `skills/financial-risk-to-action.md` — priorizar achados com impacto financeiro

**Base metodológica relevante:**
- `patterns/control-deficiency-severity.md` — avaliação de severidade de falhas de controle
- `concepts/control-maturity-rubrics.md` — escala de maturidade de controles
- `checklists/audit-artifacts-definition-of-done.md` — critérios de conclusão de achado e plano de ação

**Artefato esperado:** achado formalizado com critério, condição, causa, consequência e recomendação; plano de ação com owner e prazo.

---

### Fase 4 — Comunicação

O que acontece aqui: apresentar resultados para gestão e comitê de auditoria.

**Cobertura atual:** parcial. Workflow específico de comunicação ainda não construído — congelado até piloto rodar.

**O que usar enquanto isso:**
- `templates/output-achado-5c.md` — estrutura padrão de achado para comunicação
- `skills/audit-dashboard-visualization.md` — escolher visual para apresentação de riscos, achados e status
- `modes/formatting.md` — linguagem e formato corretos para artefatos formais

---

### Fase 5 — Follow-up

O que acontece aqui: monitorar execução do plano de ação, revalidar controles remediados.

**Cobertura atual:** parcial. Workflow de follow-up congelado até piloto rodar.

**O que usar enquanto isso:**
- `templates/Followup_Plano_Acao_v2_template.xlsx` — tracker de plano de ação gerado por script
- `states.yml` — estados canônicos de achado e plano de ação

---

## Entrada 2 — Por situação

### Estou começando um engagement e não sei por onde ir

1. Verifique se existe perfil do cliente: `context/clients/<slug>/index.md`
   - Se não existe → rode `skills/client-context.md` modo `init`
2. Entenda o negócio antes de avaliar risco → `modes/business-understanding.md`
3. Siga a sequência de planejamento → `workflows/audit-planning.md`

---

### Preciso mapear riscos e controles de um processo

1. Identifique o processo pelo código (P2P, OTC, RTR, H2R etc.)
2. Consulte WCGWs do processo → `context/wcgw-master.json` filtrando pelo `process_code`
3. Siga o workflow → `workflows/risk-control-mapping.md`
4. Para transformações operacionais (SSC, GBS, carve-out) → `skills/operating-model-analysis.md` antes de mapear

---

### Preciso desenhar ou avaliar um teste de controle

1. Entenda o tipo do controle (preventivo/detectivo, manual/automatizado/IT-dependent) → `concepts/control-types-and-reliance.md`
2. Documente o controle de forma testável → `skills/control-documentation.md`
3. Defina o tamanho da amostra → `skills/sample-size-calculator.md`
4. Siga o workflow → `workflows/test-execution.md`

---

### Tenho um achado e preciso formalizá-lo

1. Redija com os 5 Cs → `workflows/finding-drafting.md`
2. Classifique a severidade → `workflows/finding-rating.md`
3. Questione o julgamento antes de fechar → `skills/challenge-reasoning.md`
4. Verifique DoD → `checklists/audit-artifacts-definition-of-done.md`

---

### Preciso entender um processo que o cliente descreveu em reunião

1. Carregue a transcrição → `workflows/transcript-analysis.md`
2. Gere fluxograma → `skills/process-flow-mermaid.md` ou `skills/process-flow-bpmn.md`
3. Compare com walkthrough anterior se existir → `workflows/walkthrough-standardization.md`

---

### Preciso avaliar o ambiente de controle da entidade

→ `processes/entity-level-controls.md` — cobre COSO P1–P5 com critérios de teste e red flags

---

### Preciso verificar conformidade contra uma norma

→ `modes/regulatory-check.md` — SOX, IIA IPPF, LGPD, ISO e outras

---

### Tenho narrativas de processo e preciso chegar a um plano de ação

Sequência completa narrativa → plano de ação:

1. Extraia o processo da narrativa → `workflows/transcript-analysis.md`
2. Gere fluxograma para validar entendimento → `skills/process-flow-mermaid.md`
3. Mapeie riscos, controles e testes → `workflows/risk-control-mapping.md`
   - Consulte WCGWs do processo → `context/wcgw-master.json` filtrando pelo `process_code`
4. Execute ou avalie os testes → `workflows/test-execution.md`
5. Formalize as observações como achados → `workflows/finding-drafting.md`
6. Classifique severidade → `workflows/finding-rating.md`
7. Plano de ação sai como parte do achado → `templates/output-achado-5c.md`

Se a narrativa vier de reunião gravada ou transcrição bruta, comece pelo passo 1. Se já tiver o processo mapeado, comece pelo passo 3.

---

### Venho de auditoria externa — o que é diferente aqui

**Mudança de postura central:** na externa, você parte de uma asserção e busca evidência para suportá-la. Na interna, você parte do processo e identifica onde o risco mora. A lógica é inversa.

**Conceitos que funcionam diferente:**

| Tema | Auditoria externa | Auditoria interna |
|---|---|---|
| Escopo | Definido pelas demonstrações financeiras e assertivas | Definido pelo risco do processo e objetivos da organização |
| Severidade | Material weakness / significant deficiency (impacto no DF) | Crítico / Alto / Moderado / Baixo (impacto no objetivo do processo) |
| WCGW | Ligado a assertivas PCAOB (existência, completude, acurácia) | Ligado ao objetivo do processo (eficiência, compliance, operação) |
| Controles IT | ITGC como suporte a controles de aplicação relevantes para DF | ITGC como risco próprio — acesso, mudança, operações de TI |
| Relato | Relatório do auditor independente para usuários externos | Relatório de achados para gestão e comitê de auditoria interno |

**Por onde começar:** leia `concepts/risk-scoring-foundations.md` e `processes/entity-level-controls.md`. São os dois conceitos que mais divergem da lógica de externa.

---

## Referência rápida — o que usar para cada artefato

| Artefato | Workflow principal | Template |
|---|---|---|
| Plano anual de auditoria | `modes/risk-assessment.md` | `scripts/generate_plano_anual_v2.py` |
| Matriz de avaliação de riscos | `workflows/audit-planning.md` | `scripts/generate_rcm_risco_v2.py` |
| RCM | `workflows/risk-control-mapping.md` | `scripts/generate_rcm_risco_v2.py` |
| Papel de teste | `workflows/test-execution.md` | `scripts/generate_papel_teste_v2.py` |
| Achado 5 Cs | `workflows/finding-drafting.md` | `templates/output-achado-5c.md` |
| Tracker de achados | `workflows/finding-rating.md` | `scripts/generate_tracker_achados_v2.py` |
| Follow-up de plano de ação | — | `scripts/generate_followup_pa_v2.py` |
| Walkthrough narrativo | `workflows/walkthrough-standardization.md` | `templates/output-walkthrough.md` |
| Política corporativa | — | `scripts/export_politica_docx.py` |
