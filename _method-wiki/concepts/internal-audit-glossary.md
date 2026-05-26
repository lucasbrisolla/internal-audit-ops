# Internal Audit Glossary

## Papel

Vocabulário técnico curto para documentação de riscos, controles, testes e achados de auditoria interna.

## Quando usar

- padronizar termos em walkthroughs, RCMs, papéis de teste ou achados
- revisar se a linguagem técnica está precisa
- explicar termos de controle sem carregar módulos metodológicos maiores

## Termos de controle

| Termo | Definição operacional |
|---|---|
| Gatilho do processo | Evento que inicia a transação ou atividade em escopo |
| Entrada e registro | Ponto em que a transação entra no sistema ou no controle formal |
| Validação | Verificação de dados antes do processamento ou da aprovação |
| Aprovação | Autorização formal por responsável competente |
| Segregação de funções | Separação entre quem executa, registra, aprova e monitora |
| Controle preventivo | Controle que impede que o erro ocorra |
| Controle detectivo | Controle que identifica erro ou exceção após a ocorrência |
| Controle automatizado | Controle executado pelo sistema sem intervenção humana relevante |
| Controle manual | Controle executado por pessoa, sujeito a erro ou julgamento humano |
| Override | Ação que contorna, cancela ou altera um controle existente |
| Exceção | Item que não passou pelo controle conforme o critério esperado |
| Evidência | Suporte documental, sistêmico ou observacional para uma conclusão |
| Rastreabilidade | Capacidade de reconstruir o caminho de uma transação ou decisão |
| Lacuna de controle | Ausência de controle para um risco relevante |

## Asserções de auditoria

| Asserção | O que testa |
|---|---|
| Existência / Ocorrência | O saldo ou transação existe de fato? |
| Integridade / Completude | Todos os itens relevantes estão incluídos? |
| Valoração / Acurácia | Os valores estão corretos e devidamente calculados? |
| Corte (cut-off) | As transações foram registradas no período correto? |
| Direitos e Obrigações | A entidade tem direito sobre o ativo ou obrigação pelo passivo? |
| Apresentação e Divulgação | As informações estão classificadas e divulgadas corretamente? |

## ToD vs. ToE

**Test of Design (ToD)** pergunta se o controle, caso operado como desenhado, mitigaria o risco. Normalmente envolve entrevista, leitura de política, inspeção de fluxograma e walkthrough de uma transação.

**Test of Effectiveness (ToE)** pergunta se o controle operou de forma consistente e efetiva no período. Normalmente envolve amostragem, reperformance, observação direta ou análise de exceções.

Regra prática: falha no ToD dispensa o ToE. Se o desenho é falho, a efetividade operacional não salva o controle.

## REF por asserção

Cada teste deve ter uma `REF` que indica a asserção coberta:

| REF | Asserção |
|---|---|
| E | Existência / Ocorrência |
| C | Completude / Integridade |
| D | Direitos e Obrigações / Valoração |
| S | Apresentação, Suficiência e Divulgação |

Sem `REF`, o programa de trabalho não demonstra cobertura das asserções.
