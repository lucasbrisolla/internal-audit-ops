---
lista: controles-mestres
tipo: master-list
descricao: Catálogo mestre de controles típicos de auditoria interna, com atributos mínimos para desenho, teste e evidência.
uso:
  - audit-planning
  - risk-control-mapping
  - test-execution
  - finding-drafting
campos:
  - id
  - controle
  - objetivo
  - objetivo_de_auditoria
  - tipo
  - natureza
  - frequência
  - evidência_mínima
  - asserções_cobertas
  - processos_aplicáveis
---

# Controles Mestres

Base de referência para seleção e documentação de controles em RCM, desenho de testes e revisão de achados.

## Dicionário dos campos

- **Tipo:** preventivo ou detectivo.
- **Objetivo de auditoria:** financeiro, operacional, compliance, tecnologia, fraude (aceita combinação).
- **Natureza:** manual, automatizado ou híbrido.
- **Frequência:** por transação, diária, semanal, mensal, trimestral ou eventual.
- **Evidência mínima:** trilha mínima para concluir que o controle operou.

## Catálogo de controles

| ID | Controle | Objetivo | Objetivo de auditoria | Tipo | Natureza | Frequência | Evidência mínima | Asserções cobertas | Processos aplicáveis |
|---|---|---|---|---|---|---|---|---|---|
| CTRL-001 | Aprovação por alçada formal | Garantir que decisões relevantes respeitem níveis de autoridade definidos | Compliance, Fraude | Preventivo | Híbrido | Por transação | Log/aprovação com usuário, data e valor | Existência, Valoração | P2P, OTC, RTR, FA |
| CTRL-002 | Bloqueio sistêmico de transação sem pré-requisito | Impedir execução sem documento/etapa obrigatória (ex.: OC, recebimento, crédito) | Operacional, Compliance | Preventivo | Automatizado | Por transação | Configuração ativa + evidência de bloqueio | Existência, Completude | P2P, OTC, H2R |
| CTRL-003 | Three-way match (OC × NF × recebimento) | Evitar pagamento sem entrega válida e sem aderência ao pedido aprovado | Financeiro, Fraude | Preventivo | Híbrido | Por transação | Relatório de matching com exceções | Existência, Valoração, Corte | P2P |
| CTRL-004 | Segregação de funções em pontos críticos | Reduzir risco de fraude/erro por concentração de poder operacional | Fraude, Compliance | Preventivo | Híbrido | Contínua | Matriz SoD + revisão de acessos/perfis | Existência, Completude | P2P, OTC, H2R, RTR, UAM |
| CTRL-005 | Revisão independente de reconciliação | Validar saldos e tratar diferenças com aprovação por revisor independente | Financeiro, Operacional | Detectivo | Manual | Mensal | Reconciliação assinada + itens reconciliantes | Completude, Valoração | RTR, OTC, Treasury |
| CTRL-006 | Detecção de duplicidade por chave crítica | Evitar registros/pagamentos duplicados (NF, título, cliente, fornecedor) | Financeiro, Operacional | Preventivo | Automatizado | Por transação | Regra de duplicidade + log de bloqueio/exceção | Existência, Completude | P2P, OTC |
| CTRL-007 | Revisão de exceções de relatório automático | Detectar anomalias e assegurar tratamento tempestivo de desvios | Operacional, Tecnologia | Detectivo | Híbrido | Diária/Semanal | Relatório de exceções + evidência de tratamento | Existência, Completude | P2P, OTC, ITGC |
| CTRL-008 | Conciliação de remessa e retorno bancário | Garantir que pagamentos/recebimentos executados estejam refletidos corretamente no ERP | Financeiro, Compliance | Detectivo | Híbrido | Diária | Conciliação retorno × remessa × razão | Completude, Valoração, Corte | P2P, OTC, Treasury |
| CTRL-009 | Revisão periódica de acessos | Confirmar aderência entre perfil de acesso e função exercida | Tecnologia, Compliance | Detectivo | Híbrido | Trimestral | Lista de acessos revisada/aprovada | Existência | UAM, ITGC |
| CTRL-010 | Aprovação de alteração de dados bancários | Evitar desvio por mudança indevida de conta de pagamento/recebimento | Fraude, Compliance | Preventivo | Híbrido | Por evento | Workflow aprovado + log de alteração | Existência | P2P, OTC, H2R |
| CTRL-011 | Gestão formal de mudanças de sistema | Garantir que mudanças sejam aprovadas, testadas e homologadas antes de produção | Tecnologia, Compliance | Preventivo | Híbrido | Por mudança | Ticket com aprovação, teste e deploy | Existência, Completude | ITGC |
| CTRL-012 | Monitoramento de falha de jobs críticos | Detectar falhas de processamento antes de impacto operacional/financeiro | Tecnologia, Operacional | Detectivo | Automatizado | Diária | Log de execução + alerta + tratativa | Completude, Corte | ITGC, RTR |
| CTRL-013 | Validação de integração entre sistemas | Assegurar completude e integridade de dados entre origem e destino | Tecnologia, Operacional | Detectivo | Híbrido | Diária/Mensal | Reconciliação origem × destino | Completude, Valoração | ITGC, P2P, OTC, H2R |
| CTRL-014 | Revisão analítica de fechamento | Identificar variações atípicas e exigir justificativa suportada por evidência | Financeiro | Detectivo | Manual | Mensal | Papel de revisão com variações e respostas | Valoração, Apresentação | RTR, OTC, FA |
| CTRL-015 | Inventário físico com teste bidirecional | Confirmar existência e completude de ativos/estoques | Operacional, Financeiro | Detectivo | Manual | Periódica | Ata de contagem + conciliação com razão | Existência, Completude, Valoração | Inventory, FA |
| CTRL-016 | Controle de corte de período | Garantir registro no período correto de receita, despesa, passivo e ativo | Financeiro | Detectivo | Híbrido | Mensal | Teste de transações próximas ao fechamento | Corte, Completude | OTC, P2P, RTR |
| CTRL-017 | Aprovação formal de write-off/provisão | Evitar baixas/provisões arbitrárias que distorçam resultado | Financeiro, Compliance | Preventivo | Manual | Por evento/Mensal | Memorando de suporte + aprovação por alçada | Valoração, Apresentação | OTC, RTR |
| CTRL-018 | Revisão de parâmetros críticos de sistema | Evitar alterações indevidas em regras com impacto de processo e reporte | Tecnologia, Fraude | Preventivo | Híbrido | Mensal/Por mudança | Relatório de parâmetros + aprovação | Existência, Valoração | ITGC, RTR |
| CTRL-019 | Evidência de aceite de serviço intangível | Comprovar prestação efetiva antes de pagamento/reconhecimento | Operacional, Compliance | Preventivo | Manual | Por transação | Aceite formal, relatório técnico ou ata | Existência, Valoração | P2P, OTC |
| CTRL-020 | Follow-up de plano de ação com owner e prazo | Assegurar remediação efetiva de achados | Compliance, Operacional | Detectivo | Manual | Mensal | Status com evidência de implementação | Completude, Existência | Todos |

## Regras de uso

1. Esta lista é referência base, não substitui customização por cliente.
2. Um controle pode mitigar múltiplos riscos e aparecer em mais de uma linha da RCM.
3. Se o controle da operação não existir no catálogo, criar descrição específica no trabalho e avaliar se deve ser promovido para esta lista.
4. Ao incluir novo controle mestre, manter ID único e atualizar os campos obrigatórios.
