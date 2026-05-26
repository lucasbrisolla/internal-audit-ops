# Exemplo — Transcript Analysis: Reuniao de Alinhamento ITGC + Migracao ERP

**Tipo de input:** transcricao de reuniao de alinhamento entre equipe de auditoria e diretor financeiro do cliente  
**Contexto:** grupo de grande porte, primeiro ano apos migracao de ERP para plataforma integrada  
**Trilha metodologica:** auditoria interna  
**Workflow aplicado:** `transcript-analysis` → alimenta `risk-control-mapping` e `audit-planning`

---

## Input bruto (transcrição resumida)

```
- Virada do ERP concluída: todas as entidades agora no sistema integrado. Ainda sem
  confiança de que os controles estão funcionando. Oportunidade de não discutir riscos
  de migração só no quarto trimestre — ponto de controle de transição já no interim.

- Resposta a pontos de auditoria anteriores: duas fragilidades de controle ainda em aberto.
  Cliente espera enderecar ate outubro.

- Fechamento contabil: time de TI concordou em implementar melhorias. Reavaliar em
  meados de outubro se as fragilidades remanescentes ainda afetam confiabilidade,
  tempestividade e monitoramento do processo.

- Validar fechamento contabil, contas a receber e folha como prioridades do walkthrough.

- Teste de controle de folha de pagamento: dois angulos — integridade do cadastro e
  controle de acesso (amostra de 25 funcionarios). Modulos de folha em avaliacao.

- Deficiência de conciliação: problema envolve múltiplas contas (contas a receber,
  depósitos judiciais, ativo fixo, fornecedores). Volume alto de informações não
  conciliadas. Conciliação precisa ser feita antes do fechamento, não depois.

- Imobilizado: relatorio auxiliar item a item indisponivel (~50M sem cobertura). Inventario
  fisico nao viavel neste exercicio. Alternativa: inventario de alto valor (top 10 itens
  por entidade) + ciclo ABC para os proximos exercicios.
```

---

## Output do transcript-analysis

### 1. Leitura rápida

Reuniao de alinhamento de auditoria interna em grupo com migracao recente de ERP. Foco em: (1) tratar fragilidades do ciclo anterior antes que se consolidem como reincidencia, (2) mapear impacto da migracao no risco operacional e de controle, (3) calibrar prioridades de inventario e conciliacao para o exercicio.

---

### 2. Processo extraído

| Etapa | Descrição | Ator |
|---|---|---|
| 1 | Avaliação de controles pós-migração ERP | Equipe de TI + auditores |
| 2 | Testes ITGC no interim (agosto–setembro) | Time de IT da firma |
| 3 | Reavaliacao das fragilidades de controle em outubro | Senior + gerente |
| 4 | Walkthrough de fechamento contabil (foco: fechamento, AR e folha) | Equipe de auditoria |
| 5 | Teste de controle de folha: cadastro + acesso (25 funcionarios) | Equipe + CoE |
| 6 | Reconciliacao de contas criticas antes do fechamento | Contabilidade do cliente |
| 7 | Inventario de alto valor de imobilizado (top 10 itens) | Cliente + auditores |

---

### 3. Atores, sistemas e controles identificados

**Atores:**
- Diretor financeiro (cliente) — responsavel pelas fragilidades e cronograma de correcao
- Gerente de contabilidade (cliente) — conciliacoes e fechamento contabil
- Time de TI do cliente — implementacao de melhorias de controle
- Time de IT da firma — ITGC e mapeamento de modulos
- CoE da firma — testes de controle de folha

**Sistemas:**
- ERP integrado (recém-migrado) — módulos: contas a receber, ativo fixo, folha de pagamento
- Sistema legado — integracao via programa de interface financeira ainda em uso para alguns modulos

**Controles identificados:**
- Conciliacao de contas criticas antes do fechamento contabil (preventivo / manual) — **fragil**
- Controles de acesso ao modulo de folha (preventivo / automatizado) — **em avaliacao**
- Controle de migracao de dados (integridade do saldo migrado) — **nao testado ainda**
- Inventario fisico de imobilizado — **inexistente; alternativa sendo negociada**

---

### 4. Sinais de risco identificados

| Risco | Tipo | Evidência na transcrição |
|---|---|---|
| Integridade de dados pos-migracao ERP | TI / completude | "Ainda sem confianca de que os controles estao funcionando" |
| Fechamento contabil sem conciliacoes tempestivas | Processo / acuracia | "Conciliacao precisa ser feita antes do fechamento, nao depois" |
| Imobilizado sem cobertura de inventario | Existencia | "~50M sem acesso ao relatorio item a item" |
| Fragilidades de controle nao enderecadas do ano anterior | Reincidencia | "Duas fragilidades de controle em aberto" |
| Modulos ERP com integracao via sistema legado | TI / completude | "Nao usava o modulo nativo — mandava pelo programa de integracao" |

---

### 5. Lacunas e pontos a confirmar

- [ ] Confirmar quais módulos do ERP foram migrados e quais ainda usam integração legada
- [ ] Obter evidencia das implementacoes de controle do time de TI ate outubro para reavaliacao das fragilidades abertas
- [ ] Definir escopo do inventario de alto valor: quais entidades, criterios de selecao dos top 10 itens
- [ ] Verificar se modulo de contas a receber migrou integralmente — impacta teste de completude
- [ ] Confirmar se ha relatorios confiaveis para o modulo de folha — impacta extensao dos testes proprios

---

### 6. Próximo uso recomendado

1. **`risk-control-mapping`** — usar sinais de risco como input para riscos e controles de fechamento contabil, imobilizado, folha e contas a receber pos-migracao.
2. **`audit-planning`** — incluir ponto de controle de outubro para reavaliacao das fragilidades abertas e priorizar testes de migracao, acesso e conciliacao.
3. **`test-execution`** — desenhar teste de controle de migracao de dados antes de confiar nos saldos e relatorios do ERP novo.
