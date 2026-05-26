# Journal Entry Testing

## Papel

Hub metodológico para teste de journal entries (JE), com foco em risco presumido de management override, definição de população, seleção baseada em risco, uso de data analytics, documentação do julgamento e execução do teste ao longo do ano.

## Quando usar

- responder ao risco presumido de management override
- estruturar programa de JE testing
- definir critérios de seleção e recortes de JE
- orientar equipe sobre documentação, evidência e ceticismo em JE

## Objetivo do procedimento

O teste de JE deve responder explicitamente ao risco de management override e complementar lacunas deixadas por outros procedimentos. A cobertura não deve se limitar a lançamentos “estranhos”; ela precisa refletir o entendimento do processo de reporte financeiro, as contas significativas e os cenários em que manipulação pode ocorrer.

## Sequência recomendada

### 1. Entendimento inicial

- entender o processo de reporte financeiro e os pontos onde podem ocorrer lançamentos inapropriados
- inquirir pessoas-chave sobre atividades incomuns, ajustes relevantes e práticas não usuais
- identificar contas, classes de lançamento e momentos de maior risco

### 2. Definição da população

- confirmar integridade e acurácia da base de JE antes de selecionar itens
- incluir lançamentos de fim de período e pós-fechamento
- considerar origem, preparador, aprovador, timing, conta e natureza do lançamento

### 3. Seleção baseada em risco

- usar abordagem top-down para priorizar lançamentos de maior risco
- combinar filtros objetivos com julgamento executivo da equipe
- documentar por que cada recorte foi escolhido e qual risco ele pretende cobrir

### 4. Execução do teste

- para cada JE selecionado, testar justificativa de negócio
- validar autorização
- revisar contabilização e período
- confrontar suporte documental e finalidade econômica do lançamento

### 5. Reavaliação contínua

- atualizar o risco de override conforme novas evidências
- expandir ou ajustar a seleção quando surgirem sinais de maior risco
- desafiar se o entendimento do risco é suficiente antes de concluir

## Data analytics em JE

- data analytics pode fortalecer abordagem top-down e baseada em risco
- deve melhorar entendimento do processo contábil e da possibilidade de override
- não substitui julgamento: ajuda a priorizar itens, recortes e atributos de maior risco
- quando viável, usar 100% da base para triagem e aplicar teste detalhado sobre subconjuntos relevantes

## Atributos típicos de maior risco

- lançamentos de fim de período
- lançamentos pós-fechamento
- lançamentos manuais ou fora do fluxo normal
- usuários, fontes ou combinações de contas pouco usuais
- lançamentos sem racional econômico claro
- lançamentos em contas e classes significativas com histórico de risco

## Critérios práticos de seleção

- combinar período, preparador, autorizador e natureza do lançamento
- observar itens incomuns, manuais, concentrados em certos usuários ou próximos ao fechamento
- sustentar a seleção com racional de negócio e risco, não apenas com filtro automático

## Regras de documentação

- conectar objetivo do procedimento, risco avaliado e estratégia de seleção
- documentar o julgamento da equipe na definição de recortes
- demonstrar por que os itens escolhidos respondem ao risco de override
- registrar discussão técnica quando atributos de maior risco exigirem debate adicional

## Armadilhas comuns

- testar JE como rotina mecânica, sem conexão explícita com o risco de override
- selecionar lançamentos sem explicar o racional de risco
- confiar apenas em filtros automáticos sem entendimento do processo
- concluir sem revisar se a cobertura alcançou cenários de maior risco

## Evidências úteis

- justificativa de negócio
- suporte documental do lançamento
- trilha de aprovação
- coerência entre contabilização, período e finalidade econômica

## Artefatos relacionados

- `heuristics/audit-bias-and-judgment-calibration.md`
- `patterns/misstatement-response-and-materiality-reassessment.md`
