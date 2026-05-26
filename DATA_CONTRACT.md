# Data Contract

Define quais arquivos pertencem à **camada do usuário** (nunca sobrescritos) e quais pertencem à **camada do sistema** (atualizáveis com segurança).

## User Layer — Nunca Sobrescrever

Contém dados reais, experiência acumulada e trabalho produzido pelo mantenedor do repositório. Nenhum processo de update pode ler, modificar ou deletar estes arquivos.

| Arquivo / Pasta | Conteúdo |
|---|---|
| `context/clients/` | Perfis de clientes, reuniões, engagements, tarefas abertas |
| `context/experience/` | Postmortems e aprendizados de projetos reais anonimizados |
| `context/audit-landscape-2025.md` | Leitura contextual do mercado e momento da auditoria interna |
| `examples/` | Transcrições, análises e casos reais usados como calibradores |
| `playbooks/playbook-mestre-interna.md` | Playbook pessoal de auditoria interna |
| `playbooks/playbook-segmento-*.md` | Playbooks setoriais com experiência e repertório acumulado |
| `playbooks/playbook-tema-*.md` | Playbooks temáticos com repertório acumulado |

## System Layer — Atualizável com Segurança

Contém lógica do agente, metodologia, templates e instruções que evoluem com o produto.

| Arquivo / Pasta | Conteúdo |
|---|---|
| `CLAUDE.md` | Routing e instruções do agente |
| `PRODUCT_INDEX.md` | Inventário operacional sob demanda: standards, fontes estruturadas, templates e scripts |
| `states.yml` | Estados canônicos de engagement, área, achado e plano de ação |
| `domain.md` | Mapa leve de consulta metodológica sob demanda |
| `skills/` | Skills auxiliares do agente |
| `workflows/` | Workflows de execução |
| `_method-wiki/` | Base metodológica canônica |
| `books/` | Fontes de referência e trilhas de destilação metodológica |
| `scripts/` | Scripts utilitários |
| `_method-wiki-external-audit/playbooks/legacy/` | Playbooks arquivados com lógica legada de auditoria externa / ICFR / SOX |
| `archive/docs/` | Specs e planos arquivados de implementação |
| `DATA_CONTRACT.md` | Este arquivo |

## A Regra

**User Layer:** nenhum update, reorganização ou agente pode modificar, mover ou deletar estes arquivos sem aprovação explícita do mantenedor do repositório.

**System Layer:** pode ser substituído pela versão mais recente sem risco de perda de dados pessoais ou trabalho acumulado.

## Fronteira Crítica

`context/clients/` é o ativo mais sensível do produto. Cada pasta de cliente contém memória longitudinal real — perfis, decisões, tarefas, reuniões. Qualquer operação de escrita nessa pasta requer confirmação explícita do mantenedor do repositório, mesmo dentro do modo `update` da skill `client-context`.
