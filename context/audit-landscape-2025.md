# Estado da Arte — Auditoria Interna, Controles e Riscos (2025)

Referência de landscape para calibrar workflows, skill gaps e posicionamento. Atualizado com base em IIA Global Standards (jan/2025), COSO GenAI guidance (fev/2026), Deloitte Hot Topics 2025 e literatura acadêmica de process mining.

---

## Nota de calibração

COSO e ERM **não estão obsoletos** — estão sendo estendidos. O problema é prática de mercado usando COSO 1992 (versão original) enquanto a versão 2013 (ICIF) + 2017 (ERM integrado com estratégia) já incorporam o que parece "novo". Tratar framework como ultrapassado geralmente indica desconhecimento da versão atual, não limitação do framework.

O que mudou: **a prática em cima dos frameworks**, não os fundamentos.

---

## 1. Mudança de paradigma central — estático → dinâmico

| Modelo antigo | Modelo atual |
|---|---|
| Look-back — amostra trimestral, plano anual | Continuous auditing + continuous monitoring |
| Teste de controle ponto-no-tempo | Bots verificando SoD, configuração e anomalia em tempo real |
| Relatório de achado no final do exercício | Finding durante o exercício, com tempo de correção |
| Amostra de população | 100% da população via analytics |

Lógica: com IA generativa e cloud mudando configuração diariamente, look-back de 12 meses é obsoleto no dia em que o relatório sai. Tipo II SOC virou fluxo contínuo, não fotografia.

---

## 2. Process Mining — padrão emergente

**O que é:** carrega log de eventos do ERP (cada transação, cada usuário, cada timestamp) e reconstrói o processo real. Compara com o processo desenhado. Revela variantes não documentadas, bypass, exceções.

**Ferramentas:** Celonis, SAP Signavio, UiPath Process Mining, Minit.

**Impacto no walkthrough:** auditor não faz entrevista e narra — carrega log e mostra desvios. O walktrough narrativo tradicional (Word/PPT) está sendo substituído em clientes grandes.

**Onde está o mercado BR:** Big 4 + algumas nacionais de ponta. Maioria do mercado ainda não adotou.

**Consequência de perfil:** auditor que não lê log de evento, não escreve query SQL básica e não interpreta process graph está em desvantagem crescente.

Referência acadêmica: Van der Aalst, "Auditing 2.0: Using Process Mining to Support Tomorrow's Auditor."

---

## 3. Agile Auditing

| Modelo tradicional | Agile Auditing |
|---|---|
| Plano anual rígido | Backlog de riscos priorizados, revisado periodicamente |
| Dois walkthroughs/ano | Sprints de 2–4 semanas |
| Achado no relatório final | Finding entregue dentro do exercício, ao longo do engajamento |
| Reunião de kickoff + reunião de encerramento | Stand-up semanal com cliente, retrospectiva por sprint |

Benefício real: risco deixa de ser "histórico" para ser "presente". Achado com correção viável ainda no período auditado.

---

## 4. IIA Global Internal Audit Standards (efetivos jan/2025)

Substituem o IPPF (Red Book). Três mudanças estruturais:

- **Requisito explícito sobre cybersecurity** — primeira vez que IIA cria mandato de domínio específico. Risco cyber não é mais opcional no escopo de IA.
- **Governance essentials** — audit committee recebe reporte contínuo, não periódico. Relação de IA com board torna-se estrutural.
- **Quality assurance reformulado** — QAR deixa de ser caixa a marcar; vira ciclo contínuo de maturidade.

Escritório que não atualizou metodologia para 2024 Standards está operando em framework antigo.

---

## 5. Three Lines Model (2020) — evolução do Three Lines of Defense

IIA retirou a palavra "defense" em 2020. Razão não é cosmética:

- "Defense" implicava silos — cada linha operando isolada, pouca coordenação
- "Lines" implica colaboração — IA pode ser advisor da 1ª linha no desenho de controle sem ferir independência
- Integração com **governance dinâmica** — board consolida as três linhas, não recebe três relatórios separados

**Integrated Assurance:** audit interno + compliance + risco + SOX testando o mesmo objeto virou custo redundante. Prática atual combina esforço, mantém independência, reduz 30–40% de horas duplicadas.

---

## 6. Risk Sensing — predição, não reação

KRI tradicional = look-back (lagging indicator). Risk sensing = AI/ML sobre dados externos e internos para antecipar onde risco vai se materializar antes da transação consumada.

Exemplos:
- ML detecta padrão de log anômalo antes da fraude
- NLP monitora notícias e redes sociais para sinal de fornecedor problemático
- Modelo de anomalia em remessa bancária antes do pagamento sair

Em empresas maduras, IA interna lidera risk sensing. Ainda raro no mercado BR.

---

## 7. AI Governance — novo campo de controle interno

COSO lançou guia específico para GenAI (fev/2026). Oito capabilities com controle próprio:

| Capability | O que cobre |
|---|---|
| Ingestion | Controle sobre dados que alimentam o modelo |
| Transformation | Processamento e pré-tratamento |
| Posting | Output que vai para sistema downstream |
| Orchestration | Agentes e pipelines de automação |
| Judgment | Decisão autônoma do modelo |
| Monitoring | Drift, anomalia, performance contínua |
| Regulatory intelligence | Compliance normativo do uso de IA |
| Human-AI interaction | Interface homem-máquina e override |

Mudança fundamental: de controles determinísticos (regra → resultado previsível) para controles probabilísticos (modelo → resultado variável). Audit precisa testar o **comportamento do modelo**, não só a regra.

**Frameworks complementares ao COSO para IA:**
- **NIST AI RMF** — governança de risco de IA (EUA)
- **ISO 42001** — primeiro ISO específico de AI management system
- **EU AI Act** — obrigação jurídica na UE; efeito extraterritorial para empresas com operação europeia

---

## 8. Cultura e comportamento como escopo auditável

**Behavioral risk assessment / Culture audit** — saiu de RH e virou responsabilidade de IA em bancos e reguladas.

Método: **etnografia de controle**. Não testa o controle desenhado — testa como pessoas o contornam, burlam, negociam. Aplicável a: Code of Conduct, whistleblower channel, tone at the top, segregação de funções informal.

Pioneiro: De Nederlandsche Bank (2011). Hoje mainstream em reguladas de países com supervisão prudencial madura. BR: incipiente fora de bancos de grande porte.

---

## 9. ESG Assurance — de opcional para regulatório

| Regulação | Escopo | Status |
|---|---|---|
| CSRD (EU) | Dupla materialidade; relatório de sustentabilidade com assurance | Efetiva 2024–2026 por fase |
| ISSB / IFRS S1 e S2 | Disclosure de clima e sustentabilidade | Adoção voluntária crescente |
| CVM 193/23 (BR) | Relatório de sustentabilidade para companhias abertas | Efetiva por fase a partir de 2024 |

Desafio técnico: **Scope 3 emissions** (cadeia de fornecedor) — pouca tradição de controle sobre dado não-financeiro. Controle de dados ESG ainda imaturo na maioria das organizações.

---

## 10. Perfil do auditor — shift de capability

| Antes (predominante) | Agora (state of the art) |
|---|---|
| Contabilidade + normas | SQL + Python/R básico |
| Narrativa de processo | Leitura de log/event stream |
| Amostra manual em Excel | Analytics sobre população completa |
| Relatório Word | Visualização interativa (Power BI, Tableau) |
| Conhecimento de COSO | Conhecimento de COSO + NIST + ISO 42001 |
| Auditoria por processo | Auditoria por risco + dados |

Auditor "só contábil" está migrando para SSC (commodity processual). Auditor "engenheiro de dado" escala em remuneração e escopo.

---

## O que **não** é state of the art (apesar do marketing)

| Hype | Realidade |
|---|---|
| Blockchain audit | Promessa não entregue para auditoria geral; útil em nicho (crypto, supply chain específico) |
| RPA puro | Virou commodity; não é diferencial de IA nem de auditor |
| ISO 31000 puro | Boa linguagem de risco, ruim como método — genérico demais para execução |
| GRC tool centralizado sem metodologia | Archer, MetricStream: ferramenta sem método subjacente não entrega; viram repositório de papel digital |

---

## Onde o mercado BR está atrasado

- Walkthrough narrativo Word ainda dominante
- Seleção de amostra manual em Excel na maioria dos escritórios
- Process mining restrito a Big 4 + tier nacional de ponta
- Culture audit inexistente fora de banco
- AI governance sendo adotada só por reguladas e multinacionais
- Continuous auditing ainda em projeto-piloto na maioria

**Arbitragem de carreira:** adotar process mining, continuous monitoring e agile auditing agora gera vantagem diferencial em 3–5 anos no mercado BR.

---

## Referências

- IIA Global Internal Audit Standards (2024) — texto oficial
- COSO Guidance on Internal Controls for Generative AI (2026)
- Van der Aalst — "Auditing 2.0: Using Process Mining to Support Tomorrow's Auditor"
- Deloitte Internal Audit Hot Topics 2025
- Protiviti Internal Audit Capabilities and Needs Survey (anual)
- IIA Risk in Focus (anual) — priorização de riscos por região
- Journal of Information Systems — "Integrating Process Mining and Machine Learning for Advanced Internal Control Evaluation in Auditing" (2025)
