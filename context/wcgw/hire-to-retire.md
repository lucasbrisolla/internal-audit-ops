---
processo: hire-to-retire
nivel: 1
abreviacao: H2R
subprocessos:
  - recrutamento-e-admissao
  - cadastro-e-dados-do-funcionario
  - processamento-de-folha
  - beneficios-e-encargos
  - mudancas-de-remuneracao
  - desligamento-e-rescisao
assercoes_primarias:
  - existência
  - completude
  - valoração
  - corte
frameworks:
  - COSO
  - SOX
  - CLT
  - eSocial
referencias:
  - _method-wiki/processes/fraud-risk-assessment.md
  - _method-wiki/processes/user-access-management.md
---

# WCGW — Hire-to-Retire (H2R)

H2R cobre o ciclo de vida completo do funcionário — da admissão ao desligamento. O risco central é **funcionário fictício** (ghost employee): alguém que recebe salário sem trabalhar, criado ou mantido por quem controla o cadastro e a folha. Mas o risco vai além: benefícios indevidos, rescisões calculadas incorretamente e encargos subestimados também são materiais.

Folha de pagamento tende a ser um dos maiores custos operacionais — distorções aqui têm impacto direto no resultado.

---

## Subprocesso 1: Recrutamento e Admissão

Etapa onde o funcionário é contratado e integrado formalmente à organização.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| H2R-001 | Funcionário admitido sem documentação completa — vínculo sem base formal | Initiation | Existência | Alta |
| H2R-002 | Contratação sem aprovação formal da vaga — headcount não autorizado | Initiation | Existência | Alta |
| H2R-003 | Cargo ou nível hierárquico definido sem critério formal — favorecimento | Initiation | Valoração | Média |
| H2R-004 | Background check não realizado para funções sensíveis (financeiro, TI, compliance) | Initiation | Existência | Alta |
| H2R-005 | Parente ou cônjuge de gestor admitido sem aprovação de compliance — nepotismo | Initiation | Existência | Alta |
| H2R-006 | Funcionário admitido com salário fora da faixa aprovada para o cargo | Initiation | Valoração | Alta |
| H2R-007 | Contrato de trabalho não assinado ou com cláusulas divergentes do acordado | Initiation | Existência | Média |

**Controles típicos que mitigam:**
- aprovação formal de vaga por RH e gestor financeiro antes de iniciar recrutamento
- checklist de admissão com documentos obrigatórios e responsável pela verificação
- background check obrigatório para funções de alta sensibilidade
- política de conflito de interesse com declaração anual e processo de aprovação de parentes
- faixa salarial aprovada por cargo com exceções documentadas e aprovadas por alçada superior

---

## Subprocesso 2: Cadastro e Dados do Funcionário

Etapa de registro dos dados do funcionário no sistema de RH/folha. Controla quem recebe e quanto.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| H2R-008 | Funcionário fictício (ghost employee) cadastrado para desvio de folha | Recording | Existência | Crítico |
| H2R-009 | Dados bancários alterados por usuário não autorizado — salário desviado para conta terceira | Processing | Existência | Crítico |
| H2R-010 | Mesma pessoa cadastra funcionário e processa folha — segregação quebrada | Processing | Existência | Crítico |
| H2R-011 | Alteração de salário no sistema sem aprovação documentada | Processing | Valoração | Alta |
| H2R-012 | Funcionário desligado mantido ativo no sistema — pagamentos indevidos | Processing | Existência | Alta |
| H2R-013 | Cargo ou centro de custo incorreto — custo alocado à área errada | Recording | Apresentação | Média |
| H2R-014 | Acesso ao sistema de RH não restrito — qualquer usuário pode alterar dados de funcionários | Processing | Existência | Alta |

**Controles típicos que mitigam:**
- segregação entre quem cadastra funcionário, quem altera dados bancários e quem processa folha
- aprovação dupla para alteração de dados bancários com notificação ao funcionário
- relatório mensal de funcionários novos, alterados e desligados revisado por gestor independente
- acesso ao sistema de RH restrito por função com log de alterações
- reconciliação entre cadastro de RH e folha processada — qualquer divergência investigada

---

## Subprocesso 3: Processamento de Folha de Pagamento

Cálculo e pagamento dos salários, incluindo horas extras, adicionais e deduções.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| H2R-015 | Folha processada sem revisão independente antes do pagamento | Processing | Existência | Alta |
| H2R-016 | Horas extras aprovadas sem controle de ponto formal — volume não verificável | Processing | Valoração | Alta |
| H2R-017 | Horas extras aprovadas pelo próprio beneficiário — sem supervisão independente | Processing | Existência | Alta |
| H2R-018 | Adicionais (periculosidade, insalubridade, noturno) aplicados sem verificação de elegibilidade | Processing | Valoração | Média |
| H2R-019 | Folha de período anterior reprocessada sem motivo documentado | Processing | Existência | Alta |
| H2R-020 | Pagamento fora da folha (pagamento avulso) sem aprovação formal | Processing | Existência | Alta |
| H2R-021 | Folha fechada sem comparação analítica com mês anterior — variações não investigadas | Processing | Valoração | Alta |
| H2R-022 | Erros de cálculo de INSS, IRRF ou FGTS — passivo trabalhista subestimado | Processing | Valoração | Alta |

**Controles típicos que mitigam:**
- revisão da folha por gestor independente antes do processamento (aprovação formal)
- sistema de ponto eletrônico com aprovação de horas extras pelo gestor do funcionário (não pelo próprio)
- relatório de variação mensal da folha com explicação de variações acima de X%
- pagamentos avulsos com aprovação documentada e registro separado
- validação de cálculos de encargos (INSS, IRRF, FGTS) contra tabelas vigentes

---

## Subprocesso 4: Benefícios e Encargos

Gestão de benefícios (vale-refeição, plano de saúde, transporte) e encargos trabalhistas (FGTS, INSS, férias, 13º).

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| H2R-023 | Benefício concedido a funcionário inelegível — ex-funcionário ou cargo não coberto | Processing | Existência | Alta |
| H2R-024 | Provisão de férias não constituída ou subavaliada — passivo oculto | Recording | Completude | Alta |
| H2R-025 | Provisão de 13º salário não constituída mensalmente — subestimação de custo | Recording | Completude | Alta |
| H2R-026 | FGTS não recolhido no prazo — passivo com multa não reconhecido | Recording | Completude | Alta |
| H2R-027 | Benefício alterado sem comunicação ao funcionário — risco trabalhista | Processing | Existência | Média |
| H2R-028 | Encargos calculados sobre base incorreta — INSS patronal subestimado | Processing | Valoração | Alta |
| H2R-029 | Dependentes de plano de saúde não validados periodicamente — cobertura indevida | Processing | Existência | Média |

**Controles típicos que mitigam:**
- lista de elegibilidade por benefício revisada periodicamente contra folha ativa
- provisão mensal de férias e 13º com metodologia documentada e revisão do controller
- validação de dependentes de plano de saúde com documentação anual
- conciliação de recolhimentos de FGTS e INSS com guias e razão contábil
- cálculo de encargos com base atualizada às tabelas vigentes (revisão a cada alteração legislativa)

**Flag de risco elevado:** empresas com alta rotatividade — maior risco de provisões de férias e rescisões subestimadas, e de ex-funcionários mantidos em benefícios por falta de processo de desligamento.

---

## Subprocesso 5: Mudanças de Remuneração

Promoções, reajustes salariais, alterações de cargo e benefícios ao longo do vínculo.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| H2R-030 | Aumento salarial concedido sem aprovação formal — acima da alçada do gestor direto | Processing | Valoração | Alta |
| H2R-031 | Promoção retroativa criada para justificar pagamento passado irregular | Processing | Existência | Alta |
| H2R-032 | Reajuste salarial não aplicado a toda a categoria quando deveria (acordo coletivo) | Processing | Completude | Alta |
| H2R-033 | Cargo alterado no sistema sem reflexo no contrato de trabalho — divergência jurídica | Recording | Existência | Média |
| H2R-034 | Comissão ou variável calculada sobre base incorreta — superavaliação de custo ou receita | Processing | Valoração | Alta |
| H2R-035 | Stock options ou benefícios de longo prazo não reconhecidos contabilmente (IFRS 2) | Recording | Completude | Alta |

**Controles típicos que mitigam:**
- tabela de alçadas para aprovação de aumentos por faixa salarial e percentual
- processo de promoção com aprovação de RH, gestor e área financeira
- rastreabilidade entre aditivo ao contrato e alteração no sistema de RH
- metodologia de cálculo de variável/comissão documentada e aprovada antes do período
- avaliação de IFRS 2 para planos de remuneração baseada em ações

---

## Subprocesso 6: Desligamento e Rescisão

Etapa de encerramento do vínculo — cálculo, pagamento e baixa do funcionário nos sistemas.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| H2R-036 | Cálculo de rescisão incorreto — verbas indevidas pagas ou verbas devidas não pagas | Processing | Valoração | Alta |
| H2R-037 | Funcionário desligado mantido na folha por falta de comunicação ao RH | Processing | Existência | Alta |
| H2R-038 | Acesso de sistemas não revogado no desligamento — risco de segurança (ver UAM) | Processing | Existência | Alta |
| H2R-039 | FGTS de rescisão não recolhido ou recolhido com valor incorreto | Processing | Valoração | Alta |
| H2R-040 | Multa de 40% do FGTS não reconhecida na provisão — passivo subestimado | Recording | Completude | Alta |
| H2R-041 | Desligamento classificado incorretamente (pedido de demissão vs. demissão sem justa causa) — impacto em verbas | Recording | Valoração | Alta |
| H2R-042 | Aviso prévio indenizado calculado incorrectamente — base de tempo de serviço errada | Processing | Valoração | Média |
| H2R-043 | Pagamento de rescisão sem homologação quando exigida — risco jurídico | Processing | Existência | Média |

**Controles típicos que mitigam:**
- checklist de desligamento com RH, TI, gestor e financeiro — integrado ao processo de UAM
- cálculo de rescisão revisado por RH e jurídico antes do pagamento
- comunicação imediata de desligamento ao RH para baixa na folha no mesmo período
- reconciliação entre desligamentos do mês e variação de headcount na folha
- revisão da modalidade de desligamento com jurídico trabalhista para verbas corretas

---

## Leitura Rápida por Risco

| Risco Central | Subprocessos Críticos | WCGW-chave |
|---|---|---|
| Funcionário fictício (ghost employee) | Cadastro | H2R-008, H2R-010 |
| Dados bancários desviados | Cadastro | H2R-009 |
| Horas extras sem controle | Processamento | H2R-016, H2R-017 |
| Provisões de férias/13º subestimadas | Benefícios | H2R-024, H2R-025 |
| Desligado mantido na folha | Cadastro, Desligamento | H2R-012, H2R-037 |
| Rescisão calculada incorretamente | Desligamento | H2R-036, H2R-041 |
| Aumento sem aprovação formal | Mudanças | H2R-030, H2R-031 |
| Stock options não reconhecidas (IFRS 2) | Mudanças | H2R-035 |
