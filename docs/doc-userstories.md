# Documento Lista de User Stories

Documento construído a partir do **Modelo BSI - Doc 004 - Lista de User Stories**.

---

## Descrição

Este documento descreve os User Stories criados a partir da Lista de Requisitos no Documento de Visão do projeto Sistema de Gestão de Assistência Técnica.

---

## Histórico de revisões

| Data       | Versão | Descrição                                     | Autor  |
|------------|--------|-----------------------------------------------|--------|
| 30/03/2026 | 0.1.0  | Criação inicial da lista de User Stories      | Jadson |
| 31/03/2026 | 1.0.0  | Documento completo com User Stories revisado  | Jadson |
| 17/04/2026 | 1.1.0  | Correção de inconsistências e adição de novas US12 a US14 | Mariana |

---

# 📌 USER STORIES

---

## US01 - Gerenciar Cliente

**Descrição:**  
Permite ao usuário administrativo realizar todas as operações de gestão de clientes: cadastrar, atualizar, consultar e desativar clientes (PF e PJ).

**Requisitos:** RF01.1, RF01.2, RF01.3, RF01.4  

**Prioridade:** Essencial  
**Estimativa:** 8h  

**Responsáveis:**  
- Analista: Jadson  
- Desenvolvedor: Jadson  
- Revisor: Mariana  
- Testador: Jadson  

**Testes de Aceitação:**  
- Cadastrar cliente com CPF (PF) ou CNPJ (PJ) válido  
- Atualizar dados de cliente existente  
- Consultar cliente por ID, nome, CPF, CNPJ ou contato
- Desativar cliente 
- CPF/CNPJ duplicado gera erro
- Cliente com OS em aberto não pode ser desativado
- Validação de campos obrigatórios (nome, contato, documento)

---

## US02 - Gerenciar Funcionário

**Descrição:**  
Permite ao usuário administrativo gerenciar funcionários, incluindo cadastro, atualização, consulta e desativação, com classificação em Técnico ou Administrativo.

**Requisitos:** RF02.1, RF02.2, RF02.3, RF02.4  

**Prioridade:** Essencial  
**Estimativa:** 8h  

**Responsáveis:**  
- Analista: Mariana  
- Desenvolvedor: Mariana  
- Revisor: Jadson  
- Testador: Mariana  

**Testes de Aceitação:**  
- Cadastrar funcionário com tipo TECNICO (especialidade, comissão) ou ADMINISTRATIVO (cargo, setor, bônus) 
- Consulta por nome, ID, CPF, tipo ou status retorna resultados corretos 
- Dados inválidos geram erro 
- Desativar funcionário - impede login
- CPF duplicado gera erro
- Funcionário com OS em aberto não pode ser desativado

---

## US03 - Gerenciar Ordens de Serviço 

**Descrição:** 
Permite ao administrativo e técnico abrir, editar, consultar, atualizar o status da ordem de serviço conforme andamento e encerrar ordens de serviço.

**Requisitos:** RF03.1, RF03.2, RF03.3, RF03.4, RF03.5

**Prioridade:** Essencial  
**Estimativa:**  12h

**Responsáveis:**  
- Analista: Jadson  
- Desenvolvedor: Jadson  
- Revisor: Mariana  
- Testador: Jadson  

**Testes de Aceitação:**
- Abrir OS com cliente, técnico e descrição do problema
- Editar OS (descrição, técnico) - apenas se não finalizada
- Consultar OS por ID, cliente, período ou status
- Encerrar OS com status FINALIZADA e data_encerramento atual
- Cliente só vê suas próprias OS
- Técnico só vê OS onde é responsável
- OS com status FINALIZADA ou CANCELADA não pode ser editada
- Status disponíveis: ABERTA, EM_ANDAMENTO, AGUARDANDO_PECA, FINALIZADA, CANCELADA
- Técnico só altera OS onde é responsável
- Status inválido gera erro
- CANCELADA só permitido para OS em ABERTA ou EM_ANDAMENTO

---

## US04 - Gerenciar Equipamentos

**Descrição:**  
Permite cadastrar equipamentos, listar, consultar e desativar equipamentos.

**Requisitos:** RF04.1, RF04.2, RF04.3, RF04.4  

**Prioridade:** Essencial  
**Estimativa:** 6h  

**Responsáveis:**  
- Analista: Mariana  
- Desenvolvedor: Mariana  
- Revisor: Jadson  
- Testador: Mariana  

**Testes de Aceitação:**  
- Equipamento cadastrado com sucesso 
- Listar equipamentos
- Consultar equipamento por ID, código, tipo ou modelo
- Desativar equipamento 
- Código duplicado gera erro
- Equipamento vinculado a OS em aberto não pode ser desativado

---

## US05 - Vincular Equipamentos à OS

**Descrição:**  
Permite associar equipamentos a uma ordem de serviço.

**Requisitos:** RF03  

**Prioridade:** Essencial  
**Estimativa:** 4h  

**Responsáveis:**  
- Analista: Mariana  
- Desenvolvedor: Mariana  
- Revisor: Jadson  
- Testador: Mariana  

**Testes de Aceitação:**  
- Equipamento vinculado à OS com quantidade > 0 
- Equipamento inexistente gera erro  

---

## US06 - Gerenciar Visita Técnica

**Descrição:**  
Permite ao administrativo agendar visitas e ao técnico registrar a realização das visitas técnicas vinculadas a uma OS.

**Requisitos:** RF05.1, RF05.2  

**Prioridade:** Importante  
**Estimativa:** 5h  

**Responsáveis:**  
- Analista: Jadson  
- Desenvolvedor: Jadson  
- Revisor: Mariana  
- Testador: Jadson  

**Testes de Aceitação:**  
- Agendar visita com data_agendamento futura 
- OS inválida gera erro 
- Registrar realização com data_realizacao atual e resultado
- Apenas técnico designado pode registrar realização
- OS deve estar em ABERTA ou EM_ANDAMENTO
- Múltiplas visitas permitidas por OS 

---

## US07 - Gerar Relatórios

**Descrição:**
Permite gerar um relatório de ordens de serviço filtrado por período de abertura, status e técnico responsável, com opção de exportação (PDF/CSV).

**Requisitos:** RF03.6

**Prioridade:** Importante
**Estimativa:** 6h

**Responsáveis:**
- Analista: Mariana
- Desenvolvedor: Mariana
- Revisor: Jadson
- Testador: Mariana

**Testes de Aceitação:**
- Relatório gerado com sucesso no período selecionado
- Filtro por status funciona
- Filtro por técnico funciona
- Exibe: ID da OS, cliente, data_abertura, data_encerramento, status, valor_total
- Exibe totalizadores (quantidade de OS e valor total no período)
- Período inválido (data_fim < data_início) gera erro
- Opção de exportar para PDF e CSV funciona

---

## US08 - Gerenciar Contas a Receber e Pagamentos

**Descrição:**  
Gerencia automaticamente as contas a receber com valor_total da OS, data_emissão atual e data_vencimento calculada e permite registrar pagamentos (offline e online), incluindo marcar conta como paga.

**Requisitos:** RF06.1, RF06.2, RF07.1, RF07.2, RF07.3, RF07.4, RF07.5, RF07.6  

**Prioridade:** Essencial  
**Estimativa:** 12h  

**Responsáveis:**  
- Analista: Jadson  
- Desenvolvedor: Jadson  
- Revisor: Mariana  
- Testador: Jadson  

**Testes de Aceitação:**  
- Conta gerada automaticamente ao encerrar a OS  
- Campos: valor, data_emissão, data_vencimento (30 dias), status_pagamento
- Valor correto 
- Data_emissão = data atual
- Data_vencimento calculada corretamente
- OS sem valor_total válido impede encerramento 
- Cliente realiza pagamento online via gateway integrado
- Status alterado para PAGO com data_pagamento atual
- Conta já paga não pode ser alterada
- Conta vencida pode ser paga com multa
- Marcar conta como paga (status PAGO com data_pagamento atual)
- Conta com status PAGO não pode ser alterada novamente

---

## US09 - Autenticação e Controle de Acesso 

**Descrição:**
Permite login, recuperação de senha e logout para todos os perfis de usuário.

**Requisitos:** RF07.1, RF08.1, RF08.2, RF08.3

**Prioridade:** Essencial
**Estimativa:** 8h

**Responsáveis:**
- Analista: Jadson
- Desenvolvedor: Mariana
- Revisor: Jadson
- Testador: Mariana

**Testes de Aceitação:**
- Login realizado com sucesso com credenciais válidas
- E-mail ou senha incorretos geram erro
- Apenas usuários ativos podem acessar
- Sessão expira após inatividade (30 minutos)
- Senha deve ser armazenada de forma criptografada no banco de dados
- Login com e-mail e senha gera token JWT
- Senha armazenada com hash (bcrypt)
- Recuperar senha com link único (token temporário - 1 hora)
- Sessão expira após 30 minutos
- Logout invalida token
- Token contém perfil (cliente/tecnico/administrativo)

---

## US10 - Controle de Garantia 

**Descrição:**
Permite consultar e controlar o período de garantia das ordens de serviço finalizadas, com alerta para garantias próximas do vencimento ou já expiradas.

**Requisitos:** RF03

**Prioridade:** Importante
**Estimativa:** 5h

**Responsáveis:**
- Analista: Jadson
- Desenvolvedor: Jadson
- Revisor: Mariana
- Testador: Jadson

**Testes de Aceitação:**
- Exibe OS com garantia ativa (dentro do prazo)
- Exibe OS com garantia expirada (data_encerramento + garantia_dias < data atual)
- Alerta visual para garantias que vencem em até 7 dias
- Consulta por cliente ou equipamento
- Exibe quantidade de dias restantes de garantia
- Permite registrar atendimento em garantia (nova OS vinculada)

---

# Matriz de Rastreabilidade - Requisitos Funcionais x User Stories

| ID | Requisito Funcional | User Stories | Total |
|:---|:---|:---|:---:|
| RF01 | Manter Cliente | US01 | 1 |
| RF02 | Manter Funcionário | US02 | 1 |
| RF03 | Manter Ordens de Serviço | US03, US05, US06, US07, US10 | 5 |
| RF04 | Manter Equipamento | US04, US05 | 2 |
| RF05 | Agendar Visita Técnica | US06 | 1 |
| RF06 | Registrar Contas a Receber | US08 | 1 |
| RF07 | Pagar Conta | US08 | 1 |
| RF08 | Autenticar Usuário | US09 | 1 |

## 📊 Estatísticas

- **Total de Requisitos Funcionais:** 8
- **Total de User Stories:** 10
- **Média de US por RF:** 1.25
- **Total estimado de desenvolvimento:** 74h

## 🔄 Mapeamento US × Perfis de Usuário

| Perfil | User Stories |
|:---|:---|
| Cliente |	US03, US08, US09 |
| Técnico |	US03, US05, US06, US07, US09, US10 |
| Administrativo | US01, US02, US03, US04, US05, US06, US07, US08, US09, US10 |