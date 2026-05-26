# Audit Artifacts - Definition of Done

## Papel

Checklist de critério de pronto para os artefatos centrais de auditoria interna:

- walkthrough
- RCM (risk-control matrix)
- papel de teste de controle
- achado
- plano de ação

## Quando usar

- antes de encerrar uma entrega de workflow
- antes de submeter material para revisão técnica
- antes de comunicar achado para gestão
- no fechamento do engagement para evitar "feito, mas incompleto"

## Objetivo

Definir corte de qualidade mínimo para considerar um artefato concluído, reduzindo retrabalho, ambiguidade e conclusões sem evidência suficiente.

## Regra de Corte

Um artefato está `done` somente quando:

1. tem rastreabilidade entre critério, evidência e conclusão
2. consegue ser entendido por terceiro sem explicação oral adicional
3. permite revisão técnica objetiva (sem depender de inferência do revisor)

Se qualquer item crítico abaixo não estiver atendido, o status é `em revisão`, não `concluído`.

## 1) DoD - Walkthrough

- [ ] processo, fronteira e objetivo estão explicitados
- [ ] etapas estão em sequência operacional clara (início -> processamento -> saída)
- [ ] riscos e controles citados estão vinculados a etapa específica
- [ ] gatilho, executor e evidência esperada dos controles foram descritos
- [ ] sistemas, relatórios e interfaces críticas foram identificados
- [ ] lacunas de informação foram marcadas como lacuna (não como fato)
- [ ] há referência à fonte usada (reunião, documento, transcrição, WP)

## 2) DoD - RCM (Risk-Control Matrix)

- [ ] risco possui descrição objetiva de evento, causa e impacto
- [ ] controle está ligado ao risco correto (sem controle "solto")
- [ ] tipo de controle, frequência e owner estão explicitados
- [ ] evidência requerida para teste está definida
- [ ] critério de falha do controle está explícito
- [ ] status de desenho e operação não está misturado
- [ ] riscos sem controle ou controles sem risco foram tratados como exceção explícita

## 3) DoD - Papel de Teste de Controle

- [ ] objetivo do teste e critério de aprovação/reprovação estão claros
- [ ] população, período e lógica de seleção da amostra estão documentados
- [ ] procedimento executado está descrito em nível reproduzível
- [ ] evidência obtida está anexada ou referenciada de forma rastreável
- [ ] resultado por item testado está registrado (aprovado/exceção)
- [ ] exceções estão avaliadas quanto a causa, impacto e extensão
- [ ] conclusão final conecta resultado observado ao risco coberto

## 4) DoD - Achado

- [ ] os 5 Cs estão completos (critério, condição, causa, consequência, corretiva)
- [ ] critério técnico é verificável (norma/política/procedimento aplicável)
- [ ] condição descreve fato observado, não opinião
- [ ] causa e consequência estão coerentes com as evidências
- [ ] severidade possui racional documentado (impacto x probabilidade)
- [ ] recomendação é acionável (quem faz o quê, em que prazo)
- [ ] não há afirmação conclusiva sem base evidencial

## 5) DoD - Plano de Ação

- [ ] owner nomeado (responsável único pela entrega)
- [ ] ação específica (verbo de execução, sem generalidade)
- [ ] prazo definido com data
- [ ] critério de conclusão verificável (como comprovar implementação)
- [ ] dependência/risco de execução mapeado quando relevante
- [ ] status em linha com `states.yml`
- [ ] evidências de implementação previstas (ou anexadas, se concluído)
- [ ] tipo de ação classificado: Pontual / Estrutural / Roadmap
- [ ] para ações Roadmap: dependência externa identificada e controle compensatório documentado para o período de espera

## Gates de Revisão Final

- [ ] fato, inferência e lacuna estão separados com clareza
- [ ] linguagem técnica está objetiva (sem inflar severidade)
- [ ] referências internas estão válidas (links/arquivos citados)
- [ ] material permite handoff sem perda de contexto

## Rubric de Qualidade

A DoD define o corte mínimo — done vs. em revisão. A rubric define gradação: o artefato está no mínimo ou está forte? Usar após a DoD quando o artefato vai para revisão externa, comunicação com gestão ou serve de referência futura.

Escala: **Fraco** (passa a DoD mas abaixo do esperado) / **Adequado** (padrão aceitável para uso) / **Forte** (referência de qualidade).

### Walkthrough

| Dimensão | Fraco | Adequado | Forte |
|---|---|---|---|
| **Cobertura do processo** | Etapas descritas em alto nível, sem detalhamento de exceções | Fluxo principal coberto com gatilhos e executores | Fluxo principal + exceções + pontos de integração entre sistemas |
| **Vínculo risco-controle** | Riscos e controles listados sem conexão à etapa | Cada controle vinculado à etapa e ao risco que mitiga | Vínculo + critério de falha + evidência esperada por controle |
| **Rastreabilidade de fonte** | "Baseado em reunião com área" | Reunião datada com participante identificado | Transcrição ou ata referenciada + documentos complementares revisados |
| **Tratamento de lacunas** | Lacunas não sinalizadas ou preenchidas com suposição | Lacunas marcadas explicitamente no texto | Lacunas marcadas + próxima ação definida para obter a informação |

### RCM

| Dimensão | Fraco | Adequado | Forte |
|---|---|---|---|
| **Descrição do risco** | Risco genérico ("erro no processo") | Evento + causa + impacto descritos separadamente | Evento + causa + impacto + WCGW de referência vinculado |
| **Especificidade do controle** | "Aprovação gerencial" sem detalhe | Controle com gatilho, executor, frequência e evidência | Acima + critério de falha explícito + tipo (preventivo/detectivo/manual/automatizado) |
| **Cobertura de assertivas** | Assertivas não explicitadas | Assertiva principal mapeada por risco | Todas as assertivas relevantes cobertas; gaps justificados |
| **Completude SoD** | SoD não avaliada | Conflitos críticos identificados | Conflitos + verificação contra `sod-master.json` + controle compensatório quando aplicável |

### Papel de Teste de Controle

| Dimensão | Fraco | Adequado | Forte |
|---|---|---|---|
| **Definição de amostra** | N definido sem parâmetros documentados | N com confiança, tolerável e tipo de controle registrados | Acima + população validada via `ipe-validation-before-test.md` + fonte da extração |
| **Reprodutibilidade do procedimento** | Passos descritos em nível que exige interpretação | Passos reproduzíveis por auditor diferente sem esclarecimentos | Passos + screenshots ou evidências inline + critério de avaliação por item |
| **Avaliação de exceções** | Exceções listadas sem análise de causa ou impacto | Causa e impacto de cada exceção documentados | Causa + extensão + Charts 1–4 aplicados + Prudent Official Test registrado |
| **Conexão ao risco** | Conclusão do teste não conecta ao risco coberto | Conclusão referencia o risco e a assertiva testada | Conclusão + implicação para reliance e risco residual |

### Achado (5 Cs)

| Dimensão | Fraco | Adequado | Forte |
|---|---|---|---|
| **Critério** | "Política interna" sem especificação | Norma ou política citada com seção aplicável | Norma + parágrafo + versão vigente + contexto de aplicação ao cliente |
| **Condição** | Descreve o processo, não o desvio | Descreve o desvio observado com base em evidência | Desvio + frequência observada na amostra + upper limit se aplicável |
| **Causa** | "Falta de controle" ou "falha humana" | Causa raiz identificada e verificada | Causa raiz + fator sistêmico que explica persistência + se é desenho ou operação |
| **Consequência** | Risco genérico sem quantificação | Impacto estimado com base em exposição bruta | Impacto + probabilidade documentada + precedente ou dado empírico de suporte; se Fraude: Fraud Triangle documentado com vértices confirmados e lacunas sinalizadas |
| **Corretiva** | "Melhorar o processo" | Ação específica com owner e prazo | Ação + prazo + critério de verificação de implementação + tipo (Pontual/Estrutural/Roadmap) + dependência mapeada |
| **Rating** | Severidade sem racional | Severidade com impacto × probabilidade documentados | Acima + Prudent Official Test aplicado + agregação com outros achados verificada |

---

> **Como usar:** após confirmar todos os checkboxes da DoD, percorrer as dimensões relevantes da rubric e identificar onde o artefato está Fraco ou Adequado. Iterar apenas nas dimensões que têm impacto direto no uso do artefato — não transformar toda entrega em exercício de maximização de score.

## Artefatos Relacionados

- `checklists/control-attribute-design.md`
- `patterns/evidence-conclusion-linkage.md`
- `patterns/control-deficiency-severity.md`
- `processes/update-testing-and-control-exceptions.md`
