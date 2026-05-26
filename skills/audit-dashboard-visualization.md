---
name: audit-dashboard-visualization
description: Use when audit data, RCMs, findings, testing status, exceptions, risks, controls, or evidence need a chart, dashboard, visual story, or committee-ready view.
---

# audit-dashboard-visualization

## Propósito

Escolher a forma visual mais clara para evidência de auditoria. O objetivo não é tornar gráficos decorativos; é tornar risco, status, exceções e decisões mais fáceis de entender.

## Quando Usar

- o usuário pergunta qual gráfico ou dashboard usar
- achados, RCMs, status de testes, exceções, evidências ou ratings de risco precisam de resumo visual
- comitê, gestor, cliente ou revisor precisa da mensagem rapidamente
- os dados têm categorias, períodos, responsáveis, ratings, etapas ou passos de processo

## Insumos

Perguntar ou inferir:

- objetivo: qual mensagem o visual deve comunicar?
- audiência: auditor, gestor, comitê, cliente, CoE, dono do processo
- estrutura dos dados: categorias, série temporal, distribuição, relação, processo, hierarquia, tabela
- unidade de análise: achado, controle, risco, teste, entidade, área, responsável, período
- decisão necessária: monitorar, priorizar, escalar, comparar, explicar, evidenciar

## Seleção de Gráfico

| Objetivo | Visual Recomendado |
|---|---|
| Comparar áreas, responsáveis, entidades ou categorias | Gráfico de barras, ordem decrescente |
| Mostrar progresso por área de auditoria ou status de teste | Barra empilhada, heatmap, tabela de status |
| Mostrar cobertura de risco/controle | Heatmap ou matriz de RCM |
| Mostrar severidade de achados | Heatmap, matriz de bolhas, barra ordenada |
| Mostrar tendência ao longo do tempo | Gráfico de linha ou slope chart |
| Mostrar aging de itens abertos | Faixas de aging, histograma, barra empilhada |
| Mostrar fluxo de processo | Mermaid/mapa de processo, não gráfico |
| Mostrar composição de um todo | Barra empilhada; evitar pizza salvo poucas categorias |
| Mostrar exceções por causa raiz | Gráfico de Pareto |
| Mostrar trilha de evidências ou dependência | Fluxograma, linha do tempo ou swimlane |

## Padrões Específicos de Auditoria

### Visão RCM

Usar quando mostrar cobertura processo → risco → controle.

Colunas recomendadas:

| Processo | Risco | Controle | Design | Efetividade | Severidade | Status |

Melhor visual: heatmap ou matriz, não gráfico denso.

### Visão de Achados

Usar quando resumir questões em aberto.

Dimensões recomendadas:

- severidade
- responsável
- aging
- área de negócio
- causa raiz
- status do plano de ação

Melhor visual: barra ordenada para prioridade, heatmap para concentração, gráfico de aging para atrasos.

### Visão de Status de Testes

Usar quando reportar progresso de execução.

Dimensões recomendadas:

- área
- status 0→1
- status de seleção
- evidências pendentes
- status do revisor

Melhor visual: barra empilhada mais tabela de exceções.

### Narrativa de Evidência

Usar quando um achado precisa ser explicado.

Estrutura recomendada:

1. critério
2. condição
3. evidência
4. risco
5. ação

Melhor visual: cadeia de evidências em uma página, não dashboard.

## Formato de Saída

1. **Visual recomendado:** nome do gráfico/dashboard/visão
2. **Mensagem que ele deve comunicar:** uma frase
3. **Por que funciona:** razão curta ligada ao objetivo de auditoria
4. **Dados necessários:** campos requeridos
5. **Alternativa viável:** segunda melhor opção e quando preferi-la
6. **Dica de storytelling:** orientação prática de formatação ou sequenciamento

## Guardrails

- Não recomendar visuais antes de identificar a mensagem.
- Não usar gráfico de pizza para comparações precisas.
- Não esconder exceções dentro de números agregados.
- Não misturar dimensões demais em um único gráfico.
- Não polir visuais além do que a evidência suporta.
- Se a qualidade dos dados for fraca, indicar o que deve ser reconciliado antes da visualização.
