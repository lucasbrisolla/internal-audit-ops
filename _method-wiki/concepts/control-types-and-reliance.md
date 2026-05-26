# Tipos de Controle e Implicações para Reliance

> Fonte primária: referencial metodológico consolidado.
> Aplicação: walkthrough-standardization, test-execution, risk-control-mapping, finding-drafting.

---

## 1. Classificação por Modo de Execução

| Tipo | Definição | Implicação para teste |
|---|---|---|
| **Manual** | Executado por pessoa sem dependência relevante de informação de sistema | Amostra representativa; variabilidade humana é risco |
| **IT-dependent** | Execução humana depende de relatório, extração ou informação gerada por sistema | Testar controle + confiabilidade da informação usada (IPE) |
| **Application control** | Lógica parametrizada no sistema executa o controle automaticamente | 1–2 instâncias se ITGCs eficazes; risco é de programação incorreta |

### Controles híbridos

Sistema gera exceções (parte automatizada) → revisor analisa e resolve (parte manual). **Ambas as partes precisam ser eficazes.** Falha comum: testar apenas o output do sistema sem verificar se as exceções foram de fato resolvidas adequadamente.

---

## 2. Classificação por Natureza (Quando Age)

| Dimensão | Preventivo | Detectivo |
|---|---|---|
| **Quando age** | Antes ou durante o processamento | Após o fato |
| **Objetivo** | Impedir que o erro entre nos registros | Identificar erros já lançados |
| **Custo típico** | Maior — aplicado em cada transação | Menor — pode ser periódico |
| **Tempestividade** | Erro nunca chega aos livros | Erro pode permanecer por período extenso |
| **Risco se ausente** | Erros entram sem barreira | Erros distorcem reporting intermediário e decisões de gestão |
| **Exemplo** | Limite de aprovação no ERP antes de pagamento | Conciliação bancária mensal |

### Trade-off custo × timing

Controles preventivos têm custo maior por operar em cada transação, mas eliminam o risco de erro nos registros. Detectivos são mais baratos mas expõem a entidade a distorções em relatórios intermediários e a decisões baseadas em dados incorretos. A escolha deve refletir a magnitude e frequência do risco — áreas de alto risco justificam redundância preventiva.

### Princípio da detecção + correção

**Todo controle — preventivo ou detectivo — precisa de dois elementos para ser eficaz:**
1. **Identificação do desvio** — o controle detecta o erro ou condição indesejada
2. **Correção comunicada a quem pode agir** — existe processo documentado de resolução

Controle que identifica o problema mas não gera correção não é eficaz. Esse é o ponto de falha mais comum em controles detectivos: a exceção é gerada, mas não há evidência de que foi investigada e resolvida.

---

## 3. Redundância como Princípio Deliberado

Combinar preventivos + detectivos com sobreposição intencional é mais robusto do que depender de um único controle para cada risco. COSO e padrões de auditoria não prescrevem proporção — a entidade decide com base em eficiência e magnitude do risco.

Exemplo: estoque de alto valor → contagem física mensal (detectivo) + tag eletrônico na saída (preventivo). Ambos cobrem o mesmo risco de perda; a falha de um não elimina a cobertura.

---

## 4. Controles Automatizados — Vantagens e Riscos

| Dimensão | Automatizado | Manual |
|---|---|---|
| **Consistência** | Alta — opera igualmente em todas as transações | Variável — depende de atenção e julgamento |
| **Override** | Difícil sem deixar rastro | Suscetível a pressão e exceções informais |
| **Falha** | Erra de forma consistente (risco de programação incorreta) | Erro é isolado e irregular |
| **Evidência** | 1–2 instâncias suficientes se ITGCs são eficazes | Amostra representativa sempre necessária |
| **Dependência** | ITGCs comprometidos invalidam reliance | Independente de ITGCs |

Automatizados são preferíveis quando o volume de transações é alto e o risco de erro humano é relevante. A vantagem de consistência só se sustenta se ITGCs (segurança, change management) estiverem eficazes — um controle automatizado com ITGCs fracos não garante que a lógica opera como descrita e testada.

---

## 5. Implicações para Reliance

| Condição | Impacto |
|---|---|
| Controle eficaz (design + operação) | Pode reduzir extensão de evidência substantiva |
| Controle com deficiência de design | Sem reliance; aumentar testes substantivos |
| Controle com deficiência de operação | Sem reliance; extensão depende da severidade |
| Controle compensatório | Reliance parcial — verificar se cobre magnitude real do risco residual |
| Controle IT-dependent com IPE não confiável | Sem reliance na parte dependente; testar IPE antes |
| Application control com ITGC fraco | Sem garantia de consistência; tratar como manual para fins de amostragem |

---

## 6. Perguntas de Classificação (Walkthrough)

- O controle depende de relatório, extração ou informação de sistema?
- Se sim: a informação usada foi testada como IPE confiável?
- O controle age antes ou depois do processamento?
- Quando uma exceção é identificada, quem é notificado e como é resolvida?
- Existe evidência de que exceções foram investigadas e encerradas?
- Se o controle falhar, há outro controle que cobriria o mesmo risco?

---

## 7. Red Flags

- Classificar como manual um controle que usa relatório de sistema sem testar a confiabilidade do relatório
- Aceitar "o sistema faz isso automaticamente" sem verificar ITGCs e parâmetros
- Tratar controle compensatório como suficiente sem avaliar se cobre a magnitude real do risco remanescente
- Concluir que controle detectivo é eficaz sem evidência de resolução das exceções identificadas
- Downgrade de deficiência transacional com argumento de que "a gestão pegaria no review" (ver armadilha de monitoring em `concepts/control-activities-framework.md` Seção 9)

---

## Conexões Internas

- `concepts/control-activities-framework.md` — framework completo P10–P12 incluindo ITGCs, SoD, service orgs e P12
- `concepts/sample-size.md` — como o tipo de controle determina o N de amostra
- `concepts/evidence-and-testing-foundations.md` — hierarquia de evidência e condições de força
- `patterns/control-design-and-operating-effectiveness.md` — avaliação de design vs. operação
- `patterns/control-deficiency-severity.md` — quando a falha de um tipo de controle gera SD vs. MW
- `checklists/control-attribute-design.md` — atributos de documentação de controle individual
- `processes/ipe-reliability-assessment.md` — confiabilidade de informação usada em controles IT-dependent
