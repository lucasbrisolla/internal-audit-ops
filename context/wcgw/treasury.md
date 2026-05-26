---
processo: treasury
nivel: 1
abreviacao: TRE
subprocessos:
  - contas-bancarias-e-procuracoes
  - conciliacao-bancaria
  - pagamentos-e-transferencias
  - recebimentos-e-baixas-bancarias
  - aplicacoes-financeiras-e-investimentos
  - dividas-covenants-e-garantias
  - derivativos-e-hedge
  - fluxo-de-caixa-e-liquidez
assercoes_primarias:
  - existência
  - completude
  - valoração
  - corte
  - apresentação
frameworks:
  - COSO
  - SOX
  - IFRS 9
  - CPC 48
  - gestao de tesouraria
referencias:
  - _method-wiki/patterns/evidence-conclusion-linkage.md
  - _method-wiki/processes/financial-statement-disclosure-review.md
  - context/wcgw/procure-to-pay.md
  - context/wcgw/order-to-cash.md
  - context/wcgw/record-to-report.md
  - context/wcgw/user-access-management.md
---

# WCGW — Treasury (TRE)

Treasury cobre a custódia e movimentação do caixa: contas bancárias, conciliações, pagamentos, recebimentos, aplicações, dívidas, garantias, derivativos e liquidez. É um processo sensível porque caixa é o ativo mais líquido da organização e porque pequenas falhas de autorização, segregação ou conciliação podem gerar perda imediata.

OTC responde se a venda e o recebível foram registrados corretamente. Treasury responde se o dinheiro **existe**, **foi movimentado por pessoas autorizadas**, **está conciliado**, **foi aplicado ou financiado corretamente** e **está refletido no reporte financeiro**.

---

## Subprocesso 1: Contas Bancárias e Procurações

Etapa de abertura, manutenção, encerramento e governança de contas bancárias, procuradores, tokens, perfis e poderes de movimentação.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| TRE-001 | Conta bancária aberta sem aprovação formal da diretoria ou política de tesouraria | Initiation | Existência | Alta |
| TRE-002 | Conta bancária ativa não registrada no cadastro central de contas — fora do escopo de conciliação | Recording | Completude | Alta |
| TRE-003 | Procuradores bancários desatualizados após desligamento ou mudança de função | Processing | Existência | Alta |
| TRE-004 | Poderes bancários incompatíveis com função ou alçada aprovada | Processing | Existência | Alta |
| TRE-005 | Token, certificado ou credencial bancária compartilhada entre usuários | Processing | Existência | Alta |
| TRE-006 | Conta bancária encerrada no banco mas mantida ativa no ERP ou vice-versa | Recording | Completude | Média |

**Controles típicos que mitigam:**
- cadastro central de contas bancárias com status, finalidade, banco, moeda e responsáveis
- aprovação formal para abertura, alteração e encerramento de contas
- revisão periódica de procuradores e poderes bancários
- segregação entre cadastro bancário, aprovação e execução de transações
- credenciais individuais com autenticação forte e revogação tempestiva

**Flag de risco elevado:** conta bancária com baixa movimentação, fora do ERP, mantida para "uso eventual".

---

## Subprocesso 2: Conciliação Bancária

Etapa de conciliar extratos bancários, razão contábil, subledger financeiro e pendências de recebimento/pagamento.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| TRE-007 | Conciliação bancária não preparada para todas as contas relevantes | Processing | Completude | Alta |
| TRE-008 | Conciliação preparada e aprovada pela mesma pessoa | Processing | Existência | Alta |
| TRE-009 | Itens conciliatórios antigos mantidos sem investigação ou baixa | Processing | Existência | Alta |
| TRE-010 | Conciliação feita sobre extrato incompleto ou relatório bancário não confiável | Processing | Completude | Alta |
| TRE-011 | Diferenças de conciliação lançadas como ajuste genérico sem análise de causa | Recording | Existência | Alta |
| TRE-012 | Contas em moeda estrangeira conciliadas sem validar taxa de câmbio e reavaliação cambial | Recording | Valoração | Média |

**Controles típicos que mitigam:**
- conciliação mensal ou diária conforme risco e volume
- revisão independente com evidência de investigação dos itens relevantes
- aging de itens conciliatórios com responsável e prazo
- obtenção direta de extrato bancário ou arquivo oficial do banco
- reconciliação entre extrato, razão, ERP financeiro e mapa de caixa

**Armadilha comum:** aceitar "diferença temporária" sem data esperada de compensação e sem dono.

---

## Subprocesso 3: Pagamentos e Transferências

Etapa de execução de pagamentos, transferências entre contas, remessas bancárias, aprovações, rejeições e liberações de arquivo.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| TRE-013 | Pagamento executado sem aprovação conforme alçada | Processing | Existência | Alta |
| TRE-014 | Mesma pessoa prepara, aprova e libera pagamento no banco | Processing | Existência | Crítico |
| TRE-015 | Arquivo de remessa alterado após aprovação sem nova autorização | Processing | Existência | Alta |
| TRE-016 | Pagamento feito para conta bancária divergente do cadastro aprovado do fornecedor | Processing | Existência | Alta |
| TRE-017 | Transferência entre contas próprias sem documentação de finalidade ou aprovação | Processing | Existência | Média |
| TRE-018 | Rejeição bancária reprocessada manualmente sem revisão independente | Processing | Existência | Alta |

**Controles típicos que mitigam:**
- dupla aprovação bancária por alçada
- segregação entre preparação, aprovação e liberação
- hash, log ou trilha de alteração do arquivo de remessa
- bloqueio para pagamento em conta divergente do cadastro mestre aprovado
- relatório de rejeições e reprocessamentos revisado por pessoa independente

**Flag de risco elevado:** pagamento urgente fora da rotina, aprovado por exceção e liberado manualmente.

---

## Subprocesso 4: Recebimentos e Baixas Bancárias

Etapa em que entradas de caixa são identificadas, conciliadas, alocadas a clientes/títulos e baixadas no ERP.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| TRE-019 | Recebimento bancário não identificado permanece sem baixa no ERP — recebível em aberto indevidamente | Recording | Completude | Média |
| TRE-020 | Baixa de recebível registrada sem confirmação de dinheiro no banco | Recording | Existência | Alta |
| TRE-021 | Recebimento alocado ao cliente ou título incorreto | Recording | Valoração | Média |
| TRE-022 | Desconto financeiro, abatimento ou tarifa bancária lançado sem validação de origem | Recording | Valoração | Média |
| TRE-023 | Conta bancária usada para recebimentos de clientes fora do processo formal de conciliação | Processing | Completude | Alta |

**Controles típicos que mitigam:**
- conciliação diária de recebimentos com extrato bancário
- baixa automática ou semiautomática baseada em identificador de boleto/PIX/TED
- revisão de recebimentos não identificados e baixas manuais
- segregação entre cobrança, baixa e conciliação bancária
- investigação de descontos, abatimentos e tarifas relevantes

**Relação com OTC:** OTC cobre faturamento, cobrança e AR; Treasury cobre confirmação bancária e integridade da baixa financeira.

---

## Subprocesso 5: Aplicações Financeiras e Investimentos

Etapa de aplicação, resgate, mensuração, rendimento, classificação e custódia de instrumentos financeiros de curto e longo prazo.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| TRE-024 | Aplicação financeira realizada fora da política de investimentos ou limite de risco | Initiation | Existência | Alta |
| TRE-025 | Resgate de aplicação realizado sem aprovação ou sem necessidade de caixa documentada | Processing | Existência | Média |
| TRE-026 | Rendimento de aplicação não reconhecido ou reconhecido pelo valor incorreto | Recording | Valoração | Média |
| TRE-027 | Aplicação financeira registrada sem confirmação independente da instituição custodiante | Recording | Existência | Alta |
| TRE-028 | Classificação contábil do instrumento financeiro incorreta — custo amortizado, VJORA ou VJR | Reporting | Apresentação | Alta |
| TRE-029 | Perda esperada, impairment ou marcação a mercado não avaliada para instrumento relevante | Processing | Valoração | Alta |

**Controles típicos que mitigam:**
- política de investimentos com limites por instrumento, banco, rating e prazo
- aprovação formal para aplicação e resgate
- confirmação externa de saldos e rendimentos
- conciliação entre extrato de custódia, razão e mapa de aplicações
- revisão contábil da classificação IFRS 9 / CPC 48

**Flag de risco elevado:** aplicação em instituição não usual, produto complexo ou rentabilidade incompatível com risco declarado.

---

## Subprocesso 6: Dívidas, Covenants e Garantias

Etapa de contratação, mensuração, pagamento, monitoramento de covenants, garantias e disclosure de empréstimos e financiamentos.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| TRE-030 | Empréstimo ou financiamento contratado sem aprovação conforme alçada | Initiation | Existência | Alta |
| TRE-031 | Dívida registrada com taxa, prazo, principal ou encargos divergentes do contrato | Recording | Valoração | Alta |
| TRE-032 | Juros, variação cambial ou encargos financeiros não apropriados no período correto | Recording | Corte | Alta |
| TRE-033 | Covenant financeiro não monitorado tempestivamente — violação não identificada antes do reporte | Processing | Completude | Alta |
| TRE-034 | Garantia, aval ou fiança concedida sem aprovação formal ou sem disclosure adequado | Reporting | Completude | Alta |
| TRE-035 | Cláusula de vencimento antecipado não avaliada para classificação entre circulante e não circulante | Reporting | Apresentação | Alta |

**Controles típicos que mitigam:**
- aprovação formal para captação, renovação e alteração de dívida
- cadastro central de contratos de dívida com cronograma de pagamentos
- cálculo independente de juros, variação cambial e custo amortizado
- tracker de covenants com responsáveis, fórmula, prazo e evidência
- revisão de garantias, restrições e classificação contábil no fechamento

**Flag de risco elevado:** covenant próximo do limite, EBITDA ajustado com critérios subjetivos ou waiver negociado perto do fechamento.

---

## Subprocesso 7: Derivativos e Hedge

Etapa de contratação, documentação, mensuração e monitoramento de derivativos, hedge econômico ou hedge accounting.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| TRE-036 | Derivativo contratado sem aprovação da política financeira ou fora do objetivo de proteção | Initiation | Existência | Alta |
| TRE-037 | Exposição protegida não documentada — derivativo pode ser especulativo | Initiation | Existência | Alta |
| TRE-038 | Valor justo de derivativo mensurado sem fonte independente ou metodologia validada | Recording | Valoração | Alta |
| TRE-039 | Hedge accounting aplicado sem documentação formal de relação de hedge e efetividade | Reporting | Apresentação | Alta |
| TRE-040 | Inefetividade de hedge não mensurada ou não reconhecida adequadamente | Processing | Valoração | Alta |

**Controles típicos que mitigam:**
- política formal de derivativos proibindo finalidade especulativa
- aprovação por comitê financeiro ou diretoria
- documentação da exposição, instrumento, objetivo e prazo
- confirmação externa e valuation independente
- revisão técnica de hedge accounting, efetividade e disclosure

**Armadilha crítica:** chamar toda proteção econômica de hedge accounting. A contabilidade especial exige documentação e testes específicos.

---

## Subprocesso 8: Fluxo de Caixa e Liquidez

Etapa de previsão, monitoramento e decisão sobre liquidez, capital de giro, disponibilidade mínima e necessidade de financiamento.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| TRE-041 | Forecast de caixa preparado sem base em dados atualizados de AR, AP, folha, dívida e CAPEX | Processing | Completude | Alta |
| TRE-042 | Diferenças recorrentes entre caixa previsto e realizado não analisadas | Processing | Valoração | Média |
| TRE-043 | Caixa restrito tratado como caixa disponível para operação | Reporting | Apresentação | Alta |
| TRE-044 | Necessidade de financiamento identificada tarde demais — decisão tomada sob urgência e pior condição | Initiation | Existência | Média |
| TRE-045 | Concentração excessiva de caixa em um único banco sem avaliação de risco de contraparte | Processing | Valoração | Média |

**Controles típicos que mitigam:**
- forecast rolling de caixa com integração a AR, AP, folha, dívida e CAPEX
- análise de previsto x realizado com causa raiz
- segregação entre caixa livre e caixa restrito
- limites de concentração por banco e rating
- comitê de liquidez para decisões de captação, aplicação e reserva mínima

---

## Leitura Rápida por Risco

| Risco Central | Subprocessos Críticos | WCGW-chave |
|---|---|---|
| Conta bancária fora do controle | Contas bancárias | TRE-001, TRE-002, TRE-006 |
| Poder bancário indevido | Contas bancárias | TRE-003, TRE-004, TRE-005 |
| Conciliação incompleta ou sem revisão | Conciliação | TRE-007, TRE-008, TRE-009 |
| Pagamento indevido ou fraudulento | Pagamentos | TRE-013, TRE-014, TRE-016 |
| Baixa de recebível sem dinheiro | Recebimentos | TRE-020, TRE-023 |
| Aplicação fora da política ou mal mensurada | Aplicações | TRE-024, TRE-027, TRE-029 |
| Dívida ou covenant mal monitorado | Dívidas | TRE-031, TRE-033, TRE-035 |
| Derivativo especulativo ou mal contabilizado | Derivativos | TRE-036, TRE-038, TRE-039 |
| Caixa restrito tratado como disponível | Liquidez | TRE-043 |
