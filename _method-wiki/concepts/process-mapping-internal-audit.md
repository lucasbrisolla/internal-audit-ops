# Process Mapping — Auditoria Interna

## Papel

Base conceitual para mapeamento de processos em auditoria interna. Define o padrão de mercado (SIPOC), a abordagem em camadas, o overlay de riscos e controles, e o output esperado — diferenciando da lógica SCOT de auditoria externa.

## Quando usar

- entendimento inicial do processo auditado
- desenho de walkthrough de auditoria interna
- identificação de gaps de controle e segregação de funções
- suporte à elaboração de RCM e programa de trabalho
- base para achados e recomendações

## Diferença fundamental em relação à auditoria externa

Em auditoria externa, o mapeamento segue o caminho crítico da transação **até o reporte nas demonstrações financeiras**. O critério de escopo é materialidade financeira e a estrutura de análise é o SCOT (iniciação → registro → processamento → reporte de DF).

Em auditoria interna, o processo é mapeado até o **objetivo do processo** — que pode ser operacional, de compliance ou financeiro. Processos como RH, TI ou logística têm objetivos que não chegam ao reporte de DF, mas são igualmente relevantes. O padrão de mercado para esse mapeamento não é uma adaptação do SCOT: é o **SIPOC**.

## Padrão de mercado: SIPOC

O SIPOC (Supplier → Input → Process → Output → Customer) é o framework consagrado pelo IIA e pelo CIA Exam para mapeamento de processos em auditoria interna. Captura dimensões que o SCOT não cobre:

| Dimensão | O que mapeia | Relevância para auditoria interna |
|---|---|---|
| **Supplier** | Quem fornece os insumos do processo | Identifica dependências externas, terceiros, riscos de fornecedor |
| **Input** | Dado, documento ou recurso que entra | Valida completude e qualidade dos inputs — gap frequente |
| **Process** | Etapas internas de transformação | Onde vivem os controles, segregações e riscos operacionais |
| **Output** | Resultado entregue | Critério de sucesso do processo — base para o teste de eficácia |
| **Customer** | Quem recebe o output | Define quem valida, quem é impactado por falha |

### Por que não apenas adaptar o SCOT?

O SCOT foi desenhado para rastrear assertivas financeiras (existência, completude, competência) até o reporte de DF. Funciona bem para auditoria externa. Em auditoria interna:

- Processos operacionais (RH, logística, TI) não terminam em DF — o SCOT perde o ponto de chegada
- SIPOC mapeia quem são os fornecedores e clientes do processo — dimensão crítica para identificar riscos de interface
- A etapa "Output" do SIPOC é o critério de eficácia do controle; o SCOT não tem equivalente direto
- SIPOC é compatível com COSO ERM 2017 e IIA Three Lines Model; SCOT não

## Abordagem em camadas

O estado da arte em auditoria interna usa mapeamento em três camadas progressivas:

```
Camada 1 — Classificação do processo (APQC PCF / E2E)
    Onde o processo se encaixa no mapa global? OTC? P2P? H2R?
    Evita escopo incompleto e identifica interfaces entre processos.

Camada 2 — SIPOC
    Quem são os fornecedores e clientes deste processo?
    Quais são os inputs, etapas macro e outputs?
    Define as fronteiras e os critérios de eficácia antes de descer no detalhe.

Camada 3 — BPMN (swimlanes por ator)
    Fluxo detalhado as-is, com atores, decisões e sistemas.
    Swimlanes por departamento/ator — não por fase do processo.
    Base para overlay de riscos e controles.
```

O overlay de riscos e controles (RCM) é aplicado sobre a Camada 3.

## O que se mapeia no SIPOC por processo de auditoria

| Dimensão | Faturamento (exemplo) | RH — Folha (exemplo) |
|---|---|---|
| Supplier | Comercial (contrato), sistema operacional | DP, gestores, banco de horas |
| Input | Contrato assinado, mapa de faturamento | Ponto eletrônico, férias aprovadas |
| Process | Emissão de NF, envio SAP, boleto | Cálculo, aprovação, pagamento |
| Output | Fatura enviada ao cliente | Crédito na conta do colaborador |
| Customer | Cliente | Colaborador, RFB, previdência |

## Overlay de riscos e controles (RCM)

Após construir o BPMN (Camada 3), sobrepor:

1. **Risco inerente por etapa** — o que pode dar errado naquela fase sem nenhum controle
2. **Controle existente** — o que a empresa faz para mitigar
3. **Avaliação do controle** — o controle é bem desenhado? Opera de fato?
4. **Exposição residual** — o risco remanescente após o controle

O resultado é o **RCM (Risk and Control Matrix)** — artefato central de auditoria interna, equivalente ao CRM de auditoria externa.

## Foco específico de auditoria interna

Diferente da auditoria externa, que foca em assertivas financeiras, auditoria interna prioriza:

- **Segregação de funções** — a mesma pessoa não deve iniciar, registrar e aprovar
- **Dependência de sistema** — o processo depende de parametrização correta do ERP?
- **Controles manuais sem evidência** — etapas executadas sem rastro auditável
- **Gaps de governança** — ausência de política, alçada ou procedimento formal
- **Riscos operacionais** — erros, fraudes, ineficiências que não necessariamente geram distorção em DF
- **Riscos de interface** — handoffs entre fornecedores, departamentos e clientes do processo (dimensão SIPOC)

## Output esperado por camada

| Camada | Artefato | Conteúdo |
|---|---|---|
| 1 — Classificação | Enquadramento APQC / E2E | Processo mapeado no PCF global; interfaces identificadas |
| 2 — SIPOC | Tabela SIPOC | S / I / P / O / C com fronteiras e critérios de eficácia |
| 3 — BPMN | Fluxograma BPMN 2.0 | Processo as-is com swimlanes por ator |
| Overlay | RCM | Processo → risco inerente → controle → avaliação → exposição residual |
| Execução | Programa de trabalho | Testes derivados dos gaps identificados no RCM |
| Conclusão | Achados | Observações formalizadas com critério, condição, causa e efeito |

## Red flags no mapeamento

- pular o SIPOC e ir direto para o BPMN — perde fronteiras e critérios de eficácia
- processo mapeado só por narrativa, sem fluxo visual — dificulta identificação de gaps
- swimlanes por fase em vez de por ator — oculta problemas de segregação
- mapa construído sem walkthrough real — risco de mapear o processo "como deveria ser" e não "como é"
- ausência de overlay de risco — mapa vira documentação sem valor de auditoria
- controles identificados sem evidência de operação — design e operação são questões separadas
- SIPOC construído sem entrevistar quem recebe o output (Customer) — critério de eficácia definido de forma incompleta

## Como construir o SIPOC na prática

### Passo a passo operacional

**Passo 1 — Definir o processo (P primeiro)**
Antes de qualquer entrevista, delimitar o processo pelo nome do E2E e pelas etapas macro. Evitar começar pelo Supplier ou Customer sem saber o que o processo faz.

Pergunta-chave: *"Quais são as 4–7 etapas principais deste processo, do início ao fim?"*

**Passo 2 — Identificar o Output**
O Output define o critério de eficácia. Sem ele, o auditor não sabe o que testar.

Perguntas-chave:
- *"O que este processo entrega ao final?"*
- *"Como vocês sabem que o processo funcionou?"*
- *"Existe um SLA, prazo ou padrão de qualidade para esse output?"*

**Passo 3 — Identificar o Customer**
Quem recebe e valida o output? Pode ser interno (outro departamento) ou externo (cliente, regulador, banco).

Perguntas-chave:
- *"Quem usa o que esse processo entrega?"*
- *"Quem reclama quando algo sai errado?"*

**Passo 4 — Identificar os Inputs**
Quais dados, documentos ou recursos precisam existir para o processo começar?

Perguntas-chave:
- *"O que precisa chegar aqui para vocês conseguirem executar?"*
- *"Já aconteceu de o processo travar por falta de informação? O quê?"*

**Passo 5 — Identificar os Suppliers**
Quem fornece cada input? Um input sem supplier identificado é um risco de interface não mapeado.

**Passo 6 — Validar fronteiras**
Confirmar onde o processo começa (primeiro input recebido) e onde termina (output entregue ao customer). Tudo fora dessas fronteiras é escopo de outro processo.

---

### Exemplo operacional — P2P (Procure to Pay)

| Dimensão | Conteúdo |
|---|---|
| **Supplier** | Solicitante (área requisitante), fornecedor homologado, jurídico (contrato) |
| **Input** | Requisição de compra aprovada, cotações, contrato assinado, nota fiscal do fornecedor |
| **Process** | Requisição → aprovação de compra → emissão de PO → recebimento de mercadoria/serviço → matching NF×PO×recebimento → pagamento |
| **Output** | Pagamento realizado dentro do prazo, com evidência de recebimento e matching aprovado |
| **Customer** | Fornecedor (recebe pagamento), área requisitante (recebe bem/serviço), contabilidade (registra a obrigação) |

**Fronteira de início:** requisição de compra aprovada pelo gestor da área  
**Fronteira de fim:** débito na conta bancária confirmado e baixa do contas a pagar no ERP

**Critério de eficácia derivado do Output:** pagamento correto (valor, fornecedor, conta), no prazo (SLA contratual), com evidência de recebimento (três vias do matching)

---

### Perguntas de ouro para o walkthrough

| Momento | Pergunta |
|---|---|
| Início | *"Me mostra um exemplo real — pega um caso que aconteceu semana passada"* |
| Cada etapa | *"Quem faz isso? No sistema ou fora dele? O que fica registrado?"* |
| Cada decisão | *"O que acontece se der errado aqui? Quem percebe?"* |
| Supplier | *"Já veio errado? O que você faz quando chega incompleto?"* |
| Output | *"Como você sabe que terminou? Alguém confirma?"* |
| Customer | *"Eles já reclamaram? Por quê?"* |

---

### Armadilhas frequentes no SIPOC

| Armadilha | Consequência | Correção |
|---|---|---|
| Definir Output sem perguntar ao Customer | Critério de eficácia definido pelo auditor, não pela operação | Entrevistar quem recebe o output antes de fechar o SIPOC |
| Supplier genérico ("o sistema") | Risco de interface não rastreável | Identificar a área ou pessoa que alimenta o sistema |
| Input sem dono | Ninguém responde quando o input chega errado | Mapear supplier para cada input |
| Processo com mais de 8 etapas macro | SIPOC virou BPMN — perdeu a visão de fronteira | Agregar etapas; detalhe vai para Camada 3 |
| Começar pelo BPMN sem SIPOC | Processo mapeado sem critério de eficácia | Bloquear Camada 3 até ter Output e Customer confirmados |

## Artefatos relacionados

- `concepts/scot-and-wcgw-foundations.md` — base conceitual de SCOT e WCGW (auditoria externa)
- `concepts/control-types-and-reliance.md` — classificação de controles
- `concepts/risk-scoring-foundations.md` — RI, RR e heat map
- `skills/process-flow-bpmn.md` — geração de BPMN 2.0 a partir de narrativa de processo
- `skills/wcgw-mapping.md` — identificação de WCGWs por processo
