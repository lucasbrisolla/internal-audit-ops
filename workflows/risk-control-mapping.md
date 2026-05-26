# workflow: risk-control-mapping

## Goal

Construir uma Risk Control Matrix (RCM) para auditoria interna a partir da descrição de um processo: mapear atividades -> riscos -> controles -> testes sugeridos.

## Use When

- há um processo descrito e precisa-se estruturar riscos e controles
- a equipe precisa de uma RCM como base para o programa de trabalho
- o objetivo é identificar lacunas de controle em processo operacional, compliance ou financeiro
- revisão ou atualização de uma RCM existente

> Para mapeamento com lógica primária de `SCOT`, `assertions`, `ICFR`, `SOX` ou `WCGW` orientado a reporte financeiro, usar `_method-wiki-external-audit/workflows/risk-control-mapping-external-audit.md`.

## Inputs

- descrição do processo (walkthrough, transcrição ou texto descritivo)
- objetivo do processo e critérios de sucesso
- controles já conhecidos, se houver
- contexto do cliente, setor ou regulação aplicável

## Mapping Sequence

### 1. Mapear atividades por responsável

Usar `skills/wcgw-mapping.md` — Step 2 (Mapa de Atividades por Responsável).

Decompor o processo em atividades concretas por área, sistema, input e output. Cada atividade com ponto de controle esperado é uma linha potencial da RCM.

Em auditoria interna, não usar `SCOT` como estrutura primária. Priorizar:

- objetivo do processo
- fronteira
- atores / áreas
- entradas e saídas
- interfaces críticas

### 2. Identificar riscos relevantes por atividade

Para cada atividade mapeada, perguntar:

- o que pode dar errado aqui?
- o risco é de erro, fraude, não conformidade, falha operacional, falha sistêmica ou terceiro?
- qual seria o impacto no objetivo do processo?
- o problema afeta qualidade, prazo, integridade, segurança, continuidade ou compliance?

Se útil, consultar `context/wcgw-master.json` como referência calibradora, sem copiar mecanicamente.

### 3. Documentar e avaliar controles

Para cada risco:

- existe controle preventivo ou detectivo mapeado?
- se sim: expandir com `skills/control-documentation.md`
- avaliar qualidade com `skills/control-evaluation.md`
- se não houver controle: registrar como **lacuna de controle**

**ToD e ToE — uso em auditoria interna:**
- **ToD:** o controle, se operado como desenhado, mitigaria o risco?
- **ToE:** o controle está sendo executado com consistência e evidência suficiente?

### 4. Pontuar risco inerente e residual

Usar `skills/risk-scoring.md`:

- calibrar impacto e probabilidade
- calcular risco inerente
- derivar risco residual com base na qualidade do controle

### 5. Montar a RCM

| Cód. | Atividade | Risco | Objetivo Afetado | Controle | Tipo | Owner | Score Ctrl | Resultado Ctrl | Impacto | Prob | RI | RR | Ação |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

Status de controle: **Mapeado** / **Lacuna** / **A confirmar**

Ação de RR: **Monitorar** / **Recomendar melhoria** / **Achado formal** / **Achado prioritário**

## Decision Rules

- um risco sem controle mapeado é uma lacuna — registrar explicitamente
- não criar controles que "deveriam existir"
- um controle pode mitigar mais de um risco
- priorizar riscos com impacto relevante para o objetivo do processo
- se o processo não estiver claro o suficiente, sinalizar o que falta antes de avançar
- se o cliente passou por troca de sistema nos últimos 12 meses, consultar `processes/erp-transition-and-control-remediation.md` antes de classificar riscos — distinguir risco estrutural do processo de risco de transição; tratar como risco operacional comum gera recomendação errada

## Gate de Pronto (DoD)

Antes de considerar a RCM concluída, validar:

- `_method-wiki/checklists/audit-artifacts-definition-of-done.md` -> seção `1) DoD - Walkthrough`
- `_method-wiki/checklists/audit-artifacts-definition-of-done.md` -> seção `2) DoD - RCM (Risk-Control Matrix)`
- `_method-wiki/checklists/audit-artifacts-definition-of-done.md` -> seção `Gates de Revisão Final`
- registrar decisão de gate no template: `templates/revisao-dod-artefato.md`

## Output

- RCM completa com riscos, controles e status
- lacunas de controle identificadas
- sugestão de foco para o programa de trabalho com base nos riscos sem cobertura

## Output Format

1. leitura do processo e objetivo de controle
2. RCM (tabela)
3. lacunas identificadas
4. priorização sugerida para testes
