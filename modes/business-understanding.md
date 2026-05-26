# mode: business-understanding

## Papel

Construir entendimento da entidade antes de qualquer trabalho de auditoria: modelo de negócio, indústria, pressões, estrutura organizacional e ambiente de controle em nível macro. Não é workflow de execução — é camada de contexto que alimenta `audit-planning`, `risk-assessment` e `risk-control-mapping`.

Diferença de `skills/client-context.md`: esse skill mantém o perfil persistente do cliente (índice, pessoas, processos). Este modo **usa** o perfil do cliente e vai além — analisa, interpreta e produz leitura de risco do negócio.

## Quando Usar

- início de relacionamento com novo cliente ou nova unidade de negócio
- antes de construir o plano anual de auditoria
- quando o contexto da entidade mudou (M&A, reestruturação, novo CEO, nova regulação)
- quando o output do `audit-planning` parece genérico — sinal de que o entendimento do negócio está raso

## Inputs

- perfil do cliente em `context/clients/<cliente>/` (se existir — rodar `skills/client-context.md` modo `init` se não existir)
- documentos sobre o negócio: relatório anual, organograma, site institucional, apresentação para conselho
- entrevistas ou transcrições com gestão (`workflows/transcript-analysis.md`)
- qualquer informação prévia do setor (relatórios de mercado, regulação aplicável)

## Sequência de Entendimento

### 1. Perfil da entidade

Capturar antes de interpretar:

- Atividade principal e produtos/serviços oferecidos
- Porte: receita, headcount, ativos, número de unidades/filiais
- Estrutura societária: controladora, subsidiárias, joint ventures, partes relacionadas relevantes
- Estágio do negócio: crescimento, maturidade, reestruturação, declínio

### 2. Modelo de negócio e cadeia de valor

Entender como a empresa gera e captura valor:

- Quem são os clientes e como a empresa os alcança?
- Quais os principais processos que geram receita?
- Onde estão as margens — quais produtos/segmentos são mais lucrativos?
- Quais os principais custos e onde há maior exposição a variação?
- Há dependência crítica de fornecedor, tecnologia ou pessoa-chave?

### 3. Indústria e ambiente externo

Contextualizar riscos que vêm de fora da entidade:

- Qual a dinâmica competitiva do setor? A empresa é price-taker ou tem poder de precificação?
- Há sazonalidade relevante que afeta controles ou exposição?
- Quais as regulações setoriais aplicáveis (agências, normas, licenças)?
- O setor está passando por disrupção tecnológica, consolidação ou pressão regulatória?
- Qual o ciclo macroeconômico — a empresa é cíclica ou anticíclica?

### 4. Objetivos, pressões e incentivos

Este passo é o mais crítico para o auditor — é onde surgem os riscos não óbvios:

- Quais os objetivos formais da gestão (metas, guidance, bônus)?
- Há pressão de curto prazo sobre resultados? Quem está pressionando e por quê?
- Onde a gestão tem maior discricionariedade contábil ou operacional?
- Há histórico de turnover alto em áreas financeiras ou de controle?
- Qual a postura cultural em relação a riscos e controles?

Sinal de alerta: pressão intensa + discricionariedade alta + controles fracos = risco de fraude elevado. Registrar como input para `workflows/audit-planning.md` e para o Fraud Risk Assessment.

### 5. Estrutura organizacional e governança

- Quem são os tomadores de decisão e qual o nível de centralização?
- O comitê de auditoria ou conselho é ativo ou passivo?
- A função de auditoria interna tem independência real (reporte funcional ao comitê)?
- Existem funções de segunda linha (Compliance, Gestão de Riscos, Controles Internos)?
- Há segregação de funções adequada nos processos-chave?

### 6. Ambiente de controle (ELC)

Avaliar o tom geral da organização em relação a controles internos — referência: COSO Componente 1 (`context/standards/sox.md`, Princípios 1–5):

| Elemento | Evidência a buscar |
|---|---|
| Código de ética e conduta | Existe? É comunicado? Há casos de violação? |
| Comprometimento com competência | Planos de capacitação, rotatividade, qualificação em funções-chave |
| Accountability | Consequências reais por falhas de controle? |
| Supervisão do board/comitê | Frequência de reuniões, qualidade das atas, perguntas ao management |
| Estrutura organizacional | Linha de reporte clara, delegação documentada, segregação |

### 7. Sistemas e dependências de TI

- Quais os sistemas centrais (ERP, CRM, BI) e qual o nível de integração entre eles?
- Há processos críticos rodando em planilhas ou sistemas locais (shadow IT)?
- O ambiente de TI é estável ou passou por mudanças recentes (migração, upgrade, novo ERP)?
- Há dependência de terceiros para processos críticos (outsourcing de TI, folha, fiscal)?

### 8. Mudanças recentes e sinais de risco

Mudanças aumentam risco inerente — sempre verificar:

- Houve M&A, carve-out ou reestruturação nos últimos 12–24 meses?
- Houve mudança na liderança (CFO, CEO, Controller)?
- Novos produtos, mercados ou canais?
- Auditoria externa emitiu ressalva, ênfase ou carta de controle nos últimos ciclos?
- Há litígios, investigações regulatórias ou notícias adversas relevantes?

## Guardrails

- Não confundir entendimento do negócio com execução — a saída é contexto, não RCM nem achado
- Não documentar o óbvio — focar no que é não-padrão, pressão ou sinal de risco
- Não assumir que o cliente é igual ao setor — calibrar pela entidade específica
- Se o entendimento revelar indícios de fraude, registrar imediatamente e tratar no `workflows/audit-planning.md` como risco elevado antes de prosseguir
- Atualizar o perfil em `context/clients/<cliente>/` após rodar este modo

## Output

Narrativa de entendimento com:

1. **Perfil executivo** — porte, atividade, estrutura (4–6 linhas)
2. **Modelo de negócio** — como gera valor, onde estão as margens, dependências críticas
3. **Pressões e incentivos** — objetivos da gestão, pontos de discricionariedade, cultura de controle
4. **Sinal de risco consolidado** — top 3–5 riscos ao nível da entidade para alimentar `risk-assessment`
5. **Gaps de entendimento** — o que não foi possível obter e o que fazer para preencher

## Artefatos Relacionados

- `skills/client-context.md` — manter perfil persistente do cliente (pré-requisito)
- `skills/operating-model-analysis.md` — quando há transformação operacional (SSC, carve-out, post-merger)
- `workflows/audit-planning.md` — receptor do entendimento do negócio
- `modes/risk-assessment.md` — próximo passo: avaliar riscos no nível da entidade
- `context/standards/sox.md` — Princípios COSO 1–5 (ambiente de controle)
- `context/standards/iia-ippf.md` — Domínio IV (planejamento anual) e Domínio V (planejamento do trabalho)
