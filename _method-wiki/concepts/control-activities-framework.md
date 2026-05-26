# Framework de Atividades de Controle

> Fonte primária: referencial metodológico consolidado.
> Aplicação: risk-control-mapping, walkthrough-standardization, test-execution, finding-drafting, audit-planning.

---

## 1. Tipos de Controle

### 1.1 Preventivo vs. Detectivo

| Dimensão | Controle Preventivo | Controle Detectivo |
|---|---|---|
| **Quando age** | Antes ou durante o processamento | Após o fato |
| **Objetivo** | Impedir que o erro entre nos registros | Identificar erros já lançados |
| **Custo típico** | Maior (aplicado em cada transação) | Menor (pode ser periódico) |
| **Exemplo** | Limite de aprovação no ERP antes de pagamento | Conciliação bancária mensal |
| **Risco se ausente** | Erros entram nos livros sem barreira | Erros permanecem por período extenso |

Combinação de preventivos + detectivos com redundância é melhor do que depender de um único tipo.

> Todo controle precisa de dois elementos para ser eficaz: **detecção do erro** E **correção comunicada a quem pode agir**. Controle que identifica o problema mas não gera correção não é eficaz.

### 1.2 Manual vs. Automatizado

| Dimensão | Manual | Automatizado |
|---|---|---|
| **Consistência** | Variável — depende de julgamento e atenção humana | Alta — opera igualmente em todas as transações |
| **Amostragem** | Requer amostra representativa | 1–2 instâncias suficientes se ITGCs são eficazes |
| **Risco** | Erro humano; não opera da mesma forma em exceções | Risco de programação incorreta; opera incorretamente de forma consistente |
| **Override** | Suscetível a pressão e exceções informais | Difícil de contornar sem deixar rastro |

**Controles híbridos:** sistema gera lista de exceções (automatizado) → revisor analisa e resolve (manual). Ambas as partes precisam ser eficazes.

---

## 2. Segregação de Funções (SoD)

### Princípio Central

Nenhum indivíduo deve ter a capacidade de iniciar, autorizar, registrar E custodiar ativos em uma mesma transação.

**Funções incompatíveis típicas:**

| Processo | Funções a separar |
|---|---|
| P2P | Aprovação de fornecedor / Emissão de PO / Processamento de pagamento |
| OTC | Aprovação de crédito / Processamento de venda / Recebimento de caixa |
| H2R | Contratação (RH) / Processamento de folha / Aprovação de horas |
| FA | Autorização de CapEx / Registro / Custódia física |
| TI | Desenvolvimento / Teste / Aprovação para produção / Acesso a produção |

### Como Avaliar SoD

1. Mapear quem tem acesso a quê no ERP (matriz usuário × transação)
2. Identificar combinações que permitiriam iniciar + aprovar sem revisão independente
3. Verificar superusuários sem compensação de monitoramento
4. Para TI: programadores não devem ter acesso direto a produção após implementação

### SoD em Entidades Pequenas

Quando SoD pura é impraticável, controles compensatórios viáveis:
- Supervisão frequente e direta por proprietário ou gestor sênior
- Revisão analítica mensal por direção
- Rodízio de funções onde possível
- Limites de valor no ERP que restringem o escopo de ação individual

### Como Testar SoD

SoD não é testada por amostragem transacional — é testada por inspeção de matriz de acesso.

**Procedimento padrão:**

1. Solicitar extração da matriz usuário × perfil (ou usuário × transação) do ERP para o período auditado
   - Validar IPE: confirmar que a extração cobre todos os usuários ativos no período, não apenas os atuais
   - Ver `_method-wiki/checklists/ipe-validation-before-test.md`

2. Para cada conflito relevante em `context/sod-master.json` filtrado pelo `process_code` em escopo:
   - Verificar se algum usuário detém simultaneamente os dois perfis/transações conflitantes
   - Priorizar conflitos com criticidade `Alta` — ex: autorizar pagamento + processar pagamento (P2P)

3. Para cada conflito identificado:
   - O usuário realmente exerceu ambas as funções no período? (inspecionar log de transações ou evidência de execução)
   - Existe controle compensatório efetivo e testado? (ex: revisão gerencial de relatório de exceções)
   - O controle compensatório foi realmente executado? (inspecionar evidência — não apenas declaração)

4. Para superusuários (admin, DBA, acesso de emergência):
   - Quem tem acesso ilimitado?
   - Há log de uso e revisão periódica desse log?
   - Cada uso de acesso privilegiado tem justificativa documentada?

**Amostra:**
- Conflitos de SoD: inspeção de 100% dos usuários com perfis críticos (não é amostragem — é completude)
- Transações de superusuário: amostra de 100% se volume < 50; N=23 a 90%/10% se volume > 50

**Critério de falha:**
- Usuário detém perfis incompatíveis sem controle compensatório efetivo → deficiência de SoD
- Superusuário sem log ou sem revisão → deficiência de acesso privilegiado
- Controle compensatório não testado (apenas declarado) → não conta como compensação; tratá-lo como ausente

**Output:**
- Lista de conflitos identificados com usuário, perfis conflitantes e período
- Avaliação de controles compensatórios por conflito (efetivo / não testado / ausente)
- Conclusão: SoD adequada / deficiência isolada / deficiência sistemática
- Se deficiência: encaminhar para `workflows/finding-drafting.md` com referência a `context/sod-master.json` para contexto de risco e controle mitigante típico

---

## 3. ITGCs — Guia de Avaliação por Domínio

### 3.1 Segurança e Acesso

**Relevância:** Sempre.

| Área | Questões-chave |
|---|---|
| Controle de acesso | Usuários têm apenas o acesso necessário? Princípio do menor privilégio |
| Senhas | Políticas ativas (complexidade, validade, bloqueio por tentativas)? |
| Onboarding/offboarding | Acessos provisionados conforme cargo? Revogados imediatamente após desligamento? |
| Revisão periódica | Acessos revisados periodicamente para eliminar excessos? |
| Superusuários | Contas de admin/DBA monitoradas? Acesso de emergência controlado? |
| Logs | Logs de acesso habilitados e revisados para anomalias? |
| Segregação dev/prod | Desenvolvedores sem acesso a dados de produção? |

**Deficiência grave:** acesso irrestrito sem controle. Presumida material weakness por risco de manipulação.

---

### 3.2 Change Management

**Relevância:** Apenas quando ocorrem mudanças em sistemas no período.

| Área | Questões-chave |
|---|---|
| Solicitação | Mudanças têm requisito documentado e aprovado antes do desenvolvimento? |
| Desenvolvimento | Código desenvolvido em ambiente separado de produção? |
| Teste | Plano de teste documentado? Usuário de negócio valida antes de go-live? |
| Aprovação para produção | Aprovação formal antes de deploy? |
| Documentação | Log de mudanças mantido? |

---

### 3.3 Desenvolvimento de Novos Sistemas (SDLC)

**Relevância:** Apenas quando há implantação de novo sistema ou módulo no período.

Elementos de um SDLC controlado:
- Especificações funcionais documentadas antes do desenvolvimento
- Análise de impacto em fluxos de dados existentes
- Ambiente de homologação separado de produção
- Testes extensivos antes do go-live
- Plano de rollback documentado e testado
- Feedback de usuários pós-implementação coletado e tratado

---

### 3.4 Operações e Manutenção

| Área | Questões-chave |
|---|---|
| Backup | Backups regulares executados? Dados testados periodicamente? |
| Armazenamento off-site | Cópias em local fisicamente separado? |
| Disaster recovery | Plano de DR documentado? Simulação realizada? |
| Monitoramento de jobs | Falhas de jobs agendados detectadas e resolvidas? |

---

### 3.5 Controles de Aplicação vs. ITGCs

| Dimensão | ITGC | Controle de Aplicação |
|---|---|---|
| **Nível** | Ambiente geral de TI | Específico de um software/módulo |
| **Objetivo** | Garantir integridade do ambiente | Garantir processamento correto de transações |
| **Exemplo** | Política de senhas; controle de mudanças | Match 3 vias no ERP; edit check de saldo negativo |
| **Teste** | Inspeção, entrevista, logs, matrizes de acesso | Amostragem ou 1–2 instâncias se ITGC eficaz |
| **Relação** | ITGC comprometido invalida reliance em controles de aplicação | Controle pode ser eficaz mesmo com ITGC fraco, mas sem garantia de consistência |

---

## 4. Planilhas como Controles de Aplicação

Planilhas integrais ao reporte devem ser tratadas como software:

| Controle esperado | Exemplo |
|---|---|
| Documentação | README descrevendo propósito, inputs e lógica |
| Controle de versão | Nomenclatura que identifica versão corrente |
| Células protegidas | Fórmulas bloqueadas contra edição acidental |
| Controle de acesso | Acesso restrito; não compartilhado livremente |

> Planilhas que alimentam saldos ou estimativas materiais (PCLD, depreciação, JCP) devem ser mapeadas e avaliadas no escopo de ITGC.

---

## 5. Organização da Documentação: Conta vs. Ciclo

| Abordagem | Como organiza | Melhor para |
|---|---|---|
| **Por conta** | Uma área/pessoa por conta | Equipes pequenas com especialização por conta |
| **Por ciclo/processo** | Uma área/pessoa por processo de negócio | Mais alinhado com como empresas se organizam; facilita walkthrough integrado |

**Recomendação:** organização por ciclo. Contas que participam de múltiplos processos são avaliadas no ciclo primário e referenciadas nos demais.

---

## 6. Processo de Fechamento — Foco Especial

| Área | Controles típicos | Risco principal |
|---|---|---|
| Estimativas contábeis | Revisão e aprovação por gestão sênior; documentação das premissas | Estimativas manipuladas para atingir metas |
| Accruals periódicos | Cálculo documentado e aprovado; comparação com benchmark | Accruals omitidos ou subestimados |
| Consolidação e eliminações | Checklist de eliminações; reconciliação de saldos intercompany | Dupla contagem ou eliminações incompletas |
| Lançamentos manuais (JE) | Aprovação prévia de JEs não rotineiros; revisão pós-fechamento | Override; JEs não suportados |
| Transações não rotineiras | Análise de tratamento contábil antes do registro; aprovação sênior | Classificação incorreta; divulgação insuficiente |

---

## 7. P10 — Integração Risco → Controle

O ponto de partida do Princípio 10 é que **riscos identificados devem dirigir a implementação de controles** — não o inverso. O auditor deve verificar se há correspondência explícita entre cada risco material e os controles que o mitigam.

### Elementos de uma Matriz Risco → Controle

Documentação mínima esperada para cada item:

| Campo | O que captura |
|---|---|
| Descrição do risco | O que pode dar errado e por quê |
| WCGW | Consequência sobre o reporte financeiro |
| Asserção(ões) afetada(s) | Completeness, Occurrence, Valuation etc. |
| Controle(s) que mitiga(m) | Identificação e descrição do controle |
| Frequência | Diário, mensal, por transação etc. |
| Magnitude potencial | Valor ou % de impacto se o controle falhar |
| Tipo | Preventivo/detectivo; manual/automatizado |
| Histórico | Deficiências passadas ou issues anteriores |

### Riscos sem controle = gap explícito

Se um risco identificado não tiver controle correspondente, isso é uma **deficiência de design** — deve ser documentada e avaliada em termos de severidade, não silenciada. Isso inclui riscos que não mapeiam facilmente a uma asserção (ex: override gerencial, baixa expertise da governança) — nesses casos, a análise deve descrever como o risco poderia se materializar e ser detectado.

### Riscos não mapeáveis a asserções

Alguns riscos de ambiente de controle (override gerencial, pressão por metas, comprometimento de governança) não têm controle transacional correspondente. Abordagem:
- Atribuir procedimentos de maior ceticismo nas áreas de maior exposição
- Alocar pessoal mais experiente
- Incrementar indagações sobre solicitações fora de política escrita
- Usar analytics para identificar anomalias que seriam consistentes com o risco

---

## 8. Service Organizations como Extensão dos Controles

Quando a entidade terceiriza funções (folha, processamento de pagamentos, custódia, TI), os controles do prestador passam a fazer parte do sistema de controle interno da entidade. A simples existência de um relatório SOC não é suficiente.

### SOC 1 Type 1 vs. Type 2

| Tipo | O que cobre | Suficiente para reliance? |
|---|---|---|
| **Type 1** | Desenho dos controles em uma data específica | **Não** — não testa operação |
| **Type 2** | Desenho + operação efetiva ao longo de um período | **Sim** — desde que cubra o período relevante |

### Checklist de avaliação do SOC report

1. **Período coberto**: o relatório cobre o exercício em avaliação? Se não, procedimentos de atualização são necessários.
2. **ITGCs do prestador**: o relatório inclui avaliação de segurança, acesso e change management do prestador?
3. **Findings**: há deficiências relatadas? Leitura das conclusões é obrigatória — "slap it in the file" não é suficiente.
4. **Limites do relatório (handoff boundary)**: atividades que antecedem a entrega ao prestador e que seguem após o retorno dos dados processados são responsabilidade da entidade e **não estão cobertas** pelo SOC.
5. **Relevância do escopo**: os controles cobertos são os que a entidade efetivamente utiliza para o processo em avaliação?

### Quando não há SOC report

A ausência de relatório não exime a entidade de obter asseguração. Alternativas:
- Cláusula de direito de auditoria no contrato (recomendada pelo SEC para públicas)
- Inspeção direta com acesso negociado
- Se nenhum procedimento alternativo for viável: documentar como limitação de escopo e avaliar como deficiência potencial

---

## 9. Armadilha: Monitoring como Substituto de Controles Transacionais

Uma tendência documentada (COSO reconheceu formalmente em 2009) é o **downgrade indevido de deficiências** com o argumento de que "a gestão identificaria o problema nas revisões analíticas mensais" ou "o CFO pega isso no review do fechamento".

### Por que esse argumento falha

- Controles de monitoring **operam acima** do nível transacional — são desenhados para supervisionar se os controles estão sendo aplicados, não para substituí-los
- Se o monitoring é usado como controle de detalhe, ele precisa de um segundo nível de supervisão — o que raramente existe
- Controles preventivos transacionais têm vantagem de **tempestividade**: impedem que erros entrem nos registros; monitoring detecta após o fato, potencialmente após impactar relatórios intermediários ou decisões de gestão

### Critério de avaliação

Para aceitar monitoring como mitigação real de uma deficiência transacional, verificar:

| Critério | Pergunta-chave |
|---|---|
| Especificidade | O controle de monitoring detectaria especificamente o erro que o controle transacional falharia em prevenir? |
| Tempestividade | A detecção ocorre antes de impacto relevante nos registros ou no reporte? |
| Baseline confiável | Os dados usados no monitoring são confiáveis? (Dados corrompidos na fonte invalidam o monitoring) |
| Ação documentada | Quando anomalias são detectadas, há processo formal de investigação e correção? |

Se algum critério falhar, o monitoring não compensa — a deficiência original mantém sua severidade.

---

## 10. P12 — Deployment via Políticas e Procedimentos

O Princípio 12 fecha o loop entre o desenho dos controles (P10/P11) e sua execução real no dia a dia. Ter controles identificados não é suficiente — eles precisam ser formalizados, atribuídos e mantidos.

### Pontos de foco (COSO 2013)

| Ponto de foco | O que verificar |
|---|---|
| **Responsabilidade e accountability** | Cada controle tem dono identificado? As linhas de autoridade chegam ao nível de execução? |
| **Execução tempestiva** | Controles operam na frequência correta? Mecanismos detectam atrasos? |
| **Ação corretiva** | Quando exceções são identificadas, há processo documentado de resolução? |
| **Competência do executor** | O responsável tem o treinamento e entendimento para executar o controle corretamente? |
| **Reavaliação periódica** | Políticas são revisadas quando negócio muda, riscos evoluem ou issues recorrentes sinalizam obsolescência? |

### Rastreabilidade P3 → P12

O Princípio 3 define estrutura, autoridade e responsabilidade no nível do ambiente de controle. O P12 é onde esses elementos **descem ao nível do controle individual**. Uma deficiência em P12 (ex: executor não sabe o que fazer; controle nunca foi documentado) pode ter raiz em P3 (estrutura de responsabilidades mal definida) ou P4 (competência insuficiente). Investigar a causa-raiz antes de classificar.

### Documentação: flowchart > narrativa

Narrativas extensas de processo são difíceis de ler, manter e atualizar. Flowcharts com pontos de controle identificados comunicam o mesmo conteúdo com menor custo de manutenção e menor risco de perder o controle no texto. Quando a entidade tem apenas narrativas, avaliar se os controles estão suficientemente destacados ou se se perdem na descrição do processo.

### Quando P12 gera deficiência

- Controle existe no papel mas executor não conhece a política ou não recebeu treinamento
- Exceções identificadas não têm processo de resolução documentado
- Política nunca foi atualizada após mudança de sistema, processo ou organização
- Novo funcionário assumiu função crítica sem direcionamento suficiente

---

## Conexões Internas

- `_method-wiki/concepts/control-objectives-assertions.md` — objetivos de controle mapeados às asserções por processo
- `_method-wiki/concepts/sample-size.md` — tamanho de amostra para controles manuais vs. automatizados
- `_method-wiki/concepts/control-types-and-reliance.md` — tipologia de controles e implicações para reliance
- `context/sod-master.json` — 35 conflitos de SoD estruturados por processo
- `context/wcgw-master.json` — WCGWs por processo incluindo ITGCs e controles de aplicação
- `workflows/risk-control-mapping.md` — usa este framework para mapear riscos → controles → asserções
- `workflows/test-execution.md` — tipo de controle determina abordagem de teste
- `_method-wiki/processes/monitoring.md` — armadilha monitoring como substituto de controles transacionais; critérios para aceitar monitoring como mitigação real
