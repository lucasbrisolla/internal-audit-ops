# Exemplo — Operating Model Analysis: Transformação SSC + Finance Business Partner

**Tipo de input:** slide de "Nova Organização" apresentado em encontro gerencial interno  
**Contexto:** grupo industrial global, múltiplas regiões, migração de plataformas regionais para SSC + FBP  
**Skill aplicada:** `operating-model-analysis`

---

## Input bruto

```
Nova Organização

From regional platforms (2016–2023):
- 6 plataformas regionais (NA, SA, EA, ME, SEA, região extra)
- Cada plataforma com operações PTP, RTR, OTC para entidades da sua região
- 1 plataforma global de suporte transacional paralela

To SSC and Finance Business Partner (FBP) model (from 2024):
- 1 SSC global entregando atividades transacionais (PTP, RTR, OTC) para todas as entidades
- Finance Business Partners regionais colocados próximos ao negócio
- Resultado declarado: aprox. -30% custos pessoal
```

---

## Output do operating-model-analysis

### 1. Leitura da Transformação

Não é melhoria de controle. É **desmontagem industrial do trabalho financeiro**: separação entre processamento padronizável (SSC — fábrica) e julgamento contextual (FBP — artesanato de negócio). O -30% de pessoal não veio de uma alavanca — veio de quatro simultâneas que COSO/ERM não nomeiam.

---

### 2. Alavancas reais do resultado declarado

| Alavanca | Mecanismo | Framework por trás |
|---|---|---|
| Arbitragem geográfica | Trabalho contábil de entidade europeia/americana realocado para SSC de custo menor | Teoria do comércio, custo de mão-de-obra |
| Deslocamento de seniority | Processo padronizado exige nível médio de cargo menor; diferença salarial captura valor | Braverman — degradação qualificada do trabalho |
| Eliminação de redundância | 6 × fechamento mensal, 6 × reconciliação, 6 × PTP → 1 time centralizado | Economias de escala (Coase) |
| Pré-condição para automação | 1 plataforma única viabiliza RPA/IA em escala; 6 plataformas tornariam inviável | Teoria da plataforma; fase 2 do corte |

---

### 3. Riscos emergentes da estrutura

| Risco | Tipo | Mecanismo | Severidade | Status |
|---|---|---|---|---|
| Handshake SSC ↔ entidade local sem accountability clara | Interface | Quando número errado, ninguém sabe quem responde | Alta | Hipótese — verificar |
| Single point of failure operacional global | Concentração | Falha regional = impacto local antes; falha SSC = parada global agora | Alta | Estrutural — BCP? |
| Compliance local não coberto pelo processo padronizado | Padronização | BR, FR, EUA têm obrigações fiscais/contábeis distintas; processo único cria gap | Alta | Verificar por jurisdição |
| Controles não revalidados no novo modelo | Transição | Controles antigos desativados; SSC ainda imaturo; primeiro exercício = gap provável | Alta | Primeiro ano pós-go-live |
| Knowledge drain | Transição | Especialistas locais dispensados; conhecimento tácito não transferido ao SSC | Média | Difícil quantificar |
| FBP em risco de obsolescência | Modelo | RPA/IA automatiza SSC; FBP precisa evoluir para gestor de exceção ou vira custo dispensável | Média | Horizonte 3–5 anos |

---

### 4. Redistribuição de poder

| Papel | Antes | Depois |
|---|---|---|
| CFO regional | Controlava número e processo — feudo | Perdeu equipe de processamento; virou gerente SSC (menor escopo) ou FBP (sem operação) |
| Analista financeiro local | Processamento + análise — escopo amplo | Cindido: SSC = operador de processo; FBP = analista sem equipe |
| Audit interno | Auditava processo com estrutura estável | Precisa auditar interface SSC ↔ entidade + concentração + padronização vs. idiossincrasia |

Não é decisão de controle — é design organizacional. Coase aplicado.

---

### 5. Ângulo de auditoria prioritário

1. **Teste de handshake SSC ↔ entidade**: existe controle formal de reconciliação e aprovação na interface? Quem aprova o dado antes de entrar no relatório financeiro local?
2. **Alçadas pós-migração**: quem tem acesso e aprovação no ERP central? Configuração revalidada ou transferida do modelo antigo?
3. **Cobertura regulatória por jurisdição**: processo padronizado do SSC cobre obrigações locais de cada entidade? Amostra em 3–5 jurisdições críticas.
4. **BCP do SSC**: existe plano de continuidade para single point of failure? RTO/RPO definidos?
5. **Maturidade do ambiente de controle**: primeiro ano — não comparar com operação estável. Baseline precisa ser estabelecido, não assumido.

---

### 6. Posicionamento

> **Pergunta-chave para o cliente:** "Como está definida a accountability no handshake entre SSC e cada entidade — quem responde quando o número está errado?"
>
> **Argumento de valor do auditor:** "O desafio não é controlar melhor dentro do processo existente. É garantir que a nova estrutura tem accountability clara nos pontos de interface, que a padronização não criou gap de compliance local, e que o ambiente de controle foi revalidado — não apenas assumido como transferido."
>
> **O que não está nos manuais:** COSO/ERM mapeiam risco dentro de processo dado. Aqui o processo foi reconstruído. O risco principal não é de transação — é de estrutura.

---

### 7. Próximo uso recomendado

1. **`risk-control-mapping`** — riscos de interface e concentração acima como input de WCGW
2. **`audit-planning`** — ponto de controle explícito para primeiro exercício pós-go-live; SSC como entidade auditável separada
3. **`walkthrough-standardization`** — walkthrough do processo SSC, não só das entidades locais
