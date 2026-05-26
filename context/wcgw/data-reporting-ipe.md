---
processo: data-reporting-ipe
nivel: 1
abreviacao: DRI
subprocessos:
  - fontes-de-dados-e-data-lineage
  - relatorios-ipe-e-extrações
  - dashboards-bi-e-metricas
  - reconciliacao-e-completude-de-dados
  - qualidade-transformacao-e-master-data
  - acesso-governanca-e-change-de-reportes
  - modelos-planilhas-e-calculos-manuais
  - retencao-e-evidencia-de-reporting
assercoes_primarias:
  - existência
  - completude
  - valoração
  - corte
  - apresentação
frameworks:
  - COSO
  - data governance
  - IPE reliability
  - SOX
referencias:
  - _method-wiki/processes/ipe-reliability-assessment.md
  - _method-wiki/patterns/evidence-conclusion-linkage.md
  - context/wcgw/it-general-controls.md
  - context/wcgw/user-access-management.md
  - context/wcgw/record-to-report.md
---

# WCGW — Data, Reporting, BI & IPE (DRI)

Data & Reporting cobre a confiabilidade dos dados, relatórios, dashboards, extrações, planilhas e IPEs usados para tomar decisão, executar controles ou suportar auditoria. O risco central é confiar em um número bonito sem saber de onde ele veio, como foi transformado, quem pode alterá-lo e se ele reconcilia com a fonte de verdade.

Para auditoria interna, essa família é transversal: qualquer teste que dependa de relatório, base extraída, dashboard ou planilha precisa avaliar completude, acurácia, corte, governança e rastreabilidade da informação.

---

## Subprocesso 1: Fontes de Dados e Data Lineage

Etapa de identificar sistema fonte, owner, transformações, dependências e caminho do dado até o relatório ou dashboard.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| DRI-001 | Relatório crítico usado sem identificar sistema fonte e owner do dado | Initiation | Existência | Alta |
| DRI-002 | Data lineage inexistente — transformações entre fonte e reporte não são rastreáveis | Processing | Completude | Alta |
| DRI-003 | Dashboard combina fontes com granularidade ou período incompatíveis | Processing | Valoração | Alta |
| DRI-004 | Métrica reportada deriva de tabela intermediária sem controle ou reconciliação com fonte primária | Processing | Completude | Alta |
| DRI-005 | Campo crítico do relatório não possui definição formal ou regra de negócio documentada | Initiation | Apresentação | Média |
| DRI-006 | Fonte de verdade não definida quando há múltiplos sistemas para o mesmo dado | Initiation | Existência | Alta |

**Controles típicos que mitigam:**
- catálogo de dados com owner, fonte e definição de campos críticos
- data lineage documentado para reports e dashboards críticos
- definição de system of record por domínio de dado
- revisão de regras de transformação por owner de negócio
- reconciliação entre camada intermediária e fonte primária

**Flag de risco elevado:** relatório criado por área usuária a partir de exportações manuais e joins locais.

---

## Subprocesso 2: Relatórios IPE e Extrações

Etapa de gerar, parametrizar, extrair e usar reports como Informação Produzida pela Entidade (IPE) em controles, testes e decisões.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| DRI-007 | Relatório usado como evidência sem validar parâmetros de extração | Processing | Completude | Alta |
| DRI-008 | População extraída exclui registros por filtro incorreto, período errado ou status omitido | Processing | Completude | Alta |
| DRI-009 | Relatório gerado por usuário com possibilidade de editar dados antes da exportação | Processing | Existência | Alta |
| DRI-010 | Extração não contém timestamp, usuário, sistema ou versão do relatório | Recording | Existência | Média |
| DRI-011 | Relatório customizado alterado sem revalidar lógica antes de uso em controle | Processing | Existência | Alta |
| DRI-012 | Total do relatório não reconciliado com razão, subledger ou outra fonte independente | Reporting | Valoração | Alta |

**Controles típicos que mitigam:**
- checklist de IPE com fonte, parâmetros, data, usuário e owner
- validação de completude e acurácia antes de usar o relatório
- reconciliação de totais com fonte independente
- controle de mudanças para reports customizados
- restrição de edição entre extração e uso

**Armadilha crítica:** testar amostra de um relatório sem testar antes se a população está completa.

---

## Subprocesso 3: Dashboards BI e Métricas

Etapa de desenvolvimento, manutenção, publicação e uso de dashboards, KPIs, scorecards e métricas gerenciais.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| DRI-013 | KPI definido de forma ambígua — áreas calculam o mesmo indicador de formas diferentes | Initiation | Apresentação | Alta |
| DRI-014 | Dashboard BI não reconcilia com relatório oficial usado no fechamento ou gestão | Reporting | Valoração | Alta |
| DRI-015 | Métrica crítica exclui exceções, cancelamentos, devoluções ou ajustes sem divulgação | Reporting | Completude | Alta |
| DRI-016 | Atualização do dashboard falha silenciosamente e usuários continuam usando dado antigo | Processing | Completude | Alta |
| DRI-017 | Indicador usado em bônus ou meta não passa por revisão independente | Processing | Existência | Alta |
| DRI-018 | Filtro padrão do dashboard muda interpretação do indicador sem transparência para usuários | Reporting | Apresentação | Média |

**Controles típicos que mitigam:**
- dicionário de KPIs com fórmula, escopo, filtros e owner
- reconciliação periódica entre BI e fonte oficial
- monitoramento de atualização/carga do dashboard
- aprovação de mudanças em métricas usadas em metas
- visualização de data refresh, filtros e escopo no dashboard

**Flag de risco elevado:** KPI usado para remuneração variável, covenant, reporte ESG ou apresentação a investidores.

---

## Subprocesso 4: Reconciliação e Completude de Dados

Etapa de validar populações, totais, períodos, duplicidades, lacunas e integridade entre sistemas ou relatórios.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| DRI-019 | População de teste não reconciliada com total do sistema fonte | Processing | Completude | Alta |
| DRI-020 | Registros duplicados inflando volume, valor ou indicador | Processing | Existência | Alta |
| DRI-021 | Registros sem chave única impedem rastreamento ponta a ponta | Recording | Completude | Média |
| DRI-022 | Período de dados não fecha com calendário contábil ou operacional | Recording | Corte | Alta |
| DRI-023 | Diferenças entre sistemas tratadas como timing sem evidência de compensação | Processing | Valoração | Alta |
| DRI-024 | Registros rejeitados em carga ou integração ficam fora do reporte final | Processing | Completude | Alta |

**Controles típicos que mitigam:**
- reconciliação de total, quantidade e valor entre origem e destino
- identificação de chave única e testes de duplicidade
- validação de período e cut-off
- log de registros rejeitados ou excluídos
- investigação formal de diferenças relevantes

**Relação com ITGC:** interfaces e jobs podem processar corretamente tecnicamente, mas ainda assim o dado final precisa ser reconciliado para uso como evidência.

---

## Subprocesso 5: Qualidade, Transformação e Master Data

Etapa de governar qualidade de dados, transformações, regras de negócio, enriquecimento, de-para e dados mestres usados em reportes.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| DRI-025 | Regra de transformação ou de-para aplicada sem aprovação do owner de negócio | Processing | Existência | Alta |
| DRI-026 | Master data desatualizado distorce classificação de cliente, produto, centro de custo ou processo | Processing | Apresentação | Alta |
| DRI-027 | Dados nulos, inválidos ou outliers substituídos manualmente sem trilha | Processing | Valoração | Alta |
| DRI-028 | Correção de qualidade de dados feita diretamente na base de reporting sem corrigir fonte | Processing | Existência | Média |
| DRI-029 | Regra de limpeza remove transações legítimas da população | Processing | Completude | Alta |
| DRI-030 | Mudança em tabela de de-para altera histórico sem versionamento | Reporting | Apresentação | Média |

**Controles típicos que mitigam:**
- aprovação de regras de transformação e de-para
- controle de versão de regras e tabelas mestres
- data quality checks para nulos, duplicados, outliers e inconsistências
- correção na fonte sempre que possível
- trilha de ajustes manuais sobre dados reportados

**Flag de risco elevado:** muita explicação começa com "a gente limpa essa base antes de usar".

---

## Subprocesso 6: Acesso, Governança e Change de Reportes

Etapa de controlar quem cria, altera, publica, aprova e acessa relatórios, datasets, dashboards e modelos de dados.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| DRI-031 | Usuário de negócio altera relatório crítico sem controle de mudança | Processing | Existência | Alta |
| DRI-032 | Acesso de edição em dataset crítico concedido a usuários sem necessidade | Processing | Existência | Alta |
| DRI-033 | Dashboard publicado sem revisão ou aprovação do owner da métrica | Processing | Existência | Média |
| DRI-034 | Ambiente de desenvolvimento e produção de BI não segregado | Processing | Existência | Alta |
| DRI-035 | Versão antiga de relatório permanece disponível e é usada por usuários | Reporting | Apresentação | Média |

**Controles típicos que mitigam:**
- workflow de mudança para reports e datasets críticos
- segregação entre desenvolvimento, homologação e produção
- restrição de edição a owners autorizados
- aprovação antes de publicação
- descontinuação controlada de versões antigas

**Relação com UAM:** UAM controla perfis; DRI avalia se esses perfis protegem reportes e datasets críticos.

---

## Subprocesso 7: Modelos, Planilhas e Cálculos Manuais

Etapa de governar planilhas, modelos de cálculo, macros, templates manuais, working papers e arquivos usados em controles ou fechamento.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| DRI-036 | Planilha crítica sem proteção de fórmulas ou controle de versão | Processing | Existência | Alta |
| DRI-037 | Fórmula manual alterada sem revisão independente | Processing | Valoração | Alta |
| DRI-038 | Input manual digitado sem evidência de fonte ou revisão | Recording | Existência | Alta |
| DRI-039 | Macro ou script local executado sem documentação e sem validação de resultado | Processing | Existência | Alta |
| DRI-040 | Modelo de cálculo reutilizado para novo período sem limpar dados antigos | Recording | Corte | Média |
| DRI-041 | Planilha crítica armazenada fora de repositório controlado | Recording | Existência | Média |

**Controles típicos que mitigam:**
- inventário de EUCs/planilhas críticas
- proteção de células e fórmulas
- revisão independente de inputs, fórmulas e outputs
- controle de versão e armazenamento central
- validação de macros ou scripts locais

**Armadilha comum:** chamar planilha crítica de "só apoio" quando ela calcula provisão, métrica, amostra ou ajuste contábil.

---

## Subprocesso 8: Retenção e Evidência de Reporting

Etapa de preservar evidência, versões, logs, parâmetros, aprovações e outputs usados para suportar decisões, controles e auditoria.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| DRI-042 | Evidência de relatório não retém parâmetros, data de extração ou versão | Recording | Existência | Média |
| DRI-043 | Output usado em controle é sobrescrito sem retenção da versão executada | Recording | Completude | Alta |
| DRI-044 | Aprovação de relatório ou métrica não documentada | Processing | Existência | Média |
| DRI-045 | Logs de execução, carga ou refresh não retidos por período suficiente | Recording | Completude | Média |
| DRI-046 | Evidência de reporte não permite reexecução ou reperformance pelo auditor | Reporting | Existência | Alta |

**Controles típicos que mitigam:**
- retenção de output final, parâmetros e data de extração
- versionamento de relatórios usados em controle
- aprovação documentada pelo owner
- retenção de logs de carga/refresh
- pacote de evidência que permita reperformance

---

## Leitura Rápida por Risco

| Risco Central | Subprocessos Críticos | WCGW-chave |
|---|---|---|
| Fonte de verdade indefinida | Fontes e lineage | DRI-001, DRI-006 |
| Report usado sem validar população | IPE | DRI-007, DRI-008, DRI-012 |
| KPI ambíguo ou inflado | BI e métricas | DRI-013, DRI-015, DRI-017 |
| Dados incompletos entre sistemas | Reconciliação | DRI-019, DRI-023, DRI-024 |
| Transformação/de-para altera resultado | Qualidade e master data | DRI-025, DRI-029, DRI-030 |
| Report crítico alterado sem change | Governança | DRI-031, DRI-034 |
| Planilha crítica sem controle | Modelos manuais | DRI-036, DRI-037, DRI-039 |
| Evidência não reperforma | Retenção | DRI-042, DRI-043, DRI-046 |
