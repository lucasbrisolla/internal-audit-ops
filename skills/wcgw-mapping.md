# skill: wcgw-mapping

## Goal

Identificar WCGWs de um processo a partir de descrição narrativa, walkthrough ou transcrição, calibrado para auditoria interna. Foco em falha de controle, segregação, governança e exposição operacional — não em assertivas de demonstrações financeiras.

## Use When

- há um processo descrito e é preciso mapear o que pode dar errado antes de montar a RCM
- a equipe precisa de WCGWs como insumo para o programa de trabalho
- revisão de WCGWs existentes para verificar lacunas
- avaliação de mapeamento de risco produzido por terceiro

## Inputs

- descrição do processo (walkthrough, transcrição, narrativa ou texto descritivo)
- escopo do engagement (operacional, compliance, TI, financeiro — declarar antes de operar)
- contexto do cliente, setor e sistema utilizado, se disponível
- WCGWs já mapeados, se houver (para revisão)

## Mapping Sequence

### 1. Carregar biblioteca de referência

Identificar o(s) processo(s) correspondente(s) em `context/wcgw/` e carregar antes de qualquer output.

Processos mais comuns para faturamento e receita:
- `context/wcgw/order-to-cash.md`
- `context/wcgw/revenue-recognition.md`

Usar a biblioteca como referência calibradora — não copiar mecanicamente. Customizar ao processo real do cliente.

### 2. Mapear atividades por responsável

Decompor o processo em atividades operacionais concretas — não por fase contábil, mas por **o que é feito, por quem, em qual sistema, e o que dispara ou produz cada etapa**.

Para cada atividade, registrar:

| Campo | Pergunta-guia |
|---|---|
| Atividade | O que é feito nesta etapa? |
| Área / Responsável | Quem executa? É a área certa para isso? |
| Sistema | Onde ocorre? Manual, sistêmico ou híbrido? |
| Input | O que dispara esta atividade? Vem de onde? |
| Output | O que produz? Para onde vai? |
| Ponto de controle esperado | Deveria existir controle aqui? Existe? |

Focos de atenção ao mapear:

- **Handoffs entre áreas**: onde uma área entrega para outra sem protocolo formal?
- **Etapas manuais em alto volume**: onde dependência humana cria risco de omissão ou erro?
- **Decisões sem critério formal**: aprovação baseada em bom senso, relação pessoal ou hábito?
- **Dependências de terceiros**: quem fornece input externo sem controle de recebimento?
- **Integração entre sistemas**: dados transitam sem ponto de conferência humana?

> **Referência opcional — Ciclo da Transação:** para cruzamento com auditoria externa ou comunicação com equipe SOX, cada atividade pode ser marcada com a fase correspondente: Initiation / Recording / Processing / Reporting. Isso não altera a análise — é apenas tag de referência. Definições completas das 4 fases em `_method-wiki/concepts/scot-and-wcgw-foundations.md`.

### 3. Aplicar lentes de auditoria interna

Para cada etapa, perguntar:

**Controle**
- Existe controle para esse ponto?
- O controle está desenhado para mitigar o risco?
- O controle depende de ação manual sem evidência?

**Segregação de funções**
- A mesma pessoa executa etapas incompatíveis (autoriza + executa + registra + revisa)?

**Autorização e alçada**
- Existe aprovação formal antes da ação?
- A alçada está definida e respeitada?

**Dependência de sistema**
- O processo depende de integração automática sem ponto de revisão?
- Falha de migração ou parametrização pode contaminar dados sem alerta?

**Completude de execução**
- Todas as transações elegíveis são processadas?
- Há risco de omissão silenciosa (sem alerta, sem reconciliação)?

**Terceiros e outsourcing**
- Parte do processo está com terceiro sem controle de entrega ou completude?

**Governança e comunicação**
- Existe protocolo formal entre áreas que dependem uma da outra?
- Decisões são comunicadas de forma padronizada ou ad hoc?

### 4. Classificar cada WCGW

Para cada risco identificado:

| Campo | Opções |
|---|---|
| Tipo de risco | Operacional / Compliance / Governança / TI / Fraude |
| Origem | Humana / Sistêmica / Design do processo / Terceiro |
| Lacuna de controle | Sim — sem controle / Sim — controle inadequado / A confirmar |
| Severidade | Baixo / Moderado / Alto / Crítico |

**Critérios de severidade para auditoria interna:**
- **Crítico**: fraude possível, processo crítico sem controle, falha sistêmica já ocorrida, exposição financeira relevante
- **Alto**: controle existe mas com lacuna de desenho relevante, dependência manual em processo de alto volume, terceiro sem controle de completude
- **Moderado**: controle frágil ou sem evidência, comunicação informal entre áreas críticas, risco conhecido mas com mitigação parcial
- **Baixo**: risco remoto, controle compensatório presente, impacto operacional limitado

Quando threshold financeiro ou volumétrico do cliente estiver disponível, usar `skills/risk-scoring.md` para calibrar o enquadramento.

### 5. Separar risco de causa

Risco = o que pode dar errado (consequência).
Causa = por que pode dar errado (fator).

Manter separados no output. Misturar os dois impede o desenho de teste.

Exemplo:
- **Causa**: dependência de ação manual para faturamento em lote
- **Risco**: clientes elegíveis não faturados no período (incompletude do faturamento)

## Decision Rules

- Não inventar controle que "deveria existir" — registrar como lacuna e sinalizar
- Não transformar causa em risco nem risco em controle
- Não mapear WCGWs de assertiva de DF a menos que o escopo do engagement inclua reporting financeiro
- Se o processo não estiver claro o suficiente, sinalizar a lacuna antes de avançar
- Customizar ao processo real — não replicar biblioteca genericamente
- Um WCGW sem controle mapeado é uma lacuna — registrar explicitamente, nunca omitir

## Output Format

### 1. Mapa de Atividades do Processo

Tabela de atividades operacionais por responsável — base para identificação de WCGWs, handoffs e lacunas de controle:

| # | Atividade | Área / Responsável | Sistema | Input | Output | Ponto de controle esperado | Fase (ref.) |
|---|---|---|---|---|---|---|---|

> Coluna "Fase (ref.)" é opcional — usar Initiation / Recording / Processing / Reporting apenas para cruzamento com auditoria externa ou SOX. Não é requisito da análise de auditoria interna.

### 2. WCGWs Identificados

| # | Atividade / Subprocesso | WCGW (risco) | Causa principal | Tipo | Origem | Lacuna de Controle | Severidade | Fase (ref.) |
|---|---|---|---|---|---|---|---|---|

### 3. Lacunas prioritárias

Lista das lacunas sem controle identificado, ordenadas por severidade. Máximo 5 itens para focar o programa de trabalho.

### 4. O que falta confirmar

Pontos onde a descrição do processo não foi clara o suficiente para concluir sobre o risco ou o controle — sinalizar antes de avançar.
