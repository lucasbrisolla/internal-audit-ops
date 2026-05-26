---
name: context-audit
description: Use quando o agente devolve respostas genéricas, antes de construir novos modos ou workflows, quando o repositório cresceu mas a qualidade de output não acompanhou, ou quando é preciso saber exatamente o que coletar para o agente operar bem em um trabalho específico.
---

# Context Audit

## Objetivo

Mapear lacunas entre o que o repositório contém e o que o agente precisa para operar com qualidade real — devolvendo uma lista estruturada de gaps por impacto, com a pergunta concreta que precisa ser respondida para fechar cada um.

Output genérico não é problema de prompt. É problema de contexto insuficiente.

## Quando Usar

- Antes de construir novo modo, workflow ou skill
- Quando o agente devolve respostas vagas ou baseadas em inferência em vez de dados do cliente ou processo real
- Quando o repositório cresceu mas a qualidade de output não melhorou
- Quando um humano precisa saber exatamente o que trazer para a próxima sessão de trabalho
- Antes de um engagement novo: verificar o que está completo e o que está ausente no contexto do cliente

## Quando NÃO Usar

- Para verificar se arquivos existem (isso é responsabilidade do `CLAUDE.md` no onboarding)
- Para responder dúvida técnica de auditoria (usar `workflows/audit-technical-review.md`)
- Para avaliar qualidade de um artefato já gerado (usar `skills/challenge-reasoning.md`)

---

## Workflow

### 1. Inventariar o que existe

Ler os diretórios do produto e classificar o nível de preenchimento:

```
context/              → bases de conhecimento (wcgw-master.json, standards, clients/)
modes/                → modos de operação macro (business-understanding, risk-assessment...)
workflows/            → fluxos de execução (audit-planning, risk-control-mapping...)
skills/               → capacidades auxiliares (wcgw-mapping, control-evaluation...)
templates/            → formatos de input/output
_method-wiki/         → base metodológica (processos, padrões, checklists, conceitos)
```

Para cada arquivo relevante, classificar:
- `completo` — conteúdo suficiente para operar sem inventar
- `rascunho` — existe mas incompleto, desatualizado ou sem exemplos calibradores
- `ausente` — referenciado mas não existe; ou nem referenciado mas necessário

### 2. Mapear gaps por área operacional

Para cada modo ou workflow principal, verificar se o contexto de suporte existe:

| Pergunta | Se não → gap |
|---|---|
| O modo tem exemplos reais ou calibradores? | `examples/` ausente ou vazio para este workflow |
| O agente sabe quem são os atores e sistemas do processo do cliente? | `context/clients/<cliente>/` incompleto |
| O modo tem base de referência carregável (WCGWs, controles, testes)? | JSON de contexto ausente ou desatualizado |
| O modo sabe o que fazer quando faltam informações do cliente? | Guardrails de incompletude ausentes |
| O modo tem critério claro para classificar severidade? | Escalas e critérios não documentados |
| O modo tem templates de output padronizados? | Templates ausentes ou sem exemplos preenchidos |

### 3. Classificar cada gap por impacto

- `bloqueante` — o modo não consegue operar sem isso; output será inferência ou invenção
- `complementar` — opera, mas com qualidade reduzida, genérica ou sem calibração real
- `opcional` — melhoria marginal; não priorizar agora

### 4. Para cada gap bloqueante ou complementar, gerar entrada estruturada

```
**Gap:** [nome do gap]
**Modo/Workflow afetado:** [qual operação sofre mais]
**Por que importa:** [o que o agente inventa ou erra sem essa informação]
**Pergunta concreta:** [o que exatamente precisa ser respondido ou fornecido]
**Quem pode responder:** [humano, documento, sistema, observação em campo]
```

### 5. Ordenar e entregar

Devolver lista ordenada: bloqueantes primeiro, complementares depois, opcionais por último.

Encerrar com:
- Quantos gaps bloqueantes foram encontrados
- O que trazer na próxima sessão para fechar os mais críticos
- Quais modos ou workflows já podem operar bem com o contexto atual

---

## Output Obrigatório

- Inventário resumido por diretório (completo / rascunho / ausente)
- Lista de gaps ordenada por impacto
- Para cada gap bloqueante ou complementar: nome, modo afetado, por que importa, pergunta concreta, quem responde
- Recomendação de prioridade de coleta

---

## Regras

- Não simular contexto ausente. Se o dado não existe no repositório, marcar como gap — não inferir.
- Distinguir arquivo existente de arquivo preenchido. Presença não é suficiência.
- Não recomendar construir novos modos antes de fechar os gaps bloqueantes dos modos prioritários.
- Gaps sobre o processo real do cliente (como funciona na prática, quem aprova, qual sistema) são mais bloqueantes que gaps de conhecimento técnico teórico.
- Quando o gap puder ser fechado com uma única pergunta objetiva, formular essa pergunta diretamente.
- Não confundir `context/wcgw-master.json` vazio com ausência de WCGWs — verificar se o JSON foi gerado a partir dos MDs em `context/wcgw/`.
