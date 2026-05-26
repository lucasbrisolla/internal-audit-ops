---
processo: entity-level-controls
nivel: 1
abreviacao: ELC
subprocessos:
  - ambiente-de-controle
  - governanca-e-monitoramento
  - canal-de-denuncia
  - disciplina-de-fechamento
assercoes_primarias:
  - existência
  - completude
frameworks:
  - COSO ICIF
  - SOX
  - IPPF IIA
referencias:
  - _method-wiki/processes/entity-level-controls.md
  - _method-wiki/concepts/sox-and-icfr-foundations.md
  - _method-wiki/processes/fraud-risk-assessment.md
---

# WCGW — Entity-Level Controls (ELC)

ELCs são **pervasivos**: não mitigam um risco transacional específico — moldam o ambiente em que todos os outros controles operam. Um ELC fraco não gera achado isolado; ele amplifica o risco de falha em toda a organização.

O auditor que ignora ELCs e vai direto para testes de controle de processo perde o contexto que determina quão confiáveis esses controles realmente são.

---

## Subprocesso 1: Ambiente de Controle

Tom da liderança, valores, responsabilidades e estrutura que definem se controles são levados a sério.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| ELC-001 | Código de conduta inexistente ou não comunicado — funcionários sem referência formal de comportamento ético | Initiation | Existência | Alta |
| ELC-002 | Código de conduta existe mas não é assinado ou reconhecido formalmente pelos funcionários | Initiation | Existência | Média |
| ELC-003 | Liderança demonstra comportamento inconsistente com o código de conduta — tone at top deficiente | Processing | Existência | Alta |
| ELC-004 | Responsabilidades de controle interno não formalizadas — não há dono claro de cada controle | Initiation | Existência | Alta |
| ELC-005 | Política de controles internos desatualizada ou inexistente | Initiation | Existência | Média |
| ELC-006 | Comitê de Auditoria inexistente ou inativo — sem oversight independente sobre reporte financeiro | Processing | Existência | Alta |
| ELC-007 | Alta concentração de poder em um único executivo sem mecanismo de contrabalanceamento | Processing | Existência | Alta |

**Controles típicos que mitigam:**
- código de conduta com assinatura anual de todos os funcionários
- treinamentos periódicos de ética e compliance com registro de participação
- Comitê de Auditoria ativo com reuniões documentadas e pauta substantiva
- política de controles internos revisada periodicamente com aprovação da diretoria
- separação clara de responsabilidades entre CEO, CFO e Controller

**Flag de risco elevado:** empresa familiar com concentração de controle — maior probabilidade de que tone at top seja informal e override seja normalizado.

---

## Subprocesso 2: Governança e Monitoramento

Mecanismos que detectam e corrigem falhas de controle ao longo do tempo.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| ELC-008 | Ausência de função de auditoria interna ou função equivalente — sem assurance independente | Processing | Existência | Alta |
| ELC-009 | Auditoria interna existe mas sem independência real — reporta a quem é auditado | Processing | Existência | Alta |
| ELC-010 | Função de compliance sem acesso a informações necessárias para monitoramento efetivo | Processing | Existência | Alta |
| ELC-011 | Plano de auditoria interna não cobre áreas de maior risco — cobertura inadequada | Processing | Completude | Alta |
| ELC-012 | Achados de auditoria anteriores não monitorados — planos de ação sem acompanhamento | Reporting | Completude | Alta |
| ELC-013 | Risk assessment corporativo não atualizado — riscos novos não identificados formalmente | Initiation | Completude | Alta |
| ELC-014 | Ausência de interação formal entre auditoria interna, compliance e Comitê de Auditoria | Processing | Existência | Média |

**Controles típicos que mitigam:**
- função de auditoria interna reportando ao Comitê de Auditoria (não ao CFO)
- plano anual de auditoria aprovado pelo Comitê com cobertura baseada em risco
- sistema de monitoramento de planos de ação com status e responsável
- risk assessment corporativo revisado ao menos anualmente
- reuniões periódicas entre auditoria interna, compliance e Comitê de Auditoria com ata

---

## Subprocesso 3: Canal de Denúncia

Mecanismo que permite identificar fraude, irregularidade ou comportamento antiético de forma independente.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| ELC-015 | Canal de denúncia inexistente — única via é reportar ao gestor direto | Initiation | Existência | Alta |
| ELC-016 | Canal existe mas não garante anonimato — denunciante exposto a retaliação | Initiation | Existência | Alta |
| ELC-017 | Denúncias recebidas mas não investigadas formalmente — sem processo de triagem e resposta | Processing | Existência | Alta |
| ELC-018 | Canal gerido pela própria área que pode ser objeto de denúncia — conflito de interesse | Processing | Existência | Alta |
| ELC-019 | Baixo volume de denúncias interpretado como ausência de problemas — sem análise de causa | Reporting | Completude | Média |
| ELC-020 | Denunciantes históricos sofreram consequências — cultura de retaliação inibe uso do canal | Processing | Existência | Alta |
| ELC-021 | Canal não divulgado adequadamente — funcionários desconhecem existência ou forma de uso | Initiation | Existência | Média |

**Controles típicos que mitigam:**
- canal operado por terceiro independente com garantia de anonimato
- política formal de não-retaliação com comunicação ativa
- processo documentado de triagem, investigação e resposta a denúncias
- Comitê de Auditoria como destinatário final de denúncias sobre a gestão
- relatório periódico de denúncias ao Comitê (volume, natureza, status)
- comunicação ativa do canal em admissões, treinamentos e canais internos

**Flag de risco elevado:** volume de denúncias muito baixo para o tamanho da empresa — pode indicar cultura de silêncio ou desconhecimento do canal, não ausência de problemas.

---

## Subprocesso 4: Disciplina de Fechamento Contábil

Estrutura que garante confiabilidade, completude e corte adequado do reporte financeiro.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| ELC-022 | Fechamento sem cronograma formal — datas, donos e entregas não definidos | Initiation | Existência | Alta |
| ELC-023 | Política contábil desatualizada — equipe aplica critérios divergentes entre períodos | Initiation | Valoração | Alta |
| ELC-024 | Estimativas e provisões sem metodologia documentada — julgamento sem âncora formal | Processing | Valoração | Alta |
| ELC-025 | Revisão do CFO ou Controller sobre demonstrações não documentada — controle existe mas sem evidência | Processing | Existência | Média |
| ELC-026 | Ausência de checklist de fechamento — etapas críticas dependem de memória individual | Processing | Completude | Média |
| ELC-027 | Ajustes de fechamento aprovados sem revisão independente — preparador = aprovador | Processing | Existência | Alta |
| ELC-028 | Demonstrações financeiras finalizadas sem comparação analítica formal com períodos anteriores | Reporting | Valoração | Média |

**Controles típicos que mitigam:**
- cronograma de fechamento com datas, responsáveis e dependências por etapa
- política contábil aprovada pela diretoria e revisada anualmente
- metodologia documentada para cada estimativa significativa (impairment, provisões, IFRS 16)
- checklist de fechamento com evidência de conclusão por etapa
- revisão analítica formal pelo CFO/Controller com documentação de conclusões
- segregação entre quem prepara e quem aprova ajustes de fechamento relevantes

---

## Leitura Rápida por Risco

| Risco Central | Subprocessos Críticos | WCGW-chave |
|---|---|---|
| Tone at top deficiente | Ambiente de controle | ELC-003, ELC-007 |
| Sem oversight independente | Governança | ELC-006, ELC-008, ELC-009 |
| Achados anteriores sem follow-up | Governança | ELC-012 |
| Canal de denúncia inefetivo | Canal de denúncia | ELC-016, ELC-017, ELC-020 |
| Fechamento sem disciplina formal | Disciplina de fechamento | ELC-022, ELC-024, ELC-027 |
| Estimativas sem metodologia | Disciplina de fechamento | ELC-024 |
