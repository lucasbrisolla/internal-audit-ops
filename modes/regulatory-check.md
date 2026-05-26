# mode: regulatory-check

## Papel

Varredura sistemática de conformidade de uma entidade ou processo contra um framework normativo específico. Diferente de `workflows/audit-technical-review.md`, que responde dúvidas técnicas pontuais — este modo mapeia **todos os requisitos** do framework e verifica a existência de controles/evidências para cada um, produzindo um gap report estruturado.

Usado quando o objetivo é responder: "a empresa atende aos requisitos de X?" — não "o que X exige sobre Y?".

## Quando Usar

- avaliação de conformidade com SOX 404, LGPD, ISO 27001, IIA IPPF, regulação setorial
- preparação para certificação ou avaliação externa
- diagnóstico antes de engajamento de auditoria com foco em compliance
- atualização de conformidade após nova versão de norma ou nova obrigação legal
- due diligence de controles em M&A

## Inputs

- framework ou regulação alvo (ex: SOX 404, LGPD, ISO 27001, COSO 2013, IIA GIAS 2024)
- escopo: qual entidade, área ou processo será avaliado
- evidências disponíveis: políticas, procedimentos, relatórios, controles documentados
- resultado de auditorias ou avaliações anteriores sobre o mesmo framework, se houver

## Sequência de Verificação

### 1. Mapear os requisitos do framework

Antes de verificar qualquer coisa, listar o que o framework exige:

- Decompor o framework em requisitos verificáveis (cada requisito = uma linha na tabela)
- Usar como referência os arquivos de standards em `context/standards/`:
  - SOX/COSO: `sox.md` — 17 Princípios COSO + seções 302/404
  - IIA IPPF 2024: `iia-ippf.md` — 5 domínios, padrões numerados
  - IFRS: `ifrs.md` — por processo (IFRS 15, 16, IAS 36, 37)
- Para frameworks não cobertos em `context/standards/`, listar requisitos a partir do documento normativo fornecido

Estrutura mínima por requisito:

| ID | Requisito | Artigo/Seção | Obrigatório? |
|---|---|---|---|

### 2. Para cada requisito, verificar cobertura

Classificar em 4 categorias:

| Status | Critério |
|---|---|
| **Conforme** | Existe política/controle documentado, evidência de execução disponível, sem gaps conhecidos |
| **Parcial** | Controle existe mas com gaps: frequência inadequada, cobertura incompleta, evidência fraca |
| **Lacuna** | Requisito identificado mas sem controle ou política mapeada |
| **N/A** | Requisito não aplicável ao escopo avaliado — justificar |

Para cada item, registrar:
- Evidência verificada (documento, política, sistema)
- Responsável pelo controle
- Data da última verificação ou teste
- Observação sobre gap ou limitação

### 3. Priorizar lacunas

Não todas as lacunas têm o mesmo peso:

**Critérios de priorização:**

| Fator | Alto | Médio | Baixo |
|---|---|---|---|
| Impacto regulatório | Penalidade direta, notificação obrigatória, perda de licença | Achado em auditoria externa, nota explicativa | Recomendação sem penalidade |
| Exposição a fraude | Controle anti-fraude ausente | Controle compensatório existente | Risco remoto |
| Materialidade financeira | Exposição acima do threshold material | Moderada | Imaterial |
| Reincidência | Já identificado em ciclo anterior sem correção | Novo mas com histórico similar | Primeira ocorrência |

Lacunas com impacto regulatório alto + reincidência = reportar imediatamente, não aguardar ciclo de auditoria.

### 4. Montar o gap report

Estrutura padrão:

**Seção 1 — Sumário executivo**
- Framework avaliado, escopo, data
- Distribuição por status: X conformes, Y parciais, Z lacunas, W N/A
- Top 3–5 lacunas prioritárias com risco associado

**Seção 2 — Tabela de conformidade completa**

| ID | Requisito | Status | Evidência | Responsável | Gap / Observação | Prioridade |
|---|---|---|---|---|---|---|

**Seção 3 — Plano de ação para lacunas**

| Gap ID | Ação recomendada | Responsável sugerido | Prazo | Risco se não tratado |
|---|---|---|---|---|

**Seção 4 — Limitações do check**
- O que não foi possível verificar e por quê
- Fontes não acessadas
- Premissas adotadas

### 5. Registrar no contexto do cliente

Atualizar em `context/clients/<cliente>/compliance.md`:
- Framework avaliado
- Data da avaliação
- Status geral (percentual de conformidade)
- Lacunas críticas abertas

## Frameworks Cobertos em `context/standards/`

| Framework | Arquivo | Quando usar |
|---|---|---|
| SOX 404 / COSO 2013 | `sox.md` | ICFR, controles financeiros, companhias com exposição à SEC |
| IIA IPPF / GIAS 2024 | `iia-ippf.md` | Maturidade da função de auditoria interna |
| IFRS / CPC | `ifrs.md` | Julgamentos contábeis por processo |

Frameworks não cobertos (usar documento original):
- LGPD — Lei nº 13.709/2018
- ISO 27001:2022
- PCI-DSS
- Regulação setorial (BACEN, ANVISA, ANEEL, CVM)

## Guardrails

- Não classificar como "Conforme" sem evidência verificada — presunção de conformidade não é conformidade
- Não deixar "N/A" sem justificativa — o requisito pode ser aplicável mesmo que pareça distante do escopo
- Lacuna ≠ achado automático — verificar se há controle compensatório antes de classificar
- Não confundir ausência de documentação com ausência de controle — perguntar antes de classificar como lacuna
- Informar ao cliente imediatamente se lacuna implica obrigação de notificação regulatória (não aguardar relatório final)
- Não citar artigos ou requisitos sem verificar no documento normativo — `context/standards/` é referência calibrada, não substituto do texto original

## Output

1. **Sumário executivo** — distribuição por status e top lacunas (para comitê/diretoria)
2. **Tabela de conformidade completa** — todos os requisitos verificados
3. **Plano de ação** — para lacunas e itens parciais
4. **Limitações** — o que não foi coberto

## Artefatos Relacionados

- `context/standards/sox.md` — COSO e SOX 404
- `context/standards/iia-ippf.md` — IIA GIAS 2024
- `context/standards/ifrs.md` — IFRS por processo
- `context/clients/<cliente>/compliance.md` — registro persistente de compliance por cliente
- `workflows/audit-technical-review.md` — para dúvidas técnicas sobre requisito específico
- `workflows/finding-drafting.md` — para formalizar lacunas como achados
- `modes/formatting.md` — calibrar linguagem do gap report por destinatário
