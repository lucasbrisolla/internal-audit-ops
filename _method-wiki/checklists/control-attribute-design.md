# Control Attribute Design

## Papel

Checklist para desenhar atributos de controle de forma testável, objetiva e suficientemente detalhada.

## Quando usar

- ao documentar walkthrough de controle
- ao revisar matriz de risco e controle
- ao preparar a descrição do controle para reliance

## Objetivo

Garantir que o controle seja descrito com atributos suficientes para permitir teste, avaliação de precisão e definição clara da evidência necessária.

## Atributos essenciais

- por que o controle é realizado
- quem executa
- quando ocorre
- como o procedimento é iniciado
- quão preciso e sensível é o controle
- como o controle é afetado por outros componentes do controle interno
- que evidência suporta a execução do controle

## Regras práticas

- descrição vaga gera controle não testável
- se a indagação não vier acompanhada de evidência suficiente, o controle não pode ser efetivado só com discurso
- a amostra precisa ser compatível com a frequência do controle e com o período de reliance
- testar só no fim do período pode ser insuficiente para concluir sobre operação ao longo do ano

## Perguntas de revisão

- a descrição permite entender exatamente o que a pessoa faz?
- a evidência esperada está clara?
- o controle depende de sistema ou informação produzida por outro controle?
- a frequência do controle está explícita?
- existe detalhe suficiente para decidir amostra e período de teste?

## Sinais de alerta

- descrição curta demais para o time reproduzir mentalmente a execução
- frequência indefinida
- evidência implícita, mas não declarada
- controle descrito de forma genérica, sem gatilho de início nem critério de revisão

## Artefatos relacionados

- `concepts/control-types-and-reliance.md`
- `patterns/control-design-and-operating-effectiveness.md`
- `patterns/evidence-conclusion-linkage.md`
