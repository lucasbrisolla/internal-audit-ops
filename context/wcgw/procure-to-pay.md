---
processo: procure-to-pay
nivel: 1
abreviacao: P2P
subprocessos:
  - cadastro-de-fornecedor
  - requisicao-e-orcamento
  - aprovacao-de-contratacao
  - recebimento
  - lancamento-e-aprovacao-de-pagamento
  - remessa-e-retorno-bancario
  - integracoes-sistemicas
assercoes_primarias:
  - existência
  - completude
  - valoração
  - corte
frameworks:
  - COSO
  - SOX
referencias:
  - _method-wiki/processes/procure-to-pay.md
  - _method-wiki/patterns/liability-completeness-and-scot.md
---

# WCGW — Procure-to-Pay (P2P)

O P2P cobre o ciclo completo desde a necessidade de compra até o pagamento ao fornecedor. Os riscos concentram-se em três pontos críticos: **quem pode contratar**, **quem pode pagar** e **quem pode cadastrar o recebedor**. A separação dessas três funções é o controle estrutural mais importante do processo.

---

## Subprocesso 1: Cadastro de Fornecedor

Etapa onde fornecedores são incluídos, alterados ou reativados no sistema. Alta sensibilidade: quem controla o cadastro controla quem pode receber pagamentos.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| P2P-001 | Fornecedor fictício cadastrado para desvio de pagamento | Initiation | Existência | Crítico |
| P2P-002 | Dados bancários alterados por usuário não autorizado — pagamento desviado | Processing | Existência | Crítico |
| P2P-003 | Fornecedor reativado sem revisão de compliance (PEP, sanção, partes relacionadas) | Initiation | Existência | Alta |
| P2P-004 | Mesma pessoa cadastra fornecedor e aprova pagamento — segregação quebrada | Processing | Existência | Crítico |
| P2P-005 | Fornecedor duplicado cadastrado — risco de pagamento em dobro | Recording | Completude | Média |

**Controles típicos que mitigam:**
- aprovação dupla para inclusão e alteração de dados bancários
- revisão de compliance no onboarding (PEP, OFAC, listas de sanção, partes relacionadas)
- segregação entre quem cadastra e quem aprova pagamento
- relatório periódico de fornecedores novos/alterados revisado por gestor independente
- bloqueio sistêmico de duplicatas por CNPJ/CPF

**Flag de risco elevado:** empresa familiar ou com equipe reduzida — maior probabilidade de quebra de segregação no cadastro.

---

## Subprocesso 2: Requisição e Validação Orçamentária

Etapa de solicitação de compra e verificação de disponibilidade orçamentária antes de contratar.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| P2P-006 | Compra realizada sem requisição formal — sem rastreabilidade da necessidade | Initiation | Existência | Média |
| P2P-007 | Validação orçamentária contornada ou não bloqueia operacionalmente | Initiation | Valoração | Alta |
| P2P-008 | Requisição aprovada por quem tem interesse na contratação — conflito de interesse | Initiation | Existência | Alta |
| P2P-009 | Fracionamento de compra para fugir da alçada de aprovação | Initiation | Existência | Alta |
| P2P-010 | Orçamento disponível mas já comprometido com contratos em andamento — passivo oculto | Initiation | Completude | Média |

**Controles típicos que mitigam:**
- obrigatoriedade de requisição no sistema antes de qualquer contratação
- validação orçamentária sistêmica com bloqueio (não apenas aviso)
- política de alçadas por valor com aprovação escalonada
- relatório de requisições aprovadas sem saldo orçamentário
- detecção de fracionamento: relatório de OCs de mesmo fornecedor/período abaixo do limite de alçada

---

## Subprocesso 3: Aprovação de Contratação / OC

Etapa de formalização da contratação com fornecedor, incluindo cotação, aprovação e geração da OC.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| P2P-011 | OC aprovada por alçada insuficiente para o valor contratado | Processing | Existência | Alta |
| P2P-012 | Cotação mínima não realizada — contratação direta sem justificativa documentada | Initiation | Existência | Alta |
| P2P-013 | Cotação realizada mas direcionada — fornecedor preferido independente do preço | Initiation | Existência | Alta |
| P2P-014 | OC alterada após aprovação sem nova aprovação | Processing | Existência | Alta |
| P2P-015 | Contrato com fornecedor sem OC correspondente — compromisso fora do sistema | Recording | Completude | Alta |
| P2P-016 | Aprovador não leu o que aprovou — aprovação automática por volume | Processing | Existência | Média |

**Controles típicos que mitigam:**
- tabela de alçadas formalmente aprovada e atualizada
- obrigatoriedade de cotação mínima (3 fornecedores) com exceção documentada e aprovada
- log de alterações em OC aprovada com aprovação adicional obrigatória
- relatório de OCs sem contrato associado para valores acima do limite
- auditoria de amostra de aprovações: revisor verifica se aprovador tinha acesso ao suporte

**Flag de risco elevado:** processos de urgência sem cotação são comuns em operações industriais — verificar se "emergência" virou regra.

---

## Subprocesso 4: Recebimento de Mercadoria / Serviço

Etapa de confirmação que o bem ou serviço contratado foi efetivamente entregue antes do pagamento.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| P2P-017 | Pagamento liberado sem confirmação de recebimento — bem não entregue | Processing | Existência | Alta |
| P2P-018 | Recebimento registrado por quem aprovou a compra — segregação quebrada | Processing | Existência | Alta |
| P2P-019 | Recebimento parcial registrado como total — pagamento a maior | Recording | Valoração | Alta |
| P2P-020 | Serviço registrado como recebido sem evidência de entrega (intangível) | Processing | Existência | Alta |
| P2P-021 | Three-way match (OC × NF × recebimento) não realizado sistematicamente | Processing | Existência | Alta |
| P2P-022 | Recebimento registrado antes da entrega para antecipar pagamento ao fornecedor | Recording | Corte | Média |

**Controles típicos que mitigam:**
- three-way match sistêmico com bloqueio de pagamento se não houver recebimento
- segregação entre aprovador da OC e responsável pelo recebimento
- para serviços: evidência formal de entrega (relatório, aceite assinado, ata)
- relatório de notas fiscais sem recebimento correspondente pendentes de pagamento
- revisão de recebimentos registrados no último dia do mês (risco de corte)

---

## Subprocesso 5: Lançamento e Aprovação de Pagamento

Etapa de registro da obrigação (contas a pagar) e aprovação do desembolso.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| P2P-023 | NF lançada com valor superior ao da OC sem ajuste aprovado | Recording | Valoração | Alta |
| P2P-024 | Pagamento aprovado por quem também pode cadastrar fornecedor — segregação quebrada | Processing | Existência | Alta |
| P2P-025 | Pagamento duplicado: mesma NF lançada duas vezes | Recording | Existência | Alta |
| P2P-026 | Passivo não registrado: NF recebida não lançada no período — understatement de passivo | Recording | Completude | Alta |
| P2P-027 | Pagamento antecipado sem cláusula contratual justificando | Processing | Existência | Média |
| P2P-028 | Crédito de fornecedor (devolução, desconto) não aplicado — pagamento a maior | Processing | Valoração | Média |

**Controles típicos que mitigam:**
- validação sistêmica de NF contra OC com tolerância configurada (ex: ±5%)
- segregação entre lançador de NF, aprovador de pagamento e cadastrador de fornecedor
- detecção de duplicatas por CNPJ + número de NF + valor
- processo de corte: NFs recebidas até o fechamento devem ser lançadas no período
- reconciliação de saldo de fornecedor: aging de AP × extratos de fornecedor

---

## Subprocesso 6: Remessa e Retorno Bancário

Etapa de execução do pagamento via banco e tratamento de rejeições.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| P2P-029 | Arquivo de remessa alterado após aprovação — dados bancários modificados | Processing | Existência | Alta |
| P2P-030 | Rejeição bancária tratada manualmente sem revisão independente | Processing | Existência | Alta |
| P2P-031 | Pagamento enviado mas não baixado no sistema — passivo fictício mantido | Reporting | Completude | Média |
| P2P-032 | Acesso ao sistema bancário não restrito às pessoas autorizadas | Processing | Existência | Alta |
| P2P-033 | Retorno bancário não conciliado com remessa — divergências não detectadas | Reporting | Valoração | Média |

**Controles típicos que mitigam:**
- hash ou assinatura digital do arquivo de remessa para detectar alteração pós-aprovação
- revisão independente de rejeições antes de retransmissão
- conciliação automática retorno × remessa com relatório de divergências
- acesso ao banco restrito por perfil com aprovação em dois fatores
- baixa automática no AP após confirmação do retorno bancário

---

## Subprocesso 7: Integrações Sistêmicas

Pontos de integração entre sistemas auxiliares (Ariba, Basware, portais de fornecedor) e o ERP. Riscos emergem da fronteira entre sistemas — onde a responsabilidade é difusa.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| P2P-034 | Transação aprovada no sistema auxiliar não integrada ao ERP — passivo fora do sistema | Recording | Completude | Alta |
| P2P-035 | Dados alterados na integração — valor ou dado bancário diferente entre sistemas | Processing | Valoração | Alta |
| P2P-036 | Falha de integração silenciosa — transação perdida sem alerta | Processing | Completude | Alta |
| P2P-037 | Controles do sistema auxiliar não equivalentes ao ERP — gap na migração | Processing | Existência | Alta |
| P2P-038 | Log de integração não monitorado — falhas acumulam sem detecção | Reporting | Completude | Média |

**Controles típicos que mitigam:**
- reconciliação periódica entre sistemas: total de OCs aprovadas no auxiliar × lançamentos no ERP
- alerta automático para falhas de integração com re-processamento controlado
- revisão de log de integração com frequência definida
- validação de que controles do sistema auxiliar foram replicados ou compensados no ERP
- SLA de integração com monitoramento de latência e falhas

**Flag de risco elevado:** primeiro ano pós-implementação de sistema auxiliar — integração ainda instável, controles compensatórios ainda não maduros.

---

## Leitura Rápida por Risco

| Risco Central | Subprocessos Críticos | WCGW-chave |
|---|---|---|
| Fraude de fornecedor fictício | Cadastro, Pagamento | P2P-001, P2P-002, P2P-004 |
| Pagamento indevido / sem entrega | Recebimento, Pagamento | P2P-017, P2P-021, P2P-023 |
| Fracionamento / bypass de alçada | Requisição, Aprovação OC | P2P-009, P2P-011 |
| Passivo incompleto (understatement) | Lançamento, Integração | P2P-026, P2P-034 |
| Segregação quebrada | Cadastro, Recebimento, Pagamento | P2P-004, P2P-018, P2P-024 |
| Falha de integração sistêmica | Integração | P2P-034, P2P-035, P2P-036 |
