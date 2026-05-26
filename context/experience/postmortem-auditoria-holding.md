# Post-Mortem — Auditoria de Holding Multi-Entidade

Lições aprendidas em trabalho real de auditoria externa em holding com múltiplas entidades (construção civil, engenharia, arrendamento mercantil, holdings intermediárias). Registrado para calibrar planejamento e evitar reincidências.

---

## Erros operacionais — equipe de auditoria

### Circularização com data-base inadequada

Circularizações foram enviadas com data-base intermediária por antecipação de cronograma. Consequência: todos os WPs, folhas mestras e movimentações precisaram ser refeitos para reconciliar o período adicional. Staffs que rotacionavam entre projetos foram impactados por orientações conflitantes.

**Lição:** data-base de circularização deve ser definida no planejamento com avaliação explícita do custo de retrabalho. Antecipar circularização só vale quando o cliente consegue produzir documentação naquela data — verificar viabilidade antes de decidir.

### Seleções chegaram tarde demais

Diversas seleções chegaram na fase final sem tempo hábil para execução. Áreas com histórico de pendência crônica (adiantamento de clientes, partes relacionadas) não foram priorizadas no início da fase final.

**Lição:** seleções de áreas historicamente problemáticas devem ser abertas e cobradas desde o início da visita final. Não esperar a área estar "quase concluída" para selecionar.

### Seleções tecnicamente incorretas

Seleções foram realizadas com critério errado — proporcionalização indevida de contas patrimoniais na fase de seleção.

**Lição:** revisar critério de seleção antes de enviar ao cliente, especialmente em contas com movimentação complexa. Seleção errada gera retrabalho e exposição técnica.

### Retrabalho em WPs

Trabalhos duplicados ou mal alocados entre staffs por ausência de controle de áreas claro e atualizado.

**Lição:** controle de áreas deve ser revisado diariamente em visitas com equipe grande. Atribuição de área = responsável único, não grupo.

---

## Erros de gestão de equipe

### Conflito entre staffs por expectativa não comunicada

Conflito explícito entre membros da equipe por ausência de alinhamento sobre o que era esperado de cada um. Gerente ausente e responsabilidade não transferida formalmente.

**Lição:** quando sênior assume responsabilidade de gerente, formalizar realinhamento de expectativas com a equipe. Não deixar lacuna de autoridade.

### Treinamento de trainee não compensou rotatividade

Tempo investido em explicar particularidades do cliente foi perdido com saída ou rodízio de trainees.

**Lição:** documentar particularidades do cliente em arquivo de referência reutilizável, não apenas repassar verbalmente.

---

## Erros de gestão de cliente

### Cliente não priorizou a equipe de auditoria

Cliente concentrou respostas e documentações apenas na semana final, criando gargalo. Pressão formal foi insuficiente nos períodos anteriores.

**Lição:** lista de solicitações com prazo e cópia ao responsável do cliente deve ser enviada desde o primeiro dia. Atrasos devem ser escalados formalmente antes de virar crise.

### Entidades com regime específico e prazo próprio de documentação

Entidades com regime específico (consórcios, holdings intermediárias) só produzem conciliações de forma trimestral. A data-base intermediária não tinha documentação disponível para essas entidades.

**Lição:** mapear no planejamento quais entidades têm limitações de produção documental por data-base. Tratar como restrição de escopo, não como surpresa.

### Pedido de teste adicional na última semana

Gerente solicitou teste qualitativo adicional na última semana da auditoria. Não havia tempo hábil para execução.

**Lição:** qualquer teste adicional fora do programa original deve ser avaliado pelo sênior com estimativa de horas antes de aceitar. "Não há tempo" precisa ser comunicado formalmente, não absorvido silenciosamente.

---

## Padrões de falha identificados

| Padrão | Impacto |
|---|---|
| Circularização com data-base inadequada | Alto — retrabalho em múltiplas áreas |
| Seleções tardias em áreas problemáticas | Alto — recorrente sem controle de áreas ativo |
| Conflito de equipe por lacuna de liderança | Médio |
| Pedido de teste fora do escopo na fase final | Médio — comum em clientes com gestão financeira imatura |
| Retrabalho por documentação não arquivada | Alto |

---

## Checklist preventivo — planejamento de visita

- [ ] Data-base de circularização avaliada com análise de viabilidade documental do cliente
- [ ] Áreas com histórico de pendência mapeadas com prazo de seleção desde a fase interim
- [ ] Controle de áreas com responsável único por área e prazo de conclusão
- [ ] Particularidades do cliente documentadas em arquivo de referência (não só verbal)
- [ ] Entidades com limitação de produção documental identificadas no planejamento
- [ ] Pedidos de teste adicional avaliados com estimativa de horas antes de aceitar
