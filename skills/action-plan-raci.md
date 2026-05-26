# skill: action-plan-raci

## Goal

Definir e documentar a matriz RACI para ações corretivas de achados de auditoria interna, garantindo clareza de responsabilidade na implantação de controles dentro da organização.

## Use When

- achado possui ação corretiva do tipo **Estrutural** ou **Roadmap**
- ação envolve mais de uma área ou função na execução
- follow-up de plano de ação requer rastreabilidade de quem aprova e quem executa
- gestão questiona quem é responsável por determinada ação

Não aplicar para ações **Pontuais** com owner único e execução dentro da mesma área — nesse caso o campo "Responsável" no template já é suficiente.

---

## Estrutura RACI

| Papel | Definição | Regra |
|---|---|---|
| **R — Responsible** | Quem executa a ação | Pode ser mais de um; ao menos um obrigatório |
| **A — Accountable** | Quem responde pelo resultado final | Exatamente um por ação — não compartilhar |
| **C — Consulted** | Quem deve ser consultado antes ou durante | Opcional; usar quando decisão técnica depende de outra área |
| **I — Informed** | Quem deve ser informado sobre o status | Opcional; incluir gestão sênior e auditoria interna por padrão |

**Regra crítica:** A e R não podem ser a mesma pessoa em ações de controle com risco de SoD.

---

## Quando Cada Papel É Obrigatório

| Tipo de ação | R | A | C | I |
|---|---|---|---|---|
| Pontual | owner único | — | — | — |
| Estrutural | executor(es) | gestor da área | ICT / Jurídico / RH se aplicável | Auditoria Interna |
| Roadmap | executor(es) + ICT/fornecedor | gestor responsável | área impactada | Auditoria Interna + Diretoria |

---

## Como Documentar no Template

No `output-achado-5c.md`, campo "Responsável (owner único)":

- Para ações Pontuais: nome + cargo
- Para ações Estruturais e Roadmap: usar formato abaixo no lugar do campo simples:

```
R: [nome / cargo — executor]
A: [nome / cargo — accountable]
C: [área — se aplicável]
I: Auditoria Interna [+ outros se aplicável]
```

Registrar A como o nome que assina o plano de ação perante a auditoria.

---

## Sequência de Aplicação

### 1. Identificar tipo de ação

Verificar se a ação é Estrutural ou Roadmap — se Pontual, RACI não é necessário.

### 2. Mapear atores envolvidos

- Quem executa operacionalmente?
- Quem tem autoridade para aprovar a mudança?
- Alguma área precisa ser consultada (TI, Jurídico, RH, Financeiro)?
- Quem precisa ser informado do status (Diretoria, Comitê de Auditoria)?

### 3. Definir A antes de R

Começar pelo Accountable — um único nome com autoridade sobre o resultado. Se houver dúvida entre dois nomes, escolher o de hierarquia superior ou o dono do processo.

### 4. Verificar SoD

Se a ação corrige falha de segregação de funções: confirmar que R e A não são a mesma pessoa e que o executor não é quem aprova.

### 5. Registrar no template

Preencher o campo Responsável no formato RACI e registrar I como Auditoria Interna por padrão.

---

## Uso no Follow-up

No tracker de follow-up (`scripts/generate_followup_pa_v2.py`), o campo A é o interlocutor principal para cobrança de status. O campo R é quem entrega a evidência de implementação.

Em caso de descumprimento de prazo: escalar para A primeiro. Se A não resolver, escalar para o próximo nível hierárquico ou Comitê de Auditoria conforme política interna.

---

## Decision Rules

- Nunca deixar A em branco em ações Estruturais ou Roadmap
- Nunca atribuir A a um cargo genérico ("área de TI") — nome e cargo específicos
- C e I são opcionais mas devem ser explícitos quando omitidos por decisão, não por esquecimento
- RACI não substitui o critério de conclusão — ambos são obrigatórios
