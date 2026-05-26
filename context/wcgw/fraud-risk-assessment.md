---
processo: fraud-risk-assessment
nivel: 1
abreviacao: FRA
subprocessos:
  - triangulo-da-fraude
  - oportunidade-e-controles-fracos
  - management-override
  - manipulacao-de-reporte
assercoes_primarias:
  - existência
  - valoração
  - apresentação
frameworks:
  - COSO ERM
  - NBC TA 240
  - ACFE Fraud Triangle
referencias:
  - _method-wiki/processes/fraud-risk-assessment.md
  - _method-wiki/processes/journal-entry-testing.md
  - _method-wiki/processes/entity-level-controls.md
---

# WCGW — Fraud Risk Assessment (FRA)

Fraude difere de erro: pressupõe **intenção**. O risco não é que alguém cometa um engano — é que alguém, com motivação e oportunidade, tome decisão deliberada de distorcer, ocultar ou desviar.

O assessment de fraude não termina em "listamos os fatores de risco". Termina quando cada fator identificado tem uma resposta de auditoria específica. Fator sem resposta é análise incompleta.

---

## Subprocesso 1: Triângulo da Fraude — Identificação de Fatores

O triângulo de Cressey: **incentivo + oportunidade + racionalização**. Os três precisam estar presentes para fraude ocorrer. O auditor busca sinais de cada vértice.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| FRA-001 | Pressão por resultado não convertida em risco específico — "metas agressivas" sem definir o que pode ser manipulado | Initiation | Existência | Alta |
| FRA-002 | Incentivos financeiros atrelados a métricas que a gestão pode influenciar diretamente | Initiation | Existência | Alta |
| FRA-003 | Dificuldades financeiras pessoais da gestão não consideradas no assessment | Initiation | Existência | Média |
| FRA-004 | Racionalização documentada em e-mails ou comportamentos não capturada na análise | Initiation | Existência | Média |
| FRA-005 | Assessment encerrado com fatores genéricos sem conexão com o modelo de negócio específico | Initiation | Existência | Alta |
| FRA-006 | Risco de fraude presumido de receita não avaliado — NBC TA 240 exige presunção explícita | Initiation | Existência | Alta |

**O que investigar em cada vértice:**

**Incentivo / Pressão:**
- metas de resultado com bônus atrelado
- empresa em processo de venda, IPO ou captação
- covenants bancários próximos de serem violados
- pressão de acionistas controladores por distribuição de resultado
- situação financeira pessoal de executivos com ações ou dívidas relevantes

**Oportunidade:**
- controles fracos ou ausentes nas áreas de maior risco
- gestão com acesso irrestrito ao ERP
- ausência de revisão independente sobre estimativas e provisões
- processos de exceção sem rastreabilidade

**Racionalização:**
- narrativa de "estamos em momento difícil, isso é temporário"
- histórico de pequenos ajustes que individualmente pareceram razoáveis
- cultura organizacional de que fins justificam meios

---

## Subprocesso 2: Oportunidade — Controles Fracos que Viabilizam Fraude

A oportunidade é o único vértice que o auditor pode influenciar diretamente. Identificar onde controles fracos criam janela para fraude.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| FRA-007 | Segregação de funções inexistente em processos de alto risco — uma pessoa controla ciclo completo | Processing | Existência | Alta |
| FRA-008 | Acesso irrestrito ao ERP para executivos que também aprovam transações relevantes | Processing | Existência | Alta |
| FRA-009 | Ausência de revisão independente sobre estimativas significativas | Processing | Valoração | Alta |
| FRA-010 | Processos de exceção sem rastreabilidade — override não documentado | Processing | Existência | Alta |
| FRA-011 | Conta bancária corporativa sem conciliação regular ou revisão independente | Processing | Existência | Alta |
| FRA-012 | Transações com partes relacionadas sem aprovação independente | Processing | Existência | Alta |
| FRA-013 | Ausência de surprise procedures — padrões previsíveis que o fraudador aprende a contornar | Processing | Existência | Média |

**Resposta de auditoria para oportunidade identificada:**
- ampliar tamanho de amostra nas áreas com controles fracos
- incluir procedimentos substantivos onde antes havia reliance em controles
- realizar procedimentos surpresa (timing diferente do esperado)
- testar transações acima e abaixo de thresholds de aprovação

---

## Subprocesso 3: Management Override

Override é o risco presumido mais relevante em auditoria — a gestão pode contornar controles que funcionam normalmente para outros usuários.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| FRA-014 | Gestão com acesso de super user ao ERP — pode criar, aprovar e modificar qualquer transação | Processing | Existência | Alta |
| FRA-015 | Controles dependem da integridade da gestão sem mecanismo de detecção independente | Processing | Existência | Alta |
| FRA-016 | Lançamentos manuais de fim de período aprovados pela própria gestão sem revisão | Processing | Valoração | Alta |
| FRA-017 | Estimativas e provisões definidas pela gestão sem metodologia verificável | Processing | Valoração | Alta |
| FRA-018 | Transações incomuns próximas ao fechamento sem documentação adequada | Recording | Existência | Alta |
| FRA-019 | Histórico de ajustes recorrentes de fim de período que sempre melhoram o resultado | Processing | Valoração | Crítico |
| FRA-020 | Gestão pressiona a equipe de auditoria para reduzir escopo ou aceitar evidência inadequada | Processing | Existência | Alta |

**Resposta específica para override:**
- testar journal entries com foco em lançamentos manuais de fim de período
- revisar estimativas contábeis em busca de viés sistemático (sempre otimistas = sinal)
- confrontar comprometimentos com partes relacionadas e suas aprovações
- verificar se existem transações reversas ou ajustes recorrentes de mesma natureza
- desafiar justificativas da gestão com evidência independente

---

## Subprocesso 4: Manipulação de Reporte Financeiro

Fraude de reporte: distorção intencional das demonstrações financeiras para enganar usuários externos (investidores, banco, regulador).

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| FRA-021 | Reconhecimento antecipado de receita sem base contratual ou entrega efetiva | Recording | Corte | Alta |
| FRA-022 | Despesas diferidas artificialmente para melhorar resultado do período | Recording | Valoração | Alta |
| FRA-023 | Provisões revertidas indevidamente para inflar resultado | Processing | Valoração | Alta |
| FRA-024 | Transações fictícias ou circulares com partes relacionadas para aparentar volume ou resultado | Recording | Existência | Crítico |
| FRA-025 | Omissão de passivos ou contingências relevantes das demonstrações | Reporting | Completude | Alta |
| FRA-026 | Classificação inadequada de itens para melhorar métricas específicas (EBITDA, capital de giro) | Reporting | Apresentação | Alta |
| FRA-027 | Manipulação de estoques ou ativos para distorcer posição patrimonial | Recording | Valoração | Crítico |

**Sinais de alerta em reporte:**
- crescimento de receita inconsistente com setor ou operação
- margens melhorando enquanto concorrentes pioram sem explicação operacional clara
- acúmulo de recebíveis ou estoques sem correspondência com volume de negócios
- provisões que sistematicamente se revertem no período seguinte
- aumento de contas a pagar com fornecedores pouco conhecidos

**Armadilha crítica:** auditor que testa transações individualmente mas não lê as demonstrações como um todo pode perder padrões de manipulação que só aparecem na visão consolidada.

---

## Leitura Rápida por Risco

| Risco Central | Subprocessos Críticos | WCGW-chave |
|---|---|---|
| Assessment genérico sem resposta | Triângulo | FRA-001, FRA-005 |
| Receita presumida de fraude não avaliada | Triângulo | FRA-006 |
| Controles fracos criam oportunidade | Oportunidade | FRA-007, FRA-010, FRA-012 |
| Management override não coberto | Override | FRA-014, FRA-016, FRA-019 |
| Manipulação de receita / corte | Reporte | FRA-021, FRA-024 |
| Passivos omitidos | Reporte | FRA-025 |
| Pressão sobre o auditor | Override | FRA-020 |
