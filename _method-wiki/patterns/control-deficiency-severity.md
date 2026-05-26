# Control Deficiency Severity

## Papel

Padrão metodológico para avaliar severidade de falhas de controle, considerando magnitude, probabilidade e efeito de controles compensatórios.

## Quando usar

- ao concluir sobre exceções identificadas em testes de controle
- ao discutir deficiência significativa versus material weakness
- ao avaliar se controles compensatórios alteram a severidade do achado

## Objetivo

Estruturar a análise de falha de controle de forma que a conclusão vá além do erro observado e reflita o risco potencial para as demonstrações financeiras.

---

## Princípios-base

- um controle pode ter desenho adequado e ainda falhar na operação
- a severidade depende do impacto **potencial**, não apenas do erro já materializado — o fator "could" é o centro da avaliação
- a análise precisa considerar natureza, atividade afetada e magnitude possível sobre as demonstrações
- controles compensatórios só ajudam se reduzirem o risco de forma efetiva
- controles manuais são inerentemente mais voláteis que automatizados; controles automatizados falham de forma consistente quando mal configurados
- ausência de erro identificado não prova que o controle funciona — mas identificação de erro é evidência forte de falha

---

## Classificações

referencial metodológico define quatro níveis em ordem decrescente de severidade:

| Nível | Definição |
|---|---|
| **Material weakness** | Possibilidade razoável de distorção material não prevenida ou não detectada tempestivamente |
| **Significant deficiency** | Menos severa que MW, mas importante o suficiente para merecer atenção da governança |
| **Deficiency** | Falha entre exceção e significant deficiency; ampla faixa de combinações likelihood × magnitude |
| **Exception** | Desvio isolado que não chega a ser deficiência; pode indicar deficiência quando combinado com outros |

> **Nota:** "Reasonable possibility" = evento "reasonably possible" ou "probable" (FASB ASC 450). O termo anterior "more than remote" era equivalente — a mudança foi terminológica, não substantiva.

---

## Framework de avaliação de severidade (Appendix 10A)

### Quando usar cada Chart

| Chart | Aplicar quando |
|---|---|
| Chart 1 | Avaliar se exceção em teste de efetividade operacional é deficiência |
| Chart 2 | Classificar deficiências em controles manuais ou automatizados de processo/transação |
| Chart 3 | Avaliar deficiências em ITGCs |
| Chart 4 | Avaliar deficiências em controles pervasivos (exceto ITGC) — ex: ambiente de controle, monitoramento |

### Chart 1 — Exceções em testes de efetividade operacional

1. Avaliar exceção quantitativa e qualitativamente; entender a causa
2. Se taxa de desvio não é negligível → objetivo do teste não foi atingido
3. Se desvios são representativos da população → configurar como deficiência e avaliar severidade
4. Se não representativos (erro amostral) → estender teste e reavaliar

Presunções automáticas de deficiência:
- controle que opera com frequência menor que diária: 1 exceção = deficiência
- exceção que resultou em distorção financeira acima do nível de precisão do controle = deficiência

### Chart 2 — Deficiências em controles de processo/transação

**Step 1 — Determinar se é Significant Deficiency:**

- Magnitude potencial inconsequente + controles efetivos mitigando → apenas deficiência
- Magnitude potencial > inconsequente + sem mitigação efetiva → ao menos significant deficiency

**Step 2 — Determinar se é Material Weakness:**

- Magnitude potencial < material + sem compensação efetiva → significant deficiency
- Magnitude potencial ≥ material + compensação efetiva de precisão suficiente → pode ser apenas SD
- Magnitude potencial ≥ material + sem compensação → material weakness

**Prudent official test** (Boxes 7 e 8): aplicar ao final de ambos os steps — ver seção específica abaixo.

### Chart 3 — Deficiências em ITGCs

ITGCs não causam distorção diretamente — abrem a porta para falhas nos controles de aplicação.

Três situações em que ITGC sobe para material weakness:
1. Deficiência em controle de aplicação relacionada ao ITGC é classificada como MW
2. Pervasividade e significância do ITGC levam à conclusão de MW no ambiente de controle
3. ITGC classificado como SD permanece não corrigido por período razoável

Regra geral: severidade do ITGC pega carona na severidade do controle de aplicação afetado.

> **⚠️ Conflito potencial — verificar:** referencial metodológico (edição baseada no COSO 1992/2013) trata ITGC como condicional à aplicação. O Princípio 11 do COSO 2013 eleva ITGCs a princípio independente, o que logicamente tornaria uma MW em ITGC suficiente para prejudicar a avaliação global — independentemente da aplicação. referencial metodológico sinaliza isso mas afirma que a prática prevalecente ainda segue a lógica condicional. Validar com contexto regulatório do cliente antes de classificar.

### Chart 4 — Controles pervasivos (exceto ITGC)

Ex.: deficiências em ambiente de controle, avaliação de risco, monitoramento, comunicação.

Não causam distorção diretamente — aumentam a probabilidade de distorção no processo.

Step 1 (SD): possibilidade razoável de contribuir para distorção > inconsequente → SD
Step 2 (MW): possibilidade razoável de contribuir para distorção material → MW

Fatores considerados:
- pervasividade da deficiência na entidade
- significância relativa do controle deficiente no componente COSO
- histórico de distorções
- susceptibilidade a fraude ou override gerencial
- causa e frequência de exceções conhecidas
- consequências futuras possíveis

---

## Fatores-chave na avaliação de severidade

referencial metodológico lista quatro variáveis que atravessam todos os Charts:

### 1. Propósito e nível do controle

- Controles operacionais sem impacto financeiro = fora do escopo de severity assessment
- Controles pervasivos (ex.: CEO/CFO; segurança de sistema) têm impacto potencial maior do que controles de processo isolado
- Hierarquia implícita: falha em controle do qual outros dependem amplifica severidade de todos os controles dependentes

### 2. Objetivos e timing

- Deficiência identificada no início do período = mais fácil corrigir; timing reduz urgência de análise precisa de severidade
- Deficiência identificada próxima à data de reporte = avaliação precisa obrigatória
- Para entidades que reportam "as of" (data de balanço): deficiência corrigida antes dessa data pode não ser reportável

### 3. Likelihood e magnitude potencial

**Likelihood** — fatores que aumentam:
- Contas de suspense, transações com partes relacionadas
- Ativos susceptíveis a perda ou fraude
- Subjetividade, complexidade, julgamento envolvido (ex.: estimativas)
- Interdependência com outros controles com falhas
- Possíveis consequências futuras (ex.: área em crescimento)

**Magnitude** — estimativa:
- Superestimação: limitada ao saldo contábil registrado
- Subestimação: pode exceder muito o saldo registrado
- Gross exposure = pior caso de volume $ exposto à falha, antes de compensação
- Adjusted exposure = gross exposure × upper limit deviation rate

**Método upper limit (Appendix 10B):**

Em amostra de N com d desvios, usar tabela de desvio máximo a 90% de confiança:

| N amostral | 0 desvios | 1 desvio | 2 desvios |
|---|---|---|---|
| 25 | 8,8% | 14,7% | 20,0% |
| 30 | 7,4% | 12,4% | 16,8% |
| 40 | 5,6% | 9,4% | 12,8% |
| 50 | 4,6% | 7,6% | 10,3% |

Exemplo: N=30, 1 desvio → upper limit = 12,4%. Se gross exposure = R$ 1.000.000 → adjusted exposure ≈ R$ 124.000. Comparar com materialidade para classificar.

> ⚠️ Upper limit method e compensating controls são abordagens alternativas para quantificar magnitude — não aplicar as duas ao mesmo desvio.

### 4. Características do negócio e ambiente de risco

- Mesma deficiência pode ser mais ou menos severa dependendo do perfil de risco da entidade
- Ex.: senha fraca é deficiência leve em associação comunitária; potencial MW em empresa de propriedade intelectual
- Entidades menores não têm padrão mais baixo — apenas riscos subjacentes diferentes

---

## Controles compensatórios

Controle compensatório = controle que alcança o mesmo objetivo do controle faltante ou ineficaz.

Para ter efeito mitigador **completo**, precisa:
- operar com nível de precisão suficiente para prevenir ou detectar distorção > inconsequente (para SD) ou material (para MW)
- atuar sobre o mesmo risco
- ser testado para verificar efetividade operacional real — não apenas declarado como existente
- não ter deixado distorções passarem no passado (senão: evidência de ineficácia)

Fontes comuns de controles compensatórios:
- controle redundante/complementar que atinge o mesmo objetivo
- controle posterior no processo que detecta o que o anterior perdeu
- revisão de auditoria interna como parte da rotina
- controle de monitoramento de alta precisão

> **Atenção (referencial metodológico):** controles compensatórios são raramente tão precisos quanto parecem. Monitoramento foi historicamente citado em excesso como compensação — COSO publicou guia específico sobre isso em 2009. Na maioria dos casos não há controle compensatório real que reduza completamente uma MW a deficiência simples.

---

## Prudent Official Test

Etapa final obrigatória antes de qualquer conclusão de severidade.

Pergunta: *"Um profissional prudente, com o mesmo conhecimento dos fatos e circunstâncias, concordaria com minha conclusão sobre a severidade desta deficiência?"*

- Gate funciona nos dois sentidos: para elevar e para rebaixar
- Na prática: argumentos bem-sucedidos para rebaixar são raros
- Teste de realidade: "se eu lesse essa conclusão no Wall Street Journal, faria sentido para um leigo de negócios?"

Exemplos de falha no teste:
- 35 desvios em 58 itens, cada um com "razão diferente" → conclusão de que controle está bom = implausível
- Aceitar compensação de monitoramento sem evidência de que funcionou na prática

---

## Agregação de deficiências

Deficiências individuais menores podem constituir MW quando agregadas.

Regras de agregação:
- Múltiplas SDs na mesma conta, asserção ou componente COSO → avaliar se coletivamente = MW
- Muitas deficiências espalhadas por contas diferentes → menor risco de constituir MW agregada
- COSO 2013 explicita: deficiência em um princípio pode refletir em outro — considerar relações entre deficiências

Conclusão geral de controles ineficazes surge quando:
1. MW existe em qualquer componente COSO, ou
2. MW em um dos 17 Princípios, ou
3. Controles não implementados de forma integrada

> "Death by a thousand cuts" — muitas deficiências leves em uma área concentrada podem = MW mesmo sem nenhuma individual atingir o limiar.

---

## Deficiências especiais (presumidamente mais severas)

Situações que merecem avaliação com atenção redobrada — geralmente SD ou MW:

- Fraude identificada de qualquer magnitude por parte da alta administração
- Reapresentação de demonstrações financeiras por erro material passado
- Distorção material descoberta pelo auditor que não teria sido detectada pelos controles da entidade
- Supervisão ineficaz do ICFR pelo comitê de auditoria
- Ausência de expertise contábil interna para aplicar GAAP em transações da entidade
- Ausência de programas e controles antifraude
- Controles insuficientes sobre transações não rotineiras
- Controles insuficientes sobre o processo de fechamento periódico
- Indiferença gerencial em corrigir SDs ou MWs conhecidas

---

## Tipos de fraqueza mais comuns ao longo do tempo (dados empíricos)

Baseado em estudo estudo empírico de referência (76 engajamentos, ~1.000 empresas públicas, 2004-2009):

| Tipo de fraqueza | % de empresas |
|---|---|
| Documentação contábil, políticas e procedimentos | ~99% |
| Recursos e competência da equipe contábil | ~49% |
| Ajustes materiais do auditor / fechamento anual | ~60% |
| Reapresentação ou não-confiabilidade de arquivos | ~43% |
| TI, software, segurança e acesso | ~19% |
| Transações não rotineiras | ~19% |
| Conciliações inadequadas ou intempestivas | ~23% |
| SoD / desenho de controles | ~12% |

Insight: proporções são notavelmente estáveis ao longo do tempo — não há evidência de aprendizado acumulado no mercado.

---

## Perguntas úteis

- o desenho do controle era adequado?
- o problema ocorreu no desenho ou na operação?
- qual a magnitude potencial do impacto (gross exposure)?
- qual o upper limit da taxa de desvio com base na amostra?
- qual a probabilidade de o erro não ser prevenido ou detectado?
- existe controle compensatório realmente efetivo e testado?
- o controle compensatório atua no mesmo risco e com tempestividade suficiente?
- a conclusão passaria no teste do "profissional prudente"?
- existem outras deficiências que, em conjunto, poderiam constituir MW?

## Red flags

- classificar a falha olhando apenas o erro identificado, não o risco potencial
- aceitar controle compensatório fraco ou não testado como mitigação suficiente
- concluir que a falha "não é grave" sem ligação clara com magnitude e probabilidade
- subestimar severidade quando não há distorção materializada (viés documentado empiricamente: empresas subestimaram 70% das SDs no início do SOX)
- citar monitoramento como compensação sem evidência de que funcionou
- tratar ITGC isoladamente sem avaliar impacto nos controles de aplicação

---

## Deficiency Summary — Campos de Registro por Deficiência

Cada deficiência identificada deve ser registrada num summary centralizado que permita avaliação agregada por componente, princípio, conta e asserção. Campos mínimos:

| Campo | Conteúdo |
|---|---|
| **ID da deficiência** | Código único (ex: CED-1.1, CAD-3.2) para rastreabilidade |
| **Componente COSO** | Qual dos 5 componentes é afetado |
| **Princípio afetado** | Qual dos 17 Princípios (ex: P1, P11) |
| **Descrição** | O que foi observado — fático, sem julgamento de severidade ainda |
| **Ponto de controle específico** | ID do controle ou atividade onde a falha ocorre |
| **Severidade** | D / SD / MW — com raciocínio documentado |
| **Impacto em "Present"** | O controle está desenhado/implementado? (Y/N) |
| **Impacto em "Functioning"** | O controle opera efetivamente? (Y/N) |
| **Controles compensatórios** | Se existem, descrever e indicar se foram testados |
| **Dono** | Responsável pela remediação |
| **Plano e prazo de remediação** | Ação e data-alvo |
| **Princípios relacionados afetados** | Deficiências em outros princípios que derivam ou agravam esta |
| **X-Ref ao work paper** | Referência ao paper de teste ou walkthrough que identificou |

### Por que manter summary centralizado

Avaliação de MW por agregação requer visão cruzada — uma deficiência em P11 (ITGC) pode agravar deficiência em P12 (controles transacionais). Sem registro centralizado e ordenável, essas interações ficam invisíveis até o fechamento.

---

## Comunicação de Deficiências — P17 (referencial metodológico, Cap. 7)

### Cadeia de comunicação obrigatória

Deficiências não devem ser reportadas apenas ao responsável direto. A cadeia mínima:

1. **Responsável pela atividade** — quem executa ou supervisiona o controle falho
2. **Nível acima do responsável** — garante que o problema não seja suprimido pela mesma gestão que falhou
3. **Governança** — board e comitê de auditoria para deficiências que afetem a capacidade de reporte confiável

> Quanto mais próxima da alta gestão for a deficiência, mais crítico que chegue à governança por canal independente.

### Dado empírico — underassessment sistêmico

Estudo estudo empírico de referência (2004-2005): **70% das deficiências classificadas pela gestão como "major deficiency"** foram reclassificadas para severidade ainda maior pelos auditores. A taxa de subestimação era ainda mais alta para deficiências que depois foram elevadas a material weakness.

Implicação prática: ao revisar avaliação de severidade feita pela própria gestão, tratar o viés de subestimação como risco esperado, não exceção.

### Protocolo especial para fraude

Suspeita de fraude **não deve ser tratada como deficiência rotineira**. Diferenças críticas:

| Rotina | Fraude suspeita |
|---|---|
| Seguir fluxo normal de comunicação de deficiências | Escalar imediatamente para nível adequado fora da cadeia do suspeito |
| Investigação conduzida pela gestão | Investigação conduzida por terceiro independente ou auditoria interna com autonomia |
| Documentação normal de work paper | Preservação de evidência como prioridade — suspeitos alertados podem destruir sistemas e dados |
| Timeline padrão | Urgência: cada hora de atraso aumenta risco de destruição de evidência |

> **referencial metodológico:** "Não improvise investigação de fraude em campo." Sinalização prematura ao suspeito é uma das causas mais comuns de perda de evidência crítica.

### Requisitos legais e regulatórios

Em algumas situações, deficiências ou violações precisam ser comunicadas fora da organização: reguladores setoriais, autoridades legais, obrigações de disclosure. Envolver assessoria jurídica antes de decidir sobre comunicação externa em casos sensíveis.

---

## Artefatos relacionados

- `patterns/control-design-and-operating-effectiveness.md`
- `concepts/control-types-and-reliance.md`
- `concepts/sample-size.md` — seção 14 (campos de documentação de amostragem com X-Ref ao deficiency summary)
- `processes/monitoring.md` — P16 (avaliações contínuas e separadas) e interdependência com P17
- `context/standards/sox.md` (hierarquia de deficiências, Prudent Official Test, presumed MW)
- `context/standards/iia-ippf.md` (escala de severidade IIA)
