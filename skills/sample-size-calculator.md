# skill: sample-size-calculator

## Goal

Determinar o tamanho de amostra (N) defensável para um teste de controle, com base nos parâmetros técnicos relevantes, e documentar a justificativa.

## Use When

- iniciando teste de controle transacional e precisando definir tamanho de amostra
- revisando se um N proposto é estatisticamente defensável
- definindo plano de amostragem em `test-execution.md` Step 3
- planejamento de extensão de teste em `audit-planning.md`

## Inputs

- tipo de controle: transacional (alta frequência) / infrequente (mensal, trimestral) / automatizado
- frequência do controle: diário, semanal, mensal, trimestral, anual
- nível de risco / importância: padrão (90% confiança) / crítico (95% confiança) / revisão de terceiros (50–70%)
- taxa de desvio tolerável: ≤5% (crítico) / ≤10% (padrão)
- taxa de desvio esperada: 0% (sem histórico de falha) / >0% (histórico ou suspeita)
- tamanho da população (quando < 2.000)

## Execution Sequence

### 1. Classificar o tipo de controle

**Controle automatizado (application control)**:
- N = 1–2 instâncias **se** ITGCs forem eficazes e testados
- Se ITGCs forem deficientes: o benefício cai — testar com amostra transacional completa
- Documentar explicitamente: "N reduzido por reliance em ITGCs eficazes"

**Controle infrequente (frequência baixa)**:
Usar tabela de controles infrequentes — não aplicar fórmula N=F/T:

| Frequência | N recomendado |
|---|---|
| Trimestral (4 ocorrências) | 2 |
| Mensal (12 ocorrências) | 2–4 |
| Quinzenal (24 ocorrências) | 3–8 |
| Semanal (52 ocorrências) | 5–9 |

> Premissa: qualquer desvio em população pequena = controle ineficaz. Sem margem para desvio esperado.

**Controle transacional (alta frequência)**:
Seguir Steps 2–5.

### 2. Definir os quatro parâmetros

Definir **todos** os quatro antes de calcular. N sem parâmetros documentados não está justificado.

| Parâmetro | Guia |
|---|---|
| **Confiança** | 90% (padrão) / 95% (controle crítico: receita, fraude, acesso) / 50–70% (revisão de trabalho de terceiros/IA) |
| **Taxa tolerável (T)** | ≤10% (reliance padrão) / ≤5% (controle crítico) |
| **Taxa esperada** | 0% se sem histórico / 1–2% se histórico limpo / >5% = remediar antes de testar |
| **População** | >2.000: fator negligível / <500: usar tabela com N real |

### 3. Calcular N com fórmula rápida (zero desvios esperados, população grande)

```
N = F / T
```

**Tabela de fatores F:**

| Confiança | 99% | 95% | 90% | 87% | 80% | 75% | 63% | 50% |
|---|---|---|---|---|---|---|---|---|
| Fator F | 4,61 | 3,00 | 2,31 | 2,00 | 1,61 | 1,39 | 1,00 | 0,70 |

**Referência rápida (casos mais comuns):**

| Confiança | Tolerável | N | Uso típico |
|---|---|---|---|
| 90% | 10% | **23** | Controle transacional, reliance padrão |
| 90% | 5% | **46** | Controle importante, reliance alto |
| 95% | 5% | **60** | Controle crítico (receita, acesso) |
| 70% | 10% | **14** | Revisão de trabalho de AI / terceiros |

> **Regra**: se desvio esperado > 0%, dobrar N. Um desvio esperado = dobrar o N da fórmula base.

### 4. Quando taxa esperada > 0%: usar tabela AICPA (90% confiança)

> Nota de arredondamento: para 0% esperado e 10% tolerável, a fórmula N=F/T retorna 23 (2,31/0,10); a tabela AICPA publicada abaixo retorna 22. Diferença entre aproximação Poisson e tabela de atributos — ambas são defensáveis. Preferir a tabela AICPA quando disponível, por ser mais precisa.

Números fora dos parênteses = N da amostra. Número entre parênteses = desvios toleráveis:

| Taxa Esperada | Tolerável 5% | Tolerável 7% | Tolerável 10% | Tolerável 15% | Tolerável 20% |
|---|---|---|---|---|---|
| 0,00% | 45 (0) | 32 (0) | 22 (0) | 15 (0) | 11 (0) |
| 0,50% | 77 (1) | 55 (1) | 38 (1) | 25 (1) | 18 (1) |
| 1,00% | 77 (1) | 55 (1) | 38 (1) | 25 (1) | 18 (1) |
| 1,50% | 105 (2) | 55 (1) | 38 (1) | 25 (1) | 18 (1) |
| 2,00% | 132 (3) | 75 (2) | 38 (1) | 25 (1) | 18 (1) |
| 2,50% | 158 (4) | 75 (2) | 38 (2) | 25 (1) | 18 (1) |
| 3,00% | * | 94 (3) | 52 (2) | 25 (1) | 18 (1) |

`*` = impraticável — usar software especializado.

### 5. Quando taxa esperada é desconhecida: amostragem sequencial em dois estágios

Usar quando controle é novo, pós-remediação ou primeiro teste:

| Taxa Tolerável | N Estágio 1 | N Estágio 2 (adicional) |
|---|---|---|
| 10% | 23 | 29 |
| 9% | 26 | 30 |
| 8% | 30 | 30 |
| 7% | 35 | 32 |
| 6% | 41 | 38 |
| 5% | 51 | 39 |

**Regra de decisão sequencial:**
- 0 desvios no estágio 1 → aprovado com 90% de confiança — parar
- 1 desvio no estágio 1 → continuar ao estágio 2
- 2 desvios totais → reprovar; remediar antes de retestar

### 6. Regra de decisão pós-amostragem

**Zero desvios**: amostra suporta o nível de confiança planejado. Documentar parâmetros + resultado.

**1 desvio (não planejado)**: teste reprova para o nível original. Opções:
1. Dobrar o N original e realizar segundo estágio (ex: planejou 45 → testar mais 45)
2. Reduzir reliance no controle (aceitar nível menor de assurance)
3. Remediar e retestar

> Adicionar "alguns itens extras" ao N original não tem efeito estatístico — não dilui o resultado do desvio.

**Múltiplos desvios**: não ampliar amostra. Investigar causa → remediar → retestar.

### 7. Alerta sobre N fixo sem parâmetros

Quando alguém propõe N = 25, 40 ou 60 sem discutir parâmetros, é aplicação de guidance A-133 (programas federais) em contexto errado. O N resulta dos parâmetros — se os parâmetros não estão documentados, o N não está justificado.

## Output

Registrar obrigatoriamente no paper de teste:

- [ ] Tipo de controle (transacional / infrequente / automatizado)
- [ ] Parâmetros: confiança %, tolerável %, esperado %
- [ ] Tamanho da população e fonte (IPE verificado — ver `checklists/ipe-validation-before-test.md`)
- [ ] N calculado e método (fórmula / tabela infrequente / tabela AICPA / sequencial)
- [ ] Período coberto e data de execução
- [ ] Se sequencial: resultado do estágio 1 e decisão

## Conexões Internas

- `_method-wiki/concepts/sample-size.md` — base metodológica completa; consultar para casos não cobertos aqui
- `workflows/test-execution.md` — chamar esta skill no Step 3 (ToE), antes de executar o teste
- `_method-wiki/checklists/ipe-validation-before-test.md` — validar IPE da população antes de aplicar N
- `skills/control-evaluation.md` — avalia qualidade do controle; informa o parâmetro de risco da amostra
- `_method-wiki/patterns/control-deficiency-severity.md` — quando desvio é encontrado, determinar severidade