# skill: challenge-reasoning

## Goal

Interromper o raciocínio em andamento e aplicar pressão intelectual direcionada — revelando suposições ocultas, blind spots, falácias e vieses antes que uma conclusão de auditoria se consolide.

Não é sobre discordar por padrão. É sobre garantir que o que parece óbvio foi realmente examinado.

## Use When

- Antes de finalizar rating de risco, conclusão de controle ou achado
- Quando a evidência "confirma" exatamente o que se esperava encontrar
- Quando a gestão disse que o controle funciona e o auditor aceitou sem evidência
- Quando o escopo foi definido sem questionar o que ficou de fora
- Quando um achado parece sólido mas ainda não foi submetido a pressão
- Quando o mesmo risco reaparece em ciclos anteriores sem resolução
- Quando explicitamente solicitado: "questione meu raciocínio", "advocacia do diabo", "qual meu blind spot"

## Quando NÃO usar

- Para decisões operacionais rotineiras de baixo risco
- Quando a conclusão já foi examinada, questionada e está documentada
- Quando o time precisa de execução, não de reflexão

---

## Routing — Escolher a ferramenta certa

### Contextos gerais

| Contexto | Ferramenta |
|---|---|
| "Tenho certeza que a causa é X" | Detector de Suposições |
| "Não entendo por que a gestão pensa assim" | Inversão de Perspectiva |
| "Sinto fortemente que esse risco é alto" | Detector de Vieses |
| "Meu raciocínio para esse achado é..." | Verificador de Lógica |
| "Vou recomendar uma mudança estrutural no processo" | Analisador de Efeito Cascata |
| "Esse achado está bem fundamentado" | Advogado do Diabo |
| "A gestão me apresentou evidência de que o controle funciona" | Cético da Fonte |
| "Esse risco reaparece todo ciclo sem resolução" | Iluminador de Fatores Ocultos |
| "Estou preso — não consigo concluir sobre esse controle" | Empréstimo de Modelos Mentais |
| "Estamos discutindo a severidade do achado sem chegar a acordo" | Afiador de Definições |
| "A empresa sempre fez dessa forma" | Desafiador do Status Quo |
| "A discussão com a gestão ficou defensiva" | Separador de Fato vs. Opinião |
| "Acho que entendi o processo" | Validador de Compreensão |
| Contexto vago | Meta-prompt |

### Contextos específicos de auditoria interna

| Situação | Ferramenta prioritária |
|---|---|
| Rating de risco parece baixo demais dado o que o walkthrough mostrou | Detector de Suposições + Detector de Vieses |
| Controle classificado Satisfatório mas baseado só em indagação | Cético da Fonte + Verificador de Lógica |
| Achado pronto para emitir | Advogado do Diabo |
| Escopo do engagement definido sem questionar o que ficou de fora | Iluminador de Fatores Ocultos |
| Gestão apresenta "controle compensatório" para justificar lacuna | Detector de Suposições + Cético da Fonte |
| Probabilidade classificada como Improvável por "nunca aconteceu" | Desafiador do Status Quo + Detector de Vieses |
| Severidade do achado rebaixada por conforto relacional | Detector de Vieses + Advogado do Diabo |
| Deficiência classificada como D ou SD mas contexto levanta dúvida | Prudent Official Challenge |
| Risco priorizado para Q3 mas processo em expansão rápida ou volátil | Velocity & Persistence Check |

---

## As 15 Ferramentas

### 1. Detector de Suposições
**Quando:** certeza sobre a causa de algo.
> Você acredita que [crença]. Quais suposições ocultas estão por baixo disso? Que explicações alternativas poderiam existir?

### 2. Inversão de Perspectiva
**Quando:** não consegue entender o ponto de vista da gestão ou do auditado.
> Aja como [gestão/área auditada] e explique a perspectiva dela de forma que a posição pareça razoável e lógica.

### 3. Detector de Vieses
**Quando:** opinião muito forte sobre risco, controle ou achado.
> Você sente fortemente que [posição]. Que vieses — confirmação, ancoragem, excesso de confiança, viés de relacionamento — podem estar afetando esse julgamento?

### 4. Verificador de Lógica
**Quando:** antes de emitir conclusão de controle ou achado.
> Este é o raciocínio para [conclusão]: [descrever]. Identifique falácias lógicas, saltos injustificados ou pontos fracos no argumento.

### 5. Analisador de Efeito Cascata
**Quando:** recomendando mudança estrutural no processo ou controle.
> Além dos efeitos óbvios de [recomendação], quais são as consequências de segunda e terceira ordem — positivas e negativas — que provavelmente não foram consideradas?

### 6. Advogado do Diabo
**Quando:** achado parece sólido demais ou pronto para emitir.
> Apresente os argumentos mais fortes e convincentes *contra* [achado/conclusão], como se estivesse tentando destruí-lo. O que a gestão vai usar para refutar?

### 7. Cético da Fonte
**Quando:** evidência apresentada pela gestão para suportar controle.
> Que perguntas críticas devo fazer para avaliar a confiabilidade de [evidência]? Quem produziu? Quais os incentivos? É IPE ou produzida pelo próprio processo auditado?

### 8. Iluminador de Fatores Ocultos
**Quando:** risco recorrente sem resolução ou escopo que deixou algo de fora.
> Apesar de ter tentado [abordagens], o problema [X] continua. Que fatores sistêmicos ou variáveis ocultas podem estar sendo ignorados?

### 9. Empréstimo de Modelos Mentais
**Quando:** preso numa única forma de avaliar o controle ou risco.
> Como um [investigador de fraude / engenheiro de sistemas / advogado / gestor de risco] abordaria [situação]? Aplique o modelo mental principal dessa área.

### 10. Afiador de Definições
**Quando:** debate sobre severidade, materialidade ou definição de controle não avança.
> Defina de forma precisa o que "[termo]" significa neste contexto. Mostre como interpretações diferentes estão gerando o conflito.

### 11. Desafiador do Status Quo
**Quando:** justificativa é "sempre fizemos assim" ou "nunca aconteceu".
> Por que a abordagem tradicional de [processo/controle] pode estar falhando agora? O fato de nunca ter acontecido é evidência de controle ou de sorte?

### 12. Separador de Fato vs. Opinião
**Quando:** discussão com gestão ficou defensiva ou emocional.
> No debate sobre [tópico], separe: (1) fatos verificáveis com evidência; (2) interpretações e opiniões baseadas em perspectiva ou interesse.

### 13. Validador de Compreensão
**Quando:** após walkthrough ou entrevista — antes de documentar.
> Meu entendimento do processo/controle é: [descrever com as próprias palavras]. Corrija imprecisões, simplificações excessivas ou pontos que parecem entendidos mas não foram confirmados com evidência.

---

## Vieses específicos de auditoria interna

Além dos vieses cognitivos gerais, atenção a padrões recorrentes em auditoria:

| Viés | Como se manifesta | Como quebrar |
|---|---|---|
| **Viés de confirmação de entrevista** | Gestão diz que o controle funciona → auditor aceita e documenta | Perguntar: "Qual evidência posso ver que comprova isso, independente do que me foi dito?" |
| **Viés de escopo fácil** | Auditor testa o que é simples de testar, não o que tem maior risco | Perguntar: "O que eu evitei testar porque seria difícil ou incômodo?" |
| **Ancoragem no risco inerente** | RI Alto → auditor busca evidência que confirma, não que refuta | Perguntar: "O que precisaria ser verdade para esse risco ser Moderado?" |
| **Viés de relacionamento** | Achado rebaixado para preservar relação com área auditada | Perguntar: "Se eu não conhecesse essa pessoa, qual seria minha conclusão?" |
| **"Controle compensatório" como desculpa** | Controle fraco aceito porque "existe outro" — não testado | Perguntar: "O controle compensatório foi testado? Ou só mencionado?" |
| **Viés de histórico limpo** | "Nunca aconteceu" usado como evidência de controle efetivo | Perguntar: "Falta de incidente é controle ou ausência de detecção?" |
| **Viés de complexidade** | Risco complexo classificado como Baixo porque é difícil de avaliar | Perguntar: "Estou classificando como baixo porque é baixo ou porque não sei medir?" |

---

## Técnicas de Amplificação

| Técnica | Como acionar |
|---|---|
| **Virada de Chave** | "Pensa nisso de forma diferente." |
| **Foco no Essencial** | "O que eu realmente estou perguntando é: [reformular]" |
| **Pedido de Opinião** | "Se você fosse o auditor, qual seria sua conclusão?" |
| **Busca pelo Oculto** | Adicionar ao final: "O que mais devo considerar antes de concluir?" |
| **Desconstrução** | "Desmembre esse argumento para mim." |

### 14. Prudent Official Challenge

**Quando:** deficiência classificada como D ou SD, mas o contexto levanta dúvida — gestão subestimou, há histórico de falhas ou o achado toca área de risco elevado.

> *"Um profissional prudente, com o mesmo conhecimento dos fatos e circunstâncias, concordaria com essa classificação de severidade — ou a elevaria?"*

**5 sinais de que a classificação está subestimada (referência metodológica / estudo empírico):**
1. Múltiplas exceções explicadas com "razões diferentes" → padrão de falha, não evento isolado
2. Compensação invocada por controle não testado ou de precisão insuficiente
3. Severidade rebaixada sem evidência de que o risco materializado é de fato inconsequente
4. Falha que já aconteceu antes sem remediação efetiva ("SD recorrente")
5. Área susceptível a fraude, estimativa subjetiva ou transação não rotineira → likelihood subestimado

**9 cenários que presumem SD ou MW (referencial metodológico — Deficiências especiais):**
- Fraude identificada de qualquer magnitude por parte da alta administração
- Reapresentação de demonstrações financeiras por erro material passado
- Distorção material descoberta pelo auditor que não teria sido detectada internamente
- Supervisão ineficaz do ICFR pelo comitê de auditoria
- Ausência de expertise contábil interna para aplicar GAAP nas transações da entidade
- Ausência de programas e controles antifraude
- Controles insuficientes sobre transações não rotineiras
- Controles insuficientes sobre o processo de fechamento periódico
- Indiferença gerencial em corrigir SDs ou MWs conhecidas

> **Dado empírico (estudo empírico de referência):** 70% das deficiências classificadas pela gestão como "major deficiency" foram reclassificadas para severidade maior pelos auditores. Ao revisar avaliação da gestão, tratar subestimação como risco esperado — não exceção.

---

### 15. Velocity & Persistence Check

**Quando:** risco priorizado para período posterior mas o processo está em mudança rápida, crescimento acelerado ou ambiente volátil.

> Além de impacto e probabilidade, dois fatores determinam urgência real: **velocity** (quão rápido o risco pode se materializar se o controle falhar) e **persistence** (quanto tempo o risco permanece ativo antes de ser detectado e corrigido).

**Perguntas de calibração:**

| Dimensão | Pergunta |
|---|---|
| **Velocity** | Se o controle falhar hoje, em quanto tempo o impacto é irreversível? Horas? Dias? Trimestres? |
| **Velocity** | O processo está crescendo, digitalizando ou passando por mudança — o que era lento ficou rápido? |
| **Persistence** | Quanto tempo esse risco pode existir sem ser detectado pelos controles atuais? |
| **Persistence** | O ciclo de detecção (mensal, anual) é compatível com a velocidade de materialização? |

**Regra de priorização:**
- Velocity alta + Persistence alta → elevar para Q1 independente do score de RI
- Velocity alta + Persistence baixa → manter prioridade, mas adicionar trigger de monitoramento
- Velocity baixa + Persistence alta → candidato a monitoramento contínuo em vez de teste pontual
- Velocity baixa + Persistence baixa → prioridade padrão do heat map

> **Aplicação típica:** risco de acesso a sistema legado classificado como Moderado pode ter velocity alta se o volume de transações dobrou. Risco de reconciliação trimestral pode ter persistence de 90 dias — tempo suficiente para distorção acumular antes da detecção.

---

## Meta-prompt (contexto vago)

> Estou concluindo sobre [risco/controle/achado]. Qual é a pergunta de pensamento crítico mais importante que devo fazer agora e que provavelmente estou ignorando?

---

## Blind Spot Scan — aplicado a auditoria

Quando quiser feedback franco sobre o próprio raciocínio antes de finalizar:

1. **Análise direta:** Qual o principal ponto-cego nessa conclusão? O que provavelmente não está sendo percebido?
2. **Análise exploratória:** Que perspectivas não foram consideradas? Que perguntas deveriam ter sido feitas?
3. **Análise por persona:**
   - Como **gestor da área auditada**: quais os argumentos de defesa mais fortes?
   - Como **auditor externo revisando o trabalho**: o que questionaria nessa conclusão?
   - Como **conselho / comitê de auditoria**: o que estaria faltando nesse achado?
   - Como **investigador de fraude**: o que esse processo permite que ainda não foi examinado?

---

## Output obrigatório

Ao aplicar qualquer ferramenta:

- Qual ferramenta foi aplicada e por quê
- O desafio concreto ao raciocínio apresentado
- O que essa perspectiva revela que não estava visível antes
- Uma ou duas perguntas para continuar examinando antes de concluir

---

## Regras

- Não suavizar o desafio por educação. O valor está na fricção intelectual.
- Distinguir "isso está errado" de "isso tem uma suposição não examinada" — a segunda é mais útil.
- Quando múltiplas ferramentas forem aplicáveis, escolher a que ataca a suposição mais central.
- Não encerrar com resposta — encerrar com pergunta. O objetivo é mover o pensamento, não substituí-lo.
- Evidência produzida pelo próprio processo auditado (IPE) exige verificação independente antes de aceitar como suporte de controle.
