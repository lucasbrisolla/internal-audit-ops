# Critério Editorial — Base WCGW

## Objetivo

Padronizar criação, revisão e evolução dos WCGWs para manter consistência técnica, rastreabilidade e consumo confiável por workflows/scripts.

## Regra de Ouro

Cada WCGW deve ser reutilizável e auditável:

- reutilizável: aplicável em mais de um caso do mesmo processo
- auditável: rastreável à origem e com campos completos

## Campos Obrigatórios

Cada WCGW deve conter, no mínimo:

1. `id` (único no repositório)
2. `wcgw` (descrição objetiva do risco)
3. `process_slug` (processo de negócio)
4. `subprocess_slug` e `subprocess_name`
5. `scot_phase` (`Initiation`, `Recording`, `Processing`, `Reporting`)
6. `assertion` (ex.: Existência, Completude, Valoração, Corte, Apresentação)
7. `severity` (`Alta`, `Média`, `Baixa`)
8. `source_file` (arquivo Markdown de origem)

## Padrão de ID

- formato: `<ABREV>-<NNN>`
- exemplos: `P2P-001`, `OTC-014`, `ITGC-046`
- ID não pode ser reutilizado para outro risco
- ao descontinuar item, manter histórico (não reaproveitar o ID)

## Regras de Escrita

- descrever risco como evento verificável, não opinião
- evitar texto genérico (“falha de controle” sem contexto)
- preferir estrutura: evento + mecanismo de falha + impacto potencial
- evitar duplicidade semântica entre WCGWs do mesmo subprocesso

## Severidade

Critério base:

- **Alta**: pode gerar fraude, erro material ou quebra grave de controle
- **Média**: risco relevante com efeito potencial moderado
- **Baixa**: risco localizado com efeito limitado

Observação:
severidade pode ser calibrada no cliente, mas a base mestra deve manter severidade de referência.

## SCOT

Toda entrada deve mapear uma fase SCOT válida:

- `Initiation`
- `Recording`
- `Processing`
- `Reporting`

Não usar valores livres fora desse conjunto.

## Fonte e Rastreabilidade

- cada item deve apontar para `source_file`
- se houver múltiplas fontes, registrar em `source_references`
- não promover WCGW sem base documental mínima

## Processo de Mudança

1. alterar o arquivo Markdown em `context/wcgw/*.md`
2. regenerar base estruturada:
   - `python3 scripts/build_wcgw_master.py`
3. rodar validação:
   - `python3 scripts/doctor.py --report`
4. revisar impactos em workflows/scripts consumidores

## Critérios de Aceite para Novos WCGWs

- [ ] ID único e padrão correto
- [ ] campos obrigatórios completos
- [ ] fase SCOT válida
- [ ] severidade válida
- [ ] texto sem duplicidade óbvia no subprocesso
- [ ] origem rastreável

