# skill: control-documentation

## Goal

Expandir menções de controle identificadas em narrativas de processo em descrições completas, padronizadas e testáveis. Transforma "o analista confere a NF" em um controle com gatilho, executor, dado, threshold, evidência e critério de falha — pronto para ser avaliado por `control-evaluation.md`.

## Use When

- narrativa de processo foi lida e controles foram identificados mas estão descritos de forma vaga
- preparando controles para entrada no `control-evaluation.md`
- montando a Matriz de Controle a partir de uma narrativa (walkthrough, transcrição ou texto descritivo)
- revisando descrições de controles existentes que não têm atributos suficientes para teste

## Inputs

- trecho da narrativa que menciona o controle (direto ou implícito)
- risco que o controle deve mitigar (do output do `wcgw-mapping.md`)
- contexto do processo: sistemas usados, responsáveis, frequência operacional
- resultado de entrevista ou walkthrough, se disponível

---

## Expansion Sequence

### 1. Identificar controles na narrativa

Varrer a narrativa em busca de:

**Controles explícitos** — ação descrita como verificação, aprovação, conferência ou validação:
- "o analista confere...", "o sistema valida...", "é necessária aprovação de..."

**Controles implícitos** — ação que mitiga risco mas não é descrita como controle:
- integração automática entre sistemas, campo obrigatório, bloqueio sistêmico, assinatura digital

**Ausência de controle** — etapa com risco identificado e nenhuma mitigação mencionada → registrar como lacuna, não inventar controle.

---

### 2. Expandir cada controle pelos 7 atributos

Para cada controle identificado, responder:

| Atributo | Pergunta |
|---|---|
| **Por que existe** | Qual risco esse controle mitiga? Qual a consequência se falhar? |
| **Quem executa** | Cargo, área, sistema ou processo automático? |
| **Quando ocorre** | Gatilho de início: evento, data, frequência ou condição? |
| **Como é iniciado** | O que aciona o controle: alerta sistêmico, rotina manual, demanda, fechamento? |
| **Precisão e sensibilidade** | O controle detecta qualquer desvio ou só os maiores? Qual threshold dispara ação? |
| **Interação com outros controles** | Depende de output de outro controle? Alimenta outro? |
| **Evidência gerada** | O que comprova que o controle foi executado? Onde fica armazenado? |

---

### 3. Classificar o controle

| Campo | Opções |
|---|---|
| Tipo | Preventivo / Detectivo / Corretivo |
| Natureza | Manual / Automatizado / Híbrido |
| Frequência | Sob demanda / Diário / Semanal / Mensal / Por transação |
| Cobertura | Total (todas as transações) / Amostral / Por exceção |

---

### 4. Definir o critério de falha

Descrever o que caracteriza falha de execução desse controle — não do processo, do controle em si:

- Controle não executado no período
- Executado sem evidência
- Executado por pessoa sem alçada
- Threshold não aplicado corretamente
- Evidência não armazenada ou adulterável

---

### 5. Sinalizar lacunas de informação

Se a narrativa não permite responder algum atributo com segurança, registrar explicitamente — não inventar. Listar perguntas para confirmação via walkthrough ou entrevista.

---

## Decision Rules

- Não criar controle que não está na narrativa — registrar ausência como lacuna de controle
- Não confundir etapa do processo com controle — "o analista emite a fatura" é etapa, não controle
- Controle implícito deve ser documentado como tal — indicar que precisa ser confirmado com o executor
- Se o mesmo controle mitiga múltiplos riscos, documentar uma vez e referenciar nos demais riscos
- Evidência "o sistema registra automaticamente" só é válida se o sistema foi confirmado como confiável — sinalizar se IPE não verificada
- Frequência "sob demanda" sem critério de quando acionar = controle inadequado — registrar fragilidade

---

## Output Format

### Ficha de Controle

```
Código:          [ex: FAT.01]
Risco mitigado:  [código e descrição do risco — output do wcgw-mapping]
Nome:            [nome curto do controle]

POR QUE EXISTE
[Risco mitigado e consequência se o controle falhar]

QUEM EXECUTA
[Cargo / área / sistema]

QUANDO OCORRE
[Gatilho: evento, data, frequência ou condição]

COMO É INICIADO
[O que aciona o controle]

O QUE É FEITO
[Descrição passo a passo da execução — específica o suficiente para um auditor reproduzir mentalmente]

THRESHOLD / CRITÉRIO DE REVISÃO
[O que o executor verifica, qual o parâmetro de aprovação ou rejeição]

EVIDÊNCIA GERADA
[Documento, registro sistêmico, e-mail, log — onde fica, por quanto tempo]

TIPO:       Preventivo / Detectivo / Corretivo
NATUREZA:   Manual / Automatizado / Híbrido
FREQUÊNCIA: [frequência]
COBERTURA:  Total / Amostral / Por exceção

CRITÉRIO DE FALHA
[O que caracteriza falha de execução deste controle]

LACUNAS DE INFORMAÇÃO
[Atributos não confirmados na narrativa — perguntas para walkthrough]
```

### Matriz de Controles (quando múltiplos controles)

| Cód. | Risco | Nome do Controle | Tipo | Natureza | Frequência | Executor | Evidência | Lacunas |
|---|---|---|---|---|---|---|---|---|

---

## Relação com outras skills

- **Input de:** `wcgw-mapping.md` — lista de riscos e lacunas de controle identificados
- **Output para:** `control-evaluation.md` — ficha completa como entrada para pontuação dos 9 atributos
- **Consultar:** `_method-wiki/checklists/control-attribute-design.md` — referência de atributos testáveis
