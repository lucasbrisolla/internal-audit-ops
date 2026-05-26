# Tamanho de Amostra — Testes de Controles

> Fonte primária: referencial metodológico consolidado.
> Aplicação: test-execution, audit-planning, qualquer procedimento de amostragem em testes de controle.

---

## 1. Quando Amostragem Se Aplica (e Quando Não)

### Situações com amostragem

- Controles transacionais de alta frequência: aprovações de pagamento, lançamentos de venda, conciliações periódicas
- Verificação de atributos em populações: assinaturas de autorização, checklist de aprovação, evidência de revisão

### Situações sem amostragem (julgamento analítico)

- Segregação de funções — análise de compatibilidade de perfis, não seleção aleatória
- Ambiente de controle (tom do topo, competência de governança) — observação, entrevistas, análise de atas
- ITGCs: acesso e segurança, mudanças de sistema — inspeção, análise de matriz de acessos
- Controles automatizados testados via 1–2 instâncias (ver seção 5)

---

## 2. Parâmetros de Amostragem (Atributos)

Todo tamanho de amostra é derivado de quatro parâmetros. Definir os quatro antes de calcular.

| Parâmetro | O que é | Guia prático |
|---|---|---|
| **Risco / Confiança** | Risco aceitável de aceitar controle falho. Confiança = 100% − Risco | Testes de confiabilidade alta: 90%. Controles críticos (receita, fraude): 95%+. Revisão de trabalho de terceiros: 50–70% |
| **Taxa de Desvio Tolerável (T)** | Frequência de falha que mudaria a decisão de confiar no controle | Para reliance alto: ≤10%. Controles críticos: ≤5%. Não é a taxa esperada de erro financeiro |
| **Taxa de Desvio Esperada** | Desvios previstos na amostra com base em histórico | 0% se controle novo/sem histórico. 1–2% se histórico limpo. >5% sugere remediar antes de testar |
| **Tamanho da População** | Total de ocorrências do controle no período | >2.000 instâncias: fator negligível. <500: usar tabela ou software com população real |

---

## 3. Fórmula Rápida (Zero Desvios Esperados, Populações Grandes)

```
N = F / T
```

Onde:
- **N** = tamanho da amostra
- **F** = fator de confiança (tabela abaixo)
- **T** = taxa tolerável expressa como decimal (ex: 10% → 0,10)

### Tabela de Fatores F

| Confiança | 99% | 95% | 90% | 87% | 80% | 75% | 63% | 50% |
|---|---|---|---|---|---|---|---|---|
| **Fator F** | 4,61 | 3,00 | 2,31 | 2,00 | 1,61 | 1,39 | 1,00 | 0,70 |

### Exemplos rápidos

| Confiança | Tolerável | N calculado | Uso típico |
|---|---|---|---|
| 90% | 10% | **23** | Controle de alta frequência, reliance padrão |
| 90% | 5% | **46** | Controle importante, reliance alto |
| 95% | 5% | **60** | Controle crítico (receita, acesso) |
| 90% | 10% com 1 desvio esperado | **45** | Dobrar N quando esperar desvio |
| 70% | 10% | **14** | Revisão de trabalho de AI/terceiros |

> Para permitir até 1 desvio sem reprovar o teste: **dobrar o N calculado pela fórmula**.

---

## 4. Controles de Baixa Frequência (Populações Pequenas)

Usar a tabela abaixo quando o controle opera poucas vezes no ano. Não aplicar a fórmula acima nesses casos.

### Tabela de Controles Infrequentes (Tabela 8.1 — referencial metodológico / AICPA AAG-S)

| Frequência do Controle | N recomendado |
|---|---|
| Trimestral (4 ocorrências) | **2** |
| Mensal (12 ocorrências) | **2–4** |
| Quinzenal (24 ocorrências) | **3–8** |
| Semanal (52 ocorrências) | **5–9** |

> Premissa: qualquer desvio em população pequena indica controle ineficaz. Não há margem para desvio esperado nessas tabelas.

---

## 5. Tabela de Referência Rápida (90% de Confiança)

Tabela 8A.1 adaptada de AICPA AAG-S. Números fora dos parênteses = N da amostra. Número entre parênteses = desvios toleráveis.

| Taxa Esperada | Tolerável 5% | Tolerável 6% | Tolerável 7% | Tolerável 8% | Tolerável 10% | Tolerável 15% | Tolerável 20% |
|---|---|---|---|---|---|---|---|
| **0,00%** | 45 (0) | 38 (0) | 32 (0) | 28 (0) | 22 (0) | 15 (0) | 11 (0) |
| **0,50%** | 77 (1) | 64 (1) | 55 (1) | 48 (1) | 38 (1) | 25 (1) | 18 (1) |
| **1,00%** | 77 (1) | 64 (1) | 55 (1) | 48 (1) | 38 (1) | 25 (1) | 18 (1) |
| **1,50%** | 105 (2) | 64 (1) | 55 (1) | 48 (1) | 38 (1) | 25 (1) | 18 (1) |
| **2,00%** | 132 (3) | 88 (2) | 75 (2) | 48 (1) | 38 (1) | 25 (1) | 18 (1) |
| **2,50%** | 158 (4) | 110 (3) | 75 (2) | 65 (2) | 38 (2) | 25 (1) | 18 (1) |
| **3,00%** | * | 132 (4) | 94 (3) | 65 (2) | 52 (2) | 25 (1) | 18 (1) |

`*` = impraticável (tolerável e esperado muito próximos — usar software).

---

## 6. Amostragem Sequencial em Dois Estágios

Usar quando a taxa esperada é desconhecida (controle novo, pós-remediação, primeiro teste). Permite parar no estágio 1 se não houver desvio.

**Regra:**
- 0 desvios no estágio 1 → aprovado com 90% de confiança
- 1 desvio no estágio 1 → continuar ao estágio 2
- 2 desvios totais → reprovar; remediar o controle antes de novo teste

### Tabela 8A.2 — Plano Sequencial (90% Confiança)

| Taxa Tolerável | N Estágio 1 | N Estágio 2 (adicional) |
|---|---|---|
| 10% | 23 | 29 |
| 9% | 26 | 30 |
| 8% | 30 | 30 |
| 7% | 35 | 32 |
| 6% | 41 | 38 |
| 5% | 51 | 39 |
| 4% | 64 | 49 |
| 3% | 89 | 56 |
| 2% | 133 | 87 |

---

## 7. Controles Automatizados (ITGCs como Pré-condição)

Controles programados no sistema (application controls) têm tratamento especial:

- **1–2 instâncias** podem ser suficientes para estabelecer operação efetiva, **se** ITGCs forem testados e eficazes
- Se ITGCs estiverem comprometidos, os testes de controles automatizados são invalidados
- O processo manual que trata as exceções geradas pelo controle automatizado ainda exige amostra representativa

> Premissa: um controle automatizado que funciona corretamente uma vez funciona consistentemente para todas as transações — desde que o ambiente TI seja controlado.

---

## 8. Fatores que Aumentam ou Diminuem o N

Esses fatores são refletidos principalmente no parâmetro de risco ao configurar o plano de amostragem.

| Fator | Aumenta N | Diminui N |
|---|---|---|
| Frequência do controle | Alta (múltiplas vezes/dia) | Baixa (mensal) |
| Importância do controle | Alto — endereça múltiplas asserções ou é detective | Periférico, complementar |
| Julgamento exigido | Alto grau de julgamento humano | Processo simples, mecânico |
| Complexidade do procedimento | Controle complexo | Controle simples |
| Competência do executor | Alta competência (mais crítico avaliar) | Menor competência (menor reliance potencial) |

---

## 9. Regra de Decisão Pós-Amostragem

### Zero desvios encontrados
→ Amostra suporta o nível de confiança planejado. Documentar parâmetros + resultado.

### 1 desvio encontrado (não planejado)
→ Teste reprova para o nível de confiança original. Opções:
1. **Dobrar o N original** e realizar segundo estágio (ex: planejou 45 → testar mais 45)
2. Reduzir reliance no controle (aceitar nível menor de assurance)
3. Remediar o controle e retestar após remediação

> Adicionar "alguns itens extras" ao N original não tem efeito estatístico — não diluiu o resultado do desvio.

### Múltiplos desvios
→ Não aumentar amostra. Investigar causa → remediar → retestar.

---

## 10. Análise Qualitativa dos Desvios

Um desvio não é apenas um número — analise a natureza antes de aceitar mesmo dentro do limite tolerável:

| Tipo de Desvio | Ação |
|---|---|
| **Desvio isolado / erro humano pontual** | Documentar, avaliar se impacto financeiro é remoto |
| **Indicação de override de gestão** | Escalar imediatamente; pode ser Red Flag de fraude |
| **Fraude ou falha intencional** | Não aceitar como desvio normal; comunicar independentemente do N |
| **Erro sistemático (bug, glitch)** | Assumir que a *população toda* foi afetada; expandir escopo |

> O desvio encontrado na amostra é representativo da população — não um outlier isolado. Nunca dispensar desvio como "exceção única" sem investigação.

---

## 11. Timing dos Testes

### Testes intermediários (antes do fechamento)

Quando o teste é realizado antes do final do período, é necessário "fechar o gap" até a data-base:

1. Calcular N com base na população estimada do ano inteiro (ex: 22 itens para 1.000 transações anuais)
2. Testar proporcionalmente até a data do teste (ex: 20 itens para 900 transações até outubro)
3. Complementar próximo ao encerramento (ex: 2 itens restantes em dezembro)

Gap pequeno (<2 meses): indagação + walkthrough pode ser suficiente.
Gap maior: exige testes adicionais — simples inquiry não fecha o gap.

### Identificação precoce de desvios

Se desvios excederem o tolerável ainda no meio do ano:
→ **Remediar imediatamente**, não esperar o encerramento
→ Controle não remediado invalida reliance para todo o período não coberto

---

## 12. Documentação Mínima do Plano de Amostragem

Para cada teste que usa amostragem, documentar:

- [ ] Objetivo do teste (qual controle, qual asserção)
- [ ] Parâmetros: confiança %, tolerável %, esperado %
- [ ] Tamanho da população e fonte (IPE verificado)
- [ ] N calculado e método (fórmula / tabela / software)
- [ ] Período coberto e data de execução
- [ ] Número de desvios encontrados
- [ ] Análise qualitativa de cada desvio
- [ ] Conclusão: suporta / não suporta o nível de confiança planejado

---

## 13. Top-Down e Sequência de Teste

Antes de dimensionar amostras, definir a **sequência de avaliação**:

1. Ambiente de controle e ITGCs primeiro — deficiências aqui têm impacto pervasivo e podem invalidar testes transacionais
2. Controles compartilhados (caixa, folha, pagamentos) — testar uma única vez, referenciar em todos os processos que os utilizam
3. Controles transacionais por ciclo — usar os Ns desta referência

**Por que importa para o N:** se ITGCs forem deficientes, testes de controles automatizados precisam ser refeitos com amostra transacional completa — o benefício do "1–2 instâncias" para automated controls desaparece. Identificar ITGCs no início evita retrabalho.

### Confusão frequente: sample sizes de 25/40/60

Esses números vêm de guidance de A-133 (programas federais), não de AICPA AAG-S para controles de reporte financeiro. Quando alguém sugere fixar o N em 25, 40 ou 60 sem discutir parâmetros (risco, tolerável, esperado), provavelmente está aplicando guidance errada ao contexto.

**Regra:** o N resulta dos parâmetros. Se os parâmetros não estão documentados, o N não está justificado.

---

## 14. Documentação do Processo de Amostragem — Campos Obrigatórios

Além dos parâmetros de dimensionamento (seção 12), cada aplicação de amostragem requer documentação de campos específicos que suportam a conclusão e permitem revisão independente.

### Campos obrigatórios por teste amostral

| Campo | Conteúdo esperado |
|---|---|
| **Controle sendo testado** | ID e descrição do controle; X-Ref ao work paper do controle |
| **Asserção(ões) primária(s)** | Ex: Occurrence, Valuation |
| **Descrição da população** | O que compõe a população (ex: "cheques emitidos acima de R$ 5.000") |
| **Como completude foi garantida** | Sequência numérica verificada? Busca por itens logo abaixo do threshold? |
| **Procedimento de teste** | O que será examinado em cada item selecionado |
| **Definição de exceção** | Critério preciso de falha — definir antes de executar, não depois de encontrar desvio |
| **Método de seleção** | Aleatório sistemático, haphazard, estratificado |
| **Nível de asseguração desejado** | Normalmente alto (90%); registrar se diferente e justificar |
| **Reliance em trabalho de terceiros** | Se IA ou outro testou parte da população, a confiança necessária deste teste pode ser reduzida — documentar explicitamente |
| **Controle "unusually important"?** | Se sim: usar tolerable deviation menor (ex: 2%) e/ou confiança maior (ex: 95%) |
| **Parâmetros** | Confiança %, Tolerável %, Esperado %, N calculado, fonte (tabela/fórmula/software) |
| **Resultados** | Número de desvios; descrição de cada um |
| **Avaliação qualitativa dos desvios** | Ver seção 10 — desvio isolado vs. sistemático vs. indicação de fraude |
| **Conclusão** | Suporta / não suporta o nível de confiança planejado |
| **Deficiência identificada?** | Se sim: severidade e X-Ref ao deficiency summary |

### Por que definição de exceção vem antes

Definir a exceção após ver os resultados cria viés de confirmação — o avaliador tende a enquadrar o achado como "dentro do esperado". A definição prévia força o critério a ser independente do resultado.

---

## Conexões Internas

- `workflows/test-execution.md` — usa os Ns desta referência ao definir extensão de cada teste
- `concepts/evidence-and-testing-foundations.md` — tipos de evidência, walkthrough, top-down concept e situações sem amostragem
- `_method-wiki/concepts/scoping-strategy.md` — define o que entra no escopo antes de dimensionar testes
- `context/standards/sox.md` — requisitos SOX de tamanho de amostra quando o trabalho estiver na trilha externa
- `_method-wiki-external-audit/workflows/finding-rating-external-audit.md` — usar em conjunto quando a extensao de teste influenciar classificacao de deficiencia SOX
- `skills/control-evaluation.md` — avalia qualidade do controle; informa o parâmetro de risco da amostra
- `context/tests-master.json` — testes típicos por tipo de controle; inclui campo de evidência por força
