# Job Scheduling and Monitoring

## Papel

Hub metodológico para rotinas automatizadas, agendamentos e monitoramento de jobs em aplicações e ERPs relevantes.

## Quando usar

- o processo depende de rotinas automáticas para processamento, integração ou validação
- há parametrizações que disparam etapas subsequentes sem intervenção manual
- o time precisa entender quem agenda, monitora e corrige falhas nessas rotinas

## Objetivo

Avaliar se jobs automatizados relevantes são configurados, monitorados e corrigidos de modo compatível com o risco do processo e do relato financeiro.

## O que pode entrar em job scheduling

- integrações entre módulos
- disparo de etapas subsequentes em processos de RH, fiscal ou compras
- cálculos automáticos, como crédito tributário
- mensagens de erro e validações automáticas
- rotinas noturnas, cargas e fechamentos

## Perguntas úteis

- quem agenda ou parametriza as rotinas?
- o job é interno à entidade ou operado principalmente pelo fornecedor do sistema?
- existe monitoramento para confirmar se a rotina rodou corretamente?
- quando ocorre erro, há alerta, documentação e trilha de correção?
- alguém pode alterar a lógica da rotina sem controle formal?

## Evidências úteis

- descrição da rotina automatizada
- log de execução ou alerta de falha
- documentação de correção de erros
- definição de responsável pelo monitoramento
- evidência de segregação entre quem altera e quem acompanha, quando aplicável

## Red flags

- a entidade depende de job crítico, mas não sabe explicar quem monitora
- falhas são corrigidas de forma reativa, sem log ou documentação
- alterações de rotina podem ser feitas por poucas pessoas sem trilha clara
- a entidade assume que o fornecedor cobre tudo, sem entender impacto local

## Observações práticas

- em ambientes com software terceirizado, pode ser suficiente entender que o fornecedor executa a maior parte da automação, mas ainda é preciso avaliar o que a entidade monitora localmente
- mesmo quando a rotina não é criada internamente, a falha dela pode afetar processamento contábil, folha, fiscal ou integrações relevantes

## Artefatos relacionados

- `processes/entity-programmed-changes.md`
- `processes/vendor-supplied-change-management.md`
