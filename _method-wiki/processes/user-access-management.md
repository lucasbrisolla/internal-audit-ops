# User Access Management

## Papel

Hub metodológico para gestão de acessos, com foco em solicitação, aprovação, concessão, revogação, acessos privilegiados e revisão periódica.

## Quando usar

- há dependência de controles de acesso para suportar ITGC ou ICFR
- o time precisa entender como acessos são concedidos, alterados e removidos
- há risco de privilégio excessivo, SoD ou ausência de revisão periódica

## Objetivo

Avaliar se cada usuário recebe apenas o acesso necessário, com aprovação apropriada, segregação mínima e revogação tempestiva quando o acesso deixa de ser necessário.

## Blocos principais

### 1. Solicitação e aprovação

- pedido de novo acesso ou acesso adicional é formalizado
- aprovação vem de gestor ou responsável apropriado
- o racional considera função, responsabilidade e segregação de atividades
- help desk ou sistema de chamados pode concentrar o fluxo e dar trilha formal à solicitação

### 2. Concessão e manutenção

- o time de TI ou help desk executa a liberação
- mudanças de acesso são feitas por pessoas independentes da função de negócio, sempre que possível
- o uso de perfil-base semelhante pode reduzir retrabalho, mas precisa respeitar a função real do usuário

### 3. Revogação

- desligamentos ou mudanças de função disparam bloqueio tempestivo
- processo inclui devolução de equipamento e bloqueio em rede, ERP e pastas compartilhadas
- integração com RH ou departamento pessoal aumenta a chance de revogação tempestiva

### 4. Revisão periódica

- acessos privilegiados são revistos ao menos periodicamente
- papéis e menus são reavaliados para evitar acúmulo indevido

## Riscos principais

- concessão de acesso sem aprovação apropriada
- acesso incompatível com a função do usuário
- revogação tardia
- administradores ou usuários privilegiados sem revisão periódica
- papéis acumulam conflitos de segregação ao longo do tempo

## Evidências úteis

- formulário, chamado ou email de solicitação
- aprovação do gestor
- trilha de execução pelo help desk ou TI
- evidência de bloqueio ao desligamento
- revisão periódica de acessos ou lista de privilegiados
- extração do GLPI, Active Directory ou ferramenta equivalente

## Perguntas úteis

- quem aprova novos acessos e com base em quais critérios?
- quem concede e remove acessos?
- a função que administra acesso é independente do negócio?
- quanto tempo leva para bloquear acesso de desligados?
- há revisão periódica de acessos privilegiados?
- os papéis de acesso são reavaliados para prevenir SoD?

## Red flags

- concessão baseada apenas em pedido informal
- ausência de revisão periódica de acessos ou menus
- acesso privilegiado tratado como rotina sem verificação
- revogação feita só “quando alguém lembra”
- cópia de perfil usada sem revisão crítica do que o novo usuário realmente precisa

## Observações práticas

- GLPI ou ferramenta similar costuma ser uma boa fonte para testar formalização, aprovação e encerramento de acessos
- quando o próprio supervisor inicia acessos e entende que o pedido já vale como aprovação, vale testar se isso é consistente e suficiente para o nível de risco
- ausência de revisão periódica ativa é um red flag claro e pode configurar deficiência relevante dependendo do contexto

## Artefatos relacionados

- `processes/security-settings-and-authentication.md`
- `processes/fraud-risk-assessment.md`
