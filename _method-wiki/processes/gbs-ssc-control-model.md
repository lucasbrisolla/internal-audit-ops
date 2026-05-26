# GBS and SSC Control Model

## Papel

Referência para trabalhos de auditoria em empresas com serviços compartilhados, GBS, CSC, finance business partners ou transformações operacionais multisite.

## Quando usar

- entender modelo operacional de finanças ou operações centralizadas
- planejar auditoria em transição para SSC/GBS
- mapear riscos estruturais antes de mapear controles
- avaliar governança entre operação transacional, CoE e negócio

## Global Business Services

`GBS` centraliza processos transacionais em estrutura regional ou global, separando execução padronizada de parceria estratégica com o negócio.

Processos tipicamente centralizados:

| Sigla | Nome | Cobertura |
|---|---|---|
| P2P | Procure-to-Pay | Compras, recebimento e pagamento a fornecedores |
| OTC | Order-to-Cash | Pedido, faturamento e recebimento de clientes |
| RTR | Record-to-Report | Lançamentos contábeis, fechamento, consolidação e reporte |

## Three-tier finance model

| Camada | Estrutura | Função |
|---|---|---|
| Transacional | SSC / GBS | Executa P2P, OTC e RTR em volume, com padronização e custo baixo |
| Especialista | CoE | Expertise técnica em fiscal, tesouraria, contabilidade técnica ou temas especializados |
| Estratégica | FBP | Parceiro do negócio em análise, suporte à decisão e forecast |

## Três linhas de defesa em SSC/GBS

| Linha | Quem | Papel |
|---|---|---|
| 1ª linha | Operações / donos do processo / SSC | Executam e possuem os controles no dia a dia |
| 2ª linha | Risk management, compliance, controladoria, FBP | Monitoram qualidade, SLAs, políticas e conformidade |
| 3ª linha | Auditoria interna | Dá assurance independente sobre as duas primeiras linhas |

Achado de controle ausente na 1ª linha é diferente de ausência de oversight da 2ª linha. As causas e recomendações devem refletir essa distinção.

## Riscos específicos de transformação GBS

| Risco | Onde auditar |
|---|---|
| Controles existiam na operação regional mas não foram redesenhados no GBS | Design do novo modelo (ToD) |
| Período de transição com operação dupla gera gap de controle | Migração, corte e cutover |
| SLA entre GBS e entidades não é monitorado | Governança do CSC |
| Segregação de funções violada no modelo centralizado | Matriz de SoD no sistema global |
| Regulatório local ignorado na padronização global | Conformidade por jurisdição |

## Implicação de auditoria

Transformação para modelo GBS/SSC é decisão estratégica que altera o perfil de risco operacional. O risk assessment corporativo deve ser atualizado, e a auditoria deve avaliar tanto o desenho do modelo quanto a operação após estabilização.

## Abordagem recomendada

- Antes do go-live: avaliar desenho dos controles, SoD, SLAs, cutover e aderência regulatória local.
- Durante a implantação: monitorar gestão do projeto, treinamento, migração, controles temporários e operação paralela.
- Após o go-live: testar se os controles operam como desenhados, se SLAs são monitorados e se exceções são tratadas.
