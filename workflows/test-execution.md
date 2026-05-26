# workflow: test-execution

## Goal

Desenhar, executar e concluir sobre um teste de controle — ToD ou ToE — com base em evidência e critério definido.

## Use When

- há um controle a ser testado e precisa-se definir o procedimento
- existe uma amostra ou conjunto de evidências para avaliar
- é preciso concluir sobre efetividade de um controle com base em resultados
- identificação de exceções requer avaliação e enquadramento

## Inputs

- controle a ser testado
- risco associado e asserção relevante
- critério do controle (política, norma, procedimento operacional)
- tipo de teste: ToD, ToE ou ambos
- evidências disponíveis (documentos, registros sistêmicos, amostra)
- contexto do processo e da organização

## Execution Sequence

### 1. Confirmar o objeto do teste

Antes de executar:

- Qual controle específico está sendo testado?
- Qual o critério? (o que deveria acontecer para considerar o controle efetivo)
- Qual a asserção em jogo?
- ToD, ToE ou ambos?

Sem critério definido, o teste não pode concluir.

### 2. ToD — Avaliar o Design

Perguntas:

- O controle, operado como desenhado, seria suficiente para mitigar o risco?
- Há dependência crítica de pessoa que compromete a continuidade?
- O controle tem frequência adequada ao risco?
- Existe segregação de funções no controle?

Procedimento típico: entrevista com responsável, leitura de política, inspeção de workflow ou sistema, walkthrough de uma transação da ponta à ponta.

Conclusão possível:
- **Design adequado**: o controle, se operado corretamente, mitiga o risco
- **Design inadequado**: falha estrutural — o controle não seria suficiente mesmo executado corretamente

Se o design for inadequado, não realizar ToE. Encaminhar direto para finding.

### 3. ToE — Avaliar a Efetividade

Definir a amostra:

**Gate obrigatório — validar IPE antes de definir população:**
Quando o teste depende de listagem, relatório ou base fornecida pela entidade, executar `_method-wiki/checklists/ipe-validation-before-test.md` antes de prosseguir. Resultado esperado: IPE confiável ou confiável com restrição documentada. Se IPE não confiável: redesenhar procedimento ou exigir alternativa.

- Frequência do controle: diário, semanal, mensal, por transação?
- Tamanho da amostra: usar `skills/sample-size-calculator.md` para determinar N defensável com base em tipo de controle, frequência e nível de risco
- Período coberto pelo teste

Executar o teste:

- Inspecionar evidência de execução do controle (aprovação, carimbo, log sistêmico, e-mail, relatório)
- Reperformar o controle quando necessário (recalcular, reconciliar, verificar o que foi validado)
- Observar diretamente quando for controle físico ou presencial

Avaliar cada item da amostra:

- O controle foi executado conforme o critério?
- Há desvio, omissão, atraso ou evidência insuficiente?

### 4. Avaliar exceções

Para cada item que não passou no critério, seguir o decision tree abaixo. Referência metodológica: `_method-wiki/patterns/control-deficiency-severity.md` Charts 1–4.

**Decision tree de exceção:**

```
Exceção encontrada
       │
       ▼
É desvio de DESIGN? (controle, operado como desenhado, não mitiga o risco)
       │
    Sim ──► Parar ToE. Achado de design inadequado. → finding-drafting.md
       │
    Não
       │
       ▼
É indicação de override gerencial ou fraude?
       │
    Sim ──► Escalar imediatamente. Não tratar como desvio normal.
       │      Referência: control-deficiency-severity.md "Protocolo especial para fraude"
    Não
       │
       ▼
É erro sistemático (bug, glitch, configuração)?
       │
    Sim ──► Assumir que TODA a população foi afetada. Expandir escopo.
       │      → Não encerrar como desvio isolado.
    Não
       │
       ▼
Calcular taxa de desvio da amostra (desvios / N)
       │
       ▼
Taxa de desvio ≤ tolerável definido no plano?
       │
    Não ──► Objetivo do teste não foi atingido.
       │      Opções:
       │      1. Ampliar amostra (dobrar N) e reavaliar
       │      2. Concluir como controle inefetivo
       │      3. → finding-drafting.md + finding-rating.md
    Sim
       │
       ▼
Desvios são representativos da população ou erro amostral isolado?
       │
 Representativos ──► Configurar como deficiência. Avaliar severidade:
       │              - Chart 1: exceção em ToE → deficiência?
       │              - Chart 2: controles manuais/automatizados
       │              - Chart 3: se for ITGC
       │              - Chart 4: se for controle pervasivo
       │              → control-deficiency-severity.md + finding-rating.md
 Erro amostral ──► Estender teste e reavaliar antes de concluir
```

**Análise qualitativa de cada desvio (sempre):**

| Tipo de desvio | Ação |
|---|---|
| Erro humano pontual | Documentar; avaliar se impacto financeiro é remoto |
| Indicação de override gerencial | Escalar imediatamente — pode ser red flag de fraude |
| Fraude ou falha intencional | Não aceitar como desvio normal; comunicar independentemente do N |
| Erro sistemático (bug, glitch) | Assumir população toda afetada; expandir escopo |

> Regra: o desvio encontrado na amostra é representativo da população — nunca dispensar como "exceção única" sem investigação.

### 5. Concluir

Tipos de conclusão:

- **Controle efetivo**: nenhuma exceção material identificada na amostra
- **Controle com exceções limitadas**: exceções encontradas, mas sem indicação de falha sistemática — avaliar necessidade de ampliar amostra
- **Controle inefetivo**: exceções sistemáticas ou material que indicam que o controle não está operando como desenhado
- **Inconclusivo**: evidência insuficiente para concluir — sinalizar o que falta

## Decision Rules

- Não concluir sobre efetividade sem critério definido
- Não mascarar exceções com linguagem suave — registrar o que foi encontrado
- Se a amostra for pequena, sinalizar a limitação explicitamente
- Exceção não é automaticamente achado — avaliar materialidade e causa antes de enquadrar
- Controle com design inadequado não precisa de ToE — o achado é de design

## Gate de Pronto (DoD)

Antes de fechar o teste como concluído, validar:

- `_method-wiki/checklists/audit-artifacts-definition-of-done.md` -> seção `3) DoD - Papel de Teste de Controle`
- `_method-wiki/checklists/audit-artifacts-definition-of-done.md` -> seção `Gates de Revisão Final`
- registrar decisão de gate no template: `templates/revisao-dod-artefato.md`

Se houver pendência crítica de evidência, amostra, exceção ou conclusão, manter status `em revisão` e não classificar como teste fechado.

## Output

- objetivo e critério do teste
- tipo de teste executado (ToD/ToE)
- amostra e evidências revisadas
- exceções identificadas com detalhe
- conclusão sobre o controle
- encaminhamento: fechar o teste ou acionar finding-drafting

## Output Format

1. controle testado e critério
2. procedimento executado
3. exceções encontradas (se houver)
4. conclusão
5. próximo passo
