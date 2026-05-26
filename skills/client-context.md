# skill: client-context

## Goal

Construir e manter um perfil persistente e evolutivo da empresa auditada, organizado em múltiplos MDs temáticos com um index leve para o agente carregar apenas o contexto relevante por tarefa.

Esta skill é a base de memória longitudinal do agente sobre cada cliente. Ela opera antes de qualquer workflow e é atualizada ao longo de toda a relação com o cliente.

## Use When

- início de qualquer trabalho com um cliente novo (modo `init`)
- início a partir de fontes legadas: exportação Notion, Word, planilha, papéis de trabalho anteriores (modo `init` com fonte externa — absorve o que era `context-migration`)
- retorno a cliente já perfilado com informação nova (modo `update`)
- documento escrito recebido: política interna, organograma, manual de processo, contrato, ata formal, relatório de gestão (modo `update` com fonte documental — absorve o que era `context-extraction`)
- transcrição de reunião ou walkthrough contém informação sobre pessoas, processos ou decisões do cliente
- qualquer workflow que dependa de contexto específico do cliente (audit-planning, risk-control-mapping, finding-drafting)
- o mantenedor do repositório pede explicitamente "salva contexto" ou "atualiza perfil do cliente"

## Inputs

- qualquer combinação de: texto livre, transcrição de reunião, documento formal, apresentação, proposta comercial, e-mail
- documentos escritos: política interna, manual de processo, organograma, contrato, ata, relatório de gestão (extrair para `context/clients/*/` via modo `update`)
- fontes legadas: exportações Notion, arquivos Word de engagements anteriores, planilhas de controle (migrar para estrutura `context/clients/*/` via modo `init`)
- para `update`: arquivos existentes em `context/clients/<slug>/` + novo input

## Estrutura de Arquivos

```
context/clients/<client-slug>/
  index.md                    ← sempre carregado; mapa de carregamento
  profile.md                  ← identificação, setor, porte, ERP, jurisdições
  org-structure.md            ← organograma, áreas, divisões, subsidiárias
  people.md                   ← pessoas-chave, cargos, papéis no engagement
  processes.md                ← processos mapeados, status, owner
  control-environment.md      ← ERP, ferramentas, frameworks, maturidade
  compliance.md               ← normas aplicáveis (SOX, CVM, IFRS, CPC, NBC TA)
  goals-pressures.md          ← metas da gestão, pressões, contexto estratégico
  risk-signals.md             ← flags de risco derivados do perfil (inferidos)
  open-tasks.md               ← tarefas e decisões abertas entre sessões
  engagements/
    <YYYY>-q<N>-<tema>.md    ← histórico por trabalho de auditoria
  meetings/
    <YYYY-MM-DD>-<tema>.md    ← output de cada reunião/walkthrough
```

Exemplo de engagement: `2025-q1-sox.md`

**Slug:** nome do cliente simplificado, minúsculo, sem espaços, sem acentos.
Exemplos: `mineradora-xyz`, `holding-abc`, `banco-regional`.
Em caso de ambiguidade ou colisão de nomes, usar sufixo numérico (`banco-regional-2`). Confirmar o slug com o mantenedor do repositório antes de criar a estrutura se houver dúvida.

**`<tema>`** nos nomes de arquivo deve ser slug em português, sem espaços, sem acentos, máximo 4 palavras. Exemplos: `kick-off-planejamento`, `walkthrough-contas-pagar`, `sox-p2p-itgc`.

## Modo: init

Usado na primeira vez com um cliente.

### Sequência

1. Receber qualquer input disponível sobre o cliente
2. Extrair o que há — não inferir cargo, responsabilidade ou decisão sem base explícita. Exceção: `risk-signals.md` é o espaço designado para inferências do agente a partir do perfil
3. Popular cada MD com o que foi extraído
4. Lacunas marcadas com `[?]` — nunca silenciar ausência de informação
5. Se o input contiver informação de engagement (escopo do trabalho, período, objetivo), criar `engagements/<ano>-q<N>-<tema>.md` e registrar na tabela de Engagements do `index.md`
6. Criar `index.md` com descrição e gatilho de cada arquivo
7. Ao final, propor ao mantenedor do repositório:

> "Perfil criado para [nome do cliente]. Campos em aberto: [lista]. Quer completar agora ou deixar para próxima sessão?"

### O que popular no `init`

Ao criar cada arquivo, usar os campos da seção **Formato dos MDs** abaixo.

## Modo: update

Usado quando o cliente já tem perfil e há informação nova.

### Sequência

1. Ler `index.md` para mapear o que existe
2. Carregar apenas os MDs relevantes ao novo input
3. Identificar delta: o que é novo, o que mudou, o que contradiz o existente
4. Formular proposta de atualização antes de salvar:

> "Identifiquei as seguintes atualizações para o perfil de [cliente]:
> - `people.md`: adicionar [Nome], Gerente de TI
> - `open-tasks.md`: nova tarefa — solicitar população de acessos até 30/04
> Confirma?"

5. Salvar apenas após aprovação do mantenedor do repositório, ou quando ele disser "salva contexto"

### Gatilho automático durante workflows

Ao fim de qualquer workflow, se o agente identificar informação nova sobre o cliente, sinalizar:

> "Identifiquei contexto novo: [X]. Quer salvar em `[arquivo].md`?"

Nunca salvar automaticamente sem confirmação.

## Formato dos MDs

### `index.md`

```markdown
# Client Context Index — <Nome do Cliente>

**Slug:** <client-slug>
**Setor:** <setor>
**Última atualização:** YYYY-MM-DD

## Perfil Geral

| Arquivo | Conteúdo | Carregar quando |
|---|---|---|
| [profile.md](profile.md) | Identificação, setor, porte, ERP, jurisdições | Qualquer workflow novo |
| [org-structure.md](org-structure.md) | Organograma, áreas, divisões | Quando mencionar área, diretoria ou subsidiária |
| [people.md](people.md) | Pessoas-chave e papéis | Quando mencionar nome ou cargo |
| [compliance.md](compliance.md) | Normas aplicáveis | audit-planning, technical-review, finding-drafting |

## Operacional

| Arquivo | Conteúdo | Carregar quando |
|---|---|---|
| [processes.md](processes.md) | Processos mapeados e status | risk-control-mapping, walkthrough, test-execution |
| [control-environment.md](control-environment.md) | ERP, frameworks, maturidade | risk-control-mapping, test-execution |
| [goals-pressures.md](goals-pressures.md) | Metas e pressões da gestão | audit-planning, finding-drafting |
| [risk-signals.md](risk-signals.md) | Flags de risco de contexto | audit-planning |

## Tático

| Arquivo | Conteúdo | Carregar quando |
|---|---|---|
| [open-tasks.md](open-tasks.md) | Tarefas e decisões abertas | Toda sessão ativa com o cliente |

## Reuniões

| Data | Tema | Arquivo |
|---|---|---|
| YYYY-MM-DD | [tema] | [meetings/YYYY-MM-DD-tema.md](meetings/YYYY-MM-DD-tema.md) |

## Engagements

| Período | Escopo | Arquivo |
|---|---|---|
| YYYY-q1 | [escopo] | [engagements/YYYY-q1-tema.md](engagements/YYYY-q1-tema.md) |
```

### `profile.md`

```markdown
# Perfil — <Nome do Cliente>

**Razão Social:** [?]
**Nome Comercial:** [?]
**Setor:** [?]
**Porte:** [pequena / média / grande / multinacional]
**Tipo de Capital:** [aberto / fechado / familiar / cooperativa]
**Jurisdições:** [países/estados relevantes]
**ERP Principal:** [ver control-environment.md]
**Sistemas Principais:** [ver control-environment.md]
**Ano de Fundação:** [?]
**Número Aproximado de Funcionários:** [?]
**Receita Anual Aproximada:** [?]
**Estrutura Societária:** [?]
**Auditoria Externa:** [firma / [?]]
**Abordagem de Auditoria Interna:** [RBA / Compliance / Control-Based / [?]]
**Contexto Atual:** [resumo de 2-3 linhas sobre o momento da empresa]
```

### `org-structure.md`

```markdown
# Estrutura Organizacional — <Nome do Cliente>

## Organograma Simplificado

[texto descritivo ou lista hierárquica]

## Áreas e Divisões

| Área | Responsável | Função Principal |
|---|---|---|
| [?] | [?] | [?] |

## Subsidiárias / Unidades de Negócio

| Entidade | Localização | ERP | Relevância para Auditoria |
|---|---|---|---|
| [?] | [?] | [?] | [?] |

## Estrutura de Governança

- Conselho de Administração: [?]
- Comitê de Auditoria: [existe / não existe / [?]]
- CFO / Diretor Financeiro: [?]
- Controller: [?]
```

### `people.md`

```markdown
# Pessoas-Chave — <Nome do Cliente>

| Nome | Cargo | Área | Papel no Engagement | Contato |
|---|---|---|---|---|
| [?] | [?] | [?] | [interlocutor / aprovador / auditado / informante] | [?] |

## Notas

[observações sobre dinâmica, perfil ou sensibilidade de cada pessoa — apenas o que for relevante para o trabalho]
```

### `processes.md`

```markdown
# Processos Mapeados — <Nome do Cliente>

| Processo | Área Owner | ERP / Sistema | Status | Última Auditoria |
|---|---|---|---|---|
| [ex: Procure-to-Pay] | [?] | [?] | [mapeado / parcial / [?]] | [?] |

## Notas de Processo

[observações específicas: variações locais, exceções conhecidas, complexidades]
```

### `control-environment.md`

```markdown
# Ambiente de Controle — <Nome do Cliente>

**ERP Principal:** [?]
**Versão / Módulos em Uso:** [?]
**Sistemas Satélites:** [?]
**Framework Declarado:** [COSO / SOX / ISO 31000 / nenhum / [?]]
**Maturidade Percebida:** [inicial / repetível / definido / gerenciado / otimizado / [?]]
**Políticas Formalizadas:** [sim / parcial / não / [?]]
**Segregação de Funções:** [adequada / parcial / deficiente / [?]]
**Trilha de Auditoria (Audit Trail):** [completa / parcial / ausente / [?]]

## Observações

[pontos específicos sobre controles, automações ou gaps identificados]
```

### `compliance.md`

```markdown
# Compliance e Regulação — <Nome do Cliente>

| Norma | Aplicabilidade | Observação |
|---|---|---|
| SOX | [sim / não / [?]] | [?] |
| CVM | [sim / não / [?]] | [?] |
| IFRS | [sim / não / [?]] | [?] |
| CPC | [sim / não / [?]] | [?] |
| NBC TA | [sim / não / [?]] | [?] |
| [outras] | [?] | [?] |

## Obrigações Específicas

[obrigações regulatórias particulares do setor ou jurisdição]
```

### `goals-pressures.md`

```markdown
# Metas e Pressões — <Nome do Cliente>

## Objetivos Declarados da Gestão

- [?]

## Pressões Externas

- [ex: preparação para IPO, regulador ativo, integração pós-M&A]

## Pressões Internas

- [ex: redução de custo, transformação digital, mudança de liderança]

## Contexto Estratégico

[situação atual da empresa em 3-5 linhas — o que está mudando e por quê]
```

### `risk-signals.md`

```markdown
# Sinais de Risco de Contexto — <Nome do Cliente>

> Estes sinais são inferências do agente a partir do perfil da empresa — não declarações do cliente.
> Usar para orientar audit-planning e risk-control-mapping, não como achados.

| Sinal | Base no Perfil | Risco Potencial | Área para Investigar |
|---|---|---|---|
| [ex: empresa familiar sem comitê de auditoria] | [org-structure.md] | [override de controles, segregação fraca] | [ELC, aprovações por alçada] |
| [?] | [?] | [?] | [?] |
```

### `open-tasks.md`

```markdown
# Tarefas e Decisões Abertas — <Nome do Cliente>

## Abertas

- [ ] [Origem: reunião YYYY-MM-DD] [descrição da tarefa] — prazo: [?] — responsável: [?]

## Concluídas

- [x] [Origem: reunião YYYY-MM-DD] [descrição] — concluída em: YYYY-MM-DD
```

### `meetings/<YYYY-MM-DD>-<tema>.md`

```markdown
# Reunião — <Tema>

**Data:** YYYY-MM-DD
**Participantes:** [lista]
**Objetivo da Reunião:**

## Pauta

## Decisões

## Próximos Passos

| Tarefa | Responsável | Prazo |
|---|---|---|
| [?] | [?] | [?] |

## Pendências / Pontos em Aberto

## Observações de Contexto

[informações sobre o cliente capturadas durante a reunião — candidatas a update de perfil]
```

### `engagements/<YYYY>-q<N>-<tema>.md`

```markdown
# Engagement — <Tema>

**Período:** YYYY-q1
**Escopo:** [processos / áreas auditadas]
**Objetivo:** [assurance / consultoria / SOX / [?]]
**Equipe:** [?]
**Status:** [planejamento / execução / encerramento / concluído]

## Resumo

## Principais Achados

| Achado | Severidade | Status do Plano de Ação |
|---|---|---|
| [?] | [crítico / alto / médio / baixo / informativo] | [aberto / em andamento / implementado] |

## Lições Aprendidas

## Impacto no Próximo Engagement
```

## Decision Rules

- Nunca inferir cargo, responsabilidade ou decisão sem base explícita no input
- `[?]` sinaliza lacuna — nunca omitir campo sem sinalizar
- `risk-signals.md` contém inferências do agente, não declarações do cliente — manter separação clara
- Não sobrescrever arquivo existente sem propor delta antes
- Itens de `open-tasks.md` nunca deletados — apenas marcados `[x]`
- Ao atualizar `index.md`, sempre incluir nova entrada nas tabelas de Reuniões ou Engagements
- Quando input contiver transcrição de reunião (independentemente de ter passado por `transcript-analysis`), propor salvar em `meetings/` + atualizar `open-tasks.md`
- Se `index.md` não existir durante modo `update`, tratar como `init` parcial: reconstruir o index a partir dos arquivos existentes em `context/clients/<slug>/` e sinalizar o mantenedor do repositório

## Output do Modo `init`

1. Estrutura de pastas criada em `context/clients/<slug>/`
2. Todos os MDs preenchidos com o que foi extraído do input
3. Lacunas marcadas com `[?]`
4. `index.md` completo com gatilhos de carregamento
5. Sumário ao mantenedor do repositório: campos preenchidos vs. campos em aberto

## Output do Modo `update`

1. Delta identificado: lista de mudanças propostas por arquivo
2. Aguardar aprovação antes de salvar
3. Após aprovação: arquivos atualizados + `index.md` com data de última atualização revisada
