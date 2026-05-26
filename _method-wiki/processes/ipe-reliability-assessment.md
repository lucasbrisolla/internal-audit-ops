# IPE Reliability Assessment

## Papel

Hub metodológico para avaliação de confiabilidade de IPE, cobrindo completude, precisão, extração, parâmetros de usuário, reconciliação com razão e riscos de intervenção manual.

## Quando usar

- relatório, listagem ou base gerada pela entidade sustenta evidência de auditoria
- há extração de dados do razão ou de sistemas auxiliares
- existem parâmetros de usuário, filtros ou manipulação manual relevantes
- o trabalho depende de completude e precisão da base para conclusão

## Objetivo da avaliação

Confirmar se a informação produzida pela entidade é suficientemente confiável para sustentar evidência de auditoria. A análise precisa cobrir não só o relatório final, mas também a origem dos dados, a lógica de extração e as intervenções manuais que possam comprometer o escopo.

## Trilhas de risco

### 1. Dados-fonte

- dados-fonte incompletos ou imprecisos
- base gerada a partir de fonte errada ou incompleta

### 2. Extração

- extração incorreta
- parâmetros inadequados ou incompletos
- filtro de usuário que reduz escopo sem percepção da equipe

### 3. Intervenção manual

- manipulação via EUC ou outros meios
- transformação manual sem trilha suficiente
- conciliações ou ajustes feitos fora do sistema sem controle claro

## Procedimentos mínimos

- validar parâmetros de usuário em toda extração relevante
- confirmar reconciliação ou consistência com contas do razão
- avaliar completude e precisão da base
- entender tecnologia usada, origem do relatório e eventuais transformações manuais
- desenhar mitigação específica para cada risco relevante

## Conexão com o uso em auditoria

- a confiabilidade da IPE define o quanto ela pode sustentar analytics, teste de detalhe ou conclusão sobre controle
- quando a base tem limitações, o desenho do procedimento precisa ser recalibrado
- reconciliação, origem, extração e transformação devem ser lidas como uma trilha única, não como checagens isoladas

## Perguntas críticas

- quais parâmetros foram usados para gerar a base?
- a extração cobre exatamente o escopo pretendido?
- a base reconcile com o razão ou com outra referência confiável?
- houve intervenção manual, EUC ou tratamento externo?
- a mitigação adotada responde ao risco identificado ou é genérica?

## Vínculo com Books and Records

Toda base usada como população de teste ou como evidência deve ser rastreável aos registros oficiais da entidade (livros contábeis, razão). O vínculo não pode ser assumido — precisa ser demonstrado:

- reconciliar totais da base com saldos do razão ou relatórios contábeis oficiais
- verificar se o período coberto pela extração corresponde exatamente ao período auditado
- documentar a fonte do relatório (sistema, módulo, parâmetros) de forma reproduzível

Essa verificação não é opcional quando a base sustenta a seleção de amostra ou uma conclusão de controle.

### Documento original vs. cópia

Quando possível, preferir exame do documento original ao invés de cópia. Cópias podem ter sido adulteradas ou estar incompletas. Em ambientes eletrônicos, preferir acesso direto ao sistema (live data) ao invés de exportações que possam ter sido manipuladas antes de chegar ao auditor.

## Vínculo com Information & Communication (COSO P13–P15)

A confiabilidade de IPE não é apenas uma questão de procedimento de teste — é evidência direta sobre o componente **Information & Communication** do COSO (Princípios 13–15), que avalia se a entidade gera e usa informação relevante, completa e precisa.

Quando IPE de um processo é testada e confirmada como confiável, essa evidência pode ser referenciada na avaliação de P13–P15. Quando IPE revela problemas de completude ou precisão, isso é input de avaliação do componente de informação — não apenas um achado de processo.

## Alertas

- não assumir confiabilidade de relatório só porque ele veio “do sistema”
- parâmetro não validado pode invalidar o escopo inteiro do teste
- reconciliação superficial não substitui avaliação do risco de extração
- preferir acesso direto ao sistema (live data) ao invés de exportações intermediadas pela entidade em áreas de maior risco
