# Objetivos de Controle × Asserções — Referência por Processo

> Fonte primária: referencial metodológico consolidado.
> Aplicação: risk-control-mapping, walkthrough-standardization, finding-drafting, test-execution.

---

## Como Usar

Este arquivo mapeia objetivos de controle típicos às asserções das demonstrações financeiras que cada um endereça. Use para:

1. **Verificar completude do RCM** — todos os objetivos e asserções relevantes estão cobertos por algum controle?
2. **Redigir achados** — identificar qual asserção está em risco quando um controle falha
3. **Planejar testes** — confirmar que o teste endereça a asserção certa (ex: teste de existência ≠ teste de completude)
4. **Walkthrough** — garantir que a cobertura de asserções está documentada explicitamente

---

## Asserções Utilizadas (PCAOB)

| Asserção | O que verifica |
|---|---|
| **Completeness** | Todas as transações e eventos que deveriam ser registrados foram registrados |
| **Occurrence / Existence** | Transações e eventos registrados realmente ocorreram e pertencem à entidade |
| **Valuation** | Transações, eventos e saldos estão registrados pelo valor correto (inclui cutoff) |
| **Rights and Obligations** | A entidade detém ou controla os direitos relativos aos ativos; os passivos são obrigações reais |
| **Presentation and Disclosure** | Itens estão classificados, descritos e divulgados adequadamente |
| **All** | Controle relevante para todas as asserções acima (tipicamente SoD e acesso a dados) |

---

## OTC — Receita, Vendas e Contas a Receber

| Objetivo de Controle | Asserções |
|---|---|
| Funções com potencial conflito (aprovação de cliente, vendas, recebimentos de caixa) são segregadas | All |
| Preços usados nas vendas registradas são corretos | Valuation |
| Apenas pedidos de vendas válidos são atendidos | Occurrence |
| Todos os pedidos válidos são processados, registrados e atendidos | Completeness |
| Informações relevantes são capturadas e reportadas com precisão e pontualidade | Occurrence, Valuation |
| Uma nota fiscal é gerada para cada remessa ou ordem de serviço concluída | Completeness |
| Notas fiscais são registradas no período correto | Valuation (cutoff) |
| A provisão para devedores duvidosos é estimada adequadamente | Valuation |
| Mercadorias corretas são expedidas e registradas com precisão | Valuation |
| Entregas são registradas no período correto | Valuation (cutoff) |
| Estoque registrado pertence à empresa | Rights and Obligations |
| Recebimentos de caixa são registrados com precisão | Completeness, Existence, Valuation |
| A empresa detém os direitos sobre caixa e contas a receber registrados | Rights and Obligations |
| Créditos emitidos são autorizados e registrados corretamente | Occurrence, Valuation |
| Créditos (a contas a receber) são calculados com precisão | Valuation |
| Todas as notas de crédito e ajustes em contas a receber são registrados | Completeness |
| Controles físicos sobre caixa limitam o risco de desvio | Occurrence, Rights and Obligations |
| Lançamentos no razão geral são tempestivos e precisos; divulgação adequada | Completeness, Valuation, Disclosure |
| Acesso a arquivos de dados restrito a pessoal autorizado | All |
| Mudanças aprovadas em arquivos de dados são registradas com precisão e tempestividade | All |

---

## P2P — Compras e Pagamentos

| Objetivo de Controle | Asserções |
|---|---|
| Funções com potencial conflito (aprovação de fornecedor, compras, processamento de pagamento) são segregadas | All |
| Ordens de compra e requisições de serviço são autorizadas, completas, tempestivas e precisas | Occurrence, Valuation |
| Todos os bens e serviços recebidos foram encomendados e foram processados e registrados com precisão | Occurrence, Valuation |
| Devoluções e abatimentos são autorizados, processados e registrados com precisão | Occurrence, Valuation |
| Todas as notas fiscais são processadas com rapidez e precisão; duplicatas são prevenidas | Occurrence, Valuation, Existence |
| Pagamentos foram autorizados, os bens/serviços foram recebidos e registrados no período correto; moedas estrangeiras registradas corretamente; pagamentos duplicados prevenidos; pagamentos em aberto investigados | Rights and Obligations, Valuation, Completeness |
| TEDs autorizadas previamente quanto a valor e beneficiário e controladas | Valuation, Existence, Completeness |
| Controles físicos sobre caixa e cheques limitam o risco de desvio | Completeness, Valuation, Rights and Obligations |
| Lançamentos no razão geral são tempestivos e precisos | Valuation, Presentation/Disclosure |
| Acesso a arquivos de dados restrito a pessoal autorizado | All |
| Mudanças aprovadas em arquivos de dados são registradas com precisão e tempestividade | All |

---

## INV — Estoque

| Objetivo de Controle | Asserções |
|---|---|
| Compras, registro de estoque e contagem/acesso físico são segregados | All |
| Transferências entre locais ou categorias contábeis são autorizadas, precisas e completas; apenas remessas autorizadas são realizadas | Valuation, Completeness, Existence |
| Contagens físicas periódicas garantem precisão e completude | Completeness, Valuation |
| Registros completos e precisos de custos de produto (materiais, mão-de-obra, overhead em cada fase RM/WIP/FG) | Allocation (Valuation) |
| Cutoff adequado para todos os bens que entram ou saem do sistema no final do período | Completeness, Existence |
| Métodos de custeio e alocação (PEPS, UEPS, custo médio) em conformidade com normas e aplicados consistentemente | Allocation (Valuation) |
| Custos-padrão são atualizados e mantidos | Allocation (Valuation) |
| Mudanças em custos-padrão são aprovadas antes de implementadas; base documentada | Allocation (Valuation) |
| Variações de custo-padrão e encargos de overhead atualizados e aplicados ao estoque e CPV conforme normas | Allocation |
| Avaliações de obsolescência realizadas; write-downs tempestivos e autorizados | Valuation |
| Estoque protegido de perda por furto, uso indevido ou dano físico | Existence, Completeness |
| Lançamentos no razão geral são tempestivos e precisos | Valuation, Completeness |
| Acesso a arquivos de dados restrito; mudanças aprovadas registradas com precisão | All |

---

## H2R — Folha de Pagamento e Benefícios

| Objetivo de Controle | Asserções |
|---|---|
| Contratação (RH) e processamento da folha são segregados; aprovação de relatórios de tempo segregada das demais funções de folha | All |
| Folha é autorizada apenas conforme registros de tempo ou acordos contratuais | Occurrence, Valuation |
| Folha é completa e precisa (incluindo para a pessoa correta) no período correto, com deduções de benefícios corretas | Completeness, Valuation |
| Dados de benefícios e deduções de folha são processados com precisão para os registros de cada funcionário conforme os planos | Valuation |
| Cheques ausentes, duplicados ou em aberto há muito tempo são investigados | Completeness, Valuation |
| Cheques, carimbos de assinatura e afins são protegidos de uso não autorizado | All |
| Lançamentos no razão geral são tempestivos e precisos | Valuation |
| Acesso a arquivos de dados (incluindo tabelas de retenção) restrito; mudanças aprovadas registradas com precisão | All |
| Dados pessoais protegidos de divulgação | All |

---

## FA — Ativo Imobilizado

| Objetivo de Controle | Asserções |
|---|---|
| Manutenção de registros e disposição/supervisão física de ativos são segregados | All |
| Investimentos de capital são aprovados e documentados antes da aquisição | Occurrence, Valuation |
| Todos os ativos imobilizados estão registrados; novos ativos registrados com precisão e tempestividade | Completeness, Rights and Obligations, Valuation |
| Ativos são capitalizados ou lançados a despesa conforme normas e política da empresa | Valuation |
| Ativos registrados são de propriedade da entidade | Rights and Obligations |
| Métodos de depreciação (contábil e fiscal) em conformidade com normas e aplicados com precisão | Valuation |
| Proteção de ativos relevantes contra perda por furto, uso indevido, falta de manutenção ou dano físico | Completeness, Valuation |
| Ativos imobilizados (incluindo ativos ociosos) são revisados periodicamente para impairment | Valuation |
| Juros, custos, folha e overhead de ativos construídos internamente contabilizados conforme normas e acumulados tempestivamente | Valuation, Completeness |
| Baixas são pré-aprovadas e registradas conforme normas em tempo hábil | Existence, Disclosure |
| Lançamentos no razão geral são tempestivos e precisos | Valuation |
| Acesso a arquivos de dados restrito; mudanças aprovadas registradas com precisão | All |

---

## Goodwill e Intangíveis

| Objetivo de Controle | Asserções |
|---|---|
| Responsáveis por contabilidade e controles físicos não têm funções incompatíveis | All |
| Valores contábeis de goodwill e outros intangíveis permanecem válidos; impairment considerado | Valuation |
| Amortização de intangíveis registrada no período correto | Valuation |
| Acesso a arquivos de dados restrito; mudanças aprovadas registradas com precisão | All |

---

## TAX — Accrual e Compliance Tributário

| Objetivo de Controle | Asserções |
|---|---|
| Todas as transações e eventos relevantes registrados de forma completa, precisa e tempestiva; questões tributárias identificadas e resolvidas tempestivamente | All |
| Processos, preparação e entrega de documentos tributários realizados com precisão e pontualidade; pagamentos efetuados no prazo (incluindo ICMS/ISS coletados) | All |
| Impostos diferidos refletidos corretamente (FASB ASC 740), incluindo realização de ativos fiscais diferidos e posições tributárias; suporte adequado nos cálculos | Valuation, Disclosure |
| Posições tributárias reconhecidas atendem critérios normativos | Valuation |
| Recuperabilidade de ativos fiscais diferidos revisada; evidências corroborativas obtidas | Valuation |
| Estratégias e posições tributárias consistentes com objetivos da entidade | Valuation |
| Lançamentos no razão geral são tempestivos e precisos | Valuation |
| Gestão/governança cientes de questões e riscos tributários significativos; divulgação adequada | Presentation and Disclosure |
| Acesso a arquivos de dados ou planilhas restrito; mudanças aprovadas registradas com precisão | All |

---

## Compromissos e Contingências

| Objetivo de Controle | Asserções |
|---|---|
| Responsáveis não têm funções incompatíveis | All |
| Obrigações contratuais são autorizadas e divulgadas conforme exigido | Completeness, Disclosure |
| Compromissos e contingências são estimados e identificados tempestivamente | Completeness, Valuation |
| Litígios pendentes são identificados, estimados e divulgados tempestivamente | Completeness, Valuation, Disclosure |
| Ações regulatórias ou exposições são avaliadas quanto a consequências contábeis e estimadas/divulgadas conforme normas | Valuation, Disclosure |
| Recalls de produtos são autorizados, estimados, comunicados e registrados tempestivamente | Completeness, Accuracy, Disclosure |
| Instrumentos financeiros derivativos identificados, categorizados, classificados e contabilizados com precisão; políticas cobrem autorização e práticas permitidas | All |
| Sistemas de informação adequados para manutenção dos registros necessários para contabilização de derivativos | Valuation |
| Acesso a arquivos de dados restrito; mudanças aprovadas registradas com precisão | All |

---

## Patrimônio Líquido

| Objetivo de Controle | Asserções |
|---|---|
| Responsáveis não têm funções incompatíveis | All |
| Apenas mudanças autorizadas no número de ações em circulação ou participações são registradas, com precisão e no período correto | Existence, Rights and Obligations, Valuation |
| Recompra de ações ou distribuições são autorizadas e registradas com precisão no período correto | Completeness, Valuation |
| Opções concedidas conforme plano aprovado pelo board; controles previnem backdating ou spring-loading | Completeness, Occurrence, Valuation |
| Valorações de opções realizadas para registro da remuneração; exercícios, extinções, modificações e cancelamentos registrados de forma completa, precisa e nos períodos corretos | Completeness, Existence, Valuation, Disclosure |
| Dividendos ou distribuições são autorizados e registrados com precisão no período correto | Valuation |
| Lançamentos no razão geral são tempestivos e precisos | Valuation |
| Acesso a arquivos de dados restrito; mudanças aprovadas registradas com precisão | All |

---

## TRE — Investimentos e Tesouraria

| Objetivo de Controle | Asserções |
|---|---|
| Gestão de caixa, investimentos e dívida são segregados | All |
| Execução de transações de caixa limitada a indivíduos autorizados | Occurrence, Rights and Obligations |
| Apenas transações de investimento válidas e autorizadas registradas de forma completa, precisa e no período correto; com contraparte aprovada | All |
| Informações suficientes para classificação de títulos (mantidos até vencimento, disponíveis para venda, negociação) e mensuração a fair value | Valuation, Disclosure |
| Valoração tempestiva de títulos; método conforme normas; relatório SOC 1 da organização de serviço examinado quando aplicável | Valuation |
| Negociações em aberto há muito tempo ou incomuns (valor, contraparte, natureza) identificadas e revisadas | Existence, Valuation |
| Controles físicos sobre investimentos mantidos para reduzir risco de furto | Completeness, Existence |
| Contas bancárias: abertura/encerramento autorizado; conciliadas periodicamente; atividade monitorada | Completeness, Valuation |
| Caixa denominado na moeda correta | Valuation, Disclosure |
| Compliance com covenants de empréstimos monitorado | Rights and Obligations, Disclosure |
| TEDs: autorizadas previamente quanto a valor, beneficiário e timing | Existence, Completeness, Valuation |
| Derivativos em contratos de dívida identificados; contabilizados conforme normas | Completeness, Accuracy |
| Dívida com terceiros e juros: completa, autorizada, precisa e no período correto; estrutura híbrida classificada e divulgada adequadamente | All |
| Empréstimos intercompany e juros: completos, autorizados, precisos e no período correto; eliminações para consolidação | Completeness, Existence, Valuation |
| Fair value aplicado a dívidas relevantes conforme normas | Valuation |
| Arranjos off-balance sheet identificados e contabilizados conforme normas | Completeness, Existence, Valuation |
| Controles físicos sobre caixa e títulos negociáveis mantidos | Completeness, Existence |
| Lançamentos no razão geral tempestivos e precisos | Valuation |
| Acesso a arquivos de dados restrito; mudanças aprovadas registradas com precisão | All |

---

## RTR — Processo de Fechamento e Consolidação (Period End)

| Objetivo de Controle | Asserções |
|---|---|
| Transações com partes relacionadas: todas identificadas; valores, entidades e timing corretos; tratamento GAAP e divulgação examinados | All |
| Fair value de ativos e passivos relevantes: todos os processos identificados; laudos de qualidade obtidos tempestivamente (Instrumentos Financeiros, Investimentos, Imobilizado, Goodwill, Provisões) | Completeness, Valuation |
| Todas as provisões e ajustes preparados com precisão | Completeness, Valuation |
| Todas as entidades consolidadas ou pickup por equivalência patrimonial; eliminações realizadas; tradução conforme normas | Completeness, Valuation |
| Despesa e accrual tributário revisados para precisão e completude; posições tributárias identificadas | Valuation, Disclosure |
| Acesso a arquivos de dados relacionados restrito; mudanças aprovadas registradas com precisão | All |

---

## Empréstimos (Instituições Financeiras)

| Objetivo de Controle | Asserções |
|---|---|
| Setup, processamento, cobranças e contabilização de empréstimos são segregados | All |
| Todos os empréstimos processados conforme políticas e regulação | Rights and Obligations, Completeness, Valuation |
| Apenas solicitações de empréstimo completas, válidas e precisas são aceitas | Completeness, Existence, Valuation |
| Todos os empréstimos são devidamente autorizados, processados com precisão e registrados tempestivamente | Valuation |
| Pagamentos de empréstimos autorizados são registrados de forma completa, precisa e tempestiva | Valuation, Completeness |
| Vendas de empréstimos são autorizadas; empréstimos destinados à venda classificados corretamente; registradas com precisão e tempestividade | Occurrence, Rights and Obligations, Valuation |
| Todos os recebimentos/pagamentos de serviços depositados e registrados de forma completa, precisa e tempestiva | Completeness, Valuation |
| Contas inadimplentes monitoradas; provisões estabelecidas | Valuation |
| Reembolsos de empréstimos são precisos e devidamente registrados | Completeness, Existence, Valuation |
| Provisões para perdas com empréstimos e baixas são precisas | Valuation |
| Aquisições e vendas de ativos retomados são autorizadas e devidamente registradas | Occurrence, Existence, Valuation |
| Controles físicos adequados sobre arquivos de empréstimos e garantias | All |
| Lançamentos no razão geral tempestivos e precisos | Valuation |
| Acesso a arquivos de dados (ex: cadastro de empréstimos e cálculos de juros) restrito; mudanças aprovadas registradas com precisão | All |

---

## Ciclo Genérico (Aplicável a Qualquer Processo)

| Objetivo de Controle | Asserções |
|---|---|
| Responsáveis por contabilidade e controles físicos não têm funções incompatíveis | All |
| Transações são autorizadas e registradas de forma completa, precisa e tempestiva | Completeness, Existence, Valuation |
| Proteção de ativos ou informações relevantes contra perda por furto, uso indevido ou dano físico | All |
| Lançamentos no razão geral são tempestivos e precisos | Valuation |
| Acesso a arquivos de dados restrito a pessoal autorizado | All |
| Mudanças aprovadas em arquivos de dados são registradas com precisão e tempestividade | All |

---

## Notas de Uso

- **SoD cobre "All"** — controles de segregação de funções são relevantes para todas as asserções pois sua ausência pode comprometer qualquer uma delas
- **"All" em acesso a dados** — controles de acesso a sistemas cobrem todas as asserções pelos mesmos motivos: usuário não autorizado pode comprometer qualquer aspecto do registro
- **Cutoff é subconjunto de Valuation** — erro de competência resulta em saldo incorreto; tratar como Valuation com nota de cutoff
- **Disclosure** — além das asserções de transação, checar se controles garantem que informação chega completa e correta às notas explicativas

---

## Conexões Internas

- `context/controls-master.json` — 598 controles típicos com `process_code`; complementar com as asserções deste mapeamento
- `workflows/risk-control-mapping.md` — usa este mapeamento para garantir cobertura completa de asserções no RCM
- `workflows/finding-drafting.md` — identificar a asserção afetada no campo "Critério" do achado
- `context/standards/sox.md` — asserções PCAOB usadas quando o caso migrar para a trilha externa / SOX 404
- `_method-wiki-external-audit/workflows/risk-control-mapping-external-audit.md` — usar este mapeamento como base principal em ICFR / SOX
- `_method-wiki/concepts/scoping-strategy.md` — asserções orientam quais riscos de overstatement vs. understatement mapear no scoping
