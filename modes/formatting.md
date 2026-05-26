# mode: formatting

## Papel

Guia curto de estilo e padronização de saída para os artefatos do `internal-audit-ops`. Não é workflow ativo; é referência de acabamento para workflows, skills e templates.

## Quando Consultar

- ao finalizar qualquer artefato antes de entregar ao cliente
- ao redigir política, norma ou procedimento corporativo
- ao escolher entre narrativa, tabela, lista ou fluxograma
- ao citar norma técnica, lei ou framework
- ao revisar linguagem de achado, walkthrough ou relatório

---

## 1. Linguagem e Tom

### Padrão geral

- PT-BR com acentuação correta em todo texto de saída
- Grafia sem acento reservada para: IDs, chaves técnicas, paths, nomes de arquivo (`wcgw-master.json`, `P2P-001`)
- Tom formal e impessoal — sem "você", "a gente", "nós"; preferir "a empresa", "o auditor", "a área responsável"
- Voz ativa preferida: "o gestor aprova" > "a aprovação é realizada pelo gestor"
- Frases curtas — máximo 3 cláusulas por sentença em documentos formais
- Em auditoria interna, não usar `SCOT` como formato padrão de walkthrough; isso pertence à trilha externa

### O que evitar

| Evitar | Preferir |
|---|---|
| finding | achado |
| control | controle |
| walkthrough (em texto corrido) | narrativa de processo / relato de walkthrough |
| issue | problema / observação |
| gap | lacuna |
| owner | responsável / gestor responsável |
| deadline | prazo |
| compliance | conformidade (exceto quando nome próprio de área) |
| statement | asserção (quando contábil) / declaração |
| best practice | melhor prática |

### Intensidade técnica por destinatário

| Destinatário | Tom | Jargão técnico |
|---|---|---|
| Papel de trabalho / WP interno | Técnico, conciso | Livre — WCGW, ToD/ToE, RI/RR |
| Relatório para gestão operacional | Semiformal | Moderado — explicar siglas na primeira ocorrência |
| Relatório para conselho / comitê | Formal, executivo | Mínimo — foco em impacto e ação |
| Política corporativa | Formal, normativo | Definir termos na seção de Definições |
| Norma interna / procedimento | Técnico-normativo | Específico ao domínio |

---

## 2. Estrutura de Documentos

- Numerar seções em documentos formais (políticas, normas, relatórios)
- Não numerar em papéis de trabalho e templates de uso interno
- Máximo 3 níveis de hierarquia na maioria dos documentos

### Tamanho de parágrafo

| Tipo de documento | Parágrafo ideal |
|---|---|
| Política / norma | 3–6 linhas por parágrafo |
| Relatório de auditoria | 4–8 linhas por achado narrativo |
| Walkthrough narrativo | 4–8 linhas por bloco lógico do processo |
| E-mail / comunicação | 2–4 linhas |

---

## 3. Tabela vs. Lista vs. Narrativa

| Situação | Formato preferido |
|---|---|
| Múltiplos itens com atributos comparáveis | Tabela |
| Sequência de etapas com dependência | Lista numerada |
| Itens independentes sem ordem | Lista com marcadores |
| Processo com fluxo e decisões | Mermaid ou BPMN |
| Análise de causa/consequência | Narrativa |
| Achado formal | Template 5Cs (`templates/output-achado-5c.md`) |
| Responsabilidades por papel | Tabela papel/responsabilidade |
| Definições | Tabela termo/definição |

---

## 4. Citação de Normas e Frameworks

### Padrão de citação

| Tipo | Formato |
|---|---|
| Lei federal | Lei nº 13.709/2018 (LGPD), Art. 46 |
| CPC | CPC 47 — Receita de Contrato com Cliente, item 31 |
| IFRS | IFRS 15 — Revenue from Contracts with Customers, par. 31 |
| NBC TA | NBC TA 315 (R2) — Identificação e Avaliação dos Riscos |
| COSO | COSO ERM 2017 — Componente X, Princípio Y |
| SOX | SOX Section 302 / Section 404 |
| ISO | ISO/IEC 27001:2022 — Controle A.8.2 |
| Política interna | POL-UAM-001 — Política de Gestão de Acessos, seção 4.2 |
| Contrato | Contrato nº [X], Cláusula Y |

### Primeira ocorrência

Escrever nome completo + sigla entre parênteses: "Lei Geral de Proteção de Dados (LGPD)". Usar apenas a sigla nas ocorrências seguintes.

---

## 5. Números, Datas e Valores

| Elemento | Formato |
|---|---|
| Data | DD/MM/AAAA em texto corrido; AAAA-MM-DD em campos de sistema/JSON |
| Valor monetário | R$ 1.250.000,00 (ponto como separador de milhar, vírgula como decimal) |
| Percentual | 12,5% (vírgula decimal, sem espaço antes do %) |
| Quantidade | Por extenso até dez; numeral a partir de 11 |
| Amostra | n=25 / universo=312 (não "vinte e cinco de trezentos e doze") |

## 6. Políticas Corporativas — Estrutura Padrão

Todo documento gerado via `scripts/export_politica_docx.py` deve seguir esta estrutura mínima:

| # | Seção | Obrigatório | Observação |
|---|---|---|---|
| — | Capa (metadados) | Sim | Título, código, versão, data, aprovador |
| — | Histórico de revisões | Sim | Mínimo 1 entrada |
| 1 | Objetivo | Sim | O que a política regula e por quê existe |
| 2 | Escopo | Sim | Aplicável a quem; o que está excluído |
| 3 | Definições | Sim | Termos técnicos usados no documento |
| 4 | Diretrizes | Sim | Regras e requisitos — mínimo 1 subseção |
| 5 | Responsabilidades | Sim | Tabela papel/responsabilidade |
| 6 | Penalidades e Consequências | Recomendado | O que acontece em caso de descumprimento |
| 7 | Referências | Recomendado | Normas, leis e políticas relacionadas |
| 8 | Vigência | Sim | Data de entrada em vigor e periodicidade de revisão |
| — | Bloco de assinaturas | Sim | Elaborado por / Revisado por / Aprovado por |

Verificar conformidade antes de exportar: `python3 scripts/policy_register.py checar <arquivo.json>`

## 7. Normas Internas — Estrutura Padrão

Distinto de política (que define o quê e por quê), norma define **como** — procedimento operacional, instrução de trabalho ou padrão técnico.

| # | Seção | Observação |
|---|---|---|
| 1 | Objetivo | O que esta norma padroniza |
| 2 | Aplicação | Quando e por quem é usada |
| 3 | Definições | Termos específicos do domínio |
| 4 | Procedimento | Passo a passo numerado; responsável por etapa; sistema utilizado |
| 5 | Exceções | Situações que fogem ao fluxo padrão e como tratá-las |
| 6 | Controles | Pontos de verificação e evidências esperadas |
| 7 | Referências | Política-mãe, norma técnica ou regulamento base |
| 8 | Vigência e revisão | |

## 8. Escolha de Formato de Fluxograma

| Situação | Formato |
|---|---|
| Embed inline no Obsidian, documentação rápida | Mermaid — `skills/process-flow-mermaid.md` |
| Repositório formal, intercâmbio com ferramentas BPM | BPMN 2.0 — `skills/process-flow-bpmn.md` |
| Tabela estruturada para automação / RCM | Mapa de atividades / tabela estruturada do template aplicável |
| Apresentação executiva simples | Narrativa curta ou lista de etapas |

## 9. Modelos Padrão por Tipo de Documento

| Tipo | Template JSON | Script de exportação |
|---|---|---|
| Política corporativa | `templates/politica-exemplo.json` (base) | `scripts/export_politica_docx.py` |
| Achado de auditoria (5Cs) | `templates/achado-exemplo.json` | `scripts/export_achado_docx.py` |
| Walkthrough de processo | `templates/output-walkthrough.md` | — (Markdown direto) |
| Input de trabalho | `templates/input-trabalho.md` | — (Markdown direto) |

## Artefatos Relacionados

- `templates/output-walkthrough.md` — estrutura de saída de walkthrough
- `templates/output-achado-5c.md` — estrutura de achado formal
- `templates/politica-exemplo.json` — schema de política completo
- `scripts/export_politica_docx.py` — geração de política em .docx
- `scripts/export_achado_docx.py` — geração de achado em .docx
- `scripts/policy_register.py checar` — checklist de conformidade de política
- `_method-wiki/checklists/audit-artifacts-definition-of-done.md` — DoD por artefato
