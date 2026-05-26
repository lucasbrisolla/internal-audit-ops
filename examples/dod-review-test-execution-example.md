# Exemplo - Revisão DoD (Papel de Teste de Controle)

## Identificação

- **Data:** 2026-04-24
- **Cliente / Engagement:** Exemplo S.A. - Q2/2026
- **Workflow:** `test-execution`
- **Artefato avaliado:** papel de teste de controle
- **Responsável pela elaboração:** Auditor Interno A
- **Responsável pela revisão:** Revisor Técnico B

## Referência de Critério

- **Checklist-base:** `_method-wiki/checklists/audit-artifacts-definition-of-done.md`
- **Seção aplicada:** `3) DoD - Papel de Teste de Controle` + `Gates de Revisão Final`

## Resultado da Revisão DoD (rodada 1)

### Itens críticos atendidos

- [ ] Sim
- [x] Não

### Pendências críticas identificadas

1. População e lógica de seleção da amostra não estavam documentadas.
2. Evidências de 2 itens da amostra não tinham referência rastreável.
3. Conclusão não conectava explicitamente o resultado ao risco coberto.

### Ajustes requeridos

1. Incluir base de população, recorte temporal e critério de amostragem.
2. Referenciar evidência por item testado (arquivo, aba, linha ou log).
3. Reescrever a conclusão final com vínculo direto risco -> critério -> resultado.

## Decisão de Gate (rodada 1)

- [ ] **Concluído** (DoD atendido)
- [x] **Em revisão** (DoD não atendido)

**Justificativa curta da decisão:**  
Há lacunas críticas de amostra, rastreabilidade e conclusão técnica.

## Resultado da Revisão DoD (rodada 2)

### Itens críticos atendidos

- [x] Sim
- [ ] Não

### Pendências críticas identificadas

Nenhuma.

## Decisão de Gate (rodada 2)

- [x] **Concluído** (DoD atendido)
- [ ] **Em revisão** (DoD não atendido)

**Justificativa curta da decisão:**  
Artefato passou a atender critérios mínimos de reprodutibilidade, evidência e conclusão.

## Próximo Passo

- [x] Encaminhar para etapa seguinte do workflow
- [ ] Retornar para ajuste técnico do artefato
- [ ] Escalar pendência crítica para gestor / revisor

