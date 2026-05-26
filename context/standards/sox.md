# SOX — Sarbanes-Oxley Act

Referencial primario para controles internos sobre relatorio financeiro (ICFR) em companhias listadas nos EUA e subsidiarias de grupos sujeitos a lei. Esta referencia pertence primariamente a trilha de auditoria externa / ICFR / SOX e deve ser combinada com `_method-wiki-external-audit/`.

---

## 1. Seções Relevantes para Auditoria Interna

| Seção | Escopo | Relevância operacional |
|---|---|---|
| Section 302 | CEO/CFO certificam trimestralmente a eficácia dos controles de disclosure | Controles de reporte, sub-certificação por área |
| Section 404(a) | Management Assessment: avaliação anual da eficácia dos ICFR | Escopo de controles, metodologia de avaliação, relatório de management |
| Section 404(b) | Auditor externo atesta a avaliação do management (só para large accelerated filers) | Alinhamento entre auditoria interna e externa; escopo de reliance |
| Section 409 | Disclosure em tempo real de eventos materiais | Relevante para controles de monitoramento e reporting |

---

## 2. Framework de Controle — COSO 2013

SOX 404 exige que o management use um framework reconhecido. O padrão de mercado é o **COSO Internal Control — Integrated Framework (2013)**.

### 5 Componentes COSO

| Componente | O que cobre | Pontos de atenção em auditoria |
|---|---|---|
| **Control Environment** | Tone at the top, valores, estrutura de governança, competência | ELC (Entity-Level Controls): código de conduta, comitê de auditoria, avaliação de RH |
| **Risk Assessment** | Identificação e análise de riscos aos objetivos | Fraud risk assessment obrigatório; mudanças no ambiente de negócio |
| **Control Activities** | Políticas e procedimentos que endereçam os riscos | Controles preventivos vs. detectivos; ITGCs e controles de aplicação |
| **Information & Communication** | Qualidade e fluxo de informação relevante | IPE (Information Produced by the Entity); trilha de auditoria |
| **Monitoring** | Avaliações contínuas e separadas; comunicação de deficiências | Management review controls; self-assessment |

### 17 Princípios COSO (mapeados por componente)

| # | Princípio | Componente |
|---|---|---|
| 1 | Comprometimento com integridade e valores éticos | Control Environment |
| 2 | Independência do board na supervisão | Control Environment |
| 3 | Estrutura organizacional, autoridade e responsabilidade | Control Environment |
| 4 | Comprometimento com competência | Control Environment |
| 5 | Accountability | Control Environment |
| 6 | Objetivos claros para identificar riscos | Risk Assessment |
| 7 | Identificação e análise de riscos | Risk Assessment |
| 8 | Avaliação de risco de fraude | Risk Assessment |
| 9 | Identificação e análise de mudanças significativas | Risk Assessment |
| 10 | Seleção e desenvolvimento de atividades de controle | Control Activities |
| 11 | Controles gerais de tecnologia (ITGC) | Control Activities |
| 12 | Implementação via políticas e procedimentos | Control Activities |
| 13 | Informação relevante, de qualidade e oportuna | Information & Communication |
| 14 | Comunicação interna eficaz | Information & Communication |
| 15 | Comunicação com partes externas | Information & Communication |
| 16 | Avaliações contínuas e/ou separadas | Monitoring |
| 17 | Comunicação de deficiências | Monitoring |

---

## 3. Classificação de Deficiências de Controle

Critério central para rating de achados em contexto SOX. A classificação determina obrigações de reporte e impacto no relatório de management (404(a)).

> Fonte expandida: referencial metodológico consolidado, 

### 3.1 Hierarquia de Severidade

| Nível | Definição | Obrigação de reporte |
|---|---|---|
| **Exception / Deviation** | Achado pontual que não chega a configurar deficiência; pode sinalizar problema em conjunto com outros | Nenhuma obrigação formal; documentar e monitorar |
| **Control Deficiency** | Controle ausente ou não opera como desenhado | Nenhuma obrigação de reporte externo; corrigir internamente |
| **Significant Deficiency** | Deficiência (ou combinação) menos severa que MW, mas importante o suficiente para atenção da governança | Reportar ao comitê de auditoria por escrito |
| **Material Weakness** | Deficiência (ou combinação) com possibilidade razoável (*reasonable possibility*) de misstatement material não ser prevenido ou detectado tempestivamente | Divulgação obrigatória no relatório 404(a); impede assertiva de controles eficazes |

> **Reasonable possibility** = o evento é "reasonably possible" ou "probable" (FASB ASC 450 / FAS 5). Não é "mais do que remoto" — é o próximo nível acima de remoto.

---

### 3.2 Dois Tipos de Deficiência

| Tipo | Definição | Exemplo |
|---|---|---|
| **Design Deficiency** | Controle necessário está ausente, ou o controle existente não está desenhado para atingir o objetivo de controle mesmo se operar corretamente | Ausência de controle sobre classificação GAAP de receitas; processo de aprovação que não cobre todas as transações acima do limite |
| **Operating Deficiency** | Controle bem desenhado não opera confiável ou consistentemente, ou o executor não tem qualificação/autoridade para executá-lo | Reconciliação bancária realizada mas sem revisão independente; aprovações obtidas mas sem verificação dos documentos de suporte |

---

### 3.3 Framework de Avaliação de Severidade

#### Passo 1 — Likelihood (Probabilidade de Misstatement)

A probabilidade já está satisfeita quando:
- O controle está ausente (design deficiency): 100% — sem controle, o risco não é mitigado
- O número de desvios em testes excedeu o planejado: o limite superior estatístico da taxa de desvio indica a probabilidade

Fatores que aumentam likelihood:
- Conta ou processo com alto risco inerente (estimativas, transações não rotineiras, receita)
- Ausência de controles compensatórios ou redundantes
- Controles de acesso e segurança TI deficientes (risco de cobertura de rastros)
- Histórico de restatements ou erros na área

#### Passo 2 — Magnitude (Valor Exposto)

Estimar o valor bruto de transações "expostas" à falha do controle no período:

| Situação | Estimativa de Magnitude |
|---|---|
| Overstatement | Máximo = saldo registrado da conta |
| Understatement | Pode ser maior que o saldo registrado (transações não capturadas) |
| Operações | Volume total de transações que passam pelo ponto de controle deficiente |

> Não confundir "valor do erro identificado" com "valor exposto". A avaliação de MW é baseada no *could* (poderia ocorrer), não apenas no que ocorreu.

#### Passo 3 — Controles Compensatórios

Controles compensatórios são controles que alcançam o mesmo objetivo do controle deficiente, podendo mitigar ou reduzir a severidade. Para ser aceito:
- Deve ser documentado e testado como eficaz (não apenas hipotetizado)
- Deve operar com precisão suficiente para prevenir ou detectar misstatements acima do inconsequente
- Evidência de misstatements passados que passaram pelo "compensatório" invalida o argumento

**Fontes típicas de controles compensatórios:**
- Controles de monitoramento que detectam anomalias antes do fechamento
- Controles redundantes posteriores no processo (revisão final antes de pagamento)
- Testes de auditoria interna em rotina (se competentes e objetivos)

> Aviso: COSO emitiu guidance em 2009 alertando para o uso excessivo de "monitoring" como controle compensatório. Monitoring de alta precisão é raro; não assumir sem evidência.

#### Passo 4 — Teste do Prudent Official

Antes de finalizar a classificação: "Um profissional experiente com os mesmos fatos e circunstâncias chegaria à mesma conclusão?"

Se a resposta for não → reconsiderar a classificação.

Se a notícia saísse no jornal, o raciocínio seria plausível a um leitor razoável de negócios?

---

### 3.4 Deficiências Especiais — Presumidas Material Weakness

As situações abaixo devem ser avaliadas se configuram MW. Na prática, argumentos contrários são raros e exigem documentação robusta:

| Situação | Base |
|---|---|
| Fraude de qualquer valor identificada em **senior management** (CEO, CFO, controller, proprietários) | PCAOB AS 2201; SEC Release 33-8810 |
| Restatement de demonstrações financeiras publicadas para corrigir erro material | PCAOB / AICPA AU-C 265 |
| Erro material identificado nas demonstrações correntes em circunstâncias que indicam que o ICFR da entidade não o detectaria | SEC Release 33-8810 |
| Supervisão ineficaz do ICFR pelo comitê de auditoria | SEC Release 33-8810 |

---

### 3.5 Deficiências Mais Frequentes (Referência Empírica)

Dados de estudo estudo empírico de referência (2011) sobre 76 engagements de acelerados nos EUA, dois anos consecutivos. Proporção de empresas com cada tipo:

| Tipo de Deficiência | Freq. (%) |
|---|---|
| Documentação de contabilidade, políticas e procedimentos | ~95% |
| Recursos e competência de pessoal contábil | ~45% |
| Ajustes materiais e/ou numerosos de auditores / year-end | ~55% |
| Restatement ou não-confiabilidade de relatórios | ~50% |
| TI, software, segurança e acesso | ~18% |
| Conciliações de contas intempestivas ou inadequadas | ~25% |
| Segregação de funções / design de controles | ~15% |
| Questões de transações não rotineiras | ~17% |
| Competência, tom ou confiabilidade da alta gestão | ~4% |
| Questões éticas ou de compliance de pessoal | ~4% |

> Padrão: documentação, competência e ajustes de auditores são os tipos mais persistentes. Segregação de funções e restatements mostraram redução; questões éticas e de JE aumentaram.

---

### 3.6 ITGC — Regra Especial para Deficiências

ITGCs não causam misstatements diretamente — eles *permitem* que misstatements ocorram nos controles de aplicação e dados que suportam.

| Situação | Classificação da Deficiência ITGC |
|---|---|
| Deficiência ITGC + deficiência de controle de aplicação relacionada | Severidade mínima do ITGC = severidade da deficiência de aplicação |
| Deficiência ITGC isolada, sem impacto identificado em aplicações | Pode ser classificada como deficiência simples no relatório "as-of" (mas auditor deve ampliar testes substantivos) |
| Acesso e segurança sem proteção de fato (senhas inexistentes, qualquer usuário acessa) | Presumida Material Weakness (risco de manipulação e cobertura de rastros) |

> Sob o COSO 2013 (Princípio 11), ITGCs ineficazes deveriam em tese impedir a assertiva de controles eficazes. Esta área continua em evolução na prática.

---

### 3.7 Agregação de Deficiências

Deficiências individualmente menores podem configurar MW quando agregadas:

- Múltiplas Significant Deficiencies na **mesma conta, asserção ou componente COSO** → avaliar se em conjunto constituem MW
- Deficiências distribuídas por contas e asserções diferentes → risco de agregação menor, mas ainda avaliar
- Grande número de deficiências de qualquer nível concentradas em um processo → "morte por mil cortes" — pode ser MW ao olhar de um prudent official

**Conclusão geral sobre efetividade:**
Controles ineficazes quando: (1) existe MW em qualquer componente ou princípio COSO, (2) qualquer um dos 17 Princípios tem lacuna material, ou (3) controles não são implementados de forma integrada. Não existe opinião parcial — a cadeia é tão forte quanto seu elo mais fraco.

---

### Fatores de Agravamento (elevam a classificação)

- Fraude envolvida, independente do valor
- Alta direção (management override)
- Falha em múltiplos controles compensatórios
- Restatement de demonstrações financeiras anterior
- Identificada pelo auditor externo, não pelo management
- Conta com alto risco de fraude (caixa, receita, remuneração)
- Remediação não realizada após comunicação prévia (indica fraqueza no ambiente de controle)

---

## 4. ITGCs — IT General Controls (Contexto SOX)

Controles de TI que sustentam a confiabilidade dos controles automatizados e dos relatórios financeiros gerados por sistemas.

| Domínio ITGC | Controles típicos | Risco se ausente |
|---|---|---|
| **Change Management** | Aprovação formal de mudanças, teste em ambiente separado, segregação dev/prod | Mudança não autorizada altera lógica de cálculo ou relatório financeiro |
| **Logical Access** | Provisioning/deprovisioning, revisão periódica de acessos, MFA para sistemas financeiros | Usuário não autorizado manipula dado ou lança transação |
| **Computer Operations** | Monitoramento de jobs, backups, recuperação de desastre | Perda de dados financeiros; processamento incorreto por job failure |
| **Program Development** | SDLC, controles de desenvolvimento, validação de input | Sistema produz output incorreto; ausência de trilha de auditoria |

---

## 5. Scoping — O Que Entra em Escopo SOX 404

### Critérios de materialidade por conta

Contas e processos entram em escopo se:
- O saldo ou volume de transações é material para as demonstrações (tipicamente >5% do benchmark — lucro pré-tax, receita ou total de ativos)
- Existe risco de misstatement material por erro ou fraude

### Processos tipicamente in-scope

| Processo | Contas afetadas |
|---|---|
| OTC / Revenue Recognition | Receita, contas a receber, provisão para devedores duvidosos |
| P2P | Contas a pagar, accruals, despesas operacionais |
| RTR / Close | Todas as contas — processo de fechamento e consolidação |
| Fixed Assets | Ativo imobilizado, depreciação, impairment |
| Treasury | Caixa, aplicações financeiras, instrumentos de hedge |
| H2R / Payroll | Folha de pagamento, benefícios, provisões trabalhistas |
| Tax | Imposto corrente, diferido, obrigações fiscais |
| ITGC | Suporta todos os processos acima |

### Controles-chave vs. controles secundários

- **Controles-chave (key controls):** endereçam diretamente o risco de misstatement material; testados anualmente com ToE (Test of Effectiveness)
- **Controles secundários:** mitigantes adicionais; podem ser documentados mas não testados com a mesma frequência

---

## 6. Abordagem de Teste — SOX 404

| Fase | Atividade | Output |
|---|---|---|
| **Walkthroughs** | Confirmar design e implementacao do controle (ToD) | SCOT table atualizada; narrativa de processo |
| **Test of Design (ToD)** | Avaliar se o controle, se operar como desenhado, previne ou detecta o risco | Conclusão: design adequado / inadequado |
| **Test of Effectiveness (ToE)** | Testar se o controle operou efetivamente durante o período | Amostragem conforme risco; evidência documentada |
| **Rollforward** | Verificar se controles operaram no período final (após a data de avaliação até o relatório) | Atualização de conclusões para eventos do período |

### Tamanho de amostra padrão (ToE)

| Frequência do controle | Amostra mínima (guia PCAOB / prática de mercado) |
|---|---|
| Diário | 25 itens |
| Semanal | 10 itens |
| Mensal | 3 itens |
| Trimestral | 2 itens |
| Anual | 1 item (com procedimentos adicionais) |

---

## 7. Uso no internal-audit-ops

| Situação | Como usar este arquivo |
|---|---|
| Redigir achado com critério normativo | Seção 3 — classificação de deficiência como critério |
| Mapear controles-chave no RCM | Seção 5 — scoping e distinção key/secondary |
| Avaliar ITGC | Seção 4 — domínios e riscos |
| Definir escopo de trabalho | Seção 5 — processos in-scope e materialidade |
| Questionar rating de severidade | Seção 3 — fatores de agravamento e indicadores de MW |

**Referência cruzada:**
- `context/wcgw/it-general-controls.md` — WCGWs por domínio ITGC
- `context/wcgw/entity-level-controls.md` — WCGWs para componente Control Environment
- `context/sod-master.json` — conflitos SoD com criticidade mapeada
- `_method-wiki-external-audit/workflows/risk-control-mapping-external-audit.md` — onde criterios SOX alimentam o CRM / RCM da trilha externa
- `_method-wiki-external-audit/workflows/walkthrough-standardization-external-audit.md` — walkthrough em logica SCOT
- `_method-wiki/concepts/sample-size.md` — dimensionamento de amostra para ToE
- `_method-wiki-external-audit/workflows/finding-rating-external-audit.md` — aplica a hierarquia de severidade desta secao 3
