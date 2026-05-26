# workflow: transcript-analysis

## Goal

Consumir uma transcrição bruta e extrair processo, atores, controles, lacunas e sinais de risco em formato técnico utilizável para auditoria interna.

## Use When

- há uma transcrição longa de walkthrough ou reunião
- o conteúdo útil ainda está diluído em fala corrida
- é preciso transformar conversa em base técnica de documentação
- existe necessidade de separar fato, hipótese e ruído

> Para transcrições cujo output final será `SCOT`, `ICFR`, `placemat` ou documentação de auditoria externa, usar `_method-wiki-external-audit/workflows/transcript-analysis-external-audit.md`.

## Inputs

- transcrição bruta
- contexto do processo ou módulo
- objetivo da análise (walkthrough? mapeamento de risco? planejamento?)
- documento base anterior, se houver

## Analysis Sequence

### 1. Limpar o ruído

Reduzir peso de:

- repetições sem valor analítico
- pausas, hesitações e digressões
- comentários laterais que não mudam o processo
- confirmações genéricas

### 2. Extrair o processo real

Identificar na fala:

- gatilho do processo
- sequência de etapas em ordem lógica
- atores e áreas envolvidas
- sistemas mencionados
- aprovações, validações, exceções e overrides
- entradas e saídas relevantes

### 3. Separar níveis de certeza

Classificar cada ponto como:

- **Fato explícito**
- **Inferência plausível**
- **Lacuna / a confirmar**

### 4. Ler sinais de controle e risco

Perguntas enquanto lê:

- onde há dependência excessiva de uma pessoa?
- onde há aprovação formal documentada?
- onde há validação manual sem trilha?
- onde o processo depende de handoff frágil entre áreas?
- onde o output do processo pode sair incompleto, incorreto ou atrasado?

### 5. Preparar base para o próximo artefato

A saída deve estar pronta para alimentar diretamente:

- `walkthrough-standardization`
- `risk-control-mapping`
- `audit-planning`
- `finding-drafting` (se um achado emergir na transcrição)

## Decision Rules

- não transformar fala ambígua em certeza
- preservar conteúdo relevante mesmo quando mal formulado
- separar claramente o que foi dito do que foi interpretado
- em auditoria interna, priorizar fluxo operacional por ator, fronteira do processo, entradas, saídas e objetivo do processo
- quando a transcrição não bastar, sinalizar o que precisa de confirmação antes de avançar

## Output

- síntese técnica da transcrição
- processo extraído em sequência lógica
- atores, sistemas e controles percebidos
- sinais de risco identificados
- lacunas e ambiguidades com indicação de follow-up

## Output Format

1. leitura rápida da transcrição (objetivo e contexto)
2. processo extraído
3. atores, sistemas, entradas, saídas e controles identificados
4. sinais de risco e dependências críticas
5. lacunas e pontos a confirmar
6. próximo uso recomendado do material

## Integração com client-context

Ao fim do workflow, verificar se existe perfil do cliente em `context/clients/`:

**Se existe perfil (`context/clients/<slug>/index.md`):**

1. Propor salvar a reunião em `context/clients/<slug>/meetings/<YYYY-MM-DD>-<tema>.md`
2. Identificar novas tarefas e decisões e propor update de `open-tasks.md`
3. Identificar informação nova sobre pessoas, processos ou ambiente de controle e propor update do MD correspondente

**Se não existe perfil:**

> "Não encontrei perfil de cliente em `context/clients/`. Quer criar um antes de salvar esta reunião? Use `skills/client-context.md` modo `init`."
