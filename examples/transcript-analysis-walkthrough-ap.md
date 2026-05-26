# Exemplo — Transcript Analysis: Walkthrough Compras e Contas a Pagar

**Tipo de input:** notas brutas de walkthrough — processo de Compras e AP em grupo de grande porte  
**Contexto:** cliente com ERP integrado, multiplas entidades, area corporativa e unidades operacionais  
**Trilha metodologica:** auditoria interna  
**Workflow aplicado:** `transcript-analysis` → alimenta `walkthrough-standardization` e `risk-control-mapping`

---

## Input bruto (notas de campo)

```
Contas a Pagar
- Recebe a solicitação
- Calcula data de pagamento no sistema e associa
- Gera arquivo remessa via plataforma de VAN bancária
- Recebe retorno do banco, trata rejeições e reenvia remessa

Compras
- Área demandante mapeia necessidade de mercadorias e serviços
- Analistas cadastram requisição no sistema
- Verifica disponibilidade de verba para o centro de custo
- Aprovação do gestor responsável pelo centro de custo
- Inicia processo de concorrência e portal do fornecedor
- Fornecedor insere cotação no próprio portal

Observações adicionais:
- Migração de onda recente do sistema (Go-Live)
- Requisitante do corporativo entra no ERP; orçamento gerido em sistema de planejamento separado
- Chamado via ferramenta de gestão de chamados para unidades fora do corporativo
- Item precisa estar cadastrado + combinação de centro de custo × conta disponível
- Workflow definido no sistema determina aprovações
- Responsável: departamentos de suprimento, orçamentária e gestão de workflow

Compras com valor alto:
- Não começa pela requisição no ERP — começa via chamado na ferramenta de gestão
- Ex: negociação de contrato de prestação de serviço de grande porte
- Va para mesa de suprimentos (negociações) — categorias separadas por tipo

Pré-negociado no ERP:
- Quando fornecedor é selecionado automaticamente, negociação foi feita de forma prévia
- Mesa de suprimento por categoria

Premissa crítica:
- PROCESSO PARTE DA PREMISSA DE QUE TODOS FORNECEDORES ESTEJAM CADASTRADOS
- Sistema de certificação para cadastro: valida CNPJ, conflito de interesse,
  base de funcionários, riscos e compliance
```

---

## Output do transcript-analysis

### 1. Leitura rápida

Walkthrough de Compras e AP em grupo corporativo com ERP integrado e migração recente. Processo divide-se em dois fluxos: (1) compras padrão via requisição no ERP e (2) compras de alto valor via chamado + negociação. AP opera separado, conectado ao final do ciclo de compras.

---

### 2. Processo extraído

**Fluxo 1 — Compras padrão (via ERP)**

| Etapa | Ator | Sistema | Controle identificado |
|---|---|---|---|
| Identificação de necessidade | Área demandante | — | — |
| Cadastro da requisição | Analista de suprimentos | ERP | Verificação de verba disponível (centro de custo × conta) |
| Aprovação da requisição | Gestor do centro de custo | ERP | Workflow de aprovação no sistema |
| Processo de concorrência | Suprimentos | Portal do fornecedor | Cotação inserida pelo próprio fornecedor |
| Negociação e seleção | Mesa de suprimentos | ERP | Pré-negociação embute controle de preço |

**Fluxo 2 — Compras de alto valor (via chamado)**

| Etapa | Ator | Sistema | Controle identificado |
|---|---|---|---|
| Abertura de chamado | Área demandante | Ferramenta de chamados | — |
| Negociação de contrato | Mesa de suprimentos (por categoria) | ERP / externo | Negociação antes da entrada no ERP |
| Aprovação e formalização | Suprimentos + gestor | ERP | Workflow pós-negociação |

**Contas a Pagar (downstream de ambos os fluxos)**

| Etapa | Ator | Sistema | Controle identificado |
|---|---|---|---|
| Recebimento da solicitação | AP | ERP | — |
| Cálculo de data de pagamento | AP | ERP | Parametrização de prazo no sistema |
| Geração de remessa | AP | Plataforma VAN bancária | Geração automática de arquivo |
| Tratamento de rejeições e reenvio | AP | Plataforma VAN bancária | — |

---

### 3. Controles identificados

| Controle | Tipo | Posição | Observação |
|---|---|---|---|
| Verificação de verba disponível por centro de custo | Preventivo / Automatizado | Antes da requisição | Depende de parametrização correta do orçamento no sistema de planejamento |
| Workflow de aprovação do gestor | Preventivo / Automatizado | Requisição → compra | Depende de configuração de alçadas no ERP |
| Cadastro de fornecedor com validação de compliance | Preventivo / Manual + Automatizado | Antes de qualquer compra | Premissa do processo: sem cadastro, sem compra |
| Cotação inserida pelo próprio fornecedor | Preventivo / Automatizado | Concorrência | Reduz risco de adulteração interna de cotação |

---

### 4. Sinais de risco identificados

| Risco | Evidência nas notas |
|---|---|
| Migração recente de ERP — controles não validados pós-Go-Live | "Houve migração de onda recente" |
| Orçamento em sistema separado — risco de dessincronia com ERP | "Orçamento gerido em sistema de planejamento separado" |
| Compras de alto valor iniciam fora do ERP — sem trilha desde o início | "Não começa pela requisição no ERP — começa via chamado" |
| Processo depende de 100% dos fornecedores cadastrados | "PARTE DA PREMISSA DE QUE TODOS FORNECEDORES ESTEJAM CADASTRADOS" |
| Segregação entre quem negocia e quem aprova não explicitada | Não mencionada — lacuna |

---

### 5. Lacunas e pontos a confirmar

- [ ] Como é feita a integração sistema de planejamento → ERP? Quem atualiza o orçamento e com qual frequência?
- [ ] Quem são os aprovadores com poderes no sistema? Houve mudanças com o Go-Live?
- [ ] Critério formal para definir Fluxo 1 vs. Fluxo 2 — existe valor mínimo documentado?
- [ ] Certificação de fornecedores ocorre antes ou pode ocorrer em paralelo à requisição?
- [ ] Existem exceções ao processo de concorrência? Como são tratadas compras diretas?
- [ ] Quem revisa e aprova rejeições de remessa antes do reenvio ao banco?

---

### 6. Próximo uso recomendado

1. **`walkthrough-standardization`** — converter notas brutas em walkthrough interno com mapa de atividades por responsavel, sistemas, handoffs e controles.
2. **`risk-control-mapping`** — mapear riscos e controles de integracao orcamento x ERP, segregacao de funcoes, fornecedores nao cadastrados e compras iniciadas fora do ERP.
3. **`test-execution`** — desenhar testes dos controles de aprovacao, cadastro de fornecedor e tratamento de rejeicoes de remessa.
