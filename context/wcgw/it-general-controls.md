---
processo: it-general-controls
nivel: 1
abreviacao: ITGC
subprocessos:
  - change-management
  - desenvolvimento-e-implantacao
  - job-scheduling-e-batch-processing
  - interfaces-e-integracoes
  - backup-restore-e-recuperacao
  - incident-problem-management
  - infraestrutura-e-configuracoes
  - monitoramento-de-operacoes-ti
assercoes_primarias:
  - existência
  - completude
  - valoração
  - corte
  - apresentação
frameworks:
  - COSO
  - COBIT
  - ITIL
  - SOX
referencias:
  - _method-wiki/processes/entity-programmed-changes.md
  - _method-wiki/processes/job-scheduling-and-monitoring.md
  - _method-wiki/processes/vendor-supplied-change-management.md
  - _method-wiki/processes/security-settings-and-authentication.md
  - context/wcgw/user-access-management.md
---

# WCGW — IT General Controls Expanded (ITGC)

ITGCs sustentam a confiança nos sistemas que geram, processam e reportam informações financeiras e operacionais. UAM cobre quem acessa. Esta família cobre **como sistemas mudam**, **como processamentos rodam**, **como dados trafegam**, **como falhas são tratadas** e **se a operação de TI mantém integridade e disponibilidade suficientes**.

O risco central é confiar em relatório, workflow ou cálculo sistêmico sem saber se o ambiente que o produz é controlado. Quando ITGC falha, o auditor precisa reavaliar dependência em controles automatizados, IPEs, relatórios, interfaces e evidência extraída do sistema.

---

## Subprocesso 1: Change Management

Etapa de solicitação, aprovação, desenvolvimento, teste, homologação, transporte e implantação de mudanças em sistemas relevantes.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| ITGC-001 | Mudança em sistema financeiro implantada sem chamado ou solicitação formal | Initiation | Existência | Alta |
| ITGC-002 | Mudança aprovada pela mesma pessoa que desenvolveu ou transportou para produção | Processing | Existência | Alta |
| ITGC-003 | Mudança implantada sem evidência de teste funcional ou técnico | Processing | Existência | Alta |
| ITGC-004 | Homologação do usuário de negócio ausente para mudança que afeta processo financeiro | Processing | Existência | Alta |
| ITGC-005 | Mudança emergencial não revisada posteriormente | Processing | Existência | Alta |
| ITGC-006 | Log de transporte para produção não reconciliado com lista de mudanças aprovadas | Recording | Completude | Alta |
| ITGC-007 | Alteração em regra de cálculo, workflow ou relatório crítico não comunicada ao owner do controle | Processing | Completude | Alta |

**Controles típicos que mitigam:**
- workflow de mudança com solicitação, aprovação, teste, homologação e implantação
- segregação entre desenvolvedor, aprovador e transportador
- trilha de transporte para produção reconciliada com mudanças aprovadas
- revisão posterior de mudanças emergenciais
- owner de negócio aprovando mudanças que afetam controles ou relatórios críticos

**Flag de risco elevado:** mudança emergencial perto do fechamento contábil ou em módulo financeiro.

---

## Subprocesso 2: Desenvolvimento e Implantação

Etapa de desenho, construção, parametrização, customização, migração e go-live de sistemas ou funcionalidades novas.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| ITGC-008 | Requisito de controle interno não considerado no desenho do sistema | Initiation | Completude | Alta |
| ITGC-009 | Parametrização crítica migrada para produção sem revisão independente | Processing | Existência | Alta |
| ITGC-010 | Dados migrados de sistema legado sem reconciliação de completude e acurácia | Recording | Completude | Alta |
| ITGC-011 | Ambiente de teste usa dados ou configuração divergente de produção — teste não representa operação real | Processing | Valoração | Média |
| ITGC-012 | Go-live aprovado sem critérios formais de aceite e plano de rollback | Processing | Existência | Alta |
| ITGC-013 | Customização altera lógica padrão do ERP sem documentação técnica e funcional | Recording | Existência | Alta |

**Controles típicos que mitigam:**
- requisitos de controle incluídos no desenho funcional
- revisão independente de parametrizações críticas
- reconciliação de migração por quantidade, valor e amostra de registros
- critérios formais de go-live, rollback e estabilização
- documentação de customizações, owners e impactos em controle

**Armadilha comum:** tratar implantação como projeto de TI apenas. Se o sistema processa transações financeiras, o desenho de controles é parte do escopo.

---

## Subprocesso 3: Job Scheduling e Batch Processing

Etapa de agendamento, execução, monitoramento e reprocessamento de jobs, rotinas batch, integrações periódicas e processamentos automáticos.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| ITGC-014 | Job crítico falha e não gera alerta tempestivo ao responsável | Processing | Completude | Alta |
| ITGC-015 | Job de fechamento, faturamento, folha ou interface executa fora da sequência correta | Processing | Corte | Alta |
| ITGC-016 | Reprocessamento de job realizado manualmente sem aprovação ou evidência de causa | Processing | Existência | Alta |
| ITGC-017 | Parâmetro de execução de job alterado sem aprovação | Processing | Existência | Alta |
| ITGC-018 | Log de execução de jobs não retido ou não revisado | Recording | Completude | Média |
| ITGC-019 | Job cancelado ou pulado sem análise de impacto financeiro | Processing | Completude | Alta |

**Controles típicos que mitigam:**
- ferramenta de scheduler com alertas e responsáveis
- matriz de jobs críticos por sistema, frequência, dependência e owner
- revisão diária de falhas, cancelamentos e reprocessamentos
- aprovação para alteração de parâmetros e calendário de execução
- retenção de logs de execução com status e timestamp

**Flag de risco elevado:** job de interface ou fechamento falhando e sendo reprocessado por planilha ou ajuste manual.

---

## Subprocesso 4: Interfaces e Integrações

Etapa de transmissão, validação, reconciliação e monitoramento de dados entre sistemas, ERPs, bancos, portais, fiscal, folha e data warehouses.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| ITGC-020 | Interface envia transações incompletas sem alerta de rejeição | Processing | Completude | Alta |
| ITGC-021 | Dados alterados entre sistema origem e destino sem trilha de transformação | Processing | Valoração | Alta |
| ITGC-022 | Rejeições de interface tratadas manualmente sem aprovação independente | Processing | Existência | Alta |
| ITGC-023 | Reconciliação origem x destino não realizada para interface crítica | Reporting | Completude | Alta |
| ITGC-024 | Mapeamento de campos da interface desatualizado após mudança de sistema | Processing | Valoração | Alta |
| ITGC-025 | Arquivo de interface transmitido por canal inseguro ou alterável | Processing | Existência | Alta |

**Controles típicos que mitigam:**
- reconciliação de totais, quantidades e valores entre origem e destino
- log de rejeições com causa, tratamento e aprovação
- controles de hash, criptografia ou canal seguro
- documentação de mapeamento de campos e regras de transformação
- alertas automáticos para falha, rejeição ou processamento parcial

**Relação com processos de negócio:** P2P, OTC, H2R, Tax e Treasury frequentemente dependem de interfaces. Falha de interface pode virar erro transacional.

---

## Subprocesso 5: Backup, Restore e Recuperação

Etapa de cópia, retenção, proteção, teste de restauração e recuperação de sistemas/dados relevantes.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| ITGC-026 | Backup de sistema crítico não executado conforme política | Processing | Completude | Alta |
| ITGC-027 | Falha de backup não monitorada ou não corrigida tempestivamente | Processing | Existência | Alta |
| ITGC-028 | Restore não testado periodicamente — backup existe mas recuperabilidade não comprovada | Processing | Existência | Alta |
| ITGC-029 | Retenção de backup insuficiente para necessidade legal, operacional ou de auditoria | Recording | Completude | Média |
| ITGC-030 | Backup armazenado no mesmo ambiente exposto ao incidente principal | Processing | Existência | Alta |
| ITGC-031 | RTO/RPO definidos sem validação com áreas de negócio | Initiation | Completude | Média |

**Controles típicos que mitigam:**
- política de backup por criticidade de sistema
- monitoramento de sucesso/falha de backups
- teste periódico de restore com evidência
- retenção alinhada a requisitos legais e operacionais
- armazenamento segregado/offsite ou protegido contra ransomware
- RTO/RPO aprovados pelo negócio

**Armadilha crítica:** evidência de backup bem-sucedido não prova que o restore funciona.

---

## Subprocesso 6: Incident e Problem Management

Etapa de registro, triagem, priorização, resolução, escalonamento e análise de causa raiz de incidentes e problemas.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| ITGC-032 | Incidente em sistema financeiro não registrado em ferramenta oficial | Initiation | Completude | Alta |
| ITGC-033 | Incidente crítico resolvido sem análise de impacto em transações ou reporte financeiro | Processing | Completude | Alta |
| ITGC-034 | Correção aplicada diretamente em produção sem processo de mudança | Processing | Existência | Alta |
| ITGC-035 | Incidentes recorrentes tratados isoladamente sem análise de causa raiz | Processing | Existência | Média |
| ITGC-036 | SLA de resolução vencido sem escalonamento | Processing | Existência | Média |
| ITGC-037 | Comunicação ao negócio ausente para incidente que afeta controles, relatórios ou fechamento | Reporting | Completude | Alta |

**Controles típicos que mitigam:**
- ferramenta central de incidentes com prioridade, owner e status
- critérios de impacto financeiro/contábil para incidentes críticos
- ligação entre incident, problem e change management
- análise de causa raiz para recorrência
- comunicação formal a owners de processo quando controles ou reports forem afetados

**Flag de risco elevado:** "correção rápida em produção" fora do fluxo de change.

---

## Subprocesso 7: Infraestrutura e Configurações

Etapa de configuração de servidores, bancos de dados, ambientes, parâmetros técnicos, patching, hardening e monitoramento de infraestrutura.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| ITGC-038 | Patch crítico de segurança não aplicado em servidor ou banco que suporta sistema financeiro | Processing | Existência | Alta |
| ITGC-039 | Configuração de banco de dados permite alteração direta de transações sem passar pela aplicação | Processing | Existência | Alta |
| ITGC-040 | Ambientes de desenvolvimento, teste e produção não segregados adequadamente | Processing | Existência | Alta |
| ITGC-041 | Parâmetro técnico relevante alterado sem registro ou aprovação | Processing | Existência | Alta |
| ITGC-042 | Monitoramento de capacidade indisponível — risco de queda ou perda de processamento não antecipado | Processing | Completude | Média |
| ITGC-043 | Logs técnicos críticos não retidos pelo período necessário para investigação | Recording | Completude | Média |

**Controles típicos que mitigam:**
- gestão de patches por criticidade
- segregação de ambientes e restrição de acesso direto a banco
- baseline de configuração e hardening
- change management para parâmetros técnicos relevantes
- monitoramento de capacidade e disponibilidade
- retenção de logs alinhada a investigação e auditoria

**Relação com UAM:** acesso privilegiado à infraestrutura deve ser avaliado junto com `user-access-management.md`.

---

## Subprocesso 8: Monitoramento de Operações de TI

Etapa de supervisão contínua de disponibilidade, logs, alertas, eventos de segurança, capacidade e indicadores operacionais.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| ITGC-044 | Sistema crítico sem monitoramento de disponibilidade ou alerta de indisponibilidade | Processing | Completude | Alta |
| ITGC-045 | Alertas críticos fechados sem evidência de investigação | Processing | Existência | Alta |
| ITGC-046 | Logs de segurança ou operação não revisados para sistemas sensíveis | Processing | Existência | Alta |
| ITGC-047 | Evento de segurança com potencial impacto financeiro não comunicado a donos de processo | Reporting | Completude | Alta |
| ITGC-048 | Dashboard de monitoramento mostra status agregado sem detalhar sistema, severidade e owner | Reporting | Apresentação | Média |

**Controles típicos que mitigam:**
- monitoramento 24/7 ou conforme criticidade
- matriz de alertas críticos e responsáveis
- revisão periódica de logs relevantes
- protocolo de escalonamento para eventos com impacto financeiro
- dashboard com sistema, severidade, owner, status e tempo aberto

---

## Leitura Rápida por Risco

| Risco Central | Subprocessos Críticos | WCGW-chave |
|---|---|---|
| Mudança não autorizada em sistema financeiro | Change Management | ITGC-001, ITGC-002, ITGC-006 |
| Mudança sem teste ou homologação | Change Management | ITGC-003, ITGC-004, ITGC-005 |
| Migração ou go-live com dados incorretos | Desenvolvimento | ITGC-010, ITGC-012 |
| Job crítico falha sem alerta | Jobs | ITGC-014, ITGC-019 |
| Interface incompleta ou alterada | Interfaces | ITGC-020, ITGC-021, ITGC-023 |
| Backup existe mas não recupera | Backup/Restore | ITGC-026, ITGC-028, ITGC-030 |
| Incidente afeta financeiro sem análise | Incident Management | ITGC-033, ITGC-037 |
| Acesso direto a banco contorna aplicação | Infraestrutura | ITGC-039, ITGC-040 |
| Logs e alertas não revisados | Monitoramento | ITGC-045, ITGC-046, ITGC-047 |
