---
lista: red-flags-por-processo
tipo: master-list
descricao: Indicadores de anomalia por processo, com métrica exata, limiar sugerido e fonte de dados para execução direta
processos:
  - P2P
  - OTC
  - H2R
  - RTR
  - FA
  - UAM
uso:
  - audit-planning
  - risk-control-mapping
  - test-execution
nota: limiares são pontos de partida — calibrar conforme materialidade e características do cliente antes de usar
---

# Red Flags por Processo

Diferente do WCGW (o que pode errar) e da SoD (quem não deveria ter o quê), red flags são **sinais mensuráveis de que algo pode já ter errado**. Cada item abaixo é acionável: tem a métrica, o limiar e a fonte de dados necessários para executar a análise.

**Tipo de anomalia:**
- **Valor:** transação com valor atípico para o contexto
- **Frequência:** volume de transações fora do padrão esperado
- **Padrão:** comportamento sistemático que não seria esperado em operação normal
- **Timing:** transação no momento errado (fim de período, fora do horário, pós-aprovação)

---

## P2P — Procure-to-Pay

| ID | Red Flag | Métrica / Indicador | Limiar Sugerido | Fonte de Dados (IPE) | WCGW Associado | Tipo |
|---|---|---|---|---|---|---|
| RF-P2P-001 | Fornecedor com dados bancários idênticos a funcionário | Cruzamento de conta bancária do mestre de fornecedores com dados bancários da folha | Qualquer match = investigar | Extrato de mestre de fornecedores + folha de pagamento | P2P-008, H2R-009 | Padrão |
| RF-P2P-002 | Fornecedor cadastrado e pago no mesmo dia ou semana | Diferença em dias entre data de cadastro e primeiro pagamento | < 7 dias = alerta | Mestre de fornecedores + histórico de pagamentos | P2P-004 | Timing |
| RF-P2P-003 | Pagamentos fracionados abaixo do limite de aprovação | Múltiplos pagamentos ao mesmo fornecedor no mesmo dia ou semana com valor individual abaixo do threshold | ≥ 3 pagamentos ao mesmo fornecedor no mesmo dia com soma > limite de aprovação | Relatório de pagamentos por fornecedor e data | P2P-020 | Padrão |
| RF-P2P-004 | Pagamentos processados fora do horário ou em datas atípicas | Timestamp de autorização de remessa | Fora do horário comercial (ex: antes das 7h ou após 20h) ou fins de semana / feriados | Log de transações do sistema bancário | P2P-025 | Timing |
| RF-P2P-005 | Concentração excessiva em poucos fornecedores | % do volume de compras no top 5 fornecedores | > 60% do volume em ≤ 5 fornecedores sem justificativa contratual | Relatório de compras por fornecedor no período | P2P-002 | Padrão |
| RF-P2P-006 | Variação de preço por item acima do esperado | Preço médio pago por item ao mesmo fornecedor vs. períodos anteriores | Variação > 15% sem reajuste contratual documentado | Histórico de OCs e NFs por item/fornecedor | P2P-016 | Valor |
| RF-P2P-007 | NFs duplicadas — mesmo fornecedor, valor próximo, mesmo período | Duplicidade por fornecedor + valor (±5%) + período (±30 dias) | Qualquer match = investigar | Base de NFs lançadas no período | P2P-019 | Padrão |
| RF-P2P-008 | Compras diretas acima do threshold sem processo de cotação | Volume de OCs sem referência de cotação acima do valor mínimo obrigatório | > 10% do volume de compras sem cotação quando política exige | Relatório de OCs com campo de cotação vazio | P2P-006 | Frequência |
| RF-P2P-009 | Fornecedor com CNPJ inativo ou situação irregular na Receita Federal | Situação cadastral do CNPJ na data da transação | CNPJ inapto, suspenso ou baixado = investigar | Mestre de fornecedores + consulta Receita (CNPJ) | P2P-004 | Padrão |
| RF-P2P-010 | Clustering de pagamentos próximos ao limite de aprovação | Distribuição de pagamentos por faixa de valor | Concentração anormal de pagamentos entre 90–99% do limite de aprovação | Histograma de pagamentos por valor | P2P-020 | Padrão |
| RF-P2P-011 | Mesmo endereço ou telefone em múltiplos fornecedores | Cruzamento de endereço e telefone no mestre de fornecedores | ≥ 2 fornecedores com mesmo endereço ou telefone | Mestre de fornecedores | P2P-004 | Padrão |

---

## OTC — Order-to-Cash

| ID | Red Flag | Métrica / Indicador | Limiar Sugerido | Fonte de Dados (IPE) | WCGW Associado | Tipo |
|---|---|---|---|---|---|---|
| RF-OTC-001 | DSO crescente sem explicação de mix ou prazo | Days Sales Outstanding = (Contas a Receber / Receita) × dias do período | Aumento > 10 dias vs. mesmo período do ano anterior sem alteração de política | Razão de clientes + DRE do período | OTC-034, OTC-036 | Padrão |
| RF-OTC-002 | NFs emitidas nos últimos dias do período — clustering de corte | Volume e valor de NFs emitidas nos últimos 5 dias úteis do período | > 30% da receita mensal concentrada nos últimos 5 dias úteis | Relatório de NFs por data de emissão | OTC-014, OTC-024 | Timing |
| RF-OTC-003 | Receita crescendo enquanto volume operacional cai | Variação % da receita vs. variação % de volume (unidades, m², contratos ativos) | Receita cresce > 10% enquanto volume cai ou estagna — sem reajuste de preço documentado | DRE + dados operacionais do sistema | OTC-027, FRA-021 | Padrão |
| RF-OTC-004 | Grandes notas de crédito ou abatimentos próximos ao fechamento | Volume e valor de notas de crédito e abatimentos nos últimos e primeiros dias do período | Nota de crédito > 5% da NF original emitida nos últimos 3 dias úteis do período | Relatório de notas de crédito por data | OTC-025, OTC-019 | Timing |
| RF-OTC-005 | Receita revertida ou estornada no período seguinte | Valor de reversões de receita no mês M+1 referentes a NFs de M | Reversão > 2% da receita do período | Relatório de estornos por NF de origem | OTC-032, FRA-021 | Padrão |
| RF-OTC-006 | Clientes com aging > 90 dias sem PDD proporcional | % de clientes com saldo vencido > 90 dias sobre o total de AR vs. % de PDD constituída | PDD < 30% do saldo vencido > 90 dias (calibrar pelo histórico de perdas) | Aging de clientes + razão de PDD | OTC-034, OTC-036 | Valor |
| RF-OTC-007 | Concentração excessiva em poucos clientes | % da receita no top 5 clientes | > 50% da receita em ≤ 3 clientes sem contrato de longo prazo documentado | Relatório de receita por cliente | OTC-040 | Padrão |
| RF-OTC-008 | Desconto concedido acima da alçada do vendedor | Desconto aplicado vs. tabela de alçadas por vendedor | Qualquer desconto acima da alçada sem aprovação documentada do gestor | Relatório de pedidos com campo de desconto + tabela de alçadas | OTC-010 | Valor |
| RF-OTC-009 | Recebimentos em conta bancária não reconciliada | Extrato bancário de contas não incluídas na conciliação formal | Qualquer conta com entrada de clientes fora do processo de conciliação | Extrato bancário + escopo de conciliação | OTC-045 | Padrão |

---

## H2R — Hire-to-Retire

| ID | Red Flag | Métrica / Indicador | Limiar Sugerido | Fonte de Dados (IPE) | WCGW Associado | Tipo |
|---|---|---|---|---|---|---|
| RF-H2R-001 | Funcionários sem registro de ponto mas com pagamento de horas extras | Funcionários com horas extras pagas mas sem registro de ponto eletrônico no período | Qualquer ocorrência = investigar | Folha de pagamento + relatório de ponto eletrônico | H2R-016, H2R-017 | Padrão |
| RF-H2R-002 | Horas extras concentradas em poucos funcionários | % do total de horas extras pagas concentrado nos top 10 beneficiários | Top 10 responsáveis por > 50% do custo total de horas extras | Folha de pagamento com detalhamento de horas extras por matrícula | H2R-016, H2R-017 | Frequência |
| RF-H2R-003 | Salário fora da faixa aprovada para o cargo | Salário individual vs. faixa salarial aprovada para o cargo/nível | Salário > 110% do teto da faixa sem exceção documentada | Folha de pagamento + tabela de faixas salariais | H2R-006, H2R-030 | Valor |
| RF-H2R-004 | Múltiplos funcionários com mesmos dados bancários | Cruzamento de conta bancária no cadastro de funcionários | ≥ 2 funcionários com mesma conta corrente | Cadastro de funcionários (dados bancários) | H2R-008, H2R-009 | Padrão |
| RF-H2R-005 | Variação de folha acima do esperado sem variação de headcount | Variação % do custo total da folha vs. variação % de headcount | Folha cresce > 5% enquanto headcount está estável ou cai | Folha mensal + relatório de headcount | H2R-021 | Padrão |
| RF-H2R-006 | Funcionários admitidos e desligados em prazo muito curto | Tempo de permanência (dias entre admissão e desligamento) | Permanência < 30 dias com rescisão calculada | Cadastro de RH + histórico de desligamentos | H2R-037, H2R-036 | Padrão |
| RF-H2R-007 | Ex-funcionários ainda recebendo benefícios | Cruzamento de beneficiários ativos com lista de desligados | Qualquer ex-funcionário com benefício ativo após data de desligamento | Lista de beneficiários (plano de saúde, VR, VT) + registro de desligamentos | H2R-023, H2R-037 | Padrão |
| RF-H2R-008 | Aumento salarial acima do reajuste coletivo sem aprovação documentada | Variação salarial individual vs. índice de reajuste do período (ACT/CCT) | Reajuste individual > índice coletivo + 5% sem exceção documentada | Folha comparativa mês a mês por matrícula | H2R-030, H2R-031 | Valor |
| RF-H2R-009 | Funcionários com endereço igual ao de gestor direto | Cruzamento de endereço residencial no cadastro | Qualquer funcionário com mesmo endereço do gestor direto | Cadastro de RH (endereço) + estrutura hierárquica | H2R-005 | Padrão |

---

## RTR — Record-to-Report

| ID | Red Flag | Métrica / Indicador | Limiar Sugerido | Fonte de Dados (IPE) | WCGW Associado | Tipo |
|---|---|---|---|---|---|---|
| RF-RTR-001 | Volume de lançamentos manuais de fim de período acima da média | Quantidade e valor de lançamentos manuais nos últimos 3 dias úteis do período vs. média do período | Volume > 150% da média diária do mês ou valor > 5% da receita do período | Log de lançamentos com data, usuário e tipo (manual vs. automático) | RTR-010, FRA-016 | Timing |
| RF-RTR-002 | Lançamentos manuais em contas incomuns para o tipo de operação | Lançamentos em contas de resultado em módulos que só deveriam gerar lançamentos automáticos | Qualquer lançamento manual em conta de receita sem aprovação de segundo nível | Log de lançamentos por conta contábil e tipo de entrada | RTR-011, FRA-016 | Padrão |
| RF-RTR-003 | Provisões que sistematicamente se revertem no período seguinte | Valor revertido no período M+1 vs. valor constituído em M, por conta de provisão | Reversão > 50% da provisão constituída no período anterior em ≥ 3 períodos consecutivos | Razão de provisões por conta + lançamentos de reversão | RTR-014, FRA-023 | Padrão |
| RF-RTR-004 | Estimativas que sistematicamente melhoram o resultado | Direção do ajuste de estimativas ao longo dos períodos (sempre favorável vs. desfavorável) | Ajuste favorável ao resultado em > 80% dos períodos nos últimos 8 trimestres | Histórico de estimativas e ajustes por conta | RTR-014, FRA-017 | Padrão |
| RF-RTR-005 | Contas com saldo relevante sem movimentação há muito tempo | Contas com saldo > threshold sem lançamento há mais de X meses | Saldo > R$ X sem movimentação há > 6 meses | Razão contábil com data do último lançamento por conta | RTR-003 | Padrão |
| RF-RTR-006 | Margem bruta melhorando enquanto concorrentes pioram | Variação de margem bruta vs. benchmark setorial | Melhora de margem > 3 p.p. sem explicação operacional quando setor apresenta compressão | DRE + dados setoriais públicos (CVM, relatórios de setor) | FRA-027 | Padrão |
| RF-RTR-007 | Lançamentos feitos por usuário incomum ou fora do horário | Usuário e timestamp de lançamentos manuais relevantes | Lançamento > R$ X por usuário que não é do time de contabilidade ou fora do horário comercial | Log de lançamentos com usuário e timestamp | RTR-009, FRA-014 | Timing |

---

## FA — Fixed Assets

| ID | Red Flag | Métrica / Indicador | Limiar Sugerido | Fonte de Dados (IPE) | WCGW Associado | Tipo |
|---|---|---|---|---|---|---|
| RF-FA-001 | CIP (obra em andamento) sem transferência ao ativo final há muito tempo | Tempo em dias desde último lançamento em conta de CIP por projeto | CIP sem movimentação há > 12 meses com saldo > R$ X | Razão de contas de CIP com data do último lançamento | FA-005 | Padrão |
| RF-FA-002 | Ativos totalmente depreciados com valor residual zero ainda em uso operacional | Ativos com saldo líquido = 0 mas com centro de custo ativo | > 20% do imobilizado bruto com saldo líquido zero sem análise de extensão de vida útil | Relatório de imobilizado com valor bruto, depreciação acumulada e centro de custo | FA-016 | Padrão |
| RF-FA-003 | CAPEX crescendo sem correspondência em capacidade operacional ou receita | Variação % de CAPEX vs. variação % de receita ou volume produzido | CAPEX cresce > 20% enquanto receita/volume estagnados ou caem | Relatório de CAPEX + dados operacionais + DRE | FA-001, FA-002 | Padrão |
| RF-FA-004 | Alienações de ativos sem ganho nem perda — preço exatamente igual ao valor contábil | Resultado de alienação (ganho/perda) por transação | Resultado = 0 em > 30% das alienações do período | Relatório de baixas e alienações com valor contábil e preço de venda | FA-028, FA-030 | Padrão |
| RF-FA-005 | Despesas de manutenção com pico atípico — possível capitalização indevida invertida | Variação % da conta de manutenção e reparo vs. período anterior | Aumento > 30% na conta de manutenção sem aumento correspondente em ativos capitalizados | Razão de contas de manutenção + relatório de adições ao imobilizado | FA-001, FA-003 | Valor |
| RF-FA-006 | Ativo adquirido de parte relacionada com valor discrepante do mercado | Preço pago vs. avaliação de mercado para ativo equivalente | Diferença > 15% do valor de mercado sem avaliação independente documentada | Relatório de aquisições + registro de partes relacionadas | FA-006 | Valor |

---

## UAM — User Access Management

| ID | Red Flag | Métrica / Indicador | Limiar Sugerido | Fonte de Dados (IPE) | WCGW Associado | Tipo |
|---|---|---|---|---|---|---|
| RF-UAM-001 | Usuários com último login há muito tempo mas conta ativa | Diferença em dias entre data do último login e data de análise | Sem login há > 90 dias com conta ativa e sem justificativa (conta de serviço, licença) | Relatório de usuários com data do último login (AD ou ERP) | UAM-019, UAM-013 | Padrão |
| RF-UAM-002 | Logins fora do horário comercial em sistemas sensíveis | Timestamp de logins em sistemas financeiros (ERP, banking) | Login em sistema financeiro antes das 6h ou após 22h ou em feriado/fim de semana | Log de acesso do sistema com timestamp | UAM-027, FRA-014 | Timing |
| RF-UAM-003 | Logins simultâneos para o mesmo usuário | Sessões ativas simultâneas para a mesma credencial | ≥ 2 sessões simultâneas para o mesmo usuário | Log de sessões do sistema | UAM-026 | Padrão |
| RF-UAM-004 | Acessos de ex-funcionários ativos após data de desligamento | Cruzamento de data de desligamento (RH) com data do último login no sistema | Qualquer login após a data de desligamento | Lista de desligados do período + log de acesso | UAM-013, UAM-015 | Timing |
| RF-UAM-005 | Usuário com perfis de módulos sem relação com função exercida | Comparação do perfil de acesso com cargo/função do usuário | Acesso a módulo com nenhuma relação com o cargo (ex: usuário de RH com acesso a módulo bancário) | Lista de usuários com perfis + organograma com funções | UAM-009, UAM-012 | Padrão |
| RF-UAM-006 | Volume anormal de transações por usuário específico | Quantidade de transações por usuário vs. média dos usuários com mesmo perfil | Usuário com > 3x a média de transações dos pares sem justificativa operacional | Log de transações por usuário no período | UAM-028, FRA-007 | Frequência |
| RF-UAM-007 | Concessões de acesso sem chamado de solicitação correspondente | Acessos concedidos no período sem ticket de solicitação vinculado | Qualquer concessão sem chamado aprovado | Log de concessões de acesso + sistema de chamados | UAM-001, UAM-007 | Padrão |

---

## Leitura Rápida — Red Flags de Maior Impacto Cruzado

| Red Flag | Processos | IDs | Por que priorizar |
|---|---|---|---|
| Dados bancários de fornecedor = funcionário | P2P + H2R | RF-P2P-001 | Sinal clássico de ghost employee + desvio de pagamento |
| Clustering abaixo do limite de aprovação | P2P | RF-P2P-003, RF-P2P-010 | Fracionamento deliberado para evitar controle |
| Provisões que se revertem sistematicamente | RTR | RF-RTR-003 | Manipulação de resultado entre períodos |
| Lançamentos manuais fora do horário | RTR + UAM | RF-RTR-007, RF-UAM-002 | Override de controle sem supervisão |
| NFs concentradas no fim do período | OTC | RF-OTC-002 | Antecipação de receita para atingir meta |
| Ex-funcionário com login após desligamento | UAM | RF-UAM-004 | Risco de segurança + fraude potencial |
| Horas extras em funcionário sem ponto | H2R | RF-H2R-001 | Pagamento fictício sem suporte operacional |
| CIP parada > 12 meses | FA | RF-FA-001 | Ativo capitalizado que pode nunca entrar em uso |
