# Checklist — Gate de Agregação de Deficiências

## Papel

Gate de revisão obrigatório antes de fechar o relatório de deficiências. Garante que deficiências individuais menores sejam avaliadas em conjunto — evitando que achados relacionados sejam reportados como múltiplos leves quando deveriam ser um único moderado ou severo.

## Quando usar

- Após classificar individualmente cada deficiência com `finding-rating.md`
- Antes de finalizar o relatório ou comunicar ao comitê de auditoria
- Sempre que houver 2 ou mais deficiências no mesmo engagement

## Resultado possível

- **Sem necessidade de reclassificação**: deficiências são independentes — reportar individualmente
- **Reclassificação necessária**: deficiências relacionadas constituem severidade maior quando agregadas — ajustar antes de reportar

---

## Parte 1 — Concentração por Área

- [ ] **Mesma conta ou processo**: há 2 ou mais deficiências afetando a mesma conta contábil, processo ou ciclo?
  - Se sim → avaliar se o conjunto constitui controle pervasivamente frágil naquela área
- [ ] **Mesma asserção**: há 2 ou mais deficiências afetando a mesma asserção (Occurrence, Completeness, Valuation, etc.)?
  - Se sim → avaliar se o conjunto prejudica a capacidade de reportar aquela asserção com confiabilidade
- [ ] **Mesmo componente COSO**: há 2 ou mais deficiências no mesmo componente COSO (Ambiente de Controle, Avaliação de Risco, Atividades de Controle, I&C, Monitoramento)?
  - Se sim → avaliar se o componente está funcionalmente comprometido como um todo

## Parte 2 — Relações Causais e de Princípio

- [ ] **Root cause compartilhado**: 2 ou mais deficiências têm a mesma causa-raiz (ex: ausência de política, lacuna de treinamento, falha sistêmica)?
  - Se sim → agrupar e reportar como deficiência única com causa estrutural; não reportar separado
- [ ] **Princípio COSO em cadeia**: deficiência em um Princípio agrava ou habilita deficiência em outro Princípio?
  - Exemplo: P11 (ITGC fraco) → P12 (controles de aplicação comprometidos)
  - Se sim → registrar relação explicitamente no Deficiency Summary e avaliar severidade do conjunto
- [ ] **ITGC com impacto em controles de aplicação**: há deficiência em ITGC e deficiência relacionada em controle transacional dependente?
  - Se sim → Chart 3 — severidade do ITGC sobe conforme severidade do controle de aplicação afetado

## Parte 3 — "Death by a Thousand Cuts"

- [ ] **Volume de exceções leves concentradas**: há 3 ou mais deficiências individuais leves (Deficiency) na mesma área ou processo?
  - Se sim → aplicar Prudent Official Test: um profissional prudente leria esse conjunto como aceitável ou como evidência de ambiente de controle frágil?
- [ ] **SDs múltiplas no mesmo componente**: há 2 ou mais Significant Deficiencies no mesmo componente COSO?
  - Se sim → avaliar se coletivamente constituem Material Weakness (MW)

## Parte 4 — Prudent Official Test Final

Antes de fechar a avaliação:

- [ ] **Teste de realidade**: leia todas as deficiências juntas como um bloco. A conclusão final (conjunto de severidades individuais) ainda faz sentido para um profissional prudente com o mesmo conhecimento dos fatos?
  - Se não → reclassificar o conjunto antes de reportar
- [ ] **Ausência de evidência ≠ ausência de problema**: há deficiências em áreas onde os testes foram limitados? Se sim, sinalizar explicitamente que a avaliação de severidade está condicionada à extensão dos testes realizados

---

## Documentação Mínima

Registrar no Deficiency Summary:

- [ ] Deficiências reclassificadas após gate de agregação (com justificativa)
- [ ] Relações entre princípios identificadas (ex: "P11 agrava P12 — ver CED-1.1 e CAD-3.2")
- [ ] Grupos de deficiências com root cause compartilhado (ex: "CED-1.1, CED-1.2 e CED-1.3 derivam da ausência de política X")
- [ ] Resultado do Prudent Official Test (confirmado / ajustado — com narrativa de 1–2 linhas)

---

## Sinais de Alerta

- Múltiplos achados em P2P com root cause "ausência de aprovação formal" → provavelmente um único achado de controle de autorização
- Deficiência em acesso (UAM) + deficiência em journal entry → avaliar se ITGC fraco é a causa de ambos
- 4 Deficiencies em processos diferentes, todas sobre "documentação insuficiente" → avaliar se é falha pervasiva de cultura de documentação (componente COSO: Ambiente de Controle / P4)

---

## Conexões Internas

- `_method-wiki/patterns/control-deficiency-severity.md` — Charts 1–4, regras de agregação, Prudent Official Test e campos do Deficiency Summary
- `workflows/finding-rating.md` — classificação individual de cada deficiência (executar antes deste gate)
- `workflows/finding-drafting.md` — redação do achado; revisar após reclassificação por agregação
- `_method-wiki/checklists/audit-artifacts-definition-of-done.md` — DoD do relatório final
