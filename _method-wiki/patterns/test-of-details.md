# Test of Details

## Papel

Padrão metodológico para teste de detalhe com foco em adições, baixas, documentação suporte e risco de dupla contagem.

## Quando usar

- a documentação permite verificar fidedignidade de entradas e saídas
- a movimentação da conta é mais informativa do que o saldo agregado
- o objetivo é confirmar ocorrência, precisão, corte ou classificação por item

## Objetivo

Usar a movimentação detalhada de entradas e saídas para obter evidência direta sobre transações ou saldos relevantes.

## Aplicações comuns

- adições e baixas
- movimentações de imobilizado ou estoques
- variações relevantes em contas patrimoniais ou de resultado

## Cuidados essenciais

- confirmar que a documentação realmente sustenta a movimentação testada
- evitar testar duas vezes o mesmo efeito quando adições e baixas transitam entre si
- avaliar se o universo e a seleção capturam a lógica econômica da conta

## Perguntas úteis

- a documentação é suficiente e confiável?
- a movimentação testada representa ocorrência real?
- a baixa de uma conta reaparece como adição em outra trilha?
- há risco de dupla contagem na estratégia de teste?

## Red flags

- testar item com documentação fraca apenas porque está disponível
- duplicar cobertura em contas que transitam entre si
- usar teste de detalhe em universo cuja volumetria inviabiliza conclusão eficiente

## Relação com outras técnicas

- quando detalhe perde eficiência, pode ser combinado com `patterns/trend-analysis.md` e `patterns/ratio-analysis.md`
- a estratégia mais ampla fica em `processes/substantive-testing-strategy.md`
