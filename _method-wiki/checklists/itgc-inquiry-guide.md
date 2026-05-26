# ITGC Inquiry Guide

## Papel

Checklist curto para conduzir entrevistas de entendimento de ITGC com foco em acesso, mudanças, segurança e rotinas automatizadas.

## Quando usar

- kickoff de entendimento de TI
- atualização anual de walkthrough de ITGC
- preparação para entrevista com supervisor de TI, help desk, key user ou dono de sistema

## Blocos de pergunta

### 1. Ambiente e sistemas

- quais sistemas relevantes suportam o processo financeiro?
- existe mais de um ERP ou sistemas satélite relevantes?
- há soluções terceiras para compras, vendas, qualidade, planejamento ou folha?

### 2. Gestão de acessos

- como nasce o pedido de novo acesso?
- quem aprova acesso inicial e acesso adicional?
- quem executa bloqueio de desligados?
- há revisão periódica de acessos e privilégios?

### 3. Mudanças de fornecedor

- como a entidade toma conhecimento das atualizações?
- como distingue atualizações mandatórias e opcionais?
- quem decide implementar?
- há teste em base espelho e aval do usuário?

### 4. Mudanças programadas pela entidade

- o que inicia a mudança ou parametrização?
- quem pode alterar rotina ou regra?
- como a entidade testa compatibilidade e funcionamento?
- quem aprova antes da produção?

### 5. Segurança e autenticação

- quais requisitos mínimos de senha existem?
- há VPN ou autenticação adicional para acesso remoto?
- como a entidade decide as configurações de segurança?
- existe política de "acceptable use" formalizada e comunicada a todos os usuários do sistema?
- a política é monitorada e aplicada — há consequência documentada por descumprimento?
- quando foi realizado o último teste de penetração nas redes relevantes? por quem? quais foram os resultados e ações tomadas?

### 6. Jobs e rotinas automatizadas

- que rotinas automáticas são relevantes?
- quem agenda e monitora?
- como as falhas são tratadas?

## Sinais de atenção

- respostas genéricas demais, sem exemplo concreto
- dependência de uma pessoa só para explicar tudo
- ausência de revisão periódica de acesso
- teste em produção ou sem ambiente espelho
- incapacidade de explicar falha de job ou processo de correção

## Inspeção por Domínio

Após o inquiry, inspecionar evidência física para cada domínio. Inquiry sem inspeção não constitui teste — é apenas entendimento.

### Gestão de Acessos — O que inspecionar

| O que examinar | Evidência esperada | Critério de falha |
|---|---|---|
| Matriz usuário × perfil do ERP | Extração do período (validar IPE) | Usuários com perfis incompatíveis sem compensação |
| Log de provisionamento de acesso | Tickets ou aprovações de acesso concedido | Acesso concedido sem aprovação documentada |
| Log de offboarding | Registro de bloqueio por desligamento | Gap entre data de desligamento e data de bloqueio > 1 dia útil |
| Revisão periódica de acessos | Relatório de revisão assinado/aprovado | Revisão não realizada ou realizada sem evidência de análise crítica |
| Acessos privilegiados (admin/DBA) | Lista de superusuários + log de uso | Superusuário sem log ou com log não revisado |

**Amostra:** completude para conflitos críticos; N=23 a 90%/10% para log de transações de superusuário (se volume > 50).

### Change Management — O que inspecionar

| O que examinar | Evidência esperada | Critério de falha |
|---|---|---|
| Registro de mudanças no período | Log de change requests (tickets, JIRA, ServiceNow) | Mudanças sem ticket de solicitação formal |
| Aprovação antes do desenvolvimento | Aprovação documentada do responsável antes de codificar | Aprovação ausente ou datada após o desenvolvimento |
| Evidência de teste em ambiente não-produção | Plano de teste + evidência de execução + sign-off de usuário | Teste sem evidência ou teste realizado diretamente em produção |
| Aprovação para produção | Registro formal de autorização de deploy | Deploy sem aprovação documentada |
| Log de mudanças em produção | Histórico de deployments com data, responsável e versão | Ausência de log ou log sem responsável identificável |

**Amostra:** selecionar amostra de mudanças do período. N=23 a 90%/10% se > 50 mudanças; 100% se ≤ 20.

### Segurança e Autenticação — O que inspecionar

| O que examinar | Evidência esperada | Critério de falha |
|---|---|---|
| Configuração de política de senha no sistema | Screenshot ou exportação de parâmetros (complexidade, validade, bloqueio) | Parâmetros abaixo do mínimo da política da entidade |
| Contas inativas não bloqueadas | Lista de usuários com último login > 90 dias | Contas ativas sem uso recente sem justificativa |
| Configuração de MFA/VPN para acesso remoto | Tela de configuração ou relatório de autenticação | Acesso remoto sem segunda camada de autenticação |
| Log de tentativas de acesso bloqueadas | Relatório de lockout ou eventos de segurança | Ausência de log ou log não revisado |

**Nota:** configurações de sistema são 100% — não há amostragem para parâmetro de configuração. Ou está configurado corretamente ou não.

### Jobs e Rotinas Automatizadas — O que inspecionar

| O que examinar | Evidência esperada | Critério de falha |
|---|---|---|
| Agenda de jobs configurada | Lista de jobs agendados com horário, frequência e responsável | Job crítico sem agendamento formal ou sem responsável |
| Log de execução de jobs no período | Relatório de execução com status (sucesso/falha) | Falhas não tratadas ou não comunicadas |
| Evidência de tratamento de falhas | Tickets ou comunicações de tratamento de falha | Falha sem registro de investigação ou correção |
| Reconciliação de output de job crítico | Relatório gerado pelo job reconciliado com razão ou sistema-mestre | Output sem validação de completude e precisão |

**Amostra:** para log de jobs críticos, selecionar 1 mês completo do período. Para jobs de alta frequência (diário), N=23 a 90%/10% do período.

---

**Regra geral:** inquiry estabelece entendimento — inspeção estabelece evidência. Conclusão sobre efetividade exige os dois.

## Artefatos relacionados

- `processes/user-access-management.md`
- `processes/vendor-supplied-change-management.md`
- `processes/entity-programmed-changes.md`
- `processes/security-settings-and-authentication.md`
- `processes/job-scheduling-and-monitoring.md`
