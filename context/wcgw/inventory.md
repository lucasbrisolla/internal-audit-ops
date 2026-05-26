---
processo: inventory
nivel: 1
abreviacao: INV
subprocessos:
  - cadastro-e-classificacao-de-estoques
  - recebimento-e-entrada
  - movimentacao-producao-e-transferencias
  - contagem-fisica-e-conciliacao
  - custeio-e-valoracao
  - obsolescencia-perdas-e-vnr
  - estoques-em-terceiros-e-consignacao
  - corte-e-reporte
assercoes_primarias:
  - existência
  - completude
  - valoração
  - corte
  - apresentação
frameworks:
  - COSO
  - IAS 2
  - CPC 16
  - SOX
referencias:
  - _method-wiki/processes/inventory-observation-and-counting.md
  - _method-wiki/patterns/test-of-details.md
  - context/wcgw/procure-to-pay.md
  - context/wcgw/order-to-cash.md
  - context/wcgw/fraud-risk-assessment.md
---

# WCGW — Inventory (INV)

Estoques concentram risco operacional e contábil: recebem compras, alimentam produção, sustentam venda, afetam custo, margem, capital de giro e indicadores de performance. O risco não é apenas "o estoque está errado"; é **onde** ele pode estar errado: quantidade, existência física, custo, corte, obsolescência, propriedade ou classificação.

O auditor deve conectar três visões: movimentação física, registro sistêmico e mensuração contábil. Quando essas três camadas não conversam, o estoque vira uma das áreas mais fáceis para esconder perda, fraude, erro de margem ou manipulação de resultado.

---

## Subprocesso 1: Cadastro e Classificação de Estoques

Etapa em que itens, SKUs, unidades de medida, categorias, centros, depósitos e parâmetros de estoque são criados ou mantidos no sistema.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| INV-001 | Item cadastrado em categoria incorreta — classificação contábil e operacional distorcida | Initiation | Apresentação | Média |
| INV-002 | Unidade de medida configurada incorretamente — entradas, saídas ou conversões calculadas em quantidade errada | Recording | Valoração | Alta |
| INV-003 | Mesmo item cadastrado em SKUs duplicados — saldo fragmentado e risco de compras ou baixas indevidas | Recording | Completude | Média |
| INV-004 | Parâmetro de estoque mínimo/máximo desatualizado — compras desnecessárias ou ruptura não detectada | Processing | Valoração | Média |
| INV-005 | Item criado sem aprovação de área responsável — cadastro mestre exposto a erro ou manipulação | Initiation | Existência | Média |
| INV-006 | Tipo de material definido incorretamente (matéria-prima, produto acabado, MRO, sucata) — impacto em custo e apresentação | Initiation | Apresentação | Alta |

**Controles típicos que mitigam:**
- workflow de criação e alteração de item mestre
- segregação entre solicitante, cadastrador e aprovador
- validação de unidade de medida e fator de conversão por área técnica
- revisão periódica de SKUs duplicados, inativos ou sem movimentação
- matriz de classificação por tipo de material e conta contábil

---

## Subprocesso 2: Recebimento e Entrada

Etapa de recebimento físico, inspeção, conferência com pedido/NF e entrada no sistema.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| INV-007 | Estoque registrado sem recebimento físico confirmado — ativo fictício reconhecido | Recording | Existência | Alta |
| INV-008 | Mercadoria recebida fisicamente mas não registrada no sistema — estoque e passivo incompletos | Recording | Completude | Alta |
| INV-009 | Quantidade recebida registrada acima da quantidade entregue — estoque superavaliado e pagamento indevido | Recording | Valoração | Alta |
| INV-010 | Inspeção de qualidade não realizada antes da entrada — item defeituoso registrado como utilizável | Processing | Valoração | Alta |
| INV-011 | Recebimento registrado por quem aprovou a compra ou selecionou o fornecedor — segregação quebrada | Processing | Existência | Alta |
| INV-012 | Entrada registrada em depósito ou localização incorreta — saldo existe, mas não é localizável | Recording | Apresentação | Média |

**Controles típicos que mitigam:**
- conferência física independente no recebimento
- three-way match entre OC, NF e recebimento
- bloqueio de qualidade para itens sujeitos a inspeção
- segregação entre compras, recebimento e contas a pagar
- uso de coletor/código de barras para localização e quantidade

**Flag de risco elevado:** recebimentos próximos ao fechamento com entrada manual e sem evidência física.

---

## Subprocesso 3: Movimentação, Produção e Transferências

Etapa em que estoque é movimentado entre depósitos, consumido na produção, separado para venda, devolvido ou transferido.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| INV-013 | Saída de estoque registrada sem requisição ou ordem de produção aprovada | Processing | Existência | Alta |
| INV-014 | Consumo de matéria-prima registrado em quantidade diferente da lista técnica/BOM sem justificativa | Processing | Valoração | Alta |
| INV-015 | Transferência entre depósitos não confirmada pelo destinatário — estoque em trânsito sem dono claro | Processing | Completude | Média |
| INV-016 | Ajuste manual de saldo usado para corrigir perdas sem investigação de causa | Recording | Existência | Alta |
| INV-017 | Sucata, refugo ou perda de produção não registrada tempestivamente | Recording | Completude | Alta |
| INV-018 | Devolução de cliente registrada como estoque vendável sem inspeção | Processing | Valoração | Média |

**Controles típicos que mitigam:**
- requisição aprovada para saída de materiais
- BOM/lista técnica aprovada e revisão de variações de consumo
- confirmação dupla em transferências entre depósitos
- relatório de ajustes manuais por usuário, motivo e valor
- processo formal para sucata, refugo e devoluções

**Armadilha comum:** aceitar ajuste de inventário como "limpeza operacional" sem rastrear se a diferença é erro, furto, quebra, consumo indevido ou cadastro incorreto.

---

## Subprocesso 4: Contagem Física e Conciliação

Etapa de inventário físico, contagens cíclicas, reconciliação entre físico e sistema e aprovação de ajustes.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| INV-019 | Contagem física não realizada para itens relevantes — existência do estoque não verificada | Processing | Existência | Alta |
| INV-020 | Equipe de contagem tem acesso prévio às quantidades sistêmicas — risco de contagem direcionada | Processing | Existência | Alta |
| INV-021 | Diferenças de inventário aprovadas sem investigação formal | Processing | Existência | Alta |
| INV-022 | Itens em locais remotos, terceiros ou trânsito excluídos da contagem | Processing | Completude | Alta |
| INV-023 | Contagem física realizada sem controle de cut-off de entradas e saídas | Recording | Corte | Alta |
| INV-024 | Ajustes pós-contagem lançados por pessoa sem aprovação independente | Recording | Existência | Alta |

**Controles típicos que mitigam:**
- plano de inventário aprovado com escopo, datas, equipes e locais
- contagem cega ou com quantidade sistêmica ocultada
- dupla contagem para itens relevantes ou divergentes
- reconciliação formal físico x sistema com investigação de diferenças
- aprovação independente de ajustes de inventário

**Flag de risco elevado:** diferenças recorrentes nos mesmos itens, locais ou responsáveis.

---

## Subprocesso 5: Custeio e Valoração

Etapa de determinação do custo de estoque: custo médio, FIFO, standard cost, absorção de custos, variações de produção e alocação de overhead.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| INV-025 | Método de custeio configurado incorretamente ou aplicado de forma inconsistente entre períodos | Recording | Valoração | Alta |
| INV-026 | Standard cost não revisado periodicamente — custo padrão distante do custo real | Processing | Valoração | Alta |
| INV-027 | Variações de produção relevantes capitalizadas sem análise — estoque absorve ineficiência operacional | Recording | Valoração | Alta |
| INV-028 | Overhead alocado ao estoque sem base racional ou sem capacidade normal considerada | Recording | Valoração | Alta |
| INV-029 | Fretes, impostos recuperáveis ou descontos tratados incorretamente no custo do estoque | Recording | Valoração | Média |
| INV-030 | Custo de produto acabado não reconciliado com consumo de matéria-prima, mão de obra e overhead | Processing | Valoração | Alta |

**Controles típicos que mitigam:**
- política formal de custeio alinhada a CPC 16 / IAS 2
- revisão periódica de standard cost e variações relevantes
- reconciliação entre produção, consumo e custo contábil
- aprovação de parâmetros de overhead e capacidade normal
- análise de margem e custo unitário por produto

**Flag de risco elevado:** margem melhora enquanto produção cai, perdas aumentam ou custo de insumo sobe.

---

## Subprocesso 6: Obsolescência, Perdas e Valor Realizável Líquido

Etapa de identificação de itens obsoletos, vencidos, danificados, baixa rotatividade, perdas e necessidade de write-down para valor realizável líquido.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| INV-031 | Itens obsoletos ou sem giro mantidos pelo custo sem provisão ou write-down | Processing | Valoração | Alta |
| INV-032 | Estoque vencido, danificado ou deteriorado classificado como vendável | Processing | Existência | Alta |
| INV-033 | Valor realizável líquido não comparado ao custo para itens relevantes | Processing | Valoração | Alta |
| INV-034 | Provisão de obsolescência calculada com premissas desatualizadas ou arbitrárias | Processing | Valoração | Alta |
| INV-035 | Baixa de estoque aprovada sem laudo, evidência física ou justificativa operacional | Recording | Existência | Média |
| INV-036 | Estoque de baixa rotatividade excluído de análise por estar em depósito remoto ou terceiro | Processing | Completude | Alta |

**Controles típicos que mitigam:**
- aging de estoque por item, lote e localização
- análise periódica de giro, validade, dano e obsolescência
- comparação custo x valor realizável líquido
- aprovação formal para baixa, sucata ou destruição
- revisão independente de premissas de provisão

**Armadilha crítica:** usar venda futura esperada como justificativa genérica sem evidência de pedido, histórico de venda ou plano comercial realista.

---

## Subprocesso 7: Estoques em Terceiros e Consignação

Etapa de controle sobre estoques mantidos por terceiros, em poder de clientes, operadores logísticos, industrializadores, consignatários ou em trânsito.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| INV-037 | Estoque em poder de terceiro não confirmado periodicamente | Processing | Existência | Alta |
| INV-038 | Estoque de terceiros mantido nas instalações da empresa registrado como ativo próprio | Recording | Existência | Alta |
| INV-039 | Mercadoria em consignação tratada como venda antes da transferência de controle | Recording | Corte | Alta |
| INV-040 | Estoque em trânsito registrado no período errado por interpretação incorreta de Incoterms ou transferência de risco | Recording | Corte | Alta |

**Controles típicos que mitigam:**
- confirmação periódica de estoque em terceiros
- reconciliação entre relatório do terceiro e ERP
- identificação física e sistêmica de estoque próprio x estoque de terceiros
- revisão de Incoterms e cláusulas de transferência de controle
- inventário físico ou confirmação alternativa para locais relevantes

---

## Subprocesso 8: Corte e Reporte

Etapa de fechamento contábil do estoque: corte de entradas/saídas, reconciliações, divulgação e integração com custo das vendas.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| INV-041 | Entradas de estoque antes do fechamento registradas no período seguinte — estoque e passivo incompletos | Recording | Corte | Alta |
| INV-042 | Saídas ou vendas próximas ao fechamento registradas no período incorreto | Recording | Corte | Alta |
| INV-043 | Razão contábil de estoque não conciliado com relatório operacional do ERP | Reporting | Completude | Alta |
| INV-044 | Divulgação de estoques não apresenta política de mensuração, write-downs ou garantias relevantes | Reporting | Apresentação | Média |

**Controles típicos que mitigam:**
- teste de cut-off de recebimentos, expedições e notas fiscais
- reconciliação mensal razão x subledger x relatório físico
- revisão de variações entre estoque, CPV e margem bruta
- checklist de divulgação para políticas, provisões, garantias e restrições

---

## Leitura Rápida por Risco

| Risco Central | Subprocessos Críticos | WCGW-chave |
|---|---|---|
| Estoque fictício ou inexistente | Recebimento, Contagem | INV-007, INV-019, INV-021 |
| Estoque físico não registrado | Recebimento, Corte | INV-008, INV-041 |
| Quantidade ou localização incorreta | Recebimento, Movimentação | INV-009, INV-012, INV-015 |
| Ajustes manuais sem causa raiz | Movimentação, Contagem | INV-016, INV-021, INV-024 |
| Custeio incorreto | Custeio | INV-025, INV-027, INV-028, INV-030 |
| Obsolescência ou VNR não reconhecido | Obsolescência | INV-031, INV-033, INV-034 |
| Estoque em terceiro sem confirmação | Terceiros | INV-037, INV-038 |
| Consignação ou trânsito no período errado | Terceiros, Corte | INV-039, INV-040, INV-042 |
| Reconciliação incompleta no fechamento | Corte e Reporte | INV-043 |
