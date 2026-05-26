# Risk Scoring Foundations

## Papel

Base conceitual para classificação de risco inerente e residual: escalas de impacto e probabilidade, heat map com lógica documentada, bandas de RI e apetite de risco padrão. Referência consultável por qualquer workflow.

## Quando usar

- classificar impacto ou probabilidade de um risco
- verificar enquadramento de score de RI
- calcular risco residual a partir do resultado do controle
- revisar consistência de ratings numa matriz existente

---

## Conceito de risco (COSO ERM 2017)

> *"A possibilidade de que eventos ocorram e afetem a realização de estratégia e objetivos de negócio."*

Três pontos que o auditor precisa ter internalizados ao avaliar inventários de risco do cliente:

**Risco tem upside e downside.** Eventos podem ter resultado positivo (performance acima do alvo) ou negativo. Um inventário de risco que lista apenas ameaças está incompleto — e um cliente que chama toda variância positiva de "oportunidade capturada" pode estar mascarando riscos de upside não gerenciados (ex: demanda acima da capacidade → risco de supply chain).

**Distinção evento vs. condição.** Alguns riscos não têm evento discreto identificável — são condições que se acumulam gradualmente (ex: deterioração de cultura de controle, obsolescência tecnológica, mudança climática). Inventários de risco muito transacionais tendem a não capturar condições — blind spot estrutural. Sinal: todos os riscos no mapa têm causa pontual identificável, nenhum descreve tendência ou condição emergente.

**Distinção positive outcome vs. opportunity.** O COSO ERM diferencia:
- *Positive outcome*: performance que excede o alvo planejado — ainda é risco (variância)
- *Opportunity*: ação ou potencial ação que cria ou altera objetivos — é input para estratégia

Quando o cliente usa "oportunidade" no mapa de riscos para descrever outcome positivo esperado, isso mistura os dois conceitos e compromete a avaliação de severidade.

---

## Separação obrigatória: Risco Inerente vs. Risco de Controle

Avaliar sempre em duas etapas distintas:

1. **Risco inerente** — antes de considerar qualquer controle. Pergunta: *se não houvesse controle algum, qual seria o risco?*
2. **Risco residual** — após considerar a efetividade dos controles existentes.

Erro comum: avaliar RI e risco de controle juntos como "baixo" quando o RI é alto e os controles é que o tornam baixo. Isso mascara a real dependência dos controles e pode levar a subestimar áreas críticas. Ex.: folha de pagamento tem RI alto por natureza — se não houver controles, o risco é real e alto. Concluir RI baixo por causa de bons controles históricos é erro metodológico.

---

## Quatro dimensões de risco (COSO 2013)

referencial metodológico introduz velocity e persistence como critérios adicionais aos tradicionais likelihood e magnitude:

| Dimensão | Definição | Pergunta-chave |
|---|---|---|
| **Likelihood** | Probabilidade de ocorrência do evento de risco | Com que frequência pode ocorrer? |
| **Magnitude** | Tamanho do impacto se ocorrer | Qual o dano potencial? |
| **Velocity** | Velocidade com que o evento pode se materializar | Com que rapidez impacta? |
| **Persistence** | Duração e acumulação do impacto ao longo do tempo | Por quanto tempo continua afetando? |

Velocity e persistence são especialmente relevantes para:
- Riscos regulatórios (nova lei com prazo de adaptação curto)
- Riscos de TI (acesso não autorizado que pode se prolongar sem detecção)
- Riscos de mercado com efeito cumulativo (taxa de juros, câmbio)
- Mudanças organizacionais aceleradas (novo sistema, novo gestor)

Analogia (referencial metodológico): Hurricane Sandy — Category 1 em intensidade, mas devastador pela **persistência** ao longo da costa e pelo **timing** (maré alta + lua cheia). A combinação criou dano desproporcional à classificação isolada.

---

## Escala de Impacto

Avaliar em todas as dimensões relevantes. Usar a **maior** como classificação final.

| Nível | Label | Financeiro | Operacional | Compliance / Reputacional |
|---|---|---|---|---|
| 1 | Baixo | < 0,1% da receita | Impacto pontual, sem interrupção | Irregularidade interna sem exposição externa |
| 2 | Moderado | 0,1% a 0,5% da receita | Afeta subprocesso, retrabalho relevante | Não conformidade com política interna |
| 3 | Significativo | 0,5% a 2% da receita | Afeta processo completo, atraso perceptível ao cliente | Violação de contrato ou norma interna relevante |
| 4 | Alto | > 2% da receita | Interrupção de processo crítico ou perda de cliente | Violação regulatória, legal ou risco de litígio |

Percentuais são referência padrão. **Calibrar por engagement** com valores absolutos (R$) no `context/clients/*/index.md`.

---

## Escala de Probabilidade

| Nível | Label | Critério qualitativo | Frequência de referência |
|---|---|---|---|
| 1 | Improvável | Evento raro, sem histórico recente, requer combinação de falhas | < 1x nos últimos 3 anos |
| 2 | Possível | Pode ocorrer em condições específicas, histórico esporádico | 1–2x por ano |
| 3 | Provável | Ocorre com regularidade, controle frágil ou ausente | Mensal ou trimestral |
| 4 | Quase Certo | Ocorre frequentemente ou já está ocorrendo, falha sistêmica conhecida | Semanal ou contínuo |

---

## Heat Map — Risco Inerente

### Lógica da tabela

**Não é multiplicação simples.** É tabela de lookup ranqueada — cada combinação recebe score de 1 a 16 baseado em prioridade operacional conjunta.

**Por que não multiplicação:** multiplicação produz resultado simétrico — (3,2) = (2,3) = 6. Esta tabela é assimétrica por design: (3,2)=9 e (2,3)=10. Um evento de probabilidade mais alta gera pressão operacional maior do que mesmo impacto menos frequente. Ambas as dimensões têm peso comparável; assimetria reflete urgência.

**Base metodológica:** ABNT NBR 31000:2018 / ISO 31000:2018 — risco como função conjunta de consequência e probabilidade, sem fórmula obrigatória, com tabela aprovada pela equipe.

**Células em negrito** = observadas diretamente em dados reais. Demais completam por consistência lógica.

| Impacto ↓ / Prob → | Improvável (1) | Possível (2) | Provável (3) | Quase Certo (4) |
|---|---|---|---|---|
| Baixo (1) | 1 | **3** | 5 | 7 |
| Moderado (2) | **2** | **6** | **10** | 12 |
| Significativo (3) | 4 | **9** | **13** | 15 |
| Alto (4) | 6 | 11 | 14 | **16** |

### Bandas de classificação

| Score | Classificação |
|---|---|
| 1–3 | Baixo |
| 4–9 | Moderado |
| 10–12 | Alto |
| 13–15 | Alto |
| 16 | Crítico |

---

## Risco Residual

RR = RI ajustado pelo resultado da avaliação do controle mitigador (`skills/control-evaluation.md`).

| Resultado do controle | Redução de nível |
|---|---|
| Satisfatório (score ≥ 0,90) | Reduz **2 níveis** |
| Satisfatório com melhorias (score 0,75–0,89) | Reduz **1 nível** |
| Requer melhorias significativas (score 0,60–0,74) | Sem redução |
| Não satisfatório (score < 0,60) | Sem redução |
| A confirmar / não testado | Sem redução (conservador) |

**Regras:**
- Nível mínimo de RR = Baixo
- Múltiplos controles no mesmo risco: usar o **melhor** controle — não somar reduções
- RI Crítico (16) + Satisfatório → RR máximo = Alto (nunca Baixo diretamente)
- Risco de fraude: redução máxima de **1 nível**, independente do resultado do controle

---

## Apetite de Risco — Padrão

### Resposta por nível de RR

| Nível de RR | Resposta | Prazo |
|---|---|---|
| Baixo | Monitorar — sem plano de ação imediato | Próximo ciclo |
| Moderado | Recomendar melhoria — responsável e prazo definidos | 90–180 dias |
| Alto | Achado formal — owner e data obrigatórios | 30–90 dias |
| Crítico | Achado prioritário — escalada imediata para gestão sênior | Até 30 dias |

### Tolerância por categoria

| Categoria | Tolerância máxima sem achado formal |
|---|---|
| Fraude | Baixo — qualquer risco acima vira achado |
| Compliance / Regulatório | Moderado |
| Operacional | Moderado |
| Governança / TI | Moderado |

### Substituição por cliente

Cliente pode sobrescrever este padrão documentando em `context/clients/*/index.md` antes do início do engagement. Sem registro explícito, este padrão prevalece.

---

## Inherent, Target Residual e Actual Residual (COSO ERM 2017)

O COSO ERM 2017 distingue três estados de risco — mais preciso que a dicotomia inerente/residual:

| Estado | Definição |
|---|---|
| **Risco inerente** | Risco na ausência de qualquer ação direta de gestão para alterar sua severidade |
| **Target residual risk** | Quanto de risco a organização prefere assumir dado que controles serão implementados — é o alvo, não o resultado |
| **Actual residual risk** | Risco remanescente após as ações de gestão. Deve ser ≤ target residual |

**Implicação prática para o auditor:**
- Quando actual residual > target residual: a organização está fora do seu apetite — deficiência de resposta a risco
- Quando target residual não está definido: impossível avaliar se os controles existentes são suficientes ou excessivos
- Respostas redundantes (que não alteram a severidade de forma mensurável) devem ser identificadas — recursos alocados sem benefício real

---

## Quinta dimensão: Recuperabilidade (COSO ERM P12)

Além das quatro dimensões (likelihood, magnitude, velocity, persistence), o COSO ERM 2017 adiciona:

| Dimensão | Definição | Pergunta-chave |
|---|---|---|
| **Recovery** | Capacidade da entidade de retornar à tolerância após o evento | A organização consegue se recuperar e em quanto tempo? |

Recovery é distinto de persistence: persistence mede quanto tempo o risco continua impactando; recovery mede a capacidade de resposta da organização. Um risco com alta persistence mas alta recovery pode ter prioridade menor do que um com persistence menor mas recovery baixa (ex: reputacional).

Usar recovery como critério de priorização, não de severidade bruta.

---

## Bias na Avaliação de Risco

Bias sistemático distorce o scoring em duas direções:

| Tipo de bias | Efeito | Exemplo |
|---|---|---|
| **Confidence bias** | Subestima risco conhecido — "já vimos isso antes, é controlável" | Risco de câmbio avaliado como baixo por histórico de estabilidade recente |
| **Framing bias** | Mesma situação avaliada diferente conforme é apresentada como ganho ou perda | Risco de perda de receita avaliado diferente de "oportunidade não capturada" |
| **Overconfidence** | Superestima efetividade de respostas já implantadas | Controle automatizado avaliado como "elimina o risco" sem evidência de teste |

**Mitigações:**
- Descrever o risco com estrutura padrão de frase (ver `modes/risk-assessment.md` — seção Precisão na Descrição)
- Documentar a **base** da avaliação, não só a conclusão — permite detectar drift no ciclo seguinte
- Comparar avaliações entre times quando o mesmo risco é avaliado por mais de uma área

---

## Artefatos relacionados

- `skills/risk-scoring.md` — aplicação operacional com sequência completa
- `skills/wcgw-mapping.md` — identificação de riscos que alimentam este scoring
- `concepts/scot-and-wcgw-foundations.md`
- `modes/risk-assessment.md` — sequência de avaliação e uso de portfolio view
