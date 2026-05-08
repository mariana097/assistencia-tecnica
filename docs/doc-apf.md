# Contagem de Pontos de Função - Sistema de Gestão de Assistência Técnica

## 1. Introdução

São apresentadas três abordagens de contagem:
- **Contagem Indicativa (Ci)** - baseada apenas em funções de dados
- **Contagem Estimativa (Ce)** - dados com complexidade baixa + transações com complexidade média
- **Contagem Detalhada (Cd)** - classificação individual por complexidade

---

## 2. Base de Contagem

Com base no **Documento de Visão** e na **Lista de User Stories**, foram identificadas as seguintes entidades e funcionalidades.

### 2.1 Entidades do Sistema (Funções de Dados)

| # | Entidade | Descrição |
|:---:|:---|:---|
| 1 | USUARIO | Entidade base para autenticação |
| 2 | CLIENTE | Clientes PF e PJ |
| 3 | FUNCIONARIO | Funcionários (Técnico e Administrador) |
| 4 | APARELHO | Equipamentos dos clientes |
| 5 | ORDEM_SERVICO | Ordens de serviço |
| 6 | SERVICO | Catálogo de serviços |
| 7 | SERVICO_EXECUTADO | Serviços realizados em OS |
| 8 | EQUIPAMENTO | Estoque de peças/equipamentos |
| 9 | EQUIPAMENTO_USADO | Equipamentos consumidos em serviços |
| 10 | VISITA_TECNICA | Visitas agendadas |
| 11 | CONTA_RECEBER | Contas financeiras |
| 12 | PAGAMENTO | Transações de pagamento |
| 13 | NOTIFICACAO | Notificações do sistema |
| 14 | AUDITORIA_LOG | Logs de auditoria |

### 2.2 Interfaces Externas (AIE)

| # | Interface | Descrição |
|:---:|:---|:---|
| 1 | Gateway de Pagamento | Integração para pagamentos online |
| 2 | Serviço de E-mail | Envio de e-mails (recuperação de senha, notificações) |

---

## 3. Contagem Indicativa (Ci)

Na contagem indicativa, consideramos apenas as **Funções de Dados**:
- **ALI** (Arquivo Lógico Interno) = 35 PF cada
- **AIE** (Arquivo de Interface Externa) = 15 PF cada

### 3.1 Tabela de Contagem Indicativa

| Tipo | Entidade | PF |
|:---:|:---|:---:|
| ALI | USUARIO | 35 |
| ALI | CLIENTE | 35 |
| ALI | FUNCIONARIO | 35 |
| ALI | APARELHO | 35 |
| ALI | ORDEM_SERVICO | 35 |
| ALI | SERVICO | 35 |
| ALI | SERVICO_EXECUTADO | 35 |
| ALI | EQUIPAMENTO | 35 |
| ALI | EQUIPAMENTO_USADO | 35 |
| ALI | VISITA_TECNICA | 35 |
| ALI | CONTA_RECEBER | 35 |
| ALI | PAGAMENTO | 35 |
| ALI | NOTIFICACAO | 35 |
| ALI | AUDITORIA_LOG | 35 |
| AIE | Gateway de Pagamento | 15 |
| AIE | Serviço de E-mail | 15 |

### 3.2 Resultado da Contagem Indicativa

Ci = (14 ALIs × 35 PF) + (2 AIEs × 15 PF)
Ci = 490 PF + 30 PF
Ci = 520 PF

---

## 4. Contagem Estimativa (Ce)

Na contagem estimativa:
- **Funções de Dados** são classificadas como **complexidade baixa**
- **Funções de Transação** (EE, CE, SE) são classificadas como **complexidade média**
  - EE (Entrada Externa) = 4 PF
  - CE (Consulta Externa) = 4 PF
  - SE (Saída Externa) = 5 PF

### 4.1 Funções de Dados - Complexidade Baixa

| Tipo | Entidade | Complexidade | PF |
|:---:|:---|:---:|:---:|
| ALI | USUARIO | Baixa | 7 |
| ALI | CLIENTE | Baixa | 7 |
| ALI | FUNCIONARIO | Baixa | 7 |
| ALI | APARELHO | Baixa | 7 |
| ALI | ORDEM_SERVICO | Baixa | 7 |
| ALI | SERVICO | Baixa | 7 |
| ALI | SERVICO_EXECUTADO | Média | 10 |
| ALI | EQUIPAMENTO | Baixa | 7 |
| ALI | EQUIPAMENTO_USADO | Baixa | 7 |
| ALI | VISITA_TECNICA | Baixa | 7 |
| ALI | CONTA_RECEBER | Média | 10 |
| ALI | PAGAMENTO | Baixa | 7 |
| ALI | NOTIFICACAO | Baixa | 7 |
| ALI | AUDITORIA_LOG | Baixa | 7 |
| AIE | Gateway de Pagamento | Baixa | 5 |
| AIE | Serviço de E-mail | Baixa | 5 |

**Subtotal Funções de Dados (Ce)** = (12 × 7) + (2 × 10) + (2 × 5) = 84 + 20 + 10 = **114 PF**

### 4.2 Funções de Transação - Complexidade Média

| Operação | Tipo | Entidade Principal | PF |
|:---|:---:|:---|:---:|
| Realizar Login | EE | USUARIO | 4 |
| Recuperar Senha | EE | USUARIO | 4 |
| Logout | EE | USUARIO | 4 |
| Cadastrar Cliente | EE | CLIENTE | 4 |
| Alterar Cliente | EE | CLIENTE | 4 |
| Consultar Cliente | CE | CLIENTE | 4 |
| Desativar Cliente | EE | CLIENTE | 4 |
| Listar Clientes | CE | CLIENTE | 4 |
| Cadastrar Funcionário | EE | FUNCIONARIO | 4 |
| Alterar Funcionário | EE | FUNCIONARIO | 4 |
| Consultar Funcionário | CE | FUNCIONARIO | 4 |
| Desativar Funcionário | EE | FUNCIONARIO | 4 |
| Listar Funcionários | CE | FUNCIONARIO | 4 |
| Cadastrar Aparelho | EE | APARELHO | 4 |
| Alterar Aparelho | EE | APARELHO | 4 |
| Consultar Aparelho | CE | APARELHO | 4 |
| Desativar Aparelho | EE | APARELHO | 4 |
| Listar Aparelhos do Cliente | CE | APARELHO | 4 |
| Abrir OS | EE | ORDEM_SERVICO | 4 |
| Editar OS | EE | ORDEM_SERVICO | 4 |
| Consultar OS | CE | ORDEM_SERVICO | 4 |
| Atualizar Status OS | EE | ORDEM_SERVICO | 4 |
| Encerrar OS | EE | ORDEM_SERVICO | 4 |
| Listar OS (múltiplos filtros) | CE | ORDEM_SERVICO | 4 |
| Cadastrar Serviço | EE | SERVICO | 4 |
| Alterar Serviço | EE | SERVICO | 4 |
| Consultar Serviço | CE | SERVICO | 4 |
| Desativar Serviço | EE | SERVICO | 4 |
| Iniciar Execução Serviço | EE | SERVICO_EXECUTADO | 4 |
| Pausar Execução Serviço | EE | SERVICO_EXECUTADO | 4 |
| Retomar Execução Serviço | EE | SERVICO_EXECUTADO | 4 |
| Finalizar Execução Serviço | EE | SERVICO_EXECUTADO | 4 |
| Consultar Serviços Executados | CE | SERVICO_EXECUTADO | 4 |
| Cadastrar Equipamento | EE | EQUIPAMENTO | 4 |
| Atualizar Estoque | EE | EQUIPAMENTO | 4 |
| Consultar Equipamento | CE | EQUIPAMENTO | 4 |
| Desativar Equipamento | EE | EQUIPAMENTO | 4 |
| Listar Equipamentos | CE | EQUIPAMENTO | 4 |
| Registrar Equipamento Usado | EE | EQUIPAMENTO_USADO | 4 |
| Remover Equipamento Usado | EE | EQUIPAMENTO_USADO | 4 |
| Agendar Visita Técnica | EE | VISITA_TECNICA | 4 |
| Registrar Realização Visita | EE | VISITA_TECNICA | 4 |
| Visualizar Contas Pendentes | CE | CONTA_RECEBER | 4 |
| Registrar Pagamento Offline | EE | PAGAMENTO | 4 |
| Realizar Pagamento Online | EE | PAGAMENTO | 4 |
| Estornar Pagamento | EE | PAGAMENTO | 4 |
| Emitir Comprovante | SE | PAGAMENTO | 5 |
| Gerar Relatório OS | SE | ORDEM_SERVICO | 5 |
| Exportar Relatório (PDF/CSV) | SE | RELATORIO | 5 |
| Consultar Garantias Ativas | CE | SERVICO_EXECUTADO | 4 |
| Registrar Atendimento Garantia | EE | ORDEM_SERVICO | 4 |
| Enviar Notificação | EE | NOTIFICACAO | 4 |
| Marcar Notificação como Lida | EE | NOTIFICACAO | 4 |

**Total de Transações:** 58 operações
- 53 operações EE/CE (4 PF cada) = 212 PF
- 5 operações SE (5 PF cada) = 25 PF

**Subtotal Funções de Transação (Ce)** = 212 + 25 = **237 PF**

### 4.3 Resultado da Contagem Estimativa

Ce = Dados (114 PF) + Transações (237 PF)
Ce = 351 PF

---

## 5. Contagem Detalhada (Cd)

Na contagem detalhada, classificamos cada função por sua complexidade (Baixa, Média, Alta) baseada em:

- **Para ALI/AIE**: Número de TRLs (Tipos de Registro Lógico) e DERs (Elementos de Dados Referenciados)
- **Para EE/CE/SE**: Número de ALRs (Arquivos Lógicos Referenciados) e DERs

### 5.1 Tabela de Complexidade para Funções de Dados

| Complexidade | ALI (TRL) | ALI (DER) | AIE (TRL) | AIE (DER) | PF |
|:---:|:---:|:---:|:---:|:---:|:---:|
| Baixa | 1 | 1-19 | 1 | 1-5 | 7 (ALI) / 5 (AIE) |
| Média | 2 | 1-19 | 2 | 1-5 | 10 (ALI) / 7 (AIE) |
| Alta | 1-2 | 20-50 | 1-2 | 6-20 | 15 (ALI) / 10 (AIE) |

### 5.2 Funções de Dados - Classificação Detalhada

| Entidade | Tipo | TRL | DER | Complexidade | PF |
|:---|:---:|:---:|:---:|:---:|:---:|
| USUARIO | ALI | 1 | 8 | Baixa | 7 |
| CLIENTE (com PF/PJ) | ALI | 2 | 11 | Média | 10 |
| FUNCIONARIO (com TEC/ADM) | ALI | 2 | 12 | Média | 10 |
| APARELHO | ALI | 1 | 8 | Baixa | 7 |
| ORDEM_SERVICO | ALI | 1 | 9 | Baixa | 7 |
| SERVICO | ALI | 1 | 6 | Baixa | 7 |
| SERVICO_EXECUTADO | ALI | 2 | 13 | Alta | 15 |
| EQUIPAMENTO | ALI | 1 | 9 | Baixa | 7 |
| EQUIPAMENTO_USADO | ALI | 2 | 6 | Baixa | 7 |
| VISITA_TECNICA | ALI | 1 | 7 | Baixa | 7 |
| CONTA_RECEBER | ALI | 2 | 14 | Alta | 15 |
| PAGAMENTO | ALI | 1 | 8 | Baixa | 7 |
| NOTIFICACAO | ALI | 1 | 9 | Baixa | 7 |
| AUDITORIA_LOG | ALI | 1 | 10 | Média | 10 |
| Gateway de Pagamento | AIE | 1 | 5 | Baixa | 5 |
| Serviço de E-mail | AIE | 1 | 3 | Baixa | 5 |

**Subtotal Funções de Dados (Cd):**
- Baixa (7 PF): 10 entidades = 70 PF
- Média (10 PF): 3 entidades = 30 PF
- Alta (15 PF): 2 entidades = 30 PF
- AIE Baixa (5 PF): 2 entidades = 10 PF

**Total Dados = 140 PF**

### 5.3 Funções de Transação - Principais Exemplos Classificados

| Operação | Tipo | ALR | DER | Complexidade | PF |
|:---|:---:|:---:|:---:|:---:|:---:|
| Realizar Login | EE | 1 | 2 | Baixa | 3 |
| Recuperar Senha | EE | 2 | 1 | Média | 4 |
| Cadastrar Cliente | EE | 1 | 7 | Baixa | 3 |
| Consultar Cliente (filtros) | CE | 1 | 4 | Baixa | 3 |
| Cadastrar Funcionário (com tipo) | EE | 2 | 10 | Alta | 6 |
| Abrir OS | EE | 3 | 7 | Alta | 6 |
| Atualizar Status OS | EE | 1 | 2 | Baixa | 3 |
| Encerrar OS (com validações) | EE | 4 | 9 | Alta | 6 |
| Iniciar Execução Serviço | EE | 2 | 3 | Média | 4 |
| Finalizar Execução (calcula comissão) | EE | 3 | 6 | Alta | 6 |
| Registrar Pagamento Online | EE | 3 | 8 | Alta | 6 |
| Gerar Relatório OS | SE | 3 | 12 | Alta | 7 |
| Exportar Relatório (PDF/CSV) | SE | 1 | 3 | Baixa | 4 |
| Consultar Garantias Ativas | CE | 2 | 5 | Média | 4 |

### 5.4 Resumo das Transações (58 operações)

| Complexidade | Quantidade | PF/unidade | Subtotal |
|:---|:---:|:---:|:---:|
| Baixa | 30 | 3 | 90 |
| Média | 18 | 4 | 72 |
| Alta | 10 | 6 | 60 |

**Subtotal Funções de Transação (Cd)** = 90 + 72 + 60 = **222 PF**

### 5.5 Resultado da Contagem Detalhada

Cd = Dados (140 PF) + Transações (222 PF)
Cd = 362 PF

---

## 6. Resumo das Contagens

| Método | Sigla | Total PF | Variação em relação à Ci |
|:---|:---:|:---:|:---:|
| Contagem Indicativa | Ci | 520 | Base |
| Contagem Estimativa | Ce | 351 | -32,5% |
| Contagem Detalhada | Cd | 362 | -30,4% |

### 6.1 Faixa Recomendada

**350 a 370 PF** (base na Contagem Detalhada)

---

## 7. Estimativa de Custo e Prazo

### 7.1 Considerações

| Parâmetro | Valor |
|:---|:---:|
| Produtividade Python (base SERPRO) | 8 horas/PF |
| Jornada diária por desenvolvedor | 8 horas |
| Equipe | 2 desenvolvedores (Jadson e Mariana) |
| Custo por hora (base exemplo) | R$ 17,00 |
| Pontos de Função adotados | 362 PF (Cd) |

### 7.2 Cálculo Base (362 PF)

| Parâmetro | Cálculo | Resultado |
|:---|:---|:---:|
| Horas totais | 362 PF × 8h | 2.896 horas |
| Dias com 2 devs | 2.896h ÷ (2 × 8h) | 181 dias |
| Meses (~22 dias úteis/mês) | 181 ÷ 22 | ~8,2 meses |
| Custo total | 2.896h × R$ 17,00 | **R$ 49.232,00** |

### 7.3 Comparativo de Cenários

| Cenário | Produtividade | Horas | Dias (2 devs) | Meses | Custo Total |
|:---|:---:|:---:|:---:|:---:|:---:|
| Otimista | 6h/PF | 2.172h | 136 | ~6,2 | R$ 36.924,00 |
| Realista (base) | 8h/PF | 2.896h | 181 | ~8,2 | R$ 49.232,00 |
| Conservador | 10h/PF | 3.620h | 226 | ~10,3 | R$ 61.540,00 |

---

## 8. Matriz de Rastreabilidade PF × User Stories

| ID | User Story | PF Estimado (Cd) | % do Total |
|:---:|:---|:---:|:---:|
| US00 | Manter Usuário | 12 | 3,3% |
| US01 | Manter Cliente | 18 | 5,0% |
| US02 | Manter Funcionário | 22 | 6,1% |
| US03 | Gerenciar Aparelho | 15 | 4,1% |
| US04 | Gerenciar Ordem de Serviço | 35 | 9,7% |
| US05 | Manter Serviço | 12 | 3,3% |
| US06 | Registrar Serviço Executado | 28 | 7,7% |
| US07 | Gerenciar Equipamento | 18 | 5,0% |
| US08 | Gerenciar Equipamento Usado | 12 | 3,3% |
| US09 | Agendar Visita Técnica | 14 | 3,9% |
| US10 | Gerenciar Conta a Receber | 22 | 6,1% |
| US11 | Gerenciar Pagamento | 35 | 9,7% |
| US12 | Gerar Relatório | 25 | 6,9% |
| US13 | Controle de Garantia | 18 | 5,0% |
| - | Integrações, Segurança, Deploy | 76 | 21,0% |
| **TOTAL** | | **362** | **100%** |

---

## 9. Recomendações

1. **Utilizar a Contagem Detalhada (362 PF)** como base para planejamento do projeto, pois reflete com mais precisão a complexidade real do sistema.

2. **Primeira entrega (MVP)** - Priorizar as funcionalidades essenciais:
   - US00, US01, US02, US03, US04, US05, US10, US11
   - Representa cerca de 60-70% dos pontos de função (~220-250 PF)
   - Prazo estimado: 4-5 meses com 2 desenvolvedores

3. **Ajustar a produtividade inicialmente** - O valor de 8h/PF pode ser otimista para um sistema com integrações externas (gateway de pagamento, e-mail). Recomenda-se:
   - Iniciar com 10h/PF nas primeiras sprints para calibrar
   - Revisar a métrica após cada sprint

4. **Custo total estimado:** R$ 49.000,00 a R$ 62.000,00

5. **Prazo total estimado:** 6 a 10 meses (dependendo da produtividade real)

6. **Revisão contínua:** Recomenda-se revisar as estimativas após cada sprint para refinar os números e ajustar o planejamento.

---

## 10. Histórico de Revisões

| Data | Versão | Descrição | Autor |
|:---|:---:|:---|:---|
| 08/05/2026 | 1.0.0 | Criação inicial do documento de contagem de PF | Mariana |
| 08/05/2026 | 1.0.0 | Revisão e validação das contagens | Jadson |

---

