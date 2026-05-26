---
lista: sod-matrix
tipo: master-list
descricao: Pares de funções incompatíveis por processo, com criticidade, sistemas envolvidos e controles compensatórios
processos:
  - P2P
  - OTC
  - H2R
  - RTR
  - FA
  - UAM
uso:
  - risk-control-mapping
  - walkthrough-standardization
  - test-execution
  - audit-planning
criterio_criticidade:
  Alta: conflito viabiliza fraude ou erro material sem detecção — uma pessoa controla o ciclo inteiro
  Média: conflito aumenta risco mas não viabiliza fraude isolada — requer cumplicidade ou acesso adicional
---

# Matriz SoD — Segregação de Funções por Processo

SoD identifica onde uma única pessoa pode iniciar, executar e encobrir uma transação irregular. O risco não é abstrato: cada conflito abaixo é um cenário concreto onde fraude ou erro material pode ocorrer sem detecção por controles normais.

**Como usar:** ao mapear um processo, cruzar as funções mapeadas com os pares abaixo. Conflito identificado → verificar se existe controle compensatório ativo e testável.

---

## P2P — Procure-to-Pay

| ID | Função A | Função B | Risco do Conflito | Criticidade | Sistemas | Controle Compensatório |
|---|---|---|---|---|---|---|
| SOD-P2P-001 | Cadastro de fornecedor | Aprovação de pagamento | Cadastra fornecedor fictício e aprova pagamento | Alta | ERP (mestre de fornecedores + contas a pagar) | Revisão independente de novos fornecedores; aprovação de pagamento por alçada separada |
| SOD-P2P-002 | Cadastro de fornecedor | Emissão de ordem de compra | Direciona compra para fornecedor criado por si mesmo | Alta | ERP | Aprovação de OC por gestor independente do cadastro |
| SOD-P2P-003 | Aprovação de OC | Recebimento de mercadoria | Aprova compra e confirma recebimento sem verificação real | Alta | ERP (módulo compras + recebimento) | Recebimento físico documentado por área operacional independente |
| SOD-P2P-004 | Aprovação de pagamento | Execução de remessa bancária | Aprova e executa pagamento — ciclo financeiro inteiro | Alta | ERP + internet banking / sistema de pagamentos | Segundo autorizador na remessa; token em poder de pessoa diferente |
| SOD-P2P-005 | Lançamento de NF de fornecedor | Aprovação de pagamento | Lança NF e aprova pagamento correspondente | Alta | ERP (AP) | Aprovação de pagamento por pessoa que não lançou a NF |
| SOD-P2P-006 | Solicitação de compra | Aprovação de OC | Solicita e aprova a própria compra | Média | ERP | Aprovação por gestor acima do solicitante; threshold para autoapprovação zero |
| SOD-P2P-007 | Alteração de dados bancários de fornecedor | Aprovação de pagamento | Redireciona conta e aprova remessa | Alta | ERP (mestre fornecedores) + sistema bancário | Dupla aprovação para alteração de dados bancários; notificação automática ao fornecedor |

---

## OTC — Order-to-Cash

| ID | Função A | Função B | Risco do Conflito | Criticidade | Sistemas | Controle Compensatório |
|---|---|---|---|---|---|---|
| SOD-OTC-001 | Cadastro de cliente | Aprovação de pedido | Cadastra cliente fictício e aprova pedido para desvio | Alta | ERP / CRM | Segregação no sistema; aprovação de pedido por área comercial independente do cadastro |
| SOD-OTC-002 | Definição de limite de crédito | Aprovação de pedido acima do limite | Ignora critério de crédito que ele mesmo definiu | Alta | ERP / sistema de crédito | Limite de crédito definido por área de risco independente do comercial |
| SOD-OTC-003 | Registro de entrega | Emissão de nota fiscal | Confirma entrega fictícia e emite NF correspondente | Alta | ERP / sistema fiscal (NF-e) | Entrega confirmada por romaneio de transportadora antes de NF ser emitida |
| SOD-OTC-004 | Emissão de nota fiscal | Baixa de recebível | Emite NF e baixa título sem recebimento real | Alta | ERP (AR) | Conciliação bancária independente; baixa requer identificação de recebimento bancário |
| SOD-OTC-005 | Recebimento de pagamento | Baixa de título no sistema | Desvia recebimento e não registra — ou lança para conta errada | Alta | ERP (AR) + conta bancária | Conciliação bancária diária por pessoa independente de quem faz baixa |
| SOD-OTC-006 | Concessão de desconto | Aprovação de desconto | Aprova desconto acima da própria alçada | Alta | ERP / sistema comercial | Tabela de alçadas sistêmica que bloqueia aprovação pelo próprio concessor |
| SOD-OTC-007 | Renegociação de dívida | Aprovação de write-off | Renegocia condições e dá baixa como irrecuperável | Alta | ERP (AR) | Aprovação de write-off por alçada separada; revisão periódica pelo CFO |

---

## H2R — Hire-to-Retire

| ID | Função A | Função B | Risco do Conflito | Criticidade | Sistemas | Controle Compensatório |
|---|---|---|---|---|---|---|
| SOD-H2R-001 | Cadastro de funcionário | Processamento de folha | Cadastra funcionário fictício e processa pagamento | Alta | Sistema de RH / folha (ADP, SAP HCM, Datasul) | Segregação sistêmica entre módulo de cadastro e processamento; relatório de novos cadastros revisado independentemente |
| SOD-H2R-002 | Alteração de dados bancários | Processamento de folha | Redireciona salário e processa pagamento para conta própria | Alta | Sistema de RH / folha | Dupla aprovação para alteração de dados bancários; notificação por e-mail ao funcionário titular |
| SOD-H2R-003 | Aprovação de horas extras | Beneficiário das horas extras | Aprova as próprias horas extras sem supervisão | Alta | Ponto eletrônico / sistema de RH | Aprovação de horas extras pelo gestor direto do beneficiário, nunca pelo próprio |
| SOD-H2R-004 | Cadastro de funcionário | Aprovação de desligamento | Impede desligamento de funcionário fictício que criou | Média | Sistema de RH | Desligamento aprovado por gestor e RH independentes do cadastro |
| SOD-H2R-005 | Preparação da folha | Aprovação da folha | Processa e aprova folha sem revisão independente | Alta | Sistema de folha | Aprovação formal da folha pelo gestor financeiro antes do pagamento |
| SOD-H2R-006 | Gestão de benefícios | Elegibilidade de benefícios | Define e concede benefício a si mesmo ou a inelegíveis | Média | Sistema de RH / operadoras | Lista de elegibilidade mantida por RH; revisão periódica por área independente |

---

## RTR — Record-to-Report

| ID | Função A | Função B | Risco do Conflito | Criticidade | Sistemas | Controle Compensatório |
|---|---|---|---|---|---|---|
| SOD-RTR-001 | Preparação de lançamento manual | Aprovação de lançamento manual | Lança e aprova ajuste sem revisão independente | Alta | ERP (módulo contábil) | Workflow de aprovação sistêmico; autoapprovação bloqueada pelo sistema |
| SOD-RTR-002 | Preparação de reconciliação | Aprovação de reconciliação | Reconcilia e aprova sem detecção de erros ou omissões | Alta | ERP / planilha de reconciliação | Aprovador diferente do preparador com acesso independente ao razão |
| SOD-RTR-003 | Elaboração das demonstrações financeiras | Aprovação das demonstrações | Prepara e aprova o reporte sem revisão do CFO/CA | Alta | Sistema contábil / consolidação | Aprovação formal pelo CFO; revisão do Comitê de Auditoria para demonstrações anuais |
| SOD-RTR-004 | Acesso de super user ao ERP | Revisão de lançamentos manuais | Faz ajuste e revisa o próprio ajuste — ou apaga trilha | Alta | ERP (perfil administrador) | Log imutável de ações de super user; revisão por auditoria interna ou TI independente |
| SOD-RTR-005 | Definição de estimativas contábeis | Aprovação das estimativas | Define provisão ou impairment e aprova o valor | Alta | ERP / sistema de consolidação | Revisão de estimativas por Controller ou auditoria interna independente da área que definiu |

---

## FA — Fixed Assets

| ID | Função A | Função B | Risco do Conflito | Criticidade | Sistemas | Controle Compensatório |
|---|---|---|---|---|---|---|
| SOD-FA-001 | Aprovação de CAPEX | Recebimento físico do ativo | Aprova compra e confirma recebimento sem verificação | Média | ERP (módulo imobilizado) | Recebimento confirmado por área operacional independente de quem aprovou |
| SOD-FA-002 | Registro de ativo no sistema | Aprovação de baixa do ativo | Cria ativo e também o baixa — ciclo sem verificação | Alta | ERP (módulo imobilizado) | Aprovação de baixa por alçada separada do responsável pelo registro |
| SOD-FA-003 | Custódia física do ativo | Inventário físico do ativo | Conta o próprio inventário — pode ocultar desvio | Alta | Sistema de inventário / ERP | Inventário conduzido por equipe independente da custódia |
| SOD-FA-004 | Solicitação de alienação | Aprovação de alienação | Propõe e aprova venda de ativo — potencial desvio de valor | Alta | ERP (módulo imobilizado) | Aprovação de alienação por alçada superior com base no valor contábil |
| SOD-FA-005 | Definição de vida útil / depreciação | Aprovação dos parâmetros de depreciação | Define e valida estimativa que impacta diretamente o resultado | Média | ERP (parâmetros do imobilizado) | Revisão anual de vida útil aprovada pelo Controller com base técnica documentada |

---

## UAM — User Access Management

| ID | Função A | Função B | Risco do Conflito | Criticidade | Sistemas | Controle Compensatório |
|---|---|---|---|---|---|---|
| SOD-UAM-001 | Solicitação de acesso | Aprovação de acesso | Solicita e aprova o próprio acesso | Alta | Sistema de chamados (ServiceNow, GLPI, Jira) | Aprovação obrigatória por gestor direto diferente do solicitante |
| SOD-UAM-002 | Aprovação de acesso | Concessão técnica de acesso | Aprova e executa — sem verificação cruzada | Média | AD / ERP / sistemas aplicativos | TI verifica chamado aprovado antes de conceder; log de concessão vinculado ao chamado |
| SOD-UAM-003 | Administração de usuários no sistema | Revisão periódica de acessos do sistema | Cria acessos e revisa a própria lista | Alta | AD / ERP | Revisão conduzida por área de GRC ou auditoria interna com extração direta do sistema |
| SOD-UAM-004 | Gestão de perfis de acesso (TI) | Uso dos perfis em transações de negócio | TI com acesso irrestrito pode executar transações financeiras | Alta | ERP (SAP, Oracle, TOTVS) | Perfis administrativos de TI sem permissão de execução de transações de negócio |
| SOD-UAM-005 | Concessão de acesso privilegiado | Monitoramento de uso privilegiado | Concede super user e monitora o próprio uso | Alta | ERP / AD (conta admin) | Log de uso de contas privilegiadas revisado por área independente (GRC, auditoria interna) |

---

## Leitura Rápida — Conflitos de Maior Impacto

| Conflito | Processo | ID | Por que é crítico |
|---|---|---|---|
| Cadastra fornecedor + aprova pagamento | P2P | SOD-P2P-001 | Ciclo completo de fraude com fornecedor fictício |
| Aprova + executa remessa bancária | P2P | SOD-P2P-004 | Desvio sem segundo olhar |
| Altera dados bancários + processa folha | H2R | SOD-H2R-002 | Ghost employee ou redirecionamento de salário |
| Cadastra funcionário + processa folha | H2R | SOD-H2R-001 | Clássico de ghost employee |
| Prepara + aprova lançamento manual | RTR | SOD-RTR-001 | Manipulação de fechamento sem detecção |
| Registra + baixa recebível | OTC | SOD-OTC-004 | Desvio de recebimento sem rastro |
| Administra usuários + revisa acessos | UAM | SOD-UAM-003 | SoD sobre o próprio controlador de SoD |
| Super user + monitoramento de privilegiados | UAM | SOD-UAM-005 | Conflito que anula todos os outros controles |
