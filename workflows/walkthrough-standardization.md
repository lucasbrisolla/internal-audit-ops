# workflow: walkthrough-standardization

## Goal

Transformar um relato bruto de walkthrough em documentação técnica clara, formal e rastreável para auditoria interna.

Suporta três modos:

- padronização narrativa
- refinamento comparativo com base anterior
- tabela de processo para SIPOC / BPMN / RCM

> Para walkthrough com output `SCOT`, `placemat`, `Project Insight` ou documentação típica de auditoria externa, usar `_method-wiki-external-audit/workflows/walkthrough-standardization-external-audit.md`.

## Use When

- há um texto descritivo de processo mal estruturado
- existe walkthrough bruto que precisa virar documentação utilizável
- é preciso reorganizar etapas em sequência lógica
- o texto atual está coloquial, disperso ou com atores implícitos
- há uma base anterior e nova evidência que precisa ser incorporada
- é preciso gerar uma tabela estruturada para SIPOC, BPMN, Mermaid, Excel ou RCM

## Inputs

**Modo 1 — Padronização narrativa:**
- texto bruto de walkthrough ou transcrição já processada
- contexto do processo ou cliente
- objetivo da documentação

**Modo 2 — Comparativo:**
- nova transcrição ou evidência
- documento base anterior
- objetivo do refinamento

**Modo 3 — Tabela para processo / SIPOC / BPMN:**
- texto bruto, transcrição processada ou walkthrough narrativo
- nível de detalhe desejado
- objetivo de uso da tabela: SIPOC, BPMN, Mermaid, RCM ou revisão humana

## Mode 1: Standardization Sequence

### 1. Ler o relato sem embelezar

- quais etapas realmente aparecem no texto?
- o que é ação concreta e o que é comentário periférico?
- o que está explícito e o que ainda é lacuna?

### 2. Identificar os elementos do processo

Extrair, quando possível:

- atores
- sistemas
- entradas
- validações e aprovações
- saídas
- interfaces com outras áreas

### 3. Organizar o processo por lógica operacional

Em auditoria interna, priorizar:

- fronteira do processo
- objetivo do processo
- fluxo por ator / área
- inputs e outputs
- handoffs e pontos de controle

### 4. Refinar a linguagem

O texto final deve:

- usar tom profissional e impessoal
- preferir voz ativa
- nomear atores e sistemas quando houver evidência
- eliminar coloquialismos e redundâncias
- preservar lacunas em vez de escondê-las

### 5. Marcar lacunas e ambiguidades

Explicitar quando houver:

- ator não identificado
- etapa ambígua
- sequência incompleta
- controle implícito sem confirmação
- input, output ou customer não confirmados

## Mode 2: Comparative Refinement Sequence

### 1. Processar a nova evidência primeiro

- o que foi confirmado em relação ao processo atual?
- o que contradiz ou desatualiza o documento base?
- o que é informação nova não coberta na base?

### 2. Carregar o documento base

- quais etapas permanecem válidas?
- quais etapas precisam de correção?
- há algo no base que ficou obsoleto ou precisa de confirmação?

### 3. Integrar com regras de prioridade

- nova evidência explícita substitui o documento base
- silêncio da nova evidência não invalida o base
- contradição explícita deve ser sinalizada para confirmação humana

### 4. Entregar documento refinado

Marcar com clareza:

- o que permanece como fato
- o que foi atualizado
- o que foi inferido com cautela
- o que ainda precisa de confirmação

## Mode 3: Process Table for SIPOC / BPMN / RCM

### 1. Extrair etapas atômicas

Cada etapa deve responder, quando possível:

- o que acontece?
- quem executa?
- em qual sistema, planilha, portal ou documento?
- qual entrada aciona a etapa?
- qual saída é produzida?
- qual é a próxima etapa lógica?

### 2. Classificar por estrutura de auditoria interna

Preencher colunas para:

- atividade
- ator / área
- sistema / documento
- entrada
- saída
- controle identificado
- próxima etapa
- observações / lacunas

Se fizer sentido para entendimento macro, derivar também um resumo `SIPOC`.

### 3. Preservar sequência e dependência

- se a ordem narrada estiver confusa, reorganizar pela lógica operacional
- se houver ramificações, criar linhas separadas e indicar condição
- se a próxima etapa não estiver clara, registrar `A confirmar`

### 4. Preparar para automação futura

A tabela deve permitir exportação posterior para:

- SIPOC
- BPMN
- Mermaid
- Excel
- scripts Python

Para converter a tabela em diagrama Mermaid, usar `skills/process-flow-mermaid.md`.

## Decision Rules

- não inventar etapa sem base no insumo
- não omitir etapa material só para deixar o texto elegante
- quando houver dúvida, preservar a lacuna
- reorganizar o processo sem alterar seu conteúdo factual
- em auditoria interna, preferir fluxo por ator e objetivo do processo a classificações SCOT

## Output Format

**Modo 1 — Padronização narrativa:**
1. leitura rápida do objetivo do walkthrough
2. processo padronizado
3. atores, sistemas, entradas, saídas e controles identificados
4. lacunas ou pontos a confirmar

**Modo 2 — Refinamento comparativo:**
1. síntese das diferenças entre base e nova evidência
2. processo refinado
3. o que permaneceu, o que mudou, o que foi inferido
4. o que ainda precisa de confirmação

**Modo 3 — Tabela de processo:**

| ID | Etapa do Processo | Ator / Área | Sistema / Documento | Entrada | Saída | Controle Identificado | Próxima Etapa | Condição / Observação |
|---|---|---|---|---|---|---|---|---|
