# internal-audit-ops

Produto/agente para trabalhos técnicos de auditoria interna.

## Papel

Transformar insumos brutos de auditoria em artefatos claros, rastreáveis e revisáveis:

- planejamento de auditoria
- mapeamento de riscos, controles e testes
- adoção responsável de IA em rotinas de auditoria
- análise de transcrições e walkthroughs
- análise contábil de contratos e arrendamentos
- execução e documentação de testes
- redação e classificação de achados

## Entrada Principal

Use `CLAUDE.md` como porta de entrada operacional.

## Fontes de Verdade e Ordem de Consulta

1. `CLAUDE.md` (roteamento, guardrails e regra de contexto)
2. `domain.md` (vocabulário técnico e fundamentos)
3. `_method-wiki/index.md` e `_method-wiki/README.md` (índice e estrutura metodológica)
4. `_method-wiki/processes|patterns|checklists|concepts|heuristics/` (base canônica)
5. `workflows/` (sequência operacional da trilha de auditoria interna)
6. `skills/` (transformações auxiliares atômicas)
7. `context/clients/` e `context/wcgw/` (calibração por cliente/processo)
8. `playbooks/` (repertório por segmento/tema)
9. `examples/` (calibradores de entrada/saída)
10. backlog e roadmap: consultar a trilha local de backlog quando precisar de prioridades e evolução.

## Governanca de Fonte Viva

Regra operacional para evitar "adivinhação" e drift de contexto:

- fonte viva do agente: `CLAUDE.md`, `domain.md`, `workflows/`, `skills/`, `context/` e `_method-wiki/`
- `archive/docs/` é trilha histórica de design/planejamento e não substitui fonte operacional
- quando um conteúdo dessa trilha amadurecer, promover para a camada viva correspondente:
  - método estável de auditoria interna → `_method-wiki/`
  - sequência operacional de auditoria interna → `workflows/`
  - transformação atômica → `skills/`
  - memória de cliente/projeto → `context/`

## Estrutura do Produto

- `CLAUDE.md`: router operacional do agente.
- `README.md`: mapa rápido de uso e estrutura.
- `domain.md`: conhecimento técnico estável.
- `DATA_CONTRACT.md`: fronteira `User Layer` vs `System Layer`.
- `states.yml`: estados canônicos de engagement, área, achado e plano de ação.
- `_method-wiki/`: base metodológica canônica de auditoria interna.
- `workflows/`: fluxos operacionais da trilha principal de auditoria interna.
- `skills/`: capacidades auxiliares.
- `playbooks/`: repertório aplicado por contexto.
- `books/`: fontes de referência e trilhas de destilação para auditoria interna.
- `context/`: contexto por cliente, WCGW e listas mestras.
- `examples/`: exemplos calibradores.
- `templates/`: artefatos de apoio reaproveitáveis.
- `scripts/`: utilitários locais (inclui health check).
- `archive/docs/`: specs e planos arquivados de evolução.
- `archive/`: legado ou material despriorizado.

## Workflows Ativos

### Trilha de auditoria interna

- `workflows/audit-planning.md`: escopo, riscos e programa de trabalho.
- `workflows/risk-control-mapping.md`: processo, riscos, controles e testes.
- `workflows/test-execution.md`: desenho e avaliação de testes de controle.
- `workflows/walkthrough-standardization.md`: padronização e refinamento comparativo de walkthrough.
- `workflows/transcript-analysis.md`: análise de transcrição de reunião ou walkthrough.
- `workflows/finding-drafting.md`: redação de achados com base nos 5 Cs.
- `workflows/finding-rating.md`: classificação de severidade de achados.

## Skills Ativas

- `skills/client-context.md`
- `skills/process-flow-bpmn.md`
- `skills/process-flow-mermaid.md`
- `skills/audit-dashboard-visualization.md`
- `skills/operating-model-analysis.md`
- `skills/wcgw-mapping.md`
- `skills/control-documentation.md`
- `skills/control-evaluation.md`
- `skills/risk-scoring.md`
- `skills/challenge-reasoning.md`

## Exemplos Disponíveis

- `examples/internal-audit-role.md` — calibrador de auditoria interna
- `examples/operating-model-analysis-ssc.md` — calibrador de auditoria interna
- `examples/transcript-analysis-itgc-erp.md` — exemplo interno de transcript analysis em contexto de ERP / ITGC
- `examples/transcript-analysis-walkthrough-ap.md` — exemplo interno de transcript analysis para walkthrough de processo
## Health Check

Rodar validação de integridade local:

```bash
python3 scripts/doctor.py
```

Para incluir validação de links em `archive/docs/` quando essa trilha existir (opcional):

```bash
python3 scripts/doctor.py --include-docs
```

Para bloquear também warnings:

```bash
python3 scripts/doctor.py --strict
```

Para exibir resumo por seção:

```bash
python3 scripts/doctor.py --report
```

Hoje o doctor valida:

- arquivos essenciais
- workflows referenciados no `CLAUDE.md`
- skills obrigatórias
- estrutura mínima da `_method-wiki`
- `states.yml`
- `DATA_CONTRACT.md`
- perfil de cliente de exemplo e referências locais em `context/clients/`
- severidade de resultados (`erro` e `warning`)
- consistência entre referências do `CLAUDE.md` e arquivos reais

Observação:

- `archive/docs/` é tratada como camada de apoio/histórico e não bloqueia o health check por padrão.
- em `--strict`, warnings passam a bloquear o resultado final.

## Guardrails

- Não inventar etapa, controle, risco ou aprovação sem base no insumo.
- Não transformar hipótese em fato.
- Não citar norma ou critério não verificável.
- Não inflar severidade para deixar a saída mais forte.
- Separar fato, inferência e lacuna.
- Se faltar evidência, sinalizar lacuna explicitamente.
- Em caso de ambiguidade, pedir o mínimo de contexto faltante antes de concluir.

## Fonte Oficial

`Agent Products/internal-audit-ops-public/`
