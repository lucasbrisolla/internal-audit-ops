---
name: process-flow-bpmn
description: Use when a walkthrough, SCOT table, RCM, transcript or process narrative needs to be converted into a BPMN 2.0 diagram for documentation or audit analysis.
---

# process-flow-bpmn

## Objetivo

Converter descrições de processo de auditoria em BPMN 2.0 XML (Level 1 + Level 2 seletivo), sem seção de layout. O arquivo gerado é renderizado por `bpmn-to-image` ou visualizado em bpmn.io.

Use **Mermaid** (`skills/process-flow-mermaid.md`) apenas para embeds inline no Obsidian. Para armazenamento, documentação formal e análise de processo, use BPMN 2.0.

## Pré-requisito: SIPOC antes do BPMN

Em contexto de auditoria interna, o BPMN é a **Camada 3** de uma abordagem em três camadas. Antes de gerar o XML:

1. **Classificar o processo** (APQC PCF / E2E) — onde ele se encaixa? OTC, P2P, H2R?
2. **Construir o SIPOC** — Supplier / Input / Process / Output / Customer

O SIPOC define as fronteiras do processo (o que entra, o que sai, quem são os atores externos) e os critérios de eficácia (Output = o que o processo deve entregar). Sem ele, o BPMN corre o risco de mapear etapas internas sem deixar claro onde o processo começa e termina.

Referência metodológica completa: `_method-wiki/concepts/process-mapping-internal-audit.md`

Se o insumo recebido for apenas uma narrativa de processo sem SIPOC explícito, derivar as fronteiras S/I/O/C antes de definir o `startEvent` e o `endEvent` do BPMN.

## Elementos — Level 1 (sempre presentes)

| Conceito de auditoria | Elemento BPMN |
|---|---|
| Início do processo | `startEvent` |
| Fim do processo | `endEvent` |
| Etapa operacional com interação humana (revisar, aprovar, preencher) | `userTask` |
| Etapa automatizada por sistema (cálculo, integração, API, ERP) | `serviceTask` |
| Envio automático (e-mail, notificação, alerta de sistema) | `sendTask` |
| Aguardar resposta externa (confirmação, retorno de sistema, webhook) | `receiveTask` |
| Decisão por motor de regras ou política formalizada | `businessRuleTask` |
| Atividade manual sem suporte de sistema (conferência física, formulário em papel) | `manualTask` |
| Execução de script ou rotina de código | `scriptTask` |
| Etapa genérica (ator ou tipo indefinido no insumo) | `task` |
| Condição / decisão (exatamente um caminho) | `exclusiveGateway` |
| Atividades simultâneas obrigatórias (todos os caminhos) | `parallelGateway` |
| Fluxo entre etapas | `sequenceFlow` |
| Ator / departamento | `lane` dentro de `laneSet` |

## Elementos — Level 2 (seletivo para auditoria)

| Conceito de auditoria | Elemento BPMN |
|---|---|
| Subprocesso / rotina de suporte | `subProcess` |
| Documento, evidência, artefato | `dataObject` + `dataObjectReference` |
| Sistema (ERP, sistema origem, workflow) | `dataStore` + `dataStoreReference` |
| Condição múltipla simultânea (um ou mais caminhos, conforme dados) | `inclusiveGateway` |
| Roteamento por evento que ocorrer primeiro (ex: aprovação OR timeout) | `eventBasedGateway` |
| Processo com prazo máximo de resposta ou espera por evento externo (timer ou message) — etapa no fluxo, não anexada a task | `intermediateCatchEvent` |
| Emissão de mensagem ou sinal no meio do fluxo (notificar pool externo, disparar integração) | `intermediateThrowEvent` |
| Processo inter-organizacional com troca de mensagem entre entidades | `pool` + `messageFlow` |
| Tarefa que repete até condição (ex: nova análise até aprovação final) | task com marker `loopCharacteristics` |
| Tarefa executada em paralelo por múltiplos atores (ex: n aprovadores simultâneos) | task com marker `multiInstanceLoopCharacteristics` |
| SLA / prazo máximo anexado a uma tarefa específica | `boundaryEvent` com `timerEventDefinition` |
| Agrupamento visual de etapas por fase (ex: fases SCOT) sem afetar fluxo | `group` |
| Nota explicativa ou ponto a confirmar vinculado a um elemento | `textAnnotation` + `association` |

**`inclusiveGateway` vs `parallelGateway`:** use `inclusiveGateway` quando os caminhos ativos dependem de condições (ex: "valor > 50k → notificar CFO; risco alto → acionar compliance" — ambos podem ocorrer, mas nenhum é obrigatório). Use `parallelGateway` quando todos os caminhos ocorrem sempre, sem condição. Em auditoria: aprovações escalonadas por faixa de valor são `inclusiveGateway`; segregação de funções que sempre exige dois revisores simultâneos é `parallelGateway`.

**`eventBasedGateway`:** roteia pelo primeiro evento que ocorrer — não por dados. Usar quando o processo aguarda uma resposta com prazo alternativo (ex: "receber confirmação do fornecedor OU acionar escalation após 48h"). Em auditoria: controles com SLA de resposta, aprovações com vencimento automático.

**Pool vs Lane:** lane = papel dentro de um único processo controlado por um "condutor" (ex: processo interno da empresa com Analista, Supervisor, CFO). Pool separado = processo independente de outra entidade (ex: cliente, fornecedor, banco) que se comunica via `messageFlow`. Use pool quando o SIPOC identificar um Customer ou Supplier como participante ativo com processo próprio — não apenas como receptor de output.

**Task markers (loop e multiple instance):** adicionar dentro do elemento task via atributos XML.
- Loop (repetição até condição): `<bpmn:standardLoopCharacteristics testBefore="false"/>` dentro da task
- Multiple instance paralelo (n instâncias simultâneas): `<bpmn:multiInstanceLoopCharacteristics isSequential="false"/>` dentro da task

**`boundaryEvent` com timer:** evento anexado à borda de uma task — interrompe (ou não) a task quando o prazo vence. Diferente do `intermediateCatchEvent` no fluxo principal: o boundary event é acionado *enquanto a task está ativa*, sem precisar que o fluxo passe por ele. Em auditoria: aprovações com SLA regulatório, confirmações com vencimento, controles preventivos com prazo máximo de execução.

```xml
<!-- cancelActivity="true" = interrompe a task ao vencer; "false" = executa em paralelo sem cancelar -->
<bpmn:boundaryEvent id="Boundary_Timeout" attachedToRef="Task_AprovarSolicitacao" cancelActivity="true">
  <bpmn:timerEventDefinition id="TimerDef_1">
    <bpmn:timeDuration>PT48H</bpmn:timeDuration>
  </bpmn:timerEventDefinition>
</bpmn:boundaryEvent>
<!-- O fluxo de exceção sai do boundaryEvent, não da task -->
<bpmn:sequenceFlow id="Flow_Escalacao" sourceRef="Boundary_Timeout" targetRef="Task_EscalarSupervisor"/>
```

**Eventos intermediários — `intermediateCatchEvent` e `intermediateThrowEvent`:**

Diferença fundamental em relação ao `boundaryEvent`:
- `boundaryEvent` — anexado à *borda* de uma task, dispara *enquanto a task está ativa*. O fluxo principal continua ou é interrompido.
- `intermediateCatchEvent` — *é uma etapa* no fluxo: o processo chega até ele, espera, e só segue quando o evento ocorre.
- `intermediateThrowEvent` — *emite* um evento (mensagem, sinal) ao ser alcançado no fluxo; o processo não para, apenas dispara a emissão.

Em auditoria interna, usar quando o processo *explicitamente* descreve uma espera ou emissão de evento no meio do fluxo — não como substituto de gateway ou task.

| Elemento | Quando usar em auditoria |
|---|---|
| `intermediateCatchEvent` + `timerEventDefinition` | Prazo de quarentena, período de contestação, intervalo obrigatório entre etapas (ex: aguardar 5 dias úteis após comunicação de achado) |
| `intermediateCatchEvent` + `messageEventDefinition` | Aguardar confirmação de sistema externo ou de outro pool (ex: confirmação bancária de SWIFT, retorno de ERP após integração) |
| `intermediateThrowEvent` + `messageEventDefinition` | Enviar mensagem para outro pool no meio do processo (ex: notificar fornecedor de rejeição, disparar webhook para sistema de compliance) |

```xml
<!-- intermediateCatchEvent com timer (aguardar 5 dias úteis) -->
<bpmn:intermediateCatchEvent id="ICE_AguardarPrazo" name="Aguardar 5 dias úteis">
  <bpmn:timerEventDefinition id="TimerDef_Quarentena">
    <bpmn:timeDuration xsi:type="bpmn:tFormalExpression">P5D</bpmn:timeDuration>
  </bpmn:timerEventDefinition>
</bpmn:intermediateCatchEvent>
<bpmn:sequenceFlow id="Flow_ParaPrazo" sourceRef="Task_ComunicarAchado" targetRef="ICE_AguardarPrazo"/>
<bpmn:sequenceFlow id="Flow_AposPrazo" sourceRef="ICE_AguardarPrazo" targetRef="Task_RegistrarResposta"/>

<!-- intermediateCatchEvent com message (aguardar confirmação bancária) -->
<bpmn:intermediateCatchEvent id="ICE_ConfBancaria" name="Receber confirmação bancária">
  <bpmn:messageEventDefinition id="MsgDef_Banco" messageRef="Msg_ConfirmacaoBanco"/>
</bpmn:intermediateCatchEvent>
<!-- Declarar a mensagem fora do processo, dentro de definitions -->
<!-- <bpmn:message id="Msg_ConfirmacaoBanco" name="ConfirmacaoBancaria"/> -->

<!-- intermediateThrowEvent com message (enviar notificação para outro pool) -->
<bpmn:intermediateThrowEvent id="ITE_NotificarFornecedor" name="Notificar fornecedor de rejeição">
  <bpmn:messageEventDefinition id="MsgDef_Rejeicao" messageRef="Msg_RejeicaoNF"/>
</bpmn:intermediateThrowEvent>
```

**Formato de duração ISO 8601** para `timeDuration`:
- `PT48H` — 48 horas
- `P5D` — 5 dias
- `P1M` — 1 mês

**`message` declaration:** toda `messageEventDefinition` referencia um `<bpmn:message>` declarado dentro de `<bpmn:definitions>`, fora do processo. Sem essa declaração, o XML é inválido em ferramentas que validam schema.

**`intermediateThrowEvent` no bpmndi:** mesmo tamanho que `intermediateCatchEvent` (36×36). Visualmente o Catch tem dupla borda; o Throw tem borda simples com ícone preenchido — as ferramentas de renderização fazem a distinção automaticamente.

---

**`group`:** artefato visual que agrupa elementos sem afetar sequência ou fluxo. Útil para marcar fases SCOT no diagrama sem criar subprocesso. Não conecta por sequenceFlow — usa `categoryValueRef`.

```xml
<!-- No processo: declarar o group -->
<bpmn:group id="Group_FaseS" categoryValueRef="CatVal_S"/>
<!-- Fora do processo, dentro de definitions: declarar a categoria -->
<bpmn:category id="Cat_SCOT">
  <bpmn:categoryValue id="CatVal_S" value="S — Solicitação"/>
</bpmn:category>
```

**`textAnnotation` + `association`:** nota vinculada a qualquer elemento via associação pontilhada. Usar para pontos a confirmar, WCGWs identificados no diagrama, ou controles mapeados na etapa.

```xml
<bpmn:textAnnotation id="Annotation_1">
  <bpmn:text>A confirmar: quem autoriza acima de R$ 50k?</bpmn:text>
</bpmn:textAnnotation>
<bpmn:association id="Assoc_1" sourceRef="GW_LimiteAprovacao" targetRef="Annotation_1"/>
```

Não usar eventos de timer, mensagem ou sinal salvo quando o processo explicitamente os descreve.

## Paleta de Cores — Lógica Semântica

Cores sinalizam **nível de exposição a risco de controle**, não estética. Regra: quanto menos rastro automático, mais quente a cor.

| Cor | Elementos | Rationale |
|---|---|---|
| Verde `#2e7d32` | `serviceTask`, `startEvent` | Sistema executa — trilha automática, auditável por log. Risco operacional baixo. |
| Azul marca `#243782` | `userTask`, gateways | Interação humana com sistema — trilha existe mas depende de quem aprovou, quando e com qual critério. Ponto de controle mapeado. |
| Âmbar `#e65100` | `manualTask`, `boundaryEvent`, `textAnnotation` | Sem suporte de sistema — nenhuma trilha automática. Evidência depende de papel, planilha ou memória do executor. Máxima atenção do auditor. |
| Vermelho `#c62828` | `endEvent`, elementos `A confirmar` críticos | Resultado final do processo — o que precisa ser verificado contra o critério do SIPOC. Ênfase, não alerta. |

Gradiente de exposição: **verde → azul → âmbar → vermelho**.

Para paleta completa por cliente, ver `examples/generated/[cliente]-bpmn-design.md`. Aplicar via atributos `bioc:` e `color:` nos shapes do `bpmndi:` (ver seção "Como renderizar").

## Estrutura do XML

**Processo sem lanes (fluxo plano):** gerar sem a seção `bpmndi:`. O arquivo precisa passar pelo `bpmn-auto-layout` antes de abrir em qualquer ferramenta (ver "Como renderizar").

**Processo com lanes (swimlane — caso típico em auditoria):** gerar **com** a seção `bpmndi:` manual desde o início. Motivo: `bpmn-auto-layout` não gera `BPMNShape` para lanes nem para o pool — sem o `bpmndi:`, o arquivo abre com "no diagram to display" em bpmn.io e não exibe as swimlanes em nenhuma ferramenta. Usar as fórmulas e o template da seção "Template com bpmndi".

```xml
<?xml version="1.0" encoding="UTF-8"?>
<bpmn:definitions
  xmlns:bpmn="http://www.omg.org/spec/BPMN/20100524/MODEL"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  id="Definitions_1"
  targetNamespace="http://bpmn.io/schema/bpmn">

  <bpmn:process id="Process_[nome]" name="[Nome do Processo]" isExecutable="false">

    <bpmn:laneSet id="LaneSet_1">
      <bpmn:lane id="Lane_[ator]" name="[Ator / Departamento]">
        <bpmn:flowNodeRef>StartEvent_1</bpmn:flowNodeRef>
        <bpmn:flowNodeRef>Task_1</bpmn:flowNodeRef>
      </bpmn:lane>
    </bpmn:laneSet>

    <bpmn:startEvent id="StartEvent_1" name="[Gatilho]"/>

    <bpmn:userTask id="Task_1" name="[Etapa humana]"/>

    <bpmn:exclusiveGateway id="GW_1" name="[Condição?]"/>

    <bpmn:serviceTask id="Svc_1" name="[Etapa de sistema]"/>

    <bpmn:endEvent id="EndEvent_1" name="[Resultado]"/>

    <bpmn:sequenceFlow id="Flow_1" sourceRef="StartEvent_1" targetRef="Task_1"/>
    <bpmn:sequenceFlow id="Flow_2" sourceRef="Task_1" targetRef="GW_1"/>
    <bpmn:sequenceFlow id="Flow_3" name="Sim" sourceRef="GW_1" targetRef="Svc_1"/>
    <bpmn:sequenceFlow id="Flow_4" name="Não" sourceRef="GW_1" targetRef="EndEvent_1"/>
    <bpmn:sequenceFlow id="Flow_5" sourceRef="Svc_1" targetRef="EndEvent_1"/>

  </bpmn:process>

</bpmn:definitions>
```


## Regras de nomenclatura

- IDs sem espaços, acentos ou caracteres especiais: `Task_RegistrarPedido`, `GW_Aprovacao`, `Lane_Faturamento`
- Labels em PT-BR com acentuação correta: `"Aprovação do Diretor"`, `"Emissão de nota fiscal"`
- `isExecutable="false"` — diagrama é documentação, não processo executável
- Um arquivo `.bpmn` por processo principal

## Guardrails

- Não inventar etapa, ator, sistema ou decisão sem base no insumo recebido
- Lanes representam **quem executa** as atividades — pode ser papel, área, departamento ou sistema. O critério que define a lane é o ator, não o momento do processo
  - Usar lane por área/departamento quando a estrutura organizacional é o recorte natural do processo (ex: Controle de Riscos, Marketing, Compliance)
  - Usar lane por papel quando uma mesma área tem múltiplos papéis distintos no processo (ex: Analista de Faturamento, Supervisor, Gerente)
  - Sistemas e entidades externas: lane pelo nome (ex: "Sistema SAP", "Cliente") — ou pool separado se tiver processo próprio
  - **Nunca usar lane para fase temporal ou sequencial** (ex: "Fase de Aprovação", "Fase de Revisão") — isso inverte a lógica de swimlane
- Não incluir seção `bpmndi:` — o renderer faz o layout
- Não usar extensões proprietárias (`bizagi:`, `camunda:`, etc.)
- Se uma conexão for incerta, adicionar `textAnnotation` marcado como `A confirmar`
- Cada `flowNodeRef` dentro de `lane` deve referenciar um nó existente no processo

## Template de referência validado — 4 lanes (swimlane padrão de auditoria)

**Arquivo:** `templates/template-modelo.bpmn`

Usar como ponto de partida para qualquer novo diagrama com swimlanes. Cobre os casos mais complexos de layout — copiar a estrutura `bpmndi:`, ajustar IDs e coordenadas X.

### Mapa de coordenadas do template

| Lane | y início | height | center_y | Ator |
|---|---|---|---|---|
| Lane 1 | 80 | 200 | 180 | Área Responsável |
| Lane 2 | 280 | 200 | 380 | Controle de Riscos |
| Lane 3 | 480 | 140 | 550 | Marketing |
| Lane 4 | 620 | 200 | 720 | Compliance / TI |

Canvas total: width=2850, height=820. Lanes iniciam em x=30, width=2820.

### Padrões de waypoint usados no template

| Caso | Padrão de waypoints |
|---|---|
| Fluxo direto na mesma lane | `(x_right, center_y) → (x_left_next, center_y)` |
| Cross-lane descendo (lane 1→2) | `(cx, cy) → (cx, cy_target) → (left_target, cy_target)` — vai direito, desce, entra |
| Cross-lane subindo + voltando X (lane 2→1, backward) | `(cx, cy) → (cx, y_boundary) → (cx_target, y_boundary) → (cx_target, cy_target)` |
| "Não" path desviando elemento no caminho (mesma lane) | Rota abaixo: `(cx, bottom) → (cx, y+offset) → (cx_target, y+offset) → (cx_target, bottom)` |
| Loop backward (mesma lane) | Rota abaixo com y diferente do "Não" para não sobrepor |
| Drop vertical entre lanes (ex: CR→Marketing) | `(cx, bottom_cr) → (cx, top_mkt)` — linha reta vertical |

### Como adaptar para novo processo

1. Copiar o arquivo inteiro como base
2. Definir quantas lanes e suas alturas (200px padrão, 140px para lane estreita)
3. Calcular center_y de cada lane: `y_lane + height/2`
4. Posicionar elementos da esquerda para direita em X, centralizados no center_y da lane
5. Espaçamento recomendado: 130–150px entre tasks, 80px entre task e gateway adjacente
6. Para cross-lane: usar padrão da tabela acima conforme direção

## Template com bpmndi (layout manual — exemplo mínimo)

Usar quando o processo for simples (2 lanes, poucos elementos) e não valer a pena partir do template completo. Coordenadas derivadas de exemplos reais do bpmn-js.

### Tamanhos padrão dos elementos

Valores do Camunda Modeler (fonte autoritativa — `kitchen-sink.bpmn`):

| Elemento | width | height | Observação |
|---|---|---|---|
| `startEvent` / `endEvent` | 36 | 36 | |
| `intermediateCatchEvent` / `intermediateThrowEvent` | 36 | 36 | |
| `task` / `userTask` / `serviceTask` / `scriptTask` etc | 100 | 80 | |
| `exclusiveGateway` | 50 | 50 | `isMarkerVisible="true"` no BPMNShape |
| `parallelGateway` / `inclusiveGateway` / `eventBasedGateway` | 50 | 50 | |
| `participant` (pool) | variável | variável | `isHorizontal="true"` no BPMNShape |
| `dataObjectReference` | 36 | 50 | |
| `dataStoreReference` | 50 | 50 | |
| `subProcess` (expandido) | ≥350 | ≥200 | `isExpanded="true"` no BPMNShape |
| `textAnnotation` | 100 | 30 | |

### Fórmulas de coordenadas para Pool + Lanes

```
Pool:  x=12,  y=Y_pool,  width=W,        height=soma_lanes
Lane:  x=42,  y=Y_lane,  width=W−30,     height=H_lane
```

- Pool x=12, Lane x=42 → **gap de 30px = coluna do label do pool** (não reduzir)
- Primeira lane: `y = Y_pool`
- Próximas lanes: `y = y_anterior + height_anterior`
- Pool height = soma de todas as lane heights

### Posicionamento de nós dentro da lane

```
node_x = qualquer valor ≥ 42 (dentro da lane)
node_y = Y_lane + (H_lane / 2) − (node_height / 2)   ← centralizar verticalmente
```

Coordenadas são **absolutas** (relativas ao diagrama, não à lane). O nó deve estar visualmente dentro dos bounds y da sua lane ou o renderer vai renderizar seta "subindo".

### Exemplo mínimo (pool com 2 lanes horizontais)

```xml
<bpmndi:BPMNDiagram id="BPMNDiagram_1">
  <bpmndi:BPMNPlane bpmnElement="Process_faturamento">

    <!-- Pool: x=12, y=372, width=800, height=228 (114+114) -->
    <bpmndi:BPMNShape bpmnElement="Participant_1" isHorizontal="true">
      <dc:Bounds x="12" y="372" width="800" height="228"/>
    </bpmndi:BPMNShape>

    <!-- Lane 1: y=372, height=114 -->
    <bpmndi:BPMNShape bpmnElement="Lane_Faturamento" isHorizontal="true">
      <dc:Bounds x="42" y="372" width="770" height="114"/>
    </bpmndi:BPMNShape>

    <!-- Lane 2: y=486 (372+114), height=114 -->
    <bpmndi:BPMNShape bpmnElement="Lane_Financeiro" isHorizontal="true">
      <dc:Bounds x="42" y="486" width="770" height="114"/>
    </bpmndi:BPMNShape>

    <!-- startEvent centralizado em Lane 1: y=372+(114/2)−(30/2)=419 -->
    <bpmndi:BPMNShape bpmnElement="StartEvent_1">
      <dc:Bounds x="79" y="419" width="30" height="30"/>
    </bpmndi:BPMNShape>

    <!-- task em Lane 1: y=372+(114/2)−(68/2)=389 -->
    <bpmndi:BPMNShape bpmnElement="Task_EmitirNF">
      <dc:Bounds x="160" y="389" width="83" height="68"/>
    </bpmndi:BPMNShape>

    <!-- seta simples horizontal: source right edge → target left edge, mesmo y -->
    <bpmndi:BPMNEdge bpmnElement="Flow_1">
      <di:waypoint x="115" y="434"/>  <!-- startEvent: x+36, center_y (79+36=115) -->
      <di:waypoint x="160" y="434"/>  <!-- task: left edge, center_y (389+80/2=429→arredonda) -->
    </bpmndi:BPMNEdge>
    <!-- seta cross-lane: descer até lane 2 antes de ir para direita -->
    <!-- <bpmndi:BPMNEdge bpmnElement="Flow_crosslane">
      <di:waypoint x="260" y="434"/>  source center_x, source center_y (dentro lane 1)
      <di:waypoint x="260" y="540"/>  same x, dentro da lane 2 (y=486+...) 
      <di:waypoint x="350" y="540"/>  target left edge, target center_y
    </bpmndi:BPMNEdge> -->

  </bpmndi:BPMNPlane>
</bpmndi:BPMNDiagram>
```

Namespaces necessários no `<bpmn:definitions>` para layout manual:
```xml
xmlns:bpmndi="http://www.omg.org/spec/BPMN/20100524/DI"
xmlns:dc="http://www.omg.org/spec/DD/20100524/DC"
xmlns:di="http://www.omg.org/spec/DD/20100524/DI"
```

## Orientação de lanes

Por padrão, lanes são horizontais (swimlanes em linhas). Para colunas verticais (fluxo da esquerda para a direita entre departamentos):

```xml
<bpmn:laneSet id="LaneSet_1" isHorizontal="false">
```

- `isHorizontal="true"` (padrão): lanes empilhadas verticalmente, fluxo desce
- `isHorizontal="false"`: lanes em colunas, fluxo vai da esquerda para a direita

Escolher orientação antes de definir coordenadas — mudança posterior quebra todo o layout.

## Como renderizar

O arquivo `.bpmn` gerado (sem `bpmndi:`) **não abre em nenhuma ferramenta diretamente**. O passo de layout é obrigatório — tanto para importar em ferramenta quanto para renderizar como imagem.

O `layout.mjs` e o `node_modules` ficam em **`examples/generated/_bpmn-tools/`** — diretório central compartilhado por todos os diagramas. Nunca instalar dentro da pasta de cada diagrama.

```bash
# Setup único (só na primeira vez)
cd "examples/generated/_bpmn-tools"
npm install bpmn-auto-layout   # requer Node.js ≥ 20; funciona com warnings no 18+

# Gerar layout de qualquer diagrama
node _bpmn-tools/layout.mjs faturamento/faturamento-ciclo-principal.bpmn faturamento/faturamento-layout.bpmn

# Passo 3a: visualizar — arrastar processo-layout.bpmn para https://demo.bpmn.io
# Passo 3b: importar em ferramenta — usar processo-layout.bpmn (não o original)

# Passo 3c: renderizar como imagem
npx bpmn-to-image@0.9.0 "processo-layout.bpmn:/saida/processo.svg"
npx bpmn-to-image@0.9.0 "processo-layout.bpmn:/saida/processo.png"
```

### Limitação crítica: bpmn-auto-layout não renderiza swimlanes

`bpmn-auto-layout` posiciona os nós corretamente mas **não gera `BPMNShape` para lanes nem para o pool**. O resultado importado numa ferramenta mostra todos os elementos em plano único — sem divisão por ator.

Consequência: processos com `laneSet` perdem as swimlanes após o auto-layout.

**Workarounds (escolher um):**

| Opção | Quando usar |
|---|---|
| Importar `*-layout.bpmn` no demo.bpmn.io e atribuir lanes manualmente via arrastar | Processo pequeno / uso pontual |
| Gerar `bpmndi:` manual com lane shapes (ver "Template com bpmndi") | Processo grande / artefato permanente |

Para o template manual, incluir `BPMNShape` para cada lane dentro do `BPMNPlane` usando as fórmulas de coordenadas da seção abaixo.

Script `layout.mjs`:
```js
import { readFileSync, writeFileSync } from 'fs';
import { layoutProcess } from 'bpmn-auto-layout';

const input = readFileSync(process.argv[2], 'utf8');
const output = await layoutProcess(input);
writeFileSync(process.argv[3], output);
```

Requer Node.js ≥ 18. Para visualização interativa: arrastar o `.bpmn` para https://demo.bpmn.io

## Erros comuns

- **Processo com lanes gerado sem `bpmndi:`** — resultado: "no diagram to display" em bpmn.io. `bpmn-auto-layout` não gera shapes para lanes; para swimlanes, incluir `bpmndi:` manual desde a geração (ver "Template com bpmndi")
- **Importar o arquivo gerado direto na ferramenta (processo sem lanes)** — sempre usar o `*-layout.bpmn` (após rodar `bpmn-auto-layout`), nunca o original sem `bpmndi:`
- **Swimlanes sumindo após auto-layout** — limitação do `bpmn-auto-layout`: ele não gera shapes para lanes/pool; usar workaround (demo.bpmn.io manual ou bpmndi manual com lane shapes)
- Incluir seção `bpmndi:` manualmente — não fazer; o renderer posiciona os elementos
- Criar um lane por fase SCOT em vez de por ator — inverte a lógica de swimlane
- Usar lane para entidade externa (cliente, fornecedor, banco) quando ela tem processo próprio — nesses casos usar pool separado com `messageFlow`; lane é só para atores dentro do mesmo processo controlado
- Usar `exclusiveGateway` para paralelismo — usar `parallelGateway` (todos os caminhos obrigatórios) ou `inclusiveGateway` (um ou mais caminhos condicionais)
- Omitir `flowNodeRef` nas lanes — cada nó do processo deve declarar em qual lane está
- Labels longos demais — manter abaixo de 6 palavras para renderização legível
- **Alterar tipo de elemento sem atualizar a tag de fechamento** — ao mudar `userTask` para `manualTask` (ou qualquer tipo), atualizar *ambas* as tags: `<bpmn:manualTask ...>` e `</bpmn:manualTask>`; tag de fechamento divergente causa `closing tag mismatch` e invalida o arquivo inteiro
- **Seta "subindo" no diagrama** — causada por nó declarado na lane errada; verificar que cada `flowNodeRef` aponta para o nó correto e que a ordem dos `flowNodeRef` dentro da lane reflete a sequência visual esperada
- **Label do pool sobrepondo a primeira lane** — ocorre quando a coordenada x do `BPMNShape` do pool coincide com a da primeira lane; o pool deve ter largura extra à esquerda para acomodar o label
- **Mudar orientação de lanes no meio do layout** — alterar `isHorizontal` depois de definir coordenadas quebra todo o posicionamento; decidir antes de começar
