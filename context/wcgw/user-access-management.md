---
processo: user-access-management
nivel: 1
abreviacao: UAM
subprocessos:
  - solicitacao-e-aprovacao
  - concessao-e-manutencao
  - revogacao-e-desligamento
  - revisao-periodica
  - acessos-privilegiados
assercoes_primarias:
  - existência
  - completude
frameworks:
  - COSO
  - SOX
  - COBIT
  - ISO 27001
referencias:
  - _method-wiki/processes/user-access-management.md
  - _method-wiki/processes/security-settings-and-authentication.md
---

# WCGW — User Access Management (UAM)

UAM é o controle que garante que **apenas as pessoas certas têm acesso aos sistemas certos, pelo tempo necessário**. É um ITGC pervasivo: falha aqui contamina todos os controles de processo que dependem de trilha de aprovação e segregação de funções.

O risco central não é acesso não autorizado externo — é acesso interno excessivo ou indevido que viabiliza fraude, erro sem detecção ou override de controles.

---

## Subprocesso 1: Solicitação e Aprovação de Acesso

Etapa onde o acesso é formalmente pedido e aprovado antes de ser concedido.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| UAM-001 | Acesso concedido sem solicitação formal documentada | Initiation | Existência | Alta |
| UAM-002 | Aprovação feita pelo próprio beneficiário do acesso | Initiation | Existência | Alta |
| UAM-003 | Aprovador não conhece o escopo do acesso que aprovou (acesso genérico ou de perfil copiado) | Initiation | Existência | Alta |
| UAM-004 | Solicitação informal (verbal, WhatsApp) sem registro | Initiation | Existência | Alta |
| UAM-005 | Ausência de análise de SoD na aprovação — acesso concedido cria conflito não detectado | Initiation | Existência | Alta |
| UAM-006 | Acesso temporário concedido sem data de expiração definida | Initiation | Existência | Média |

**Controles típicos que mitigam:**
- sistema de chamados (GLPI, ServiceNow, Jira) como único canal de solicitação
- aprovação obrigatória pelo gestor direto, não pelo próprio solicitante
- matriz de SoD consultada automaticamente antes de aprovar
- campo obrigatório de justificativa e prazo para acessos temporários
- evidência de aprovação armazenada junto ao chamado

---

## Subprocesso 2: Concessão e Manutenção

Etapa de execução técnica do acesso após aprovação e manutenção durante o ciclo de vida.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| UAM-007 | Acesso concedido por TI sem verificar aprovação prévia | Processing | Existência | Alta |
| UAM-008 | Perfil copiado de outro usuário sem revisão crítica — acesso excessivo herdado | Processing | Existência | Alta |
| UAM-009 | Acesso concedido além do solicitado — escopo ampliado sem justificativa | Processing | Existência | Alta |
| UAM-010 | Mesma equipe que executa o processo de negócio administra os acessos a ele | Processing | Existência | Alta |
| UAM-011 | Acesso concedido mas não registrado no sistema de controle — inventário desatualizado | Recording | Completude | Média |
| UAM-012 | Mudança de função sem atualização de acesso — acúmulo indevido ao longo do tempo | Processing | Existência | Alta |

**Controles típicos que mitigam:**
- TI verifica chamado aprovado antes de executar concessão
- proibição de cópia de perfil sem revisão campo a campo
- separação entre TI que administra acessos e as áreas de negócio que os usam
- inventário de acessos atualizado automaticamente pelo sistema (AD, ERP)
- processo de revisão de acesso quando há mudança de função (job change)

---

## Subprocesso 3: Revogação e Desligamento

Etapa crítica onde o acesso deve ser removido quando o usuário sai ou muda de função.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| UAM-013 | Acesso não bloqueado no dia do desligamento — ex-funcionário com acesso ativo | Processing | Existência | Alta |
| UAM-014 | Bloqueio parcial: acesso ao ERP removido mas e-mail, VPN ou pastas compartilhadas mantidos | Processing | Existência | Alta |
| UAM-015 | Desligamento não comunicado ao TI tempestivamente — dependência de processo manual | Initiation | Existência | Alta |
| UAM-016 | Conta bloqueada mas não desativada — reativação possível sem novo processo | Processing | Existência | Média |
| UAM-017 | Terceiros e prestadores sem processo de revogação definido — acessos persistem após contrato encerrado | Processing | Existência | Alta |
| UAM-018 | Mudança de função sem revogação do acesso anterior — usuário acumula perfis incompatíveis | Processing | Existência | Alta |

**Controles típicos que mitigam:**
- integração entre RH/DP e TI com trigger automático de bloqueio no desligamento
- checklist de desligamento cobrindo: ERP, AD, VPN, e-mail, pastas, sistemas satélites
- prazo máximo definido para bloqueio após comunicação de desligamento (ex: D+0 ou D+1)
- desativação completa (não só bloqueio) com prazo definido após bloqueio
- processo equivalente para terceiros e prestadores com vínculo ao prazo contratual

**Flag de risco elevado:** empresas sem integração RH ↔ TI dependem de processo manual — maior risco de revogação tardia, especialmente em desligamentos involuntários.

---

## Subprocesso 4: Revisão Periódica de Acessos

Mecanismo de detecção: mesmo que o processo de concessão e revogação falhe, a revisão periódica deve capturar acessos indevidos acumulados.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| UAM-019 | Revisão periódica não realizada — acessos nunca revisados sistematicamente | Processing | Existência | Alta |
| UAM-020 | Revisão realizada mas apenas confirmatória — gestor aprova tudo sem análise | Processing | Existência | Alta |
| UAM-021 | Revisão cobre só usuários ativos — ex-funcionários ou terceiros inativos não incluídos | Processing | Completude | Alta |
| UAM-022 | Acessos identificados como indevidos na revisão não são removidos tempestivamente | Processing | Existência | Alta |
| UAM-023 | Frequência da revisão inadequada ao nível de risco do sistema — revisão anual para sistema crítico | Processing | Existência | Média |
| UAM-024 | Revisão feita sobre lista desatualizada — não reflete acessos reais do sistema | Processing | Completude | Alta |

**Controles típicos que mitigam:**
- revisão periódica formal com evidência de que o gestor analisou e decidiu (não só assinou)
- frequência diferenciada por criticidade: sistemas SOX / críticos = trimestral ou semestral
- inclusão de usuários inativos, terceiros e contas de serviço na revisão
- prazo máximo para remoção de acessos identificados como indevidos
- extração direto do sistema (não relatório preparado pela gestão) como base da revisão

---

## Subprocesso 5: Acessos Privilegiados

Contas com poder irrestrito (administradores, super users, contas de serviço) representam risco concentrado — um único usuário pode comprometer todos os controles do sistema.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| UAM-025 | Contas de administrador usadas para atividades rotineiras — sem conta separada para admin | Processing | Existência | Alta |
| UAM-026 | Acesso privilegiado compartilhado entre múltiplos usuários — sem rastreabilidade individual | Processing | Existência | Alta |
| UAM-027 | Super user / conta de emergência sem log de uso monitorado | Processing | Existência | Alta |
| UAM-028 | Administradores de sistema com acesso irrestrito aos dados de negócio — risco de leitura/alteração sem trilha | Processing | Existência | Crítico |
| UAM-029 | Contas de serviço com senha compartilhada, sem rotação periódica | Processing | Existência | Alta |
| UAM-030 | Acesso privilegiado não incluído na revisão periódica — tratado como exceção permanente | Processing | Completude | Alta |

**Controles típicos que mitigam:**
- contas separadas para uso administrativo e uso diário (princípio do menor privilégio)
- log completo de ações de contas privilegiadas com revisão periódica
- contas de emergência com senha em cofre, liberação formal e log de uso
- rotação de senha de contas de serviço com frequência definida
- administradores de TI sem acesso de leitura a dados de negócio sensíveis
- inclusão obrigatória de contas privilegiadas na revisão periódica

**Flag de risco elevado:** ambiente SAP com usuário SAP_ALL ativo ou perfis de desenvolvedor em produção — acesso que permite qualquer ação sem restrição e sem log adequado.

---

## Leitura Rápida por Risco

| Risco Central | Subprocessos Críticos | WCGW-chave |
|---|---|---|
| Acesso sem aprovação formal | Solicitação | UAM-001, UAM-004 |
| Perfil copiado com acesso excessivo | Concessão | UAM-008, UAM-009 |
| Ex-funcionário com acesso ativo | Revogação | UAM-013, UAM-014 |
| Acúmulo de acessos por mudança de função | Concessão, Revogação | UAM-012, UAM-018 |
| Revisão periódica apenas formal | Revisão | UAM-020, UAM-024 |
| Conta privilegiada sem monitoramento | Privilegiados | UAM-026, UAM-027 |
| Terceiros sem revogação definida | Revogação | UAM-017 |
