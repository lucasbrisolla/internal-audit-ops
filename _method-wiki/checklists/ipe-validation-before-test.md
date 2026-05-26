# Checklist — Validação de IPE Antes do Teste

## Papel

Gate de qualidade obrigatório antes de qualquer teste que dependa de relatório, listagem ou base gerada pela entidade (IPE — Information Produced by the Entity). Executar antes de selecionar amostra ou confiar em dados para conclusão de controle.

## Quando usar

- Qualquer teste de controle cujo critério de avaliação depende de relatório, extração ou base da entidade
- Antes de definir população ou selecionar amostra com base em listagem fornecida pelo cliente
- Quando a entidade fornece exportação, planilha ou output de sistema como insumo do teste

## Resultado possível

- **IPE confiável para reliance**: todos os itens obrigatórios confirmados
- **IPE confiável com restrição**: 1–2 itens secundários sem confirmação; documentar limitação e recalibrar procedimento
- **IPE não confiável**: qualquer item crítico não confirmado; não usar como base — exigir alternativa ou redesenhar procedimento

---

## Itens Obrigatórios (qualquer falha = IPE não confiável)

- [ ] **Parâmetros validados**: os parâmetros usados para gerar o relatório foram inspecionados diretamente — período, filtros, entidade, moeda, status de transação
- [ ] **Escopo confirma cobertura pretendida**: a extração cobre exatamente o que o teste pretende cobrir — nem mais, nem menos
- [ ] **Reconciliação com razão ou referência independente**: totais da base foram reconciliados com saldo contábil, relatório gerencial oficial ou outra fonte confiável para o mesmo período
- [ ] **Fonte rastreável e reproduzível**: origem do relatório está documentada (sistema, módulo, path, data de extração) de forma que outro auditor poderia reproduzir a extração

## Itens de Completude e Precisão

- [ ] **Completude confirmada**: não há evidência de que registros foram omitidos — verificar sequência numérica, total de linhas vs. referência, ou ausência de gaps no período
- [ ] **Precisão dos campos críticos**: campos usados no teste (valor, data, responsável, status) estão corretos e sem truncagem ou formatação que distorça o dado
- [ ] **Período alinhado ao escopo do teste**: o período coberto pela extração é idêntico ao período auditado — sem truncagem no início ou fim

## Itens de Intervenção Manual e Transformação

- [ ] **Intervenções manuais identificadas**: se houve manipulação da base após extração (ordenação, filtro, fórmulas, EUC), isso foi identificado e avaliado
- [ ] **Transformações têm trilha**: ajustes, concatenações ou joins realizados fora do sistema têm registros auditáveis que permitem reconstrução
- [ ] **Ausência de override não documentado**: não há colunas adicionadas, linhas deletadas ou filtros aplicados sem registro

## Itens de Acesso e Integridade

- [ ] **Acesso direto ao sistema preferido**: quando possível, a extração foi obtida diretamente do sistema (live data) em vez de exportação intermediada pela entidade
- [ ] **Documento original vs. cópia**: quando se usa cópia ou exportação, avaliar se há risco de adulteração — preferir original quando risco é alto

## Vínculo com COSO P13–P15

A avaliação de IPE é evidência direta sobre o componente **Information & Communication** (COSO P13–P15). Quando IPE revela problemas de completude ou precisão:

- Registrar como input para avaliação do componente de I&C
- Não tratar como achado isolado de processo — avaliar se é indicador pervasivo

---

## Documentação Mínima

Registrar no paper de teste:

- [ ] Fonte do relatório (sistema, módulo, parâmetros)
- [ ] Referência usada para reconciliação e resultado
- [ ] Resultado da validação: confiável / confiável com restrição / não confiável
- [ ] Se houver restrição: qual e como o procedimento foi recalibrado

---

## Conexões Internas

- `_method-wiki/processes/ipe-reliability-assessment.md` — hub metodológico completo; consultar quando a análise exigir profundidade além do gate
- `workflows/test-execution.md` — chamar este checklist no Step 3 (ToE), antes de definir amostra
- `concepts/evidence-and-testing-foundations.md` — hierarquia de evidência e situações sem amostragem
- `_method-wiki/checklists/audit-artifacts-definition-of-done.md` — DoD do papel de teste (referência cruzada)
