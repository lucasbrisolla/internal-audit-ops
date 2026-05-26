# Product Index

Inventário operacional sob demanda do `internal-audit-ops`.

Use este arquivo quando a tarefa pedir fontes estruturadas, scripts, templates, standards ou referências de produto. Não carregar por padrão no início de toda interação.

Regra editorial:

- `auditoria interna` usa `workflows/`, `templates/` e `_method-wiki/` como padrão
- preferir artefatos internos explícitos em vez de adaptar mentalmente templates de outras trilhas

## Standards de Referência

Usar ao redigir achados, avaliar deficiências ou fundamentar conclusões técnicas:

| Arquivo | Quando usar |
|---|---|
| `context/standards/sox.md` | Trilha externa / ICFR / SOX: critério de deficiência, Design vs. Operating, Likelihood x Magnitude, Prudent Official Test, presumed MW, agregação, COSO 17 princípios, ITGC scoping, tamanho de amostra SOX, reporte 404(a)/(b) |
| `context/standards/iia-ippf.md` | Independência, evidência suficiente/adequada, atributos de achado, opinião geral, follow-up e escala de severidade IIA |
| `context/standards/ifrs.md` | Julgamentos contábeis por processo: IFRS 15, IFRS 16, IFRS 9, IAS 36, IAS 37 e diferenças CPC |

## Bibliotecas Estruturadas

| Fonte | Uso |
|---|---|
| `context/wcgw-master.json` | Fonte primária de WCGWs: 761 WCGWs estruturados em 19 processos. Filtrar por `process_code`. Não carregar os MDs individuais para lookup. |
| `context/controls-master.json` | Fonte primária de controles típicos: 598 controles extraídos dos mesmos 19 processos. Filtrar por `process_code`. Campos `type` e `nature` são inferidos por keyword; itens "A classificar" exigem revisão manual. |
| `context/tests-master.json` | Fonte primária de testes típicos: 15 testes por tipo de controle (`control_type_slug`), com pré-condição, steps, dependência IPE/ITGC, evidência por força e armadilha. |
| `context/sod-master.json` | Fonte primária de SoD: 35 conflitos em 6 processos (P2P, OTC, H2R, RTR, FA, UAM), com criticidade, sistemas e controle compensatório. |
| `context/red-flags-master.json` | Fonte primária de red flags: 49 indicadores em 6 processos, com métrica, limiar sugerido, fonte IPE e WCGW associado. |
| `context/wcgw/` | Fonte secundária para leitura humana e edição; um MD por processo. Após edição, regenerar o JSON. |
| `context/wcgw/criterio-editorial-wcgw.md` | Critério editorial para manutenção de WCGWs. |

## Códigos de Processo

| process_code | Processo |
|---|---|
| OTC | Order-to-Cash — do pedido ao recebimento |
| REV | Reconhecimento de receita (IFRS 15 / CPC 47) |
| P2P | Procure-to-Pay — da requisição ao pagamento |
| RTR | Record-to-Report — fechamento e reporte financeiro |
| H2R | Hire-to-Retire — folha, benefícios e RH |
| FA | Ativo imobilizado |
| INV | Estoque |
| TRE | Tesouraria e caixa |
| TAX | Tributos |
| CAPEX | Projetos de capital |
| ITGC | ITGCs |
| UAM | Gestão de acessos |
| JE | Lançamentos manuais |
| ELC | Controles de entidade |
| FRA | Avaliação de risco de fraude |
| DRI | Dados, relatórios e IPE |
| LCT | Legal, compliance e terceiros |
| SCL | Supply chain e logística |
| ESG | ESG, meio ambiente e segurança |

## Templates de Trabalho

| Template | Quando usar |
|---|---|
| `templates/input-trabalho.md` | Trilha interna: captura cliente, processo, escopo, insumos e routing |
| `templates/output-walkthrough.md` | Trilha interna: documentar processo em narrativa por objetivo do processo, mapa de atividades e Mermaid |
| `templates/output-achado-5c.md` | Trilha interna: formalizar achado em Condition, Criteria, Cause, Consequence, Corrective Action |
| `templates/template-modelo.bpmn` | Base para diagramas BPMN 2.0 com swimlanes |
| `examples/generated/` | Exemplos calibradores de saída por workflow |
| `_method-wiki/checklists/audit-artifacts-definition-of-done.md` | DoD de walkthrough, RCM, papel de teste, achado e plano de ação |

## Templates Excel de Engagement

Gerados pelos scripts abaixo. Regenerar com `python3 scripts/generate_all_templates.py`.

| Template xlsx | Script gerador | Abas principais |
|---|---|---|
| `templates/RCM_Matriz_Riscos_template.xlsx` | `scripts/generate_rcm_risco.py` | RCM - Matriz de Controle; Matriz de Avaliação de Riscos; _Heatmap |
| `templates/Papel_Teste_Controle_template.xlsx` | `scripts/generate_papel_teste.py` | Cabeçalho do Teste; Resultados por Item; _Ref_Amostragem |
| `templates/Tracker_Achados_template.xlsx` | `scripts/generate_tracker_achados.py` | Tracker de Achados; Detalhe 5Cs; _Ref_Severidade |
| `templates/Plano_Anual_Auditoria_template.xlsx` | `scripts/generate_plano_anual.py` | Universo Auditável; Plano Anual; Resumo Executivo; _Ref_Critérios |
| `templates/Followup_Plano_Acao_template.xlsx` | `scripts/generate_followup_pa.py` | Follow-up de Plano de Ação; Histórico de Verificação; Painel de Aging |
| `templates/Matriz de Avaliação de Riscos - Receita (versão final).xlsx` | — (template legado de referência) | Matriz de Risco_V2; Matriz de Controle; Atributos |

## Registro de Políticas

`context/policy-register.json` inventaria políticas corporativas com status, vigência, área proprietária, frameworks e processo de auditoria associado.

Consultas via `scripts/policy_register.py`:

| Comando | Descrição |
|---|---|
| `python3 scripts/policy_register.py status` | Resumo por status |
| `python3 scripts/policy_register.py expiradas` | Políticas expiradas ou com data passada |
| `python3 scripts/policy_register.py alerta [dias]` | Expirando em N dias, default 90 |
| `python3 scripts/policy_register.py gap <framework>` | Domínios sem cobertura para COSO, SOX, ISO27001 ou LGPD |
| `python3 scripts/policy_register.py processo <cod>` | Políticas mapeadas ao processo |
| `python3 scripts/policy_register.py validar` | Valida integridade do registro |
| `python3 scripts/policy_register.py checar <arquivo.json>` | Checklist de conformidade, com 22 verificações em 4 camadas |

## Integridade do Produto

`scripts/doctor.py` valida integridade do produto. Seções verificadas:

| Seção | O que verifica |
|---|---|
| Arquivos Essenciais | CLAUDE.md, domain.md, DATA_CONTRACT.md, states.yml, README.md |
| Skills | Existência dos skills referenciados no CLAUDE.md |
| Workflows | Existência dos workflows referenciados; órfãos não referenciados |
| Method Wiki | Existência das pastas e arquivos mínimos de `_method-wiki/` |
| Method Wiki Index | Links do `index.md` existem no disco; MDs nas pastas sem entrada no index — cobre `_method-wiki` |
| WCGW Master | 761 WCGWs: campos obrigatórios, IDs únicos, fases SCOT e severidade válidas, source_file existente |
| States | Objetos canônicos presentes em `states.yml`; estados em perfis de cliente válidos |
| Data Contract | Seções obrigatórias presentes em `DATA_CONTRACT.md` |
| Links | Links locais no README, CLAUDE.md, `index.md` e perfis de cliente |
| Consistência do CLAUDE | Workflows, skills e WCGWs referenciados existem; órfãos sinalizados como warning |
| Perfil de Exemplo | Arquivos obrigatórios em `context/clients/_example/` |
| Perfis de Clientes | index.md presente; arquivos referenciados no index existem |
| Registro de Políticas | Integridade do JSON; políticas expiradas; alerta 90 dias |

Flags disponíveis:

| Flag | Efeito |
|---|---|
| *(sem flags)* | Modo padrão — erros bloqueiam, warnings não |
| `--strict` | Warnings também bloqueiam |
| `--report` | Exibe resumo por seção ao final |
| `--include-docs` | Inclui `docs/` ou `archive/docs/` na validação de links |

Uso: `python3 scripts/doctor.py [--strict] [--report] [--include-docs]`

## Exportação para .docx

| Script | Input | Quando usar |
|---|---|---|
| `scripts/export_achado_docx.py` | `templates/achado-exemplo.json` | Exportar achado 5Cs finalizado para Word |
| `scripts/export_politica_docx.py` | `templates/politica-exemplo.json` | Gerar política corporativa em Word |

Uso: `python3 scripts/export_achado_docx.py meu-achado.json [saida.docx]`
