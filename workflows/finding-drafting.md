# workflow: finding-drafting

## Goal

Transformar uma observação, exceção ou lacuna em um achado técnico formal, rastreável e útil para revisão humana — estruturado nos 5 Cs.

## Use When

- há uma falha, exceção ou lacuna que precisa ser formalizada
- um teste identificou desvio do critério esperado
- existe observação dispersa em notas, transcrição ou conversa que precisa virar achado
- é preciso redigir achado com linguagem técnica, objetiva e auditável

## Inputs

- observação bruta ou exceção identificada no teste
- critério violado (política, norma, procedimento)
- evidência disponível (o que foi inspecionado, reperformado ou observado)
- contexto do processo e do controle
- impacto percebido ou potencial

## Drafting Sequence

### 1. Critério — o que deveria ser

Definir antes de qualquer coisa:

- Qual a fonte normativa, política ou procedimento que estabelece o padrão?
- O critério é claro e verificável?
- Se não houver critério formal, há boas práticas do setor ou standards do IIA aplicáveis?

Sem critério, não há achado. Há apenas observação.

### 2. Condição — o que foi encontrado

Descrever o que foi observado com precisão:

- O que exatamente foi identificado na evidência?
- Em quantos itens da amostra? Em qual período?
- A condição é pontual ou sistemática?
- O que a evidência mostra diretamente?

Separar o que é fato do que é interpretação.

### 3. Causa — por que aconteceu

Identificar a raiz do problema:

- Falha de design: o controle não foi desenhado para cobrir esse risco
- Ausência de controle: não existe controle para o risco identificado
- Falha humana: o controle existe, mas não foi executado corretamente
- Falha sistêmica: o sistema não suporta o controle ou permite override
- Falta de conhecimento ou treinamento
- Processo desatualizado em relação à realidade operacional

A causa orienta a recomendação. Causa errada gera recomendação ineficaz.

### 4. Consequência — qual o impacto

Avaliar o impacto real ou potencial:

- **Financeiro**: exposição a perda, erro de reporte, pagamento indevido
- **Operacional**: ineficiência, retrabalho, falha de processo
- **Regulatório / Compliance**: não-conformidade com norma ou obrigação legal
- **Reputacional**: exposição da organização perante terceiros
- **Informação**: risco de reporte incorreto ou incompleto

Distinguir impacto real (já ocorreu) de impacto potencial (pode ocorrer se não corrigido).

**Se tipo de risco incluir Fraude:** documentar os três vértices do Fraud Triangle antes de fechar o achado:
- **Oportunidade** — acesso irrestrito, ausência de SoD, processo não documentado, sem supervisão
- **Motivação / Pressão** — incentivos financeiros, metas, pressão externa
- **Racionalização** — cultura, normalização de desvio, histórico de exceções toleradas

Vértices não confirmados = lacuna de investigação — registrar explicitamente e endereçar em fase de execução. Não fechar achado de fraude com vértice inferido como confirmado.

Ref.: `_method-wiki/processes/fraud-risk-assessment.md`

### 5. Recomendação — o que precisa mudar

A recomendação deve:

- Ser dirigida à gestão, não ao time de auditoria
- Ser específica: o que exatamente deve ser feito?
- Endereçar a causa — não apenas o sintoma
- Ser implementável dentro das restrições da organização
- Ter prazo sugerido quando relevante

**Verificar agregação antes de fechar:** se houver outros achados no mesmo componente COSO ou no mesmo processo, avaliar se o conjunto constitui deficiência mais severa que cada achado individual. Registrar conclusão no campo "Racional de severidade" do template. Ref.: `_method-wiki/patterns/control-deficiency-severity.md`.

**Classificar tipo de ação:** distinguir Pontual (correção imediata), Estrutural (mudança de processo/controle) e Roadmap (bloqueada por dependência externa — ICT, fornecedor, sistema). Para ações Roadmap: garantir que controles compensatórios cobrem o risco residual no intervalo.

## Decision Rules

- Não inflar severidade sem base na evidência
- Não transformar hipótese em achado fechado
- Se a evidência for insuficiente, registrar isso explicitamente — não forçar conclusão
- Um bom achado explica o problema sem dramatizar
- Redação técnica e curta é melhor que texto "bonito"
- Linguagem impessoal e objetiva — sem acusação direta de pessoas

## Gate de Adversarial Review

Antes da DoD, aplicar `skills/challenge-reasoning.md` no modo **Advogado do Diabo** (Ferramenta 6):

> Apresente os argumentos mais fortes contra este achado — como a gestão vai refutar cada um dos 5 Cs.

Complementar com **Prudent Official Challenge** (Ferramenta 14) se a severidade for Crítico ou Alto:

> Um profissional prudente com o mesmo conhecimento concordaria com essa classificação — ou elevaria?

**Critério de passagem:** o achado sobrevive ao desafio sem que nenhum dos 5 Cs precise ser reconstruído. Reformulações de linguagem são aceitáveis; mudança de causa, consequência ou critério indica que o achado não estava maduro.

Se o achado não passar: revisitar o C problemático antes de prosseguir. Não encaminhar para DoD com C frágil identificado.

Registrar resultado do gate no template (`output-achado-5c.md` — seção Gate de Adversarial Review).

## Gate de Pronto (DoD)

Antes de considerar o output concluído, validar o bloco de achado em:

- `_method-wiki/checklists/audit-artifacts-definition-of-done.md` -> seção `4) DoD - Achado`
- `_method-wiki/checklists/audit-artifacts-definition-of-done.md` -> seção `Gates de Revisão Final`
- registrar decisão de gate no template: `templates/revisao-dod-artefato.md`

Se qualquer item crítico estiver pendente, manter status `em revisão` e não encaminhar para comunicação final.

## Output

- achado completo nos 5 Cs
- grau de certeza declarado quando houver limitação de evidência
- indicação para `finding-rating` como próximo passo

## Output Format

**Critério**
[O que deveria ser — fonte normativa ou política]

**Condição**
[O que foi encontrado — fatos e evidências]

**Causa**
[Por que aconteceu — raiz do problema]

**Consequência**
[Impacto real ou potencial — classificado por natureza]

**Recomendação**
[O que a gestão deve fazer — específico e implementável]

---
*Grau de certeza*: [Confirmado / Inferência plausível / Pendente de confirmação]
*Encaminhar para*: `finding-rating`

## Persistência de Arquivo

Salvar achados em arquivo consolidado por processo: `templates/achados/achados-<processo>.md` (ex: `achados-recebimento.md`).

Regras:
- Múltiplos achados do mesmo processo vão no mesmo arquivo, separados por `---\n---`
- Incluir Resumo Consolidado e Nota de Agregação ao final do arquivo
- Referência interna: `REC-01`, `FAT-01` etc. (sem prefixo `ACH-`)
- Proibido criar arquivos individuais por achado (ex: `ACH-REC-01.md`)
- Proibido entregar achado apenas como resposta em chat sem persistir o arquivo
- Modelo de referência: `templates/achados/achados-faturamento.md`
