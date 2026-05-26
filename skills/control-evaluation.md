# skill: control-evaluation

## Goal

Avaliar a qualidade de um controle contra 9 atributos ponderados, produzindo score de maturidade, classificação e lacunas prioritárias. Focado em auditoria interna — não exige ancoragem em assertiva de DF.

## Use When

- avaliar se controle existente mitiga adequadamente um risco mapeado
- pontuar controles na RCM após teste de desenho e efetividade
- identificar fragilidades específicas antes de recomendar remediação
- comparar controles de mesma natureza entre processos ou períodos

## Inputs

- descrição do controle (o que faz, quem executa, quando, com que evidência)
- resultado do teste de desenho, se disponível
- resultado do teste de efetividade, se disponível
- contexto do risco que o controle deve mitigar

## Atributos e Pesos

| # | Atributo | Peso |
|---|---|---|
| 1 | Desenho do Controle | 15% |
| 2 | Execução / Operação | **40%** |
| 3 | Documentação e Evidência | 10% |
| 4 | Periodicidade | 5% |
| 5 | Responsabilidade Clara | 5% |
| 6 | Segregação de Funções | 10% |
| 7 | Automação | 5% |
| 8 | Resposta a Falhas | 5% |
| 9 | Atualização e Revisão | 5% |

Score = Σ (nota_normalizada × peso), onde nota_normalizada = nota / 5.

## Escala de Maturidade por Atributo (1–5)

### 1. Desenho do Controle
| Nível | Descrição |
|---|---|
| 1 | Inexistente, informal ou genérico — não previne nem detecta falha |
| 2 | Existe mas é frágil ou parcialmente documentado — mitiga de forma limitada |
| 3 | Desenhado com base no risco, documentação básica — pontos de fragilidade possíveis |
| 4 | Bem desenhado, formalizado, alinhado ao risco e às boas práticas |
| 5 | Previne e detecta falhas — desenho robusto e completo |

### 2. Execução / Operação
| Nível | Descrição |
|---|---|
| 1 | Não executado, esporádico ou informal — sem registros confiáveis |
| 2 | Executado ocasionalmente ou de forma inconsistente — evidências incompletas |
| 3 | Executado conforme previsto na maioria das vezes — falhas pontuais possíveis |
| 4 | Executado de forma consistente, tempestiva e com evidências completas — supervisão presente |
| 5 | Execução automatizada ou com evidências geradas automaticamente — monitoramento contínuo |

### 3. Documentação e Evidência
| Nível | Descrição |
|---|---|
| 1 | Sem evidências ou evidências informais/adulteráveis — sem critério de guarda |
| 2 | Evidência parcial ou pontual — desorganizada, sem padronização, risco de perda |
| 3 | Evidências mantidas regularmente — falta padronização ou completude |
| 4 | Evidências completas, organizadas, rastreáveis e acessíveis |
| 5 | Geradas automaticamente em tempo real — total rastreabilidade e integridade |

### 4. Periodicidade
| Nível | Descrição |
|---|---|
| 1 | Sem frequência definida — execução reativa ou aleatória |
| 2 | Frequência empírica, sem análise do risco — execução esporádica |
| 3 | Periodicidade definida e aplicada consistentemente — revisões ocasionais |
| 4 | Frequência baseada em análise de risco — desvios monitorados e tratados |
| 5 | Frequência dinâmica integrada à gestão de risco — ajuste automático |

### 5. Responsabilidade Clara
| Nível | Descrição |
|---|---|
| 1 | Sem responsável formal — qualquer pessoa disponível executa |
| 2 | Responsável conhecido informalmente — sem designação oficial, < 6 meses no controle |
| 3 | Formalmente designado, conhecimento básico — 6 meses a 1 ano no controle |
| 4 | Designado com atribuições claras, treinado, autônomo — 1 a 2 anos no controle |
| 5 | Alta capacitação, visão crítica, participação na revisão do controle — > 2 anos, plano de sucessão |

### 6. Segregação de Funções
| Nível | Descrição |
|---|---|
| 1 | Sem segregação — mesma pessoa executa, aprova e monitora |
| 2 | Segregação informal, por bom senso — sobreposição de funções críticas sem compensação |
| 3 | Segregação parcial — execução e aprovação geralmente separadas, exceções não documentadas |
| 4 | Segregação clara e formal — exceções documentadas com controles compensatórios |
| 5 | Integrada aos sistemas — controles automatizados impedem ou alertam sobre conflitos |

### 7. Automação
| Nível | Descrição |
|---|---|
| 1 | Totalmente manual — planilhas, e-mails, ação humana repetitiva |
| 2 | Manual com algum suporte sistêmico — sem integração ou validação automática |
| 3 | Parcialmente automatizado — exige ação humana para conclusão |
| 4 | Majoritariamente automatizado — ação humana limitada a exceções |
| 5 | 100% automatizado — validações em tempo real, bloqueio de transações irregulares |

### 8. Resposta a Falhas
| Nível | Descrição |
|---|---|
| 1 | Sem processo de identificação — falhas ocultadas ou tratadas só após impacto grande |
| 2 | Tratamento reativo caso a caso — sem investigação ou registro sistemático |
| 3 | Mecanismos mínimos de identificação e tratamento — ações corretivas pontuais |
| 4 | Processo estruturado — causa raiz, plano de ação, prevenção documentada |
| 5 | Monitoramento contínuo — detecção antecipada, resposta automatizada, dashboards |

### 9. Atualização e Revisão
| Nível | Descrição |
|---|---|
| 1 | Nunca revisado — alterações no processo não atualizam o controle |
| 2 | Revisão só após falha ou auditoria — sem periodicidade definida |
| 3 | Revisões periódicas sem cronograma formal — mudanças relevantes geralmente geram atualização |
| 4 | Revisão formal periódica (anual ou semestral) — histórico de alterações documentado |
| 5 | Revisão contínua com tecnologia — qualquer mudança aciona análise automática |

## Escala de Risco (referência para severidade do risco mitigado)

| Nível | Label | Código |
|---|---|---|
| 1 | Baixo | A |
| 2 | Moderado | B |
| 3 | Significativo | C |
| 4 | Alto | D |

Score de risco = heat map pré-definido por combinação Impacto × Probabilidade:

| Impacto ↓ / Prob → | Improvável (1) | Possível (2) | Provável (3) | Quase Certo (4) |
|---|---|---|---|---|
| Baixo (1) | 1 | 3 | — | — |
| Moderado (2) | 2 | 6 | 10 | — |
| Significativo (3) | — | 9 | 13 | — |
| Alto (4) | — | — | — | 16 |

Classificação: 1–3 = Baixo / 4–9 = Moderado / 10–12 = Alto / 13–16 = Crítico

**Atenção:** os critérios de enquadramento (o que é impacto Baixo vs Alto neste negócio) devem ser definidos por engagement — thresholds financeiros, volumétricos e de compliance específicos do cliente. Sem isso, a classificação é subjetiva.

## Bandas de Resultado

| Score ponderado | Resultado |
|---|---|
| 90% – 100% (≥ 0,90) | Satisfatório |
| 75% – 89% (0,75 – 0,89) | Satisfatório com melhorias |
| 60% – 74% (0,60 – 0,74) | Requer melhorias significativas |
| Abaixo de 60% (< 0,60) | Não satisfatório |

Regra especial: se Execução/Operação (peso 40%) = nível 1 ou 2 → resultado máximo é **Requer melhorias significativas**, independente dos outros atributos.

## Decision Rules

- Não concluir Satisfatório se efetividade não foi testada — registrar como "A confirmar"
- Execução é o atributo dominante: controle bem desenhado mas não executado = Não satisfatório
- Segregação de funções ausente (nível 1) em controle de alta exposição → flag automático de fraude
- Documentação insuficiente impede conclusão de efetividade — registrar lacuna explicitamente
- Não ajustar nota para cima por "intenção" ou "contexto cultural" — avaliar o que existe, não o que deveria existir

## Output Format

### 1. Ficha do Controle

| Campo | Conteúdo |
|---|---|
| Código | — |
| Risco mitigado | — |
| Descrição resumida | — |
| Tipo | Preventivo / Detectivo |
| Natureza | Manual / Automatizado / Híbrido |
| Frequência | — |
| Owner | — |

### 2. Pontuação por Atributo

| # | Atributo | Nota (1–5) | Peso | Score parcial | Observação |
|---|---|---|---|---|---|
| 1 | Desenho | | 15% | | |
| 2 | Execução | | 40% | | |
| 3 | Documentação | | 10% | | |
| 4 | Periodicidade | | 5% | | |
| 5 | Responsabilidade | | 5% | | |
| 6 | Segregação | | 10% | | |
| 7 | Automação | | 5% | | |
| 8 | Resposta a Falhas | | 5% | | |
| 9 | Atualização | | 5% | | |
| | **Total** | | 100% | **X,XX** | |

### 3. Resultado e Fragilidades

> **Resultado:** Satisfatório / Satisfatório com melhorias / Requer melhorias significativas / Não satisfatório
> **Atributo mais fraco:** [atributo] — [descrição da lacuna]
> **Flag crítico:** [se segregação ausente ou execução nível 1]

### 4. Recomendação

Uma ação objetiva por fragilidade identificada. Separar ação imediata de melhoria estrutural.
