# Monitoring

## Papel

Hub metodológico para avaliação do componente Monitoring — COSO Princípios 16 e 17. Cobre avaliações contínuas e separadas de efetividade de controles, confiabilidade de baseline analítico e comunicação de deficiências.

## Quando usar

- avaliação do componente Monitoring como parte de engagement de ELC ou ICFR
- avaliação de efetividade de programas de monitoramento contínuo (dashboards, analytics, KPIs)
- identificação de deficiências pervasivas em Monitoring com impacto em severidade de outros achados
- avaliação de efetividade do processo de comunicação e escalada de deficiências

---

## Papel do Componente no COSO

Monitoring é responsabilidade da entidade — o auditor não faz parte do sistema de controle interno. A entidade precisa monitorar a qualidade dos controles ao longo do tempo e agir quando problemas surgem, sem depender de procedimentos especiais ou de auditoria externa para identificar falhas.

> **Princípio fundamental (referencial metodológico):** processo de monitoramento altamente previsível não produz resultados confiáveis ao longo do tempo. Quem é monitorado aprende o padrão e adapta o comportamento a ele.

---

## Princípio 16 — Realiza Avaliações Contínuas e/ou Separadas

### O que avaliar

**Sete pontos de foco:**
- Mix de avaliações contínuas e separadas
- Considera taxa de mudança (ver também P9)
- Estabelece baseline de referência
- Usa pessoal qualificado (ver também P4)
- Avaliações integradas aos processos de negócio
- Ajusta escopo e frequência conforme necessário
- Avaliação objetiva

### Avaliações contínuas (ongoing)

Monitoramento incorporado ao funcionamento normal do negócio:

| Exemplo | O que verificar |
|---|---|
| Atividades rotineiras de supervisão gerencial | Existe inventário de atividades de monitoramento? Há evidência de execução? |
| Comunicações de partes externas (clientes, fornecedores) | Como feedback externo é avaliado para detectar deficiências? Quem recebe e decide sobre a escalada? |
| Sign-off de funcionários em atividades de controle | Como gestão monitora a execução dos controles a partir dessas evidências? |
| Management letter comments de auditores externos | Há evidência de que a gestão endereçou comunicações de deficiências sérias? |

### Avaliações separadas (separate evaluations)

Avaliações pontuais, distintas do fluxo operacional normal. Podem ser:
- Focadas em áreas onde deficiências foram previamente identificadas
- Acionadas por resultado de monitoramento contínuo ou dados analíticos
- Seleção aleatória de processo, localidade ou linha de produto para revisão profunda
- Visitas a localidades remotas para verificar baseline dos analytics aplicados a elas

> **Uso de aleatoriedade:** rotação imprevisível dos objetos de monitoramento funciona como deterrente. Quem é monitorado com previsibilidade aprende a se adaptar — variar o mix reduz esse risco.

### O problema do baseline

Monitoramento baseado em análise de dados e tendências requer **baseline confiável**. Se os dados transmitidos pela área monitorada já estão corrompidos, o monitoramento passa falsa segurança:

- Dados de localidade remota reconciliam com os registros contábeis oficiais da entidade?
- O baseline foi verificado por visita ou procedimento independente em algum momento?
- É possível que a área reporte apenas uma parte das operações para parecer normal nos analytics?

> **Caso real (referencial metodológico):** localidade que reportava consistentemente resultados normais foi descoberta, por visita casual de auditoria interna, como tendo operações paralelas não reportadas — gerando lucro direto para os gestores locais usando ativos e marca da empresa. O baseline analítico era irrecuperável desde o início das operações.

### Dashboards — força e armadilha

Dashboard bem construído é ferramenta efetiva de direcionamento de atenção gerencial. Riscos:

| Força | Armadilha |
|---|---|
| Visibilidade rápida de anomalias | Pontos monitorados não são reavaliados quando o negócio muda |
| Atualização contínua ou periódica | Falsa sensação de que "tudo está no radar" |
| Escalabilidade para múltiplas localidades | Dados do dashboard não são tie-in aos registros contábeis |

Dashboard é mais efetivo como **parte de um programa de monitoramento múltiplo** que inclui também elemento de imprevisibilidade — não como substituto de avaliações separadas.

### Service organizations no monitoramento

SOC reports de organizações de serviço têm limitações de cobertura temporal:
- Relatório anual ou semestral pode não cobrir o ano fiscal inteiro da entidade
- Para funções críticas, a entidade pode precisar de procedimentos adicionais ("inquiry plus") para estender a cobertura
- SOC 2 é o relatório adequado para data centers e cloud computing — na ausência, evidência suficiente sobre esses serviços é difícil de obter

Questões a avaliar: inventário de relatórios SOC está completo e atualizado? Issues relevantes identificados nos reports foram comunicados à gestão?

### Evidências úteis

- inventário de atividades de monitoramento contínuo com frequência e responsável
- evidência de execução das atividades de monitoramento (registros, relatórios, atas)
- documentação do processo de avaliação e escalada quando anomalias são detectadas
- registros de visitas a localidades e verificação de baseline
- inventário de SOC reports recebidos, revisados e com issues tratados

---

## Princípio 17 — Avalia e Comunica Deficiências

Ver seção dedicada em `patterns/control-deficiency-severity.md` — Comunicação de Deficiências (P17).

Resumo dos pontos críticos para avaliação de P17:

- Existe mecanismo formal para identificar e registrar deficiências?
- Deficiências chegam ao responsável direto **e ao nível acima**?
- Deficiências relevantes chegam à governança (board, comitê de auditoria)?
- Existe protocolo específico para suspeita de fraude — distinto do fluxo rotineiro?
- Há evidência de que ações corretivas foram tomadas após comunicação?

---

## Deficiências de Monitoring como Controles Pervasivos

Deficiências em P16/P17 são tratadas pelo Chart 4 de avaliação de severidade (ver `patterns/control-deficiency-severity.md`): não causam distorção diretamente, mas aumentam a probabilidade de que distorções em outros processos não sejam detectadas.

Implicações práticas:
- Monitoring ineficaz amplifica severidade de deficiências em outros componentes
- COSO trata ausência de monitoramento efetivo como potencial material weakness
- Auditor interno que constata ausência de função de monitoramento deve avaliar impacto em toda a avaliação de ICFR, não apenas registrar como deficiência isolada

---

## Red Flags de Monitoring

- monitoramento 100% previsível — mesmos controles, mesmas pessoas, mesmos períodos todo ciclo
- baseline analítico nunca verificado contra registros contábeis oficiais
- dashboard existente mas pontos monitorados não revisados há mais de um ciclo
- SOC reports recebidos mas não revisados ou sem tratamento de issues
- avaliações separadas concentradas apenas em áreas de baixo risco (fácil de auditar)
- ausência de inventário de atividades de monitoramento contínuo
- deficiências identificadas no monitoramento sem evidência de escalada ou ação corretiva

---

## Artefatos relacionados

- `patterns/control-deficiency-severity.md` — P17 (comunicação de deficiências) e Chart 4 (severidade de controles pervasivos)
- `processes/information-and-communication.md` — P14/P17 interdependência: monitoramento efetivo depende de comunicação efetiva
- `processes/entity-level-controls.md` — P5 (accountability) interage com P17: se deficiências comunicadas não geram ação, é falha simultânea de P5 e P17
- `concepts/control-activities-framework.md` — armadilha monitoring como substituto de controles transacionais
- `modes/risk-assessment.md` — P9 (significant change) e P16 compartilham gatilhos de revisão
