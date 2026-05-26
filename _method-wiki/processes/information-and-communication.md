# Information and Communication

## Papel

Hub metodológico para avaliação do componente Information & Communication — COSO Princípios 13, 14 e 15. Cobre qualidade da informação gerada internamente, canais de comunicação interna e comunicação com partes externas.

## Quando usar

- avaliação do componente I&C como parte de engagement de ELC ou ICFR
- identificação de deficiências de informação com impacto em múltiplos processos
- avaliação de efetividade de hotline, canais de escalada e comunicação de controles
- walkthrough de processos onde a qualidade da informação é fator de risco relevante

---

## Papel do Componente no COSO

Information & Communication tem "tentáculos" em todos os outros componentes: deficiências de informação raramente ficam contidas num único princípio. Exemplo: dado de vendas impreciso pode indicar deficiência em P13 (qualidade de dados), fragilizar a capacidade de monitoramento (P16), e comprometer a base de estimativas (P7 — risk assessment).

A avaliação não é isolada — identificar uma deficiência aqui exige verificar quais outros componentes são afetados.

---

## Princípio 13 — Gera Informação Relevante

### O que avaliar

Controles sobre os processos que garantem que informação **completa, precisa, tempestiva e custo-efetiva** chegue a quem precisa dela.

**Cinco pontos de foco:**
- Identificar requisitos de informação
- Capturar dados internos e externos
- Processar dados relevantes em informação utilizável
- Manter qualidade ao longo do processamento
- Considerar custo-benefício

### Perguntas críticas de avaliação

- A entidade mantém inventário dos relatórios gerados — para quem, com qual frequência?
- Gestores confirmam em entrevistas que recebem a informação necessária para exercer seus controles?
- Quando anomalias são identificadas nos dados, há processo de investigação e melhoria contínua?
- Informação não-financeira relevante para estimativas (ex: condições de mercado para obsolescência de estoque, dados regionais para provisões) está sendo capturada e considerada?

### Relação com IPE

Confiabilidade de IPE é evidência direta de P13. Quando testes de IPE revelam problemas de completude ou precisão, isso é input de avaliação do componente — não apenas achado de processo. Ver `processes/ipe-reliability-assessment.md`.

### Evidências úteis

- inventário de relatórios com destinatários e periodicidade
- entrevistas com owners de controle confirmando recebimento de informação necessária
- registros de correções de dados e ações corretivas após anomalias
- documentação de fontes usadas em estimativas significativas (financeiras e não-financeiras)

---

## Princípio 14 — Comunica Internamente

### O que avaliar

A entidade precisa comunicar de forma efetiva as responsabilidades de controle, políticas, expectativas de comportamento e problemas identificados — tanto por canais formais quanto informais.

**Quatro pontos de foco:**
- Comunicar informações de controle interno
- Comunicar com governança
- Disponibilizar linhas separadas de comunicação (ex: hotline)
- Selecionar métodos adequados de comunicação

### O que a comunicação interna precisa cobrir

Para que controles funcionem, cada executor precisa entender:

| O que comunicar | Por quê importa |
|---|---|
| Deveres específicos de controle | Executor sabe o que precisa fazer e quando |
| Como os controles se integram | Permite identificar quando algo a montante falhou |
| Relação entre o trabalho individual e o de outros | Motiva identificação de problemas e busca de causa |
| Comportamento esperado e inaceitável | Elimina ambiguidade sobre limites |
| O que fazer quando o inesperado ocorre | Reduz dependência de julgamento ad hoc em situações de exceção |

### Hotline e linhas separadas de comunicação

Hotline anônima é linha separada obrigatória de avaliação. Não basta existir — avaliar efetividade:

- Funcionários sabem da existência e do canal de acesso?
- Há percepção de que alegações são investigadas e resolvidas?
- Visão de áreas operacionais (produção, vendas, administrativo) está alinhada com a da liderança?
- Se terceiro opera o serviço: como a entidade monitora qualidade e volume de uso?

> **Armadilha:** hotline com baixo volume de uso não é necessariamente sinal positivo — pode indicar descrença na efetividade ou medo de represália. Triangular com surveys e entrevistas.

### Comunicação informal

Conversas, e-mails, reuniões de equipe e interações com clientes/fornecedores fazem parte do sistema de comunicação. Problemas detectados informalmente precisam de mecanismo para escalar para o nível correto — a ausência desse mecanismo é falha de P14.

Mensagens importantes não devem depender exclusivamente de canais informais: memórias desvanecem e responsabilidade de follow-up se perde.

### Comunicação com governança

O feedback loop entre gestão, auditoria interna e governança precisa funcionar em ambas as direções:
- Deficiências identificadas chegam ao board/comitê de auditoria?
- Governança comunica expectativas e resultados de volta para gestão?
- Existe canal para que funcionários reportem issues diretamente à governança quando a gestão é parte do problema?

### Relação com Monitoring

P14 e P16/P17 são interdependentes: monitoramento efetivo depende de comunicação efetiva. Deficiência de comunicação de resultados de monitoramento para o nível certo é simultaneamente P14 e P17. Ver `patterns/control-deficiency-severity.md` — seção Comunicação de Deficiências.

### Evidências úteis

- descrições de cargo com responsabilidades de controle documentadas
- registros de treinamento sobre políticas e procedimentos de controle
- evidência de que o hotline opera e que issues são tratados
- surveys de funcionários sobre awareness de políticas e expectativas
- atas de reunião de comitê de auditoria recebendo comunicações de deficiências

---

## Princípio 15 — Comunica Externamente

### O que avaliar

Canais de comunicação da entidade com clientes, fornecedores, reguladores, acionistas e público. Inclui tanto comunicações de saída (reporte financeiro, respostas regulatórias) quanto de entrada (reclamações, relatórios de reguladores, comentários de auditores).

**Cinco pontos de foco:**
- Comunicar com partes externas
- Habilitar comunicações de entrada
- Comunicar com governança
- Disponibilizar linhas separadas de comunicação
- Selecionar métodos adequados

### Fontes externas de informação sobre controles

Comunicações externas são fonte de evidência sobre deficiências internas:

| Fonte | O que pode revelar |
|---|---|
| Reclamações de clientes sobre faturamento | Problemas no processamento de vendas ou caixa |
| Relatórios de reguladores | Deficiências de controle ou questões de princípios contábeis |
| Management letter comments de auditores | Deficiências identificadas independentemente |
| Relatórios de auditoria interna | Deficiências com impacto em reporte ou compliance |

**Questão-chave:** existe processo para garantir que issues externos relevantes sejam transmitidos à governança? Não basta receber o relatório — precisa haver mecanismo documentado de triagem e escalada.

### Escopo para auditoria interna

P15 é menos denso para interna do que para externa (onde external reporting tem requisitos regulatórios específicos). O foco de interna deve ser:
- Efetividade dos canais de entrada (reclamações, reports de terceiros)
- Processo de triagem e escalada de informações externas relevantes
- Alinhamento entre comunicações externas e registros internos

---

## Deficiências e Pervasividade

Deficiências de I&C tendem a ser pervasivas — afetam múltiplos processos e princípios simultaneamente. Ao identificar uma deficiência em P13–P15, verificar:

1. Quais outros componentes são afetados (Risk Assessment, Control Activities, Monitoring)?
2. A deficiência impede a identificação tempestiva de problemas em outros controles?
3. A ausência de informação confiável cria exposição a distorção não detectada em áreas específicas?

---

## Red Flags de Information & Communication

- relatórios gerados sem destinatário claro ou sem evidência de uso
- ausência de inventário de relatórios críticos
- hotline com volume zero ou percepção de inefetividade
- problemas identificados externamente (reguladores, auditores) que não chegam ao comitê de auditoria
- comunicação de responsabilidades de controle feita apenas na admissão, nunca atualizada
- estimativas significativas sem documentação das fontes de informação usadas
- gestão que bloqueia comunicação de issues para governança

---

## Artefatos relacionados

- `processes/ipe-reliability-assessment.md` — evidência direta de P13; confiabilidade de dados gerados internamente
- `processes/entity-level-controls.md` — P14 tem cruzamento com P1/P3/P5 (comunicação de accountability e estrutura)
- `patterns/control-deficiency-severity.md` — escalada de deficiências (P17 depende de P14)
- `processes/inquiry-planning-and-follow-up.md` — hotline e surveys como fonte de evidência de P14
- `checklists/inquiry-question-bank.md` — perguntas de ELC incluem comunicação interna
