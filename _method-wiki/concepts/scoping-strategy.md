# Scoping Strategy — Auditoria Interna

> Fonte primária: referencial metodológico consolidado.
> Aplicação: audit-planning, risk-assessment, risk-control-mapping.

---

## 1. Lógica de Scoping: do Amplo para o Específico

Scoping não é uma decisão binária (in / out). É um processo iterativo de três fases:

1. **Identificação dos processos e riscos relevantes** — o que pode conter falha material?
2. **Avaliação de risco inerente** — antes de considerar controles: qual é o risco bruto?
3. **Calibração da extensão de testes** — in-scope ≠ teste extensivo. Processo em escopo com risco baixo exige cobertura mínima; processo com risco alto exige teste em profundidade.

> Princípio central: separar o julgamento de *o que entra no escopo* do julgamento de *quanto testar*. Confundir os dois leva a over-testing de áreas irrelevantes e under-testing de áreas críticas.

**Direção correta:** começar com escopo amplo e excluir apenas onde há evidência de baixo risco — não o inverso. Excluir primeiro e buscar justificativa depois é a fonte mais comum de lacunas de cobertura.

---

## 2. Identificação do Core: Mapeamento Financeiro

O "core" são as atividades principais do negócio — onde se concentram receitas, despesas, ativos e transações. Não é o limite do escopo, mas o ponto de partida para focar esforço.

### Técnica: planilha FS × segmentos

1. Listar contas e saldos das demonstrações financeiras na coluna esquerda (BP + DRE)
2. Abrir colunas por segmento / divisão / localidade / tipo de transação
3. Distribuir os valores consolidados pelos segmentos
4. Calcular % de cada segmento por conta
5. Identificar onde se concentra a maior parte de receitas, custos e ativos

O perfil resultante define o core. Contas que individualmente são triviais em valor **ainda podem exigir atenção** se envolvem risco de fraude, volatilidade ou julgamento significativo.

### Escala de cobertura por nível de risco

| Nível de risco | Cobertura esperada |
|---|---|
| Core / alto risco | Documentar controles + testar com amostra adequada |
| Risco moderado | Documentar + testar com amostra reduzida |
| Baixo risco (com evidência) | Documentar + 1–2 instâncias ou walkthrough |
| Trivial com suporte analítico | Monitoramento + revisita periódica |

---

## 3. Risco Inerente Antes de Controle

O risco inerente é o risco do processo **na ausência de qualquer controle**. Avaliá-lo primeiro evita que a presença de controles — mesmo sem evidência de eficácia — justifique baixar o escopo indevidamente.

### Fatores de Risco Inerente

| Fator | Descrição |
|---|---|
| **Likelihood** | Probabilidade de ocorrência do erro ou fraude |
| **Magnitude** | Impacto potencial se o risco se materializar |
| **Velocity** | Velocidade com que o risco se materializa |
| **Persistence** | Quanto tempo o risco persiste sem ser detectado |

Processos com alta magnitude + alta velocity + baixa detectabilidade = prioridade máxima no escopo.

### Fontes de Risco Inerente Elevado

- Estimativas com julgamento significativo
- Transações não rotineiras (combinações de negócio, instrumentos financeiros, cisões)
- Pressão para atingir metas
- Alta rotatividade em funções-chave
- Sistemas legados sem trilha de auditoria adequada
- Processos com muitas exceções manuais
- Atividades concentradas em poucos indivíduos sem cobertura substituta

---

## 4. Armadilha: Separar RI de Risco de Controle no Scoping

Um erro frequente é avaliar uma área como "baixo risco" por assumir que os controles existentes são eficazes — sem ter testado isso. O raciocínio circular é:

> "Caixa é baixo risco porque tem conciliação bancária" → mas e se a conciliação não estiver sendo feita corretamente?

No momento do scoping, o foco deve ser o **risco inerente** — o risco antes dos controles. Controles reduzem o risco residual, mas só após evidência de que estão operando. Dar pass a uma área de alto RI com base em controles não testados é uma das principais causas de lacunas de cobertura descobertas tarde.

---

## 5. Overstatement vs. Understatement — Armadilha de Completude

Scoping baseado em **valores registrados** tem um ponto cego estrutural: valores que nunca foram registrados não aparecem na base de análise.

Exemplos:
- Receita sistematicamente desviada (skimming) faz a localidade parecer menor e menos relevante — o oposto do que deveria ocorrer
- Localidade com receitas subdeclaradas para desvio local aparece como "baixo volume" no consolidado
- Licenças ou taxas não cobradas nunca entram nos registros

**Consequência prática:** áreas com risco de completude (understatement) não podem ser dimensionadas apenas pelo valor registrado. A ausência de valor nos registros não é evidência de ausência de risco. Avaliar fontes alternativas: volume operacional, número de transações esperadas, comparação com benchmarks externos.

---

## 6. Múltiplas Localidades — 3 Tipos de Risco

Quando a entidade opera em múltiplas localidades ou unidades de negócio, avaliar risco por **elemento financeiro**, não por localidade como um todo.

| Tipo de risco | Característica | Abordagem |
|---|---|---|
| **Risco coberto por controles centralizados** | Localidades usam mesmo sistema, manual e controles padronizados | Tratar como população única; testar a camada central |
| **Risco específico de localidade** | Localidade recém-adquirida, sistema diferente, ambiente operacional distinto | Avaliar separadamente; não assumir que controles centrais cobrem |
| **Localidade de baixo risco** | Tamanho insignificante, sem atividades de risco específico, sem achados históricos | Monitoramento analítico + visita periódica pode ser suficiente |

> Localidades de baixo risco **ainda devem ser revisitadas periodicamente** — a previsibilidade do processo de auditoria é em si um risco. Fraude migra para os pontos menos inspecionados.

**Atenção ao risco de completude em localidades pequenas:** uma localidade que parece insignificante pode estar subdeclarando sistematicamente. Tamanho não é indicador confiável quando understatement é o risco.

---

## 7. Organizações de Serviço no Scoping

Quando funções relevantes para o reporte financeiro são terceirizadas, os controles do prestador fazem parte do sistema de controle interno da entidade — e precisam entrar no escopo.

### Grau de interação como critério de escopo

| Grau de interação | Característica | Implicação para escopo |
|---|---|---|
| **Alto** | Entidade autoriza cada transação; SO só processa | Focar nos controles da entidade sobre inputs/outputs do SO |
| **Baixo** | SO inicia e executa transações sem autorização prévia por operação | Estender escopo ao SO; testar controles lá |

### Quando há SO report (SOC 1)

- Type 1 (design apenas): não suficiente para reliance operacional
- Type 2 (design + operação): suficiente se cobre o período relevante e não há findings relevantes
- Verificar: período coberto, ITGCs do SO, achados reportados, limites do relatório (handoff boundary)
- Atualizar com procedimentos adicionais se o relatório não cobre o período completo

### Quando não há SO report

Ausência de relatório não exime a entidade. Incluir cláusula de direito de auditoria nos contratos. Se acesso for inviável, documentar como limitação de escopo e avaliar impacto.

---

## 8. Reliance no Trabalho de Outros

Trabalho anterior de auditoria interna, auditoria externa ou reguladores pode reduzir esforço — mas apenas com três critérios satisfeitos:

| Critério | Pergunta-chave |
|---|---|
| **Escopo suficiente** | O trabalho cobriu as contas, asserções e localidades relevantes para o objetivo atual? |
| **Timing adequado** | O trabalho foi realizado em período próximo o suficiente para suportar conclusão atual? |
| **Qualidade de documentação** | Papéis de trabalho evidenciam procedimentos, supervisão, revisão e conclusões consistentes? |

Se qualquer critério falhar, reperformar os procedimentos necessários. Atenção especial: trabalho que testou correção substantiva de lançamentos ≠ trabalho que avaliou eficácia de controles.

---

## 9. Princípio: In-Scope ≠ Teste Extensivo

Incluir um processo no escopo não significa testar cada controle em profundidade máxima. A extensão do teste é calibrada pelo risco inerente:

| Risco Inerente | Cobertura de Controle | Extensão de Teste |
|---|---|---|
| Alto | Alta (múltiplos controles robustos) | Moderada — testar controles-chave |
| Alto | Baixa ou ausente | Extensiva — escopo de teste amplificado |
| Baixo | Alta | Mínima — 1–2 instâncias ou walkthrough |
| Baixo | Baixa | Avaliar inclusão com documentação de raciocínio |

A situação mais perigosa é quando uma área recebe **atenção zero** com base em julgamento de baixo risco não suportado. Toda exclusão exige raciocínio documentado — e deve ser revisitada periodicamente.

---

## 10. Sinais de Alarme que Forçam Revisão de Escopo

Scoping não é decisão única no início do trabalho. Reabrir e reavaliar quando:

- Misstatements substantivos identificados nos testes implicam falha de controle não antecipada
- Reclamações operacionais (remessas incorretas, erros de faturamento) sinalizam processo fora de controle
- Resultados de teste inesperados em área adjacente sugerem risco sistêmico
- Mudança relevante de negócio (aquisição, novo sistema, troca de pessoal-chave) após definição do escopo
- Achados de auditoria interna, externa ou regulador comunicados durante o trabalho

---

## 11. Viés SALY no Scoping

SALY (Same As Last Year) no scoping cria falsa sensação de eficiência: replicar o escopo do ano anterior sem questionar se riscos mudaram. Riscos que não eram relevantes podem ter crescido; áreas novas podem ter surgido.

Perguntas anuais obrigatórias antes de replicar escopo:
- Houve mudanças significativas de negócio, sistema ou organização?
- Algum processo antes periférico tornou-se relevante?
- Os achados do ciclo anterior sinalizam riscos não cobertos?
- O escopo atual ainda captura uma parcela significativa de receitas, despesas e ativos?

---

## 12. Apetite de Risco e Tolerância como Calibradores de Escopo (COSO ERM P7/P9)

Quando o cliente tem apetite de risco formalmente definido, o auditor usa esse apetite como calibrador — não como substituto do julgamento próprio.

### Apetite de risco: o que é e como o auditor usa

Apetite é o montante de risco que a organização está disposta a aceitar na busca de sua estratégia. Não existe padrão universal — cada organização define o seu em função de missão, cultura e objetivos.

**Formas de expressão:**
| Forma | Exemplo |
|---|---|
| Qualitativa | "Baixo apetite para riscos de compliance; moderado para risco operacional" |
| Quantitativa — alvo | Perda máxima aceitável de X% da receita |
| Quantitativa — faixa | Variação de desempenho entre Y% e Z% |
| Teto | "Não aceitaremos iniciativas que exponham a marca a risco severo" |
| Piso | "Mínimo de 25% do orçamento alocado a inovação" |

**Como o auditor usa:**
- Processos com risco residual acima do apetite declarado → cobertura obrigatória, independente de outros critérios
- Processos com risco dentro do apetite → pode reduzir extensão de teste com justificativa documentada
- Apetite declarado mas sem mecanismo de monitoramento → gap de ERM a registrar
- Apetite indefinido → tratar como ausente; não assumir tolerância implícita da organização

### Tolerância: o refinamento operacional do apetite

Tolerância é a variação aceitável de desempenho em torno do alvo de um objetivo de negócio. É mais precisa e tática que o apetite.

| Conceito | Escopo | Granularidade |
|---|---|---|
| **Apetite** | Estratégia e objetivos amplos | Qualitativo ou quantitativo amplo |
| **Tolerância** | Objetivo de negócio específico | Mensurável, expresso nas mesmas unidades do objetivo |

Exemplo: apetite = "baixo para saúde e segurança"; tolerância = "entre 0 e 7 incidentes com afastamento por ano".

**Para o auditor:** quando a performance real está fora da tolerância declarada, existe desvio documentável — mesmo que nenhum controle tenha "falhado" no sentido técnico.

### Armadilhas

- **Apetite como documento de gaveta:** se não cascateia para tolerâncias por objetivo e indicadores por processo, o apetite é declaração vazia — registrar como deficiência de ERM
- **Confundir apetite com limites de controle:** apetite é escolha estratégica; limite de controle é parâmetro operacional. São níveis distintos
- **Apetite agressivo sem capacidade de risco:** a organização pode ter apetite acima de sua capacidade real de absorver perdas — sinal de misalignment estratégico

---

## 13. Perguntas de Scoping — Referência Operacional

Adaptado do Appendix 2A de referencial metodológico:

| Área | Pergunta | Para que serve |
|---|---|---|
| **Operações e indústria** | Quais são as práticas de reporte, condições econômicas, leis e mudanças tecnológicas relevantes? | Identificar objetivos de controle e riscos do negócio |
| **Transações significativas** | Quais contas envolvem subjetividade, complexidade contábil, dependência de informação externa ou partes relacionadas? | Calibrar risco inerente por conta |
| **Escopo de localidades** | Quais unidades são financeiramente mais significativas? Têm exposição a riscos específicos? Carecem de controles documentados? | Decidir quais localidades entram no escopo ativo |
| **Organizações de serviço** | A entidade usa SO para processar informações financeiras relevantes? | Determinar extensão de escopo ao prestador |
| **Trabalho de outros** | Qual é a natureza e extensão da auditoria interna, regulatória ou externa recente? | Identificar o que pode ser aproveitado vs. reperformado |
| **Documentação existente** | Qual é o estado da documentação de controles atual? | Dimensionar esforço de documentação |
| **Visão da gestão** | Quais as principais políticas de controle? Onde a gestão enxerga fragilidades? | Focar em áreas de risco reconhecido |
| **Deficiências não remediadas** | Há deficiências reportadas em ciclos anteriores ainda abertas? | Sinalizar SD/MW potencial; incluir no escopo ativo |
| **Sinais de MW** | Houve restatement, misstatement identificado por externo, ou fraude de alta gestão no período? | Identificar MW presumida; reavaliar escopo |

---

## Conexões Internas

- `workflows/audit-planning.md` — consome o memo de scoping como input
- `modes/risk-assessment.md` — avalia RI no nível organizacional antes do scoping de processo; seção 4d (respostas a risco) e 4e (portfolio view)
- `modes/business-understanding.md` — fornece contexto sobre pressões e incentivos que amplificam RI
- `skills/risk-scoring.md` — calcula RI e residual após cobertura de controles
- `concepts/control-activities-framework.md` — seção 8 sobre service organizations como extensão de controles
- `patterns/control-deficiency-severity.md` — sinais de MW que forçam revisão de escopo
- `concepts/risk-scoring-foundations.md` — apetite de risco padrão e resposta por nível de risco residual
