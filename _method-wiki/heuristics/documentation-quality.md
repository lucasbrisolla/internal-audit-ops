# Documentation Quality

## Papel

Heurísticas para manter saídas de auditoria tecnicamente claras, rastreáveis e úteis para revisão humana.

## Quando usar

- revisar walkthrough, RCM, papel de teste ou achado antes de finalizar
- transformar transcrição bruta em documentação técnica
- distinguir fato, inferência e lacuna
- calibrar se a saída está formal demais, genérica demais ou sem evidência

## Heurísticas de documentação

- Não inventar etapa, controle ou aprovação que não esteja no insumo.
- Não omitir etapa material apenas para limpar o texto.
- Marcar ambiguidades como ambiguidades.
- Especificar atores e sistemas quando houver evidência.
- Distinguir fato, inferência plausível e lacuna.
- Preferir voz ativa e sequência lógica.
- Clareza técnica vale mais que formalidade excessiva.

## Controls vs. Processes (referencial metodológico, Cap. 1)

Erro sistemático em projetos de avaliação de controles: documentar o processo inteiro quando o requisito é documentar os **controles**.

- Processo: "o sistema gera a nota fiscal após aprovação do pedido"
- Controle: "supervisor revisa o pedido antes de autorizar emissão — evidência: campo de aprovação com ID do usuário e timestamp"

Volumes de documentação de processo não substituem descrição de controle. Um flowchart de 10 páginas sem um único controle identificado é inútil para avaliação de ICFR. O auditor interno deve perguntar: *"Onde está o controle? Quem faz o quê para garantir que o risco não se materialize?"*

Implicações práticas:
- Narrativa ou flowchart de processo pode coexistir com documentação de controles — mas são documentos distintos e com objetivos distintos
- Atualizar flowchart não substitui atualizar a documentação dos controles
- Documentação de controle precisa responder: controle existente, quem executa, com qual frequência, qual evidência de operação

---

## Failure modes comuns

- Confundir transcrição com processo finalizado.
- Misturar hipótese com fato.
- Perder ordem lógica das etapas no walkthrough.
- Descrever controle que deveria existir como se existisse.
- Inflar severidade de achado sem base na evidência.
- Transformar saída técnica em resumo genérico.
- Exagerar formalidade e perder clareza do ponto principal.
- **Documentar processo em vez de controles** — gera volume sem conteúdo avaliável.

## Critérios de qualidade de saída

Uma boa saída técnica deve ser:

- aderente ao insumo recebido
- tecnicamente clara e precisa
- rastreável, permitindo que o leitor cheque a origem de cada afirmação
- útil para revisão humana sem retrabalho
- formal o suficiente para documentação, curta o suficiente para não esconder o ponto

## Regra de evidência

Condição sem critério é observação, não achado. Causa sem evidência é hipótese, não conclusão.
