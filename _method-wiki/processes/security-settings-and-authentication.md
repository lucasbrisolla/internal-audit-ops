# Security Settings and Authentication

## Papel

Hub metodológico para configuração de segurança, requisitos de senha e mecanismos de autenticação em aplicações e ambiente de TI.

## Quando usar

- o entendimento de ITGC inclui configuração de senha, autenticação e acesso remoto
- a entidade usa VPN, home office ou autenticação adicional em sistemas relevantes
- é preciso avaliar se parâmetros mínimos de segurança estão definidos e operando

## Objetivo

Avaliar se as configurações de segurança são definidas por critério adequado e se os mecanismos de autenticação reduzem risco de acesso indevido.

## Blocos principais

### 1. Critério de configuração

- entender se a entidade usa padrão default, manual do sistema ou apoio de pessoas experientes
- avaliar se houve julgamento consciente sobre parâmetros relevantes

### 2. Requisitos de autenticação

- comprimento mínimo de senha
- expiração periódica
- autenticação de dois fatores, quando aplicável
- uso de VPN para acessos remotos

### 3. Cobertura por aplicação

- confirmar se requisitos se aplicam às aplicações relevantes, bases de dados e administradores sob controle da entidade
- tratar variações materiais em processos separados

## Riscos principais

- senha fraca ou sem política mínima
- ausência de autenticação adicional em acessos remotos relevantes
- dependência de configuração default sem avaliação
- inconsistência entre aplicações críticas

## Evidências úteis

- política de senha ou print de parametrização
- descrição do uso de VPN ou autenticação em duas etapas
- documentação de exceções
- trilha de quem definiu e mantém os parâmetros
- evidência de diretoria ou gestão participando da decisão quando o tema envolve segurança versus usabilidade

## Perguntas úteis

- como a entidade decide quais configurações de segurança usar?
- quais requisitos mínimos de senha estão em vigor?
- há autenticação adicional para home office ou acesso remoto?
- os administradores seguem o mesmo padrão ou controles reforçados?
- existem aplicações relevantes fora desse processo?

## Red flags

- ausência de requisitos mínimos de senha
- autenticação em duas etapas planejada mas não implementada em ambiente sensível
- respostas vagas sobre quem define as configurações
- processo único para aplicações com perfis de risco muito diferentes

## Observações práticas

- quando a autenticação em duas etapas ainda depende de aprovação de diretoria, isso costuma indicar maturidade parcial do controle
- o uso de VPN para home office ajuda, mas não substitui outros mecanismos de autenticação e revisão de acesso

## Artefatos relacionados

- `processes/user-access-management.md`
- `processes/vendor-supplied-change-management.md`
