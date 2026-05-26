---
processo: esg-environment-health-safety
nivel: 1
abreviacao: ESG
subprocessos:
  - licencas-e-condicionantes-ambientais
  - residuos-e-materiais-perigosos
  - emissoes-agua-e-energia
  - saude-e-seguranca-ocupacional
  - incidentes-acidentes-e-remediacao
  - terceiros-operacoes-e-cadeia
  - contingencias-multas-e-provisoes
  - metricas-esg-e-reporte
assercoes_primarias:
  - existência
  - completude
  - valoração
  - corte
  - apresentação
frameworks:
  - COSO
  - GRI
  - SASB
  - IFRS S1
  - IFRS S2
  - ISO 14001
  - ISO 45001
referencias:
  - context/wcgw/legal-compliance-third-parties.md
  - context/wcgw/record-to-report.md
  - context/wcgw/fraud-risk-assessment.md
  - context/wcgw/it-general-controls.md
---

# WCGW — ESG, Environment, Health & Safety (ESG)

ESG/EHS cobre riscos ambientais, saúde e segurança ocupacional, obrigações regulatórias, incidentes, contingências e métricas reportadas ao mercado ou à gestão. Para auditoria interna, a pergunta central não é apenas "a empresa tem uma política ESG?", mas se os dados, controles e evidências sustentam o que ela opera e reporta.

O risco é duplo: falha operacional real (licença vencida, acidente, resíduo mal destinado, emissão não monitorada) e falha de reporte (indicador ESG incompleto, inflado, inconsistente ou sem rastreabilidade).

---

## Subprocesso 1: Licenças e Condicionantes Ambientais

Etapa de obtenção, renovação, monitoramento e cumprimento de licenças, autorizações, condicionantes e permissões ambientais.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| ESG-001 | Operação executada com licença ambiental vencida, ausente ou não aplicável ao escopo real | Initiation | Existência | Alta |
| ESG-002 | Condicionantes ambientais da licença não monitoradas em tracker central | Processing | Completude | Alta |
| ESG-003 | Evidência de cumprimento de condicionante não arquivada ou não rastreável | Recording | Existência | Alta |
| ESG-004 | Mudança operacional relevante realizada sem reavaliar licença ou autorização necessária | Processing | Existência | Alta |
| ESG-005 | Prazo de renovação de licença perdido ou iniciado tarde demais | Processing | Completude | Alta |
| ESG-006 | Licença de unidade, filial ou atividade terceirizada fora do inventário regulatório | Initiation | Completude | Alta |

**Controles típicos que mitigam:**
- inventário de licenças por unidade, atividade, prazo, órgão e responsável
- tracker de condicionantes com evidências e datas
- alertas antecipados para renovação
- revisão legal/ambiental antes de mudança operacional
- reporte periódico de status de licenças à gestão

**Flag de risco elevado:** operação em expansão, mudança de capacidade produtiva ou nova unidade antes de revisão ambiental.

---

## Subprocesso 2: Resíduos e Materiais Perigosos

Etapa de geração, segregação, armazenamento, transporte, destinação, manifesto e rastreabilidade de resíduos, produtos perigosos e materiais controlados.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| ESG-007 | Resíduo perigoso classificado incorretamente como comum | Initiation | Apresentação | Alta |
| ESG-008 | Manifesto ou certificado de destinação final ausente para resíduo relevante | Recording | Completude | Alta |
| ESG-009 | Terceiro destinatário de resíduo sem licença válida ou não homologado | Processing | Existência | Alta |
| ESG-010 | Volume de resíduo destinado divergente do volume gerado/armazenado | Processing | Valoração | Alta |
| ESG-011 | Armazenamento temporário de resíduo fora de condição legal ou de segurança | Processing | Existência | Alta |
| ESG-012 | Produto químico ou material perigoso sem inventário, FISPQ ou controle de acesso | Processing | Completude | Média |

**Controles típicos que mitigam:**
- classificação formal de resíduos e materiais perigosos
- inventário de resíduos gerados, armazenados, transportados e destinados
- homologação e revalidação de transportadores/destinadores
- reconciliação entre geração, manifesto, nota fiscal e certificado de destinação
- inspeção periódica de áreas de armazenamento

**Relação com terceiros:** destinação ambiental terceirizada não transfere integralmente o risco reputacional/regulatório da empresa.

---

## Subprocesso 3: Emissões, Água e Energia

Etapa de medição, cálculo, monitoramento e reporte de emissões, consumo de água, energia, efluentes e indicadores ambientais.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| ESG-013 | Fonte relevante de emissão, água ou energia excluída do inventário | Initiation | Completude | Alta |
| ESG-014 | Medidor, sensor ou fonte de dado ambiental sem calibração ou validação | Processing | Valoração | Alta |
| ESG-015 | Fator de emissão aplicado incorretamente ou desatualizado | Processing | Valoração | Alta |
| ESG-016 | Efluente ou emissão acima do limite legal sem registro de exceção e ação corretiva | Processing | Existência | Alta |
| ESG-017 | Dados ambientais consolidados manualmente sem reconciliação com fonte primária | Reporting | Completude | Média |
| ESG-018 | Redução de emissão ou consumo reportada sem baseline consistente | Reporting | Apresentação | Média |

**Controles típicos que mitigam:**
- inventário de fontes ambientais por unidade e escopo
- calibração periódica de medidores e sensores
- metodologia documentada para cálculo de emissões e consumos
- revisão de fatores de emissão e limites regulatórios
- reconciliação de dados operacionais, medidores, notas e reportes ESG

**Flag de risco elevado:** indicador ambiental usado em meta pública ou remuneração variável.

---

## Subprocesso 4: Saúde e Segurança Ocupacional

Etapa de gestão de riscos ocupacionais, EPIs, treinamentos, permissões de trabalho, exames, inspeções e controles de segurança.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| ESG-019 | Atividade crítica executada sem permissão de trabalho ou análise preliminar de risco | Initiation | Existência | Alta |
| ESG-020 | Funcionário ou terceiro executa atividade sem treinamento obrigatório válido | Processing | Existência | Alta |
| ESG-021 | EPI obrigatório não fornecido, não utilizado ou sem evidência de entrega | Processing | Existência | Alta |
| ESG-022 | Exame ocupacional obrigatório vencido ou ausente para função de risco | Processing | Completude | Média |
| ESG-023 | Inspeções de segurança não realizadas ou achados não acompanhados | Processing | Completude | Alta |
| ESG-024 | Indicadores de segurança manipulados por subnotificação de incidentes ou quase acidentes | Reporting | Completude | Alta |

**Controles típicos que mitigam:**
- matriz de treinamentos por função e risco
- controle de permissão de trabalho para atividades críticas
- registro de entrega, uso e troca de EPI
- calendário de exames ocupacionais
- inspeções periódicas com plano de ação
- cultura de reporte de quase acidentes sem punição indevida

**Armadilha crítica:** taxa de acidente baixa pode indicar bom controle ou subnotificação. O auditor precisa olhar canais de reporte, quase acidentes e cultura.

---

## Subprocesso 5: Incidentes, Acidentes e Remediação

Etapa de registro, investigação, comunicação, resposta emergencial, remediação e aprendizagem de incidentes ambientais ou de segurança.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| ESG-025 | Incidente ambiental ou de segurança não registrado no sistema oficial | Initiation | Completude | Alta |
| ESG-026 | Comunicação obrigatória a órgão regulador ou autoridade não realizada tempestivamente | Reporting | Completude | Alta |
| ESG-027 | Investigação de acidente conduzida sem independência ou sem análise de causa raiz | Processing | Existência | Alta |
| ESG-028 | Ação corretiva definida mas não implementada ou não testada | Reporting | Completude | Alta |
| ESG-029 | Evidência de remediação ambiental não suportada por laudo, medição ou validação técnica | Recording | Existência | Alta |
| ESG-030 | Incidentes recorrentes tratados isoladamente sem ação sistêmica | Processing | Existência | Média |

**Controles típicos que mitigam:**
- sistema central de incidentes e quase acidentes
- protocolo de comunicação regulatória
- investigação com causa raiz e equipe independente quando necessário
- plano de ação com owner, prazo e evidência de fechamento
- validação técnica da remediação

**Flag de risco elevado:** incidente fechado como "erro humano" sem avaliar desenho de processo, treinamento, supervisão ou equipamento.

---

## Subprocesso 6: Terceiros, Operações e Cadeia

Etapa de gestão de terceiros críticos para ESG/EHS: transportadores, operadores logísticos, manutenção, mineração, construção, limpeza industrial, destinação de resíduos e fornecedores de alto impacto.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| ESG-031 | Terceiro executa atividade ambiental ou de segurança crítica sem homologação EHS | Initiation | Existência | Alta |
| ESG-032 | Requisito EHS não incluído no contrato ou escopo do terceiro | Initiation | Completude | Alta |
| ESG-033 | Documentação obrigatória de terceiro (licença, treinamento, ASO, seguro) vencida ou ausente | Processing | Completude | Alta |
| ESG-034 | Incidente envolvendo terceiro não incluído nos indicadores e análises de segurança | Reporting | Completude | Alta |
| ESG-035 | Auditoria ou inspeção de terceiro crítico não realizada conforme plano | Processing | Existência | Média |

**Controles típicos que mitigam:**
- due diligence EHS para terceiros críticos
- cláusulas contratuais de segurança, ambiente, reporte e direito de auditoria
- controle documental antes de acesso à operação
- inclusão de terceiros em indicadores e investigações
- inspeções e auditorias periódicas de terceiros

**Relação com LCT:** Legal/Compliance cobre contratação e cláusulas; ESG/EHS cobre se o terceiro opera conforme os requisitos ambientais e de segurança.

---

## Subprocesso 7: Contingências, Multas e Provisões

Etapa de identificar, mensurar, registrar e divulgar multas, autuações, passivos ambientais, obrigações de remediação e contingências trabalhistas/segurança.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| ESG-036 | Auto de infração ambiental ou de segurança não comunicado à contabilidade/jurídico | Reporting | Completude | Alta |
| ESG-037 | Obrigação de remediação ambiental não avaliada para provisão | Recording | Completude | Alta |
| ESG-038 | Estimativa de custo de remediação sem base técnica atualizada | Processing | Valoração | Alta |
| ESG-039 | Contingência possível não divulgada adequadamente | Reporting | Apresentação | Alta |
| ESG-040 | Multa, TAC ou compromisso regulatório registrado fora do período correto | Recording | Corte | Média |

**Controles típicos que mitigam:**
- inventário de autos, multas, TACs, processos e obrigações de remediação
- comunicação formal entre EHS, jurídico, tax/contabilidade e auditoria
- laudo técnico ou orçamento suportando estimativa de remediação
- revisão periódica de probabilidade e valor
- checklist de disclosure para contingências ambientais e de segurança

**Relação com RTR:** RTR reconhece e divulga; ESG/EHS identifica o evento, obrigação e evidência técnica.

---

## Subprocesso 8: Métricas ESG e Reporte

Etapa de coleta, cálculo, revisão e publicação de indicadores ESG internos, externos, relatórios de sustentabilidade e métricas usadas em metas.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| ESG-041 | Métrica ESG reportada sem definição formal, owner ou metodologia de cálculo | Initiation | Existência | Alta |
| ESG-042 | Fonte de dados ESG não reconciliada com sistemas operacionais, documentos ou medidores | Reporting | Completude | Alta |
| ESG-043 | Escopo do indicador muda entre períodos sem divulgação ou ajuste comparativo | Reporting | Apresentação | Média |
| ESG-044 | Indicador ESG usado em meta pública ou bônus sem revisão independente | Processing | Existência | Alta |
| ESG-045 | Dado ESG consolidado em planilha manual sem controle de versão, revisão ou trilha | Processing | Existência | Média |
| ESG-046 | Informação desfavorável omitida do reporte ESG por não existir processo de completude | Reporting | Completude | Alta |

**Controles típicos que mitigam:**
- data dictionary ESG com definição, escopo, owner, fonte e fórmula
- reconciliação de indicadores com fonte primária
- revisão independente antes de reporte externo
- controle de mudanças metodológicas
- trilha de evidência para cada métrica material

**Armadilha comum:** tratar relatório ESG como comunicação institucional. Se o dado é usado por investidor, regulador, banco ou remuneração, precisa controle.

---

## Leitura Rápida por Risco

| Risco Central | Subprocessos Críticos | WCGW-chave |
|---|---|---|
| Operar sem licença válida | Licenças | ESG-001, ESG-004, ESG-005 |
| Condicionante não cumprida ou sem evidência | Licenças | ESG-002, ESG-003 |
| Resíduo sem rastreabilidade | Resíduos | ESG-008, ESG-009, ESG-010 |
| Emissão/consumo calculado errado | Emissões | ESG-013, ESG-014, ESG-015 |
| Atividade crítica sem controle de segurança | Saúde e Segurança | ESG-019, ESG-020, ESG-021 |
| Subnotificação de incidentes | Segurança, Reporte | ESG-024, ESG-025 |
| Remediação sem validação técnica | Incidentes | ESG-028, ESG-029 |
| Terceiro crítico sem controle EHS | Terceiros | ESG-031, ESG-033, ESG-034 |
| Provisão ambiental incompleta | Contingências | ESG-036, ESG-037, ESG-038 |
| Métrica ESG sem evidência | Reporte ESG | ESG-041, ESG-042, ESG-046 |
