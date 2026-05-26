# Evidence and Testing — Foundations

## Papel

Base conceitual para planejamento de coleta de evidência em auditoria de controles. Cobre tipos e hierarquia de evidência, walkthrough (definição, qualidade e documentação), top-down concept e situações em que amostragem não se aplica.

## Quando usar

- antes de desenhar procedimentos de teste num engagement novo
- ao revisar o plano de evidência de um trabalho em andamento
- ao avaliar se a documentação existente sustenta as conclusões de controle

---

## Tipos de Evidência e Hierarquia de Força

Procedimentos disponíveis, do mais ao menos direto:

| Procedimento | Descrição | Força relativa |
|---|---|---|
| Reperformance | Auditor reexecuta o controle ou procedimento | Mais forte |
| Inspeção de documentos | Exame de registros, contratos, aprovações | Alta |
| Observação | Testemunhar a execução do controle | Alta (mas limitada ao momento observado) |
| Confirmação externa | Confirmação direta com terceiros | Alta quando disponível |
| Recálculo | Verificação aritmética de cálculos | Alta para o que verifica |
| Procedimentos analíticos | Comparação de valores, tendências, ratios | Limitada para controles — mais útil em substantivo |
| Indagação (inquiry) | Pergunta a funcionários ou gestão | Mais fraca — nunca suficiente isolada |

### Condições que aumentam a força da evidência

- fonte independente ou externa vs. interna
- controles relacionados testados e efetivos
- obtida diretamente pelo auditor vs. produzida pela entidade
- documental vs. oral
- documento original vs. cópia

> **Regra prática:** inquiry sempre acompanhada de pelo menos outra fonte. Em áreas de alto julgamento (estimativas, ambiente de controle, fraude) o auditor não pode depender da avaliação da própria entidade — precisa formar julgamento independente.

### Confiabilidade de documentos da entidade

Não assumir que relatório, base ou listagem produzida pela entidade é completa e precisa sem verificação. Exemplos de documentos tainted foram usados para ocultar fraude e dados incorretos que levaram a decisões equivocadas. Toda base de dados relevante deve ter atributos de **completude** e **precisão** verificados antes de ser usada como população de teste ou como evidência.

Vínculo direto: confiabilidade de informação interna é também objeto do componente **Information & Communication** (COSO Princípios 13–15). Evidência de IPE confiável pode ser referenciada na avaliação desse componente.

---

## Walkthrough — Definição e Propósito

Walkthrough é a rastreabilidade de uma transação do início ao fim do processo, com foco nos **pontos de controle** — não na trilha do documento em si.

**O que walkthrough É:**
- corroborative inquiry: perguntas seguidas de evidência corroborante
- teste de um item: um único item examinado em profundidade para verificar operação dos controles

**O que walkthrough NÃO É:**
- seguir o caminho do documento pelo sistema (erro mais comum)
- entrevista sem verificação subsequente
- ferramenta de treinamento de júniores sem supervisão ativa

### Escopo mínimo de um walkthrough

Deve cobrir a transação desde a iniciação até o reporte nas demonstrações financeiras, passando por:
- Initiação
- Autorização
- Registro acurado e completo nos livros
- Sumarização e reporte nas DFs ou notas

### Quando realizar e atualizar

- uma vez por ciclo/processo onde reliance é planejado
- sempre que houver mudança significativa no processamento ou no controle
- periodicamente para confirmar que nenhuma mudança silenciosa ocorreu

### Foco correto durante o walkthrough

O documento/transação é o veículo — os **controles** são o objeto de atenção. Para cada ponto de controle:
- O controle operou como descrito?
- Existe evidência documental de que operou?
- O funcionário entende o controle e seu papel?
- Como exceções são tratadas?

> **referencial metodológico:** Uma deficiência recorrente em peer reviews e inspeções é walkthrough que documenta extensivamente o processo e ignora os controles. Narrativas longas sobre o fluxo do documento frequentemente encobrem a ausência de análise dos pontos de controle.

---

## Qualidade de Documentação do Walkthrough

Critérios de qualidade (baseados em orientação PCAOB adaptável para interna):

- [ ] Vincula o walkthrough aos riscos inerentes e de fraude identificados na área
- [ ] Liga claramente cada ponto de controle à documentação de controles existente
- [ ] Identifica as asserções sendo endereçadas
- [ ] Menciona componentes de TI relevantes e eventuais deficiências de ITGC conhecidas
- [ ] Registra quem realizou, quando, com quem se entrevistou
- [ ] Documenta se o funcionário demonstra entendimento do controle e como trata exceções
- [ ] Registra a evidência obtida (não apenas a resposta à pergunta)
- [ ] Indica procedimentos adicionais sugeridos ou questões em aberto
- [ ] Conclui de forma clara

### Erro de "stovepipe"

Ocorre quando um revisador avalia o teste de forma isolada, sem considerar procedimentos relacionados em outras áreas que corroboram a mesma asserção. Exemplo: uma amostra pequena em vendas é criticada como insuficiente para existência, mas a documentação não menciona que confirmações de AR e controles de caixa foram extensamente testados e eficazes — o que reduzia o risco de existência significativamente.

**Solução:** documentar o raciocínio que levou à decisão, incluindo referências cruzadas a procedimentos em outras áreas que suportam a conclusão. Revisores não são leitores de mentes e não buscam em outras seções do trabalho para salvar documentação incompleta.

---

## Top-Down Concept

Estratégia de sequência de avaliação que prioriza o que tem **impacto pervasivo** antes dos controles transacionais:

**Ordem recomendada:**
1. **Ambiente de controle (CE)** — showstoppers identificados aqui são difíceis de remediar no final do ano e contaminam a avaliação de todos os outros componentes
2. **ITGCs** — deficiências de ITGC podem invalidar testes de controles automatizados já realizados; identificar cedo evita retrabalho
3. **Controles compartilhados** (entity-level controls comuns a múltiplos processos)
4. **Controles transacionais** — processo a processo, dentro de ciclos lógicos

> **Lógica:** uma deficiência de acesso em ITGC identificada em dezembro invalida controles automatizados testados desde janeiro. O custo de não identificar cedo é retrabalho de tudo que dependia daqueles controles.

### Aplicação prática

- Testar CE e ITGCs no início do engagement, não ao final
- Identificar controles compartilhados entre processos (ex: caixa, folha, pagamentos) e testá-los uma única vez, referenciando nos processos que os utilizam
- Ciclos com shared activities (cash receipts, cash disbursements, payroll) devem ser testados uma única vez — não duplicar o teste em cada processo que os utiliza

---

## Situações Sem Amostragem

Quando a natureza do controle ou da evidência torna amostragem inapropriada ou sem significado:

| Situação | Abordagem correta |
|---|---|
| Segregação de funções | Análise de compatibilidade de perfis de acesso — não seleção aleatória de transações |
| Ambiente de controle (tom do topo, competência de governança) | Observação, entrevistas, análise de atas, surveys |
| Competência do comitê de auditoria | Avaliação de credenciais, observação de reuniões, minutos, análise de perguntas feitas |
| ITGCs (acesso, segurança, mudança de sistemas) | Inspeção da matriz de acessos, análise de políticas, observação — sampling pode ser aplicado em logs em organizações grandes |
| Controles automatizados (application controls) | 1–2 instâncias suficientes se ITGCs efetivos e testados (ver `concepts/sample-size.md`) |
| Código de conduta — existência | Leitura e avaliação do conteúdo — não se amostram políticas |
| Código de conduta — implementação | Amostra de assinaturas anuais de funcionários (quando população é grande) ou census |

> **Regra:** amostragem é apropriada quando há uma **população de operações de controle** da qual itens podem ser selecionados sem viés. Quando não há população homogênea e frequente, usar julgamento analítico com múltiplas fontes de evidência.

---

## Documentação de Julgamentos de Evidência

O raciocínio que levou à decisão de procedimento deve ser discernível da documentação:

- Se amostra pequena foi usada: explicar por que o risco da asserção era baixo com referência cruzada aos outros testes
- Se inquiry foi a fonte principal: documentar a corroboração obtida e seus limites
- Se confiou em testes da entidade ou auditoria interna: documentar avaliação de competência e objetividade da fonte

Documentação insuficiente não é apenas risco de revisão — é também risco de o próprio time perder o raciocínio que sustentou a conclusão com o passar do tempo.

---

## Artefatos relacionados

- `concepts/sample-size.md` — dimensionamento de amostras para testes de controle
- `processes/ipe-reliability-assessment.md` — avaliação de confiabilidade de IPE antes de usá-la como evidência
- `processes/inquiry-planning-and-follow-up.md` — condução de entrevistas e walkthrough inquiries
- `workflows/walkthrough-standardization.md` — processo padronizado de walkthrough
- `workflows/test-execution.md` — execução de testes e documentação
- `_method-wiki-external-audit/workflows/walkthrough-standardization-external-audit.md` — usar quando o walkthrough precisar seguir logica SCOT / ICFR
- `patterns/control-deficiency-severity.md` — o que fazer quando desvios são encontrados
