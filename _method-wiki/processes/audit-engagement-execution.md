# Audit Engagement Execution

## Papel

Hub metodológico para execução de trabalhos de auditoria com foco em planejamento operacional, controle de pendências, escalonamento e prevenção de retrabalho.

## Quando usar

- planejar kickoff, interim, final ou fechamento de ciclo
- organizar backlog de pendências críticas
- definir checkpoints de escalonamento com cliente, equipe e especialistas
- revisar riscos operacionais de execução antes de entrar na fase final

## Objetivo

Criar uma disciplina de execução que reduza retrabalho, antecipe bloqueios e preserve qualidade técnica até a conclusão do trabalho. A nota serve como referência para transformar planejamento em rotina operacional, e não apenas em cronograma estático.

## Blocos principais

### 1. Planejamento operacional mínimo

- definir trilhas críticas de documentação, seleção e suporte técnico
- identificar dependências do cliente que podem travar o cronograma
- travar critérios de seleção e janelas de solicitação antes do pico final
- alinhar áreas de suporte como TAX, folha, TI e especialistas com escopo e prazo definidos
- decidir cedo quais testes podem ser antecipados para aliviar pressão da final

### 2. Controle de pendências

- manter backlog claro de itens críticos, dono, prazo e impacto
- separar pendência operacional de pendência técnica
- atualizar status com foco em desbloqueio, não apenas em report
- registrar explicitamente o que depende do cliente, o que depende da equipe e o que depende de terceiros
- consolidar pendências que obrigatoriamente precisam estar resolvidas antes do fechamento

### 3. Escalonamento preventivo

- escalar ausência de documentação crítica antes do fechamento
- antecipar gargalos de CoE, especialistas, circularização e cartas
- evitar escalonamento tardio quando o prazo já foi consumido
- tratar falta de resposta do cliente como risco operacional, não como mero atraso administrativo
- definir gatilhos objetivos para escalar e não depender apenas de percepção subjetiva da liderança

### 4. Anti-retrabalho

- proteger o trabalho contra mudanças tardias de data-base e escopo
- evitar rollforward sem critério e sem impacto previamente mapeado
- registrar promessas de amarração e pendências para a final em checklist explícito
- evitar reaproveitamento automático do ano anterior sem reavaliação do risco
- revisar se evidência substituta, exceção documentada ou decisão transitória ficou formalizada para follow-up

## Rotina recomendada

### 1. Antes do kickoff

- confirmar escopo, materialidade, frentes críticas e dependências
- mapear áreas com histórico de conciliação problemática ou atraso recorrente
- definir donos internos e do cliente por trilha de trabalho

### 2. Durante a execução

- monitorar backlog de pendências e seleções em frequência curta
- revisar se o cronograma continua viável diante das dependências reais
- redistribuir esforço quando uma frente crítica começa a acumular risco

### 3. Antes da fase final

- travar janela para novas solicitações técnicas relevantes
- confirmar quais amarrações ainda dependem de evidência final
- escalar lacunas críticas antes do consumo total do prazo

### 4. No fechamento

- confirmar que cada pendência crítica teve resolução, mitigação ou escalonamento formal
- registrar exceções, limitações e impactos residuais
- capturar aprendizado reutilizável para o próximo ciclo

## Riscos recorrentes

- backlog de seleções e pendências concentrado na fase final
- atraso de documentação-chave do cliente
- falta de alinhamento de expectativa entre time, liderança e cliente
- pedidos técnicos tardios sem janela de execução
- retrabalho por mudança de data-base, critério ou documentação
- circularizações, cartas ou frentes especiais sem previsibilidade suficiente
- priorização fraca de contas e trilhas críticas no planejamento

## Decisões típicas

- antecipar testes de contas de movimentação para aliviar a final
- ampliar circularização quando a confiança no sistema ou na reconciliação é baixa
- priorizar contas críticas de fechamento quando o prazo não comporta cobertura uniforme
- usar evidência temporária com ressalva explícita apenas quando a limitação estiver controlada e rastreada

---

## 5. Estrutura do Time de Projeto

### Seniority e autoridade

O time precisa de autoridade suficiente para obter cooperação tempestiva da organização. Sem senioridade, pedidos viram sugestões — e prazos escorregam. O responsável pelo projeto deve reportar a instância de governança com poder de exigir resposta (comitê de auditoria, CFO, CEO).

### Papel de auditoria interna

IA tem vantagem natural em projetos de avaliação de controles: conhece a empresa, os processos e as pessoas. Pode contribuir de duas formas:

| Modo | Contribuição |
|---|---|
| **Work product** | Documentação de design e evidência de operação produzida em ciclos anteriores — pode ser aproveitada se escopo, timing e qualidade forem suficientes |
| **Membro ativo do time** | Executa procedimentos específicos do projeto sob supervisão; mais eficiente que treinar pessoa nova |

**Limitação de objetividade:** auto-avaliação de controles do próprio departamento é aceita operacionalmente, mas reduz a confiança de terceiros (auditoria externa, comitê) no resultado. Quando possível, cruzar avaliadores entre áreas.

### Especialistas técnicos — quando acionar

| Especialidade | Gatilhos para acionamento |
|---|---|
| **IT specialist** | e-commerce relevante; dados compartilhados entre múltiplas aplicações; tecnologias emergentes (cloud); sistemas complexos ou legados sem documentação |
| **Valuation specialist** | Fair value relevante no reporte (instrumentos financeiros, imobilizado, goodwill, provisões); impairment test com premissas complexas |
| **Tax specialist** | Accrual tributário complexo; posições incertas; deferred tax com julgamento significativo |

Especialista ajuda a identificar riscos, documentar e testar controles na área — não substitui o julgamento do time principal sobre o impacto no reporte financeiro.

---

## 6. Projeto Piloto — Quando e Como Usar

Antes de lançar o projeto completo (ou ao revisar abordagem existente), testar numa área contida reduz risco de retrabalho sistêmico.

### Quando vale um piloto

- Primeira vez documentando controles de forma estruturada
- Mudança relevante de abordagem, ferramenta ou framework
- Time com pouca experiência em avaliação de COSO

### Como selecionar a área piloto

- Área **contida** — não envolva múltiplos processos em múltiplas localidades
- Preferência por processo bem organizado e centralizado (ex: contas a pagar rotineiro, folha com SO)
- Evitar processos com alta complexidade de julgamento como piloto inicial (estimativas, instrumentos financeiros)

### Debriefing pós-piloto — perguntas

1. O que funcionou bem na documentação e nos testes?
2. O que precisaria ser ajustado antes de escalar?
3. Que treinamento é necessário para consistência entre avaliadores?
4. A ferramenta de documentação atendeu? Onde criou atrito?
5. A composição do time está certa para o projeto completo?

O piloto também calibra estimativas de tempo e recurso antes do comprometimento com cronograma do projeto completo.

---

## 7. Critérios para Ferramentas de Documentação

Não há ferramenta padrão prescrita — Word e Excel são comuns e funcionam. Ao avaliar ou configurar qualquer solução, verificar:

| Critério | O que verificar |
|---|---|
| **Acesso e permissões** | Quem pode editar, revisar e aprovar cada módulo? Como proteger arquivos fechados de modificação acidental? |
| **Capacidade de rede** | Múltiplos usuários simultâneos? Mecanismo de lock de módulo em edição? Resolução de conflitos de dados? |
| **One-write** | Deficiência identificada num módulo se propaga automaticamente para o summary, ou exige entrada manual repetida (risco de inconsistência)? |
| **Cross-referencing** | Riscos linkam a controles? Deficiências linkam a princípios e contas? Evidência referenciada sem duplicação? |
| **Status e alertas** | É possível ver status do projeto por módulo? Sistema avisa quando work paper revisado é alterado após sign-off? |
| **Work paper discipline** | Formulário prompta para data, executor, supervisor, parâmetros de amostragem, pessoa entrevistada no walkthrough? |
| **Rollover anual** | Ao abrir novo ciclo, sign-offs anteriores são resetados? Texto carregado do ano anterior é forçado a confirmação antes de aceite? |
| **Arquivamento** | Arquivo de ciclo fechado fica em read-only? Navegável sem software especial? Atende prazo de retenção da política interna? |

**Documentação + teste pela mesma equipe** é mais eficiente do que equipes separadas: quem documentou já conhece os controles e está "pronto para testar". O trade-off é perder o segundo par de olhos — compensar com supervisão próxima de cada fase.

---

## 8. Pré-condições de Eficiência — Triangle of Efficiency (referencial metodológico, Cap. 1)

Projetos de avaliação de controles falham por deficit em um de três conhecimentos, não por falta de esforço:

| Vértice | O que significa na prática |
|---|---|
| **Requisitos** | Entender o que o engajamento precisa entregar — padrão aplicável (IIA, COSO, SOX), nível de assurance exigido, forma de reporte |
| **COSO / framework** | Dominar os 17 Princípios, pontos de foco e a lógica de componentes integrados — sem isso o time documenta processo em vez de controle |
| **Empresa e seus controles** | Conhecer a entidade: processos, sistemas, pessoas-chave, histórico de achados, pontos de julgamento |

Deficit em qualquer vértice gera retrabalho. O erro mais comum em primeiras implementações foi começar a documentar controles transacionais detalhados antes de compreender o escopo total dos requisitos — o resultado foi custo excessivo e cobertura desequilibrada.

Aplicação prática antes do kickoff: verificar se o time tem os três vértices cobertos. Lacuna de conhecimento de COSO → treinamento antes, não durante. Lacuna de conhecimento da empresa → envolver IA ou área de negócio antes de abrir work papers.

---

## Artefatos relacionados

- `checklists/engagement-critical-close-checklist.md`
- `postmortems/project-execution-risk-patterns.md`
- `processes/erp-transition-and-control-remediation.md`
- `concepts/scoping-strategy.md` — seção 8 (reliance no trabalho de outros) e critérios de aproveitamento de trabalho de IA anterior
