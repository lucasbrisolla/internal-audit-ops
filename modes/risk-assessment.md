# mode: risk-assessment

## Papel

Avaliação de risco no nível da entidade — identificar e priorizar riscos em todo o universo auditável para construir ou revisar o plano anual de auditoria interna. Opera em nível macro (organização inteira ou unidade de negócio), não em nível de processo.

Diferença de `workflows/audit-planning.md`: aquele define escopo e programa de um trabalho específico. Este modo mapeia riscos em toda a organização e decide **onde auditar** — é o input que alimenta o planejamento.

Diferença de `workflows/risk-control-mapping.md`: aquele constrói RCM dentro de um processo já definido em escopo. Este modo decide quais processos priorizar.

## Quando Usar

- construção ou revisão do plano anual de auditoria interna
- atualização de risk universe após mudança organizacional relevante
- quando a direção ou comitê de auditoria solicita visão de risco consolidada
- antes de definir alocação de horas/equipe para o ciclo

## Inputs

- entendimento da entidade (`modes/business-understanding.md` — executar antes se não houver contexto recente)
- universo auditável: lista de processos, unidades, sistemas e entidades auditáveis
- resultados de auditorias anteriores: achados abertos, reincidências, áreas sem cobertura
- inputs da gestão e do comitê: preocupações, iniciativas estratégicas, mudanças relevantes
- contexto de controle existente: funções de segunda linha (Compliance, Riscos), auditorias externas

## ERM vs. Controle Interno — Delimitação (COSO ERM 2017)

Dois erros frequentes ao trabalhar com clientes que têm ERM ativo:

**Erro 1 — Tratar ERM como sinônimo de "área de riscos".** O COSO ERM define ERM como cultura, capacidades e práticas integradas à estratégia — não como função, grupo ou departamento. Quando o cliente diz "o ERM diz que o risco é baixo", verificar: isso é avaliação do processo de ERM ou opinião do departamento de riscos? São coisas distintas.

**Erro 2 — Confundir o escopo de ERM com o de controle interno.** A fronteira:

| Conceito | Onde é definido | Implicação |
|---|---|---|
| Risk appetite, tolerância, estratégia, objetivos de negócio | ERM | São *precondições* do controle interno — o controle interno assume que esses estão dados |
| Atividades de controle, monitoramento, informação e comunicação | Controle interno (COSO 2013) | Implementam as respostas definidas pelo ERM |

Para o auditor: quando o cliente não tem ERM estruturado, os inputs de risk appetite e estratégia precisam ser obtidos diretamente da gestão sênior antes de qualquer avaliação de controles. Ausência de ERM não elimina a necessidade desses inputs — apenas os torna implícitos e mais difíceis de verificar.

## Sequência de Avaliação

### 1. Construir o universo auditável

Listar tudo que pode ser auditado — não filtrar ainda:

- Processos de negócio (P2P, OTC, H2R, RTR, FA, TRE, TAX, CAPEX, INV, SCL, ESG...)
- Funções de suporte (TI, Jurídico, RH, Comunicação)
- Entidades, filiais e unidades de negócio
- Sistemas críticos e infraestrutura de TI
- Projetos estratégicos e iniciativas em andamento

Organizar em tabela: `Unidade auditável | Categoria | Último ciclo auditado | Achados abertos`.

### 2. Avaliar risco inerente por unidade

Para cada unidade auditável, avaliar antes de considerar controles:

**Fatores de impacto:**
- Materialidade financeira (volume de transações, exposição a perda)
- Impacto regulatório/legal em caso de falha
- Impacto reputacional
- Criticidade operacional (processo para se a unidade falhar)

**Fatores de probabilidade:**
- Complexidade do processo ou ambiente de negócio
- Velocidade de mudança (novo sistema, novo gestor, novo produto)
- Histórico de achados e reincidência
- Dependência de pessoa-chave ou terceiro crítico
- Risco de fraude inerente (acesso a caixa, pagamentos, estoques de alto valor)

Usar escala 1–5 para cada fator. Score de risco inerente = média ponderada ou produto simplificado (impacto × probabilidade).

### 3. Avaliar a cobertura de controle existente

Para cada unidade, estimar qualidade do controle sem auditá-la:

| Nível | Critério |
|---|---|
| Alto | Controles formais, testados recentemente, sem achados materiais |
| Médio | Controles existentes mas com gaps conhecidos ou não testados há mais de 2 anos |
| Baixo | Controles fracos, ausência de segunda linha, histórico de achados repetidos |
| Desconhecido | Nunca auditado ou sem informação suficiente |

Cobertura baixa ou desconhecida aumenta o risco residual — tratar como prioridade.

### 4. Calcular risco residual e prioridade

```
Risco residual = Risco inerente × (1 − Eficácia estimada dos controles)
```

Na prática:

| Risco inerente | Controles | Risco residual | Prioridade |
|---|---|---|---|
| Alto | Alto | Médio | P1–P2 |
| Alto | Baixo/Desconhecido | Alto | P1 |
| Médio | Baixo | Alto–Médio | P1–P2 |
| Médio | Alto | Baixo | P3 |
| Baixo | Qualquer | Baixo | P3–fora do plano |

### 4b. Avaliar mudanças significativas (COSO ERM P15)

Mudanças recentes elevam o risco mesmo que o score histórico seja baixo. referencial metodológico alerta contra o viés SALY (*same as last year*) — o ambiente muda, a documentação não.

Fontes internas de mudança a considerar:
- Troca de pessoal-chave (gestor, controller, responsável por processo crítico)
- Mudança de filosofia de gestão ou tolerância a risco — novo gestor pode ter apetite implicitamente diferente, mesmo sem declaração formal
- Novo sistema, migração de ERP, automação de processo
- Reestruturação organizacional, fusão ou carve-out
- Problemas históricos de reporte financeiro e seu status

Fontes externas de mudança:
- Ambiente regulatório (nova lei, nova obrigação)
- Fatores econômicos (crescimento, taxa de juros, câmbio)
- Risco tecnológico (cibersegurança, nova dependência de sistema)
- Tendências sociais e demográficas com impacto no negócio

**Trigger pós-evento (COSO ERM P15):** após risco materializado, conduzir revisão de como a organização respondeu. Lições aprendidas de eventos passados são input para o próximo ciclo de avaliação — não apenas para o plano de ação do achado.

> **Armadilha de documentação:** descrições vagas de risco ("risco de taxa de juros = baixo") sem fundamentação tornam impossível medir mudança no ciclo seguinte. A documentação de RA precisa registrar a **base da avaliação**, não só a conclusão.

### 4c. Quando o cliente tem ERM ativo — consumir o mapa existente (COSO ERM P10)

Quando o cliente tem CRO ou função de ERM estruturada, o auditor não constrói o inventário do zero — consome e avalia o que já existe:

| Ação | Por quê |
|---|---|
| Obter o inventário de riscos da organização | Base para identificar gaps de cobertura, não duplicar esforço |
| Verificar completude do inventário | Riscos ausentes ou mal descritos são gap de ERM — podem virar objeto de auditoria |
| Comparar universo auditável com o mapa de riscos | Processos no universo sem risco correspondente no mapa = blind spot do ERM |
| Avaliar qualidade das descrições de risco | Risco mal descrito (causa ou impacto no lugar do risco) compromete a priorização |

**Precisão na descrição de risco (COSO ERM P10):** risco deve descrever o evento ou circunstância, não sua causa nem seu impacto. Estrutura recomendada:

> *"A possibilidade de [ocorrência ou circunstância] e os impactos associados em [objetivo de negócio específico]."*

| Impreciso | Preciso |
|---|---|
| Falta de treinamento aumenta o risco de erros | O risco de erros de processamento impactando a qualidade das unidades produzidas |
| Ataques de negação de serviço resultam em vazamento de dados | O risco de ataques de negação de serviço impactando a confidencialidade de dados de clientes |

Risco impreciso → avaliação de severidade incorreta → resposta inadequada.

### 4d. Respostas a risco — referência para output (COSO ERM P13)

Ao concluir a avaliação, cada risco priorizado deve ter uma resposta associada. Cinco categorias:

| Resposta | Quando aplicar |
|---|---|
| **Accept** | Risco já dentro do apetite — nenhuma ação adicional justificada |
| **Avoid** | Risco não pode ser reduzido a nível aceitável — recomendar cessação da atividade ou saída do mercado |
| **Pursue** | Organização decide aceitar risco aumentado em troca de performance superior (crescimento, novo produto) |
| **Reduce** | Ação para reduzir severidade — controles adicionais, mudança de processo |
| **Share** | Transferência parcial — seguro, outsourcing, hedge |

Para o auditor: quando a resposta documentada pelo cliente não é coerente com a severidade avaliada, isso é gap de ERM a registrar. Resposta "Accept" para risco Alto sem aprovação de governança = deficiência de P13.

### 4e. Portfolio view — perspectiva do auditor (COSO ERM P14)

Riscos avaliados isoladamente podem subestimar exposição agregada. Portfolio view permite ver:

| Padrão | O que buscar |
|---|---|
| **Concentração** | Múltiplos riscos moderados no mesmo processo ou unidade podem ser mais graves do que um risco alto isolado |
| **Correlação positiva** | Dois riscos que se materializam juntos amplificam o impacto (ex: risco de recall + risco de compliance breach) |
| **Hedge natural** | Riscos que se compensam entre unidades — queda de receita numa região compensada por outra |
| **Escalada por agregação** | Risco avaliado como baixo na unidade pode ser Alto quando consolidado no nível da entidade |

**Como o auditor usa o portfolio view:**
- Identificar onde a concentração de risco justifica trabalhos adicionais não planejados
- Questionar a gestão sobre riscos correlacionados não endereçados em conjunto
- Apresentar ao comitê de auditoria visão consolidada, não lista de riscos individuais

Quatro níveis de integração crescente (COSO ERM): visão de risco isolado → por categoria → por perfil de objetivo → portfolio completo. O plano anual mais robusto opera no nível de perfil ou portfolio.

### 4f. Apetite de risco como calibrador de prioridade (COSO ERM P7)

Quando o cliente tem apetite formalmente definido, incorporá-lo ao ranking:

| Situação | Ação |
|---|---|
| Risco residual acima do apetite declarado | Prioridade P1 automática — independente do score calculado |
| Risco dentro do apetite com tolerância documentada | Pode reduzir extensão de cobertura com justificativa |
| Apetite definido mas sem cascata para objetivos/processos | Gap de ERM — registrar; não usar apetite como calibrador confiável |
| Apetite não definido | Usar padrão de `concepts/risk-scoring-foundations.md`; documentar a ausência |

**Cascata apetite → tolerância:** apetite é estratégico ("baixo apetite para compliance"); tolerância é o refinamento operacional mensurável ("entre 0 e 7 incidentes por ano"). Processos onde a performance real está fora da tolerância declarada têm desvio documentável — incluir no plano mesmo que os controles não tenham "falhado" tecnicamente.

### 4g. Divergência de performance como evidência de avaliação de risco deficiente (COSO ERM P16)

Quando o cliente tem ERM ativo, comparar performance realizada vs. performance planejada é um teste de qualidade do processo de avaliação de risco — não apenas de eficácia dos controles.

| Padrão observado | Interpretação para o auditor |
|---|---|
| Performance consistentemente abaixo do alvo | Riscos foram subestimados ou respostas insuficientes — gap de P11/P13 |
| Performance consistentemente acima do alvo | Risco insuficiente assumido — organização pode estar sub-utilizando capacidade; ou apetite mal calibrado |
| Riscos novos surgem repetidamente fora do inventário | Processo de identificação de riscos (P10) com blind spots sistemáticos |
| Severidade real diverge do score avaliado | Base de avaliação frágil — ausência de dados históricos, overconfidence ou framing bias |

**Como o auditor usa:** divergência recorrente entre performance e apetite, ou entre risco avaliado e risco realizado, é evidência direta de deficiência no processo de ERM — auditável mesmo sem falha de controle transacional. Documentar o padrão e incluir no escopo a avaliação da metodologia de risk assessment da organização.

**Gatilhos de revisão do plano anual (P16):**
- Performance fora da tolerância declarada em mais de um período consecutivo
- Risco materializado que não constava do inventário
- Risco avaliado como Baixo que se materializou com impacto Alto

### 4h. Avaliação de maturidade do ERM do cliente (COSO ERM P17)

Quando o cliente tem ERM estruturado, o auditor pode ser solicitado a avaliar se o processo de melhoria contínua do ERM é real ou cosmético.

| Indicador                      | ERM funcional                                                                           | ERM cosmético                                               |
| ------------------------------ | --------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| Revisão de risco               | Integrada ao ciclo de negócio (reuniões de performance, budget)                         | Exercício anual desconectado da operação                    |
| Uso de lições aprendidas       | Eventos passados alimentam revisão de inventário e scoring                              | Pós-mortems não conectados ao processo de avaliação         |
| Revisão de categorias de risco | Categorias revisadas quando negócio muda (ex: cyber adicionado ao entrar em e-commerce) | Categorias fixas há anos sem revisão                        |
| Atualização de apetite         | Apetite revisado com base em dados de performance                                       | Apetite declarado uma vez; nunca revisado                   |
| Alcance                        | Melhoria ocorre em todas as unidades/funções                                            | Concentrada na função de ERM/CRO sem penetração na operação |

**Implicação para o plano:** ERM cosmético = maior carga de cobertura para auditoria interna. Não fazer reliance no inventário de riscos da segunda linha se o processo de revisão for estático. Registrar como gap de governance se a organização comercializa ERM estruturado para o board mas o processo não evolui.

### 5. Incorporar fatores dinâmicos

Ajustes que sobrepõem o score calculado:

- **Mandato do comitê**: áreas com solicitação explícita do comitê ou diretoria têm prioridade automática
- **Mudanças recentes**: processo recém-migrado para novo sistema, novo gestor ou reestruturação → elevar prioridade mesmo com score histórico baixo
- **Fraude**: qualquer área com indicadores de fraude entra como P1 independente do score
- **Regulação**: área com nova obrigação regulatória sem controles mapeados → P1
- **Reincidência**: achado material não encerrado do ciclo anterior → manter na agenda

### 6. Definir o plano de auditoria

Com o ranking de risco residual:

1. Selecionar trabalhos para o ciclo (considerar capacidade da equipe em horas)
2. Classificar cada trabalho: assurance vs. consultoria
3. Definir frequência: anual, bienal, rotação
4. Registrar explicitamente o que ficou fora do plano e por quê
5. Reservar buffer para trabalhos ad hoc (sugestão: 15–20% da capacidade)

---

## Guardrails

- Não construir o plano só com o que é fácil de auditar — a prioridade é risco, não comodidade
- Não omitir áreas com achados históricos sérios por pressão política interna
- Registrar premissas e fontes de cada score — o plano precisa ser defensável ao comitê
- Risco desconhecido ≠ risco baixo — tratar como risco médio-alto na ausência de informação
- Atualizar o universo auditável sempre que houver mudança organizacional relevante
- Fraude não é apenas mais um risco — avaliá-la separadamente (COSO Princípio 8, IIA Standard V)

## Output

1. **Universo auditável** — tabela completa com categorias e último ciclo
2. **Ranking de risco residual** — score por unidade, justificativa dos fatores determinantes
3. **Plano anual proposto** — trabalhos selecionados, tipo (assurance/consultoria), período estimado, horas
4. **Fora do plano** — o que foi avaliado e deliberadamente excluído, com razão
5. **Gaps de informação** — onde o score é frágil por falta de dados

Formato de output preferido: tabela para ranking + narrativa para justificativa das P1.

## Artefatos Relacionados

- `modes/business-understanding.md` — pré-requisito: entendimento do negócio
- `modes/risk-matrix.md` — próximo passo: formalizar o ranking em matriz visual
- `workflows/audit-planning.md` — usa este output para planejar cada trabalho individual
- `context/standards/iia-ippf.md` — Domínio IV (planejamento anual baseado em risco)
- `context/standards/sox.md` — COSO Princípio 7 (identificação de riscos) e Princípio 8 (fraude)
- `context/wcgw-master.json` — referência para riscos típicos por processo ao construir o universo
- `processes/monitoring.md` — P9 (significant change) e P16 compartilham gatilhos de revisão de escopo
