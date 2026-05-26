# Procure-to-Pay

## Papel

Hub metodológico para o processo de compras e contas a pagar, cobrindo fluxo operacional, integrações sistêmicas, alçadas, cadastro de fornecedor e pontos de controle relevantes.

## Quando usar

- mapear processo P2P para risco-controle-teste
- revisar desenho de compras, aprovação e pagamento
- identificar riscos de integração entre sistemas auxiliares e ERP
- estruturar walkthrough ou RCM de compras e contas a pagar

## Objetivo

Oferecer um blueprint reutilizável para mapear o processo P2P, identificar riscos relevantes e estruturar controles e testes sem depender de narrativa específica de um cliente.

## Fluxo-base

### 1. Compras

- requisição de compra
- validação orçamentária
- aprovações por alçada
- concorrência, cotação ou contratação
- captura de exceções ou justificativas fora do fluxo padrão

### 2. Recebimento de Bens e Serviços

- confirmação de entrega física ou prestação de serviço
- registro de nota fiscal no sistema (entrada de mercadoria / serviço)
- conferência entre o que foi pedido (PO), o que foi entregue (recebimento) e o que foi faturado (NF) — three-way match
- tratamento de divergências: quantidade, valor, especificação ou prazo
- aceitação formal pelo requisitante ou área técnica (para serviços)

### 3. Contas a pagar

- solicitação ou cálculo de pagamento
- aprovação
- remessa bancária
- retorno bancário
- tratamento de rejeições, divergências ou exceções

### 4. Integrações sensíveis

- portais de fornecedor
- sistemas de orçamento
- soluções auxiliares de procurement
- captura fiscal
- ERP e módulos financeiros

## Riscos recorrentes

- integração incompleta entre sistemas auxiliares e ERP
- aprovação fora de alçada
- cadastro inadequado de fornecedor
- fragilidade de compliance no onboarding ou na manutenção cadastral
- falhas de segregação de funções entre solicitação, aprovação e pagamento
- exceções de pagamento sem rastreabilidade suficiente
- rejeições bancárias tratadas manualmente sem revisão adequada
- concorrência ou cotação bypassada sem racional claro
- pagamento sem confirmação de recebimento — NF paga sem entrada registrada no sistema
- three-way match bypassado — NF aprovada para pagamento com divergência de quantidade ou valor não resolvida
- recebimento registrado por quem solicitou — sem separação entre quem pediu e quem confirma a entrega
- NF aceita sem aceitação formal do requisitante para serviços — risco de pagar serviço não prestado ou incompleto
- divergências de recebimento tratadas informalmente — sem registro sistêmico, sem rastreabilidade

## Controles esperados

- política clara de alçadas
- validação orçamentária antes de contratar ou aprovar
- cadastro de fornecedor com revisão de compliance
- segregação entre requisição, aprovação, cadastro e pagamento
- tratamento formal de rejeições e exceções bancárias
- reconciliação entre sistemas auxiliares e ERP quando houver integração relevante
- critérios documentados para exceção de cotação ou contratação direta
- three-way match sistêmico: bloqueio de pagamento quando PO × recebimento × NF divergem além da tolerância configurada
- separação entre quem solicita e quem confirma o recebimento (SoD de recebimento)
- aceitação formal de serviços pelo requisitante antes da liberação de pagamento
- registro obrigatório de divergências de recebimento com rastreabilidade e resolução documentada

## Evidências típicas

- política de compras e alçadas
- fluxo ou narrativa do processo
- cadastro de fornecedor e suportes de compliance
- trilha de aprovações
- evidência de remessa e retorno bancário
- logs ou relatórios de integração entre sistemas
- relatório de entradas de mercadoria / serviço (MIGO ou equivalente no ERP)
- evidência de three-way match: relatório de NFs bloqueadas por divergência e resolução documentada
- aceitações formais de serviço (e-mail, formulário ou assinatura no sistema)
- registro de divergências de recebimento e tratamento dado

## Perguntas de revisão

- onde o processo pode ser contornado sem deixar trilha?
- quais integrações são críticas para completude e precisão do passivo?
- quem consegue cadastrar, aprovar e pagar?
- como exceções e rejeições são capturadas e revisadas?
- em que ponto a validação orçamentária realmente bloqueia a operação?
- é possível pagar uma NF sem entrada de mercadoria ou serviço registrada?
- o three-way match é sistêmico (bloqueia automaticamente) ou manual (depende de alguém verificar)?
- quem confirma o recebimento? é a mesma pessoa que fez o pedido?
- como divergências de recebimento são registradas e resolvidas — há rastreabilidade?
- serviços têm aceitação formal antes do pagamento ou seguem fluxo igual a mercadorias?

## Artefatos relacionados

- `patterns/revenue-billed-vs-unbilled-reconciliation.md`
- `processes/audit-engagement-execution.md`
