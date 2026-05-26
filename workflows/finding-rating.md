# workflow: finding-rating

## Goal

Classificar a severidade de um achado de auditoria interna com base em impacto, probabilidade, exposição residual e necessidade de atenção da gestão.

## Use When

- um achado já foi redigido e precisa ser priorizado
- é preciso justificar a ordem de tratamento no relatório
- a gestão questiona a severidade e é necessário mostrar o racional

> Para lógica ICFR / SOX com `material weakness`, `significant deficiency` e foco em distorção relevante, usar `_method-wiki-external-audit/workflows/finding-rating-external-audit.md`.

## Inputs

- achado redigido (idealmente via `finding-drafting`)
- consequência avaliada (financeiro, operacional, regulatório, reputacional)
- frequência ou sistematicidade do desvio
- existência de controles compensatórios
- contexto de risco do processo e do ambiente de controle

## Rating Scale

### Crítico

Exposição severa, atual ou iminente, com necessidade de ação imediata da gestão.

Indicadores:
- risco elevado de perda, fraude, não conformidade grave ou paralisação relevante
- ausência de controle em risco central do processo
- falha sistêmica com alta chance de recorrência
- repercussão regulatória ou reputacional significativa

### Alto

Exposição relevante, com necessidade de tratamento no curto prazo.

Indicadores:
- controle-chave inefetivo em processo importante
- desvio sistemático ou recorrente
- lacuna de segregação de funções ou governança sem compensação confiável
- impacto operacional, financeiro ou de compliance significativo se não corrigido

### Médio

Exposição moderada, com ação necessária, mas sem urgência imediata.

Indicadores:
- exceções pontuais em controle geralmente efetivo
- falha com impacto limitado e mitigação parcial
- dependência excessiva de pessoa ou rotina manual sem automação, em processo de risco intermediário
- oportunidade de melhoria com risco real, mas contido

### Baixo

Exposição limitada, com foco em melhoria ou disciplina operacional.

Indicadores:
- falha administrativa ou documental sem impacto relevante
- desvio isolado sem evidência de recorrência
- melhoria de eficiência ou padronização sem lacuna material de controle

## Rating Sequence

### 1. Avaliar impacto

- Se o risco se materializar, qual seria o impacto máximo plausível?
- O impacto é financeiro, operacional, regulatório, reputacional ou de informação?
- O impacto já ocorreu ou ainda é potencial?

### 2. Avaliar probabilidade / recorrência

- A falha foi pontual, repetitiva ou estrutural?
- Há sinais de recorrência em outras áreas, períodos ou amostras?
- O desenho do processo favorece repetição do problema?

### 3. Avaliar cobertura residual

- Existe controle compensatório ou mecanismo de monitoramento confiável?
- A gestão percebe o problema a tempo de reagir?
- O risco residual permanece alto mesmo após a compensação?

### 4. Definir o rating

Combinar impacto + probabilidade + cobertura residual:

| Impacto \ Probabilidade | Alta | Média | Baixa |
|---|---|---|---|
| **Alto** | Crítico | Alto | Médio |
| **Médio** | Alto | Médio | Baixo |
| **Baixo** | Médio | Baixo | Baixo |

Se a cobertura residual for fraca ou inexistente, considerar elevar um nível.
Se houver compensação forte, tempestiva e comprovada, considerar reduzir um nível.

### 5. Aplicar Prudent Official Test (obrigatório para Crítico ou Alto)

> Um profissional prudente com o mesmo conhecimento dos fatos, sem viés de confirmação, classificaria este achado da mesma forma?

- Se sim: rating confirmado.
- Se elevaria: justificar por que o rating atual é defensável ou corrigir.
- Se rebaixaria: verificar se há pressão da gestão ou evidência insuficiente como causa.

Ref.: `_method-wiki/patterns/control-deficiency-severity.md`

### 6. Verificar agregação de deficiências

Se houver outros achados no mesmo engagement:

- Estão no mesmo componente COSO (ex: P10 — Atividades de Controle)?
- Estão no mesmo processo ou subprocesso?
- A combinação cria exposição maior do que cada achado individual?

Se sim: avaliar se a severidade agregada eleva algum dos achados. Registrar conclusão na seção de Rating de cada achado afetado.

Ref.: `_method-wiki/patterns/control-deficiency-severity.md`

### 7. Verificar Fraud Triangle (obrigatório se tipo de risco incluir Fraude)

Antes de fechar o rating, confirmar que a análise de Fraud Triangle está documentada na seção Consequência do achado:

- Oportunidade identificada ou descartada com base em evidência?
- Motivação/Pressão e Racionalização: confirmadas, descartadas ou sinalizadas como lacuna?

Rating Crítico com tipo Fraude exige ao menos o vértice de Oportunidade documentado. Vértices não investigados = lacuna explícita, não ausência de risco.

### 8. Documentar a justificativa

Registrar:

- por que o impacto foi classificado como alto / médio / baixo
- por que a probabilidade foi classificada como alta / média / baixa
- se existe mitigação residual e qual o efeito na severidade
- resultado do Prudent Official Test (se aplicável)
- conclusão sobre agregação (se aplicável)

## Decision Rules

- não rebaixar rating por pressão da gestão; reavaliar apenas com fatos novos
- não elevar severidade além do que a evidência suporta
- `Crítico` deve ser raro e defensável
- controle compensatório só reduz severity se for real, confiável e verificável
- em caso de incerteza, usar o pior cenário plausível, não o cenário mais favorável

## Output

- rating final com classificação (`Crítico` / `Alto` / `Médio` / `Baixo`)
- justificativa de impacto
- justificativa de probabilidade
- nota sobre cobertura residual ou controles compensatórios

## Output Format

**Rating**: [Crítico / Alto / Médio / Baixo]

**Justificativa de impacto**: [...]
**Justificativa de probabilidade**: [...]
**Cobertura residual / controles compensatórios**: [Sim — descrição e efeito no rating / Não]
**Prudent Official Test**: [Confirmado / Elevaria / Rebaixaria — justificativa]
**Agregação**: [Não aplicável / Aplicável — achados relacionados e efeito no rating]
**Fraud Triangle**: [N/A / Oportunidade: ___ | Motivação: ___ | Racionalização: ___ | Lacunas: ___]

**Conclusão**: [1 frase resumindo por que o rating é esse]
