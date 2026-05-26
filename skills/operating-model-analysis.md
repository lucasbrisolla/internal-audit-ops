# skill: operating-model-analysis

## Goal

Decodificar transformações estruturais — SSC, GBS, carve-out, post-merger integration, outsourcing, migração de plataforma — para identificar o que realmente aconteceu, por que a redução de custo ou eficiência ocorreu, e quais riscos novos emergiram da própria transformação.

Essa skill opera **antes** de `risk-control-mapping` e `audit-planning`. Ela questiona a estrutura operacional assumida como dada, aplicando modelos mentais de economia, teoria das organizações e gestão industrial para revelar o que frameworks de controle padrão (COSO, ERM, ISO 31000) não surfaceiam.

## Use When

- cliente passou por ou está passando por SSC/GBS, centralização de back-office, Finance Business Partner (FBP), outsourcing ou plataforma global
- a transformação é recente e os controles ainda não foram revalidados no novo modelo
- o auditor precisa entender o que mudou estruturalmente antes de mapear riscos
- há afirmação de redução de custo, ganho de eficiência ou melhoria de controle associada à transformação
- o engajamento exige posicionamento de valor além de "mapeamento de controles"
- o usuário quer preparar argumento para entrevista, proposta ou reunião de planejamento com cliente em transformação

## Inputs

- descrição ou slide da transformação (antes × depois)
- processos afetados: PTP, RTR, OTC, HR, IT — quais foram centralizados e quais permaneceram locais
- número de entidades, regiões ou plataformas envolvidas
- indicadores de resultado declarados: % de redução de custo, headcount, tempo de ciclo
- estrutura pós-transformação: quem faz o quê, onde, em qual sistema
- contexto de auditoria: primeiro ano pós-go-live, auditoria de controles, preparação de planejamento

## Análise — Sequência

### 1. Decodificar a alavanca real de resultado

Antes de aceitar a narrativa do slide, identificar de qual combinação de alavancas vem o resultado declarado:

| Alavanca | Pergunta diagnóstica | Framework por trás |
|---|---|---|
| Arbitragem geográfica | O trabalho foi para país/cidade de custo menor? | Teoria do comércio, custo de mão-de-obra |
| Deslocamento de seniority | O nível médio do cargo caiu com a padronização? | Braverman — degradação qualificada do trabalho |
| Eliminação de redundância | Quantas regiões faziam o mesmo processo? | Economias de escala (Coase) |
| Padronização forçada | O processo único substituiu N variantes locais? | Deming — redução de variação |
| Pré-condição para automação | A centralização viabiliza RPA/IA que antes era inviável? | Teoria da plataforma |
| Redistribuição de poder | Quem ganhou e quem perdeu escopo de decisão? | Teoria da firma (Coase), design organizacional |

Nomear as 2–3 alavancas principais. Não aceitar "sinergia" como resposta — nomear o mecanismo.

### 2. Mapear riscos emergentes da transformação (não do processo)

Esses riscos nascem da **mudança estrutural**, não do processo transacional em si. COSO não os captura diretamente.

**Risco de interface (handshake)**
Onde a responsabilidade passa de um ator para outro na nova estrutura? SSC ↔ FBP, SSC ↔ entidade local, plataforma global ↔ compliance local. Cada handshake é uma lacuna de accountability potencial: quando o número está errado, quem responde?

**Risco de concentração**
Antes: risco distribuído em N plataformas (falha local = impacto local). Depois: risco concentrado em 1 SSC (falha central = parada global). Aumentou o impacto potencial. Mitigação precisou ser redesenhada?

**Risco de padronização vs. idiossincrasia local**
Processo único para todas as entidades ignora diferenças regulatórias, fiscais, trabalhistas ou contábeis locais? Brasil, França, EUA: requisitos distintos. Padronização forçada cria compliance gap onde a variação era necessária, não ineficiência.

**Risco de controle em transição**
Durante a migração, controles antigos foram desativados. Controles novos podem não estar maduros. Primeiro exercício pós-go-live tem gap quase certo — o ambiente de controle está sendo construído em paralelo ao processo.

**Risco de knowledge drain**
Quem detinha conhecimento do processo saiu com a centralização? Especialistas locais foram dispensados; o conhecimento tácito (exceções, clientes problemáticos, idiossincrasias históricas) não foi transferido ao SSC.

**Risco de obsolescência do FBP**
Se RPA/IA vai automatizar as transações do SSC, o FBP precisa evoluir de "analista de variação" para "gestor de exceção e automação". Organizações que não planejaram isso criam vácuo de função em 2–3 anos.

### 3. Identificar onde o auditor tem valor real

Não onde o manual diz — onde a fricção estrutural nova cria risco não coberto:

- **Testes de controle de interface**: existe controle formal no handshake SSC ↔ entidade? Quem aprova, valida, reconcilia?
- **Revisão de alçadas pós-migração**: quem tem acesso e aprovação no novo ERP/sistema central? Mudou com a transformação?
- **Cobertura regulatória local**: o processo padronizado cobre obrigações locais de cada entidade? Teste por amostra de jurisdições críticas.
- **Plano de continuidade do SSC**: existe BCP para single point of failure da operação global?
- **Avaliação da maturidade do SSC**: primeiro ano — qual o baseline de controle? Não comparar com operação estável.

### 4. Posicionar o argumento

Sintetizar em uma afirmação de valor:

> "O desafio não é controlar melhor dentro do processo — é garantir que a nova estrutura tem accountability clara nos pontos de handshake, que a padronização não criou gap de compliance local, e que o ambiente de controle foi revalidado, não apenas assumido como transferido."

Adaptar para contexto de entrevista, planejamento ou reunião com cliente.

## Modelos Mentais de Referência

| Modelo | Quando aplicar |
|---|---|
| **Coase — Teoria da Firma** | Onde a empresa parou e o mercado começou? Quais decisões foram internalizadas vs. externalizadas? |
| **Taylor — Scientific Management** | O trabalho foi decomposto em tarefas padronizáveis e não-padronizáveis? Qual parte virou commodity? |
| **Porter — Value Chain** | Qual atividade foi separada, terceirizada ou centralizada? Foi atividade primária ou suporte? |
| **Deming — Redução de Variação** | A padronização eliminou variação necessária ou variação ineficiente? |
| **Braverman — Degradação do Trabalho** | A centralização reduziu qualificação média exigida? Impacto no risco de erro e julgamento? |
| **Teoria de Plataforma** | A centralização cria efeito de rede interno? Economias de escopo + aprendizagem? |
| **Single Point of Failure** | Engenharia de sistemas: onde está o ponto único de falha? Qual redundância existe? |

Não é necessário citar o modelo pelo nome no output — usar o raciocínio.

## Decision Rules

- Não aceitar "melhoria de controle" como explicação de redução de custo sem identificar o mecanismo real
- Não mapear riscos do processo transacional sem antes mapear riscos da estrutura que mudou
- Não assumir que controles migrados com o processo funcionam igual ao ambiente anterior
- Não confundir padronização com melhoria — avaliar se a variação eliminada era ineficiência ou requisito local
- Quando o cliente descrever benefícios sem trade-offs, usar **Advogado do Diabo**: que risco foi aceito implicitamente?
- Distinguir risco de **transição** (temporário, migração) de risco de **modelo** (permanente, estrutural)

## Output Format

### 1. Leitura da Transformação

Descrever o que realmente aconteceu em 3–5 linhas. Nomear as alavancas reais de resultado, não a narrativa do slide.

### 2. Riscos Emergentes da Estrutura

| Risco | Tipo | Mecanismo | Severidade Potencial | Evidência ou Hipótese |
|---|---|---|---|---|
| Handshake SSC ↔ entidade sem controle formal | Interface | Accountability difusa | Alta | A ser verificado |
| ... | | | | |

Tipo: Interface / Concentração / Padronização / Transição / Knowledge / Modelo

### 3. Ângulo de Auditoria

Onde o auditor tem valor que vai além do checklist padrão. Listar 3–5 áreas de teste ou revisão prioritárias com justificativa estrutural.

### 4. Posicionamento

> **Pergunta-chave para o cliente:** [formulação que captura o risco central sem ser adversarial]
> **Argumento de valor do auditor:** [síntese do que o auditor vê que o gestor não vê]
> **O que não está nos manuais:** [o risco ou mecanismo que COSO/ERM não nomeia diretamente]
