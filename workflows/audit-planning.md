# workflow: audit-planning

## Goal

Definir escopo, riscos relevantes e programa de trabalho para um engagement de auditoria interna.

## Use When

- início de um trabalho novo
- necessidade de definir o que será testado e por quê
- priorização de riscos antes da execução
- solicitação de programa de trabalho por processo, área ou ciclo

> Para planejamento orientado a `ICFR`, `SOX`, `SCOT`, assertivas de DF ou caminho crítico até reporte financeiro, usar `_method-wiki-external-audit/workflows/audit-planning-external-audit.md`.

## Inputs

- processo, área ou tema em escopo
- objetivo do trabalho (`assurance` ou `consultoria`)
- contexto do cliente, setor ou regulação aplicável
- restrições de tempo, equipe ou acesso
- riscos conhecidos ou suspeitos, se houver
- perfil do cliente em `context/clients/*`, se existir

## Planning Sequence

### 1. Enquadrar o objetivo do trabalho

Definir antes de qualquer coisa:

- o trabalho é de **assurance** ou **consultoria**?
- qual critério será usado para avaliar? (política, procedimento, regulação, standard, SLA, meta operacional)
- qual o objetivo do processo auditado? operacional, compliance, financeiro, TI, governança?
- o que ficará explicitamente fora do escopo?

Sem critério e sem objetivo do processo, não há planejamento consistente.

### 2. Delimitar o processo e sua fronteira

Antes de descer para riscos, entender o processo em alto nível usando a lógica de auditoria interna:

- qual é o **gatilho** do processo?
- quais são as **4–7 etapas macro**?
- quem são os **atores / áreas** envolvidos?
- quais são os **inputs** críticos?
- qual é o **output** esperado?
- quem é o **customer / destinatário** do output?

Referência metodológica: `_method-wiki/concepts/process-mapping-internal-audit.md`.

Em auditoria interna, não usar `SCOT` como estrutura primária de leitura.

### 2.5. Carregar WCGWs da biblioteca e comparar com o processo

Antes de identificar riscos livres, verificar a biblioteca de WCGWs para o(s) processo(s) em escopo:

1. Consultar `context/wcgw-master.json` filtrando pelo `process_code` relevante
2. Para cada WCGW da biblioteca aplicável ao processo:
   - O risco já está mapeado nas etapas do processo?
   - Existe controle documentado que o mitiga?
   - O WCGW tem severidade alta (`high`)? Se sim, priorizar cobertura.
3. Registrar quais WCGWs da biblioteca foram incluídos no escopo e quais foram explicitamente excluídos (com justificativa)

> Usar `skills/wcgw-mapping.md` quando a tarefa exigir mapeamento mais aprofundado de WCGWs a partir de narrativa ou walkthrough.

**Por que fazer antes do Step 3:** a biblioteca de WCGWs representa riscos conhecidos e padronizados por processo. Identificar riscos sem verificar a biblioteca antes aumenta a probabilidade de gaps em riscos conhecidos. O Step 3 complementa — não substitui — a biblioteca.

### 3. Identificar riscos relevantes

Para cada etapa, objetivo ou interface do processo, perguntar:

- o que pode dar errado aqui?
- o risco é de erro, fraude, não conformidade, falha operacional, falha sistêmica, terceiro ou governança?
- qual objetivo do processo seria afetado?
- o problema afeta prazo, qualidade, integridade, segurança, continuidade, compliance ou custo?

Priorizar riscos com base em:

- **Impacto**: financeiro, operacional, regulatório, reputacional, informacional
- **Probabilidade**: histórico de falhas, complexidade do processo, dependência de pessoa, fragilidade de handoff, grau de automação

Quando necessário, usar `skills/risk-scoring.md` para calibrar a leitura de risco inerente.

### 4. Identificar controles existentes e lacunas

Para cada risco relevante:

- existe controle mapeado?
- o controle é preventivo ou detectivo?
- é manual, automatizado ou híbrido?
- quem opera e com que frequência?
- qual evidência de execução se espera encontrar?

Se não houver controle mapeado, registrar explicitamente como **lacuna de controle**.

### 5. Definir a abordagem de teste

Para cada controle ou risco selecionado:

- vale testar **ToD**, **ToE** ou ambos?
- qual a natureza do teste faz mais sentido: inspeção, observação, reperformance, entrevista, walkthrough, análise documental ou analítica?
- qual nível de profundidade é compatível com o risco?
- a cobertura será ampla ou focada em poucos riscos materiais?

Princípio central: **estar em escopo não significa teste extensivo**. A extensão do teste deve ser calibrada pelo risco inerente e pela criticidade do objetivo do processo.

### 6. Montar o programa de trabalho

Estrutura mínima por item:

| Objetivo de Auditoria | Processo / Etapa | Risco | Controle / Lacuna | Tipo de Teste | Procedimento | Responsável |
|---|---|---|---|---|---|---|

### 7. Explicitar exclusões e trade-offs

Registrar:

- o que ficou fora do escopo
- por que ficou fora
- quais dependências ou limitações podem reduzir a profundidade do trabalho
- quais riscos serão apenas monitorados, e não testados extensivamente

## Decision Rules

- não testar o que não está ligado a um risco relevante ou objetivo do processo
- não pular a etapa de definição de critério
- não usar controles assumidos como justificativa para baixar escopo sem evidência
- priorizar profundidade em poucos riscos relevantes a superficialidade em muitos
- registrar explicitamente o que ficou fora do escopo e por quê
- quando houver dúvida entre lógica interna e externa, manter o foco no objetivo do processo, não no caminho até DF

## Output

- objetivo, critério e escopo definidos
- delimitação do processo e sua fronteira
- riscos relevantes priorizados
- controles e lacunas por risco
- programa de trabalho com procedimentos e responsáveis
- fora de escopo e justificativa

## Output Format

1. objetivo e enquadramento do trabalho
2. processo em alto nível (`gatilho`, etapas, inputs, output, customer)
3. riscos relevantes identificados
4. controles e lacunas por risco
5. programa de trabalho (tabela)
6. fora do escopo, limitações e justificativas
