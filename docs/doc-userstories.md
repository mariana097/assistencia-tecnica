# Lista de User Stories

| ID   | Título      | Descrição                                                     | Requisitos Funcionais | Responsável |
|------|-------------|---------------------------------------------------------------|----------------------|--------------|
| US00 | Manter Usuário | Permite login, recuperação de senha e logout para todos os perfis de usuário. O email será o login e ele pode registrar-se diretamente no sistema. Além disso o usuário poderá alterar alguns dados, como o e-mail ou a senha. O usuário administrador do sistema pode realizar as operações de cadastrar, atualizar, consultar, desativar e listar os usuários comuns do sistema.| RF00 | Mariana |     
| US01 | Manter cliente | O sistema deve manter um cadastro de cliente que tem acesso ao sistema via login e senha. Um cliente tem os atributos nome, id, endereço, contato. O usuário administrador do sistema pode realizar as operações de cadastrar, atualizar, consultar, desativar e listar os clientes do sistema.| RF01 | Jadson |
| US02 | Manter Funcionario | O sistema deve manter um cadastro de funcionário que tem acesso ao sistema via login e senha. Um funcionário tem os atributos id, nome, cpf, contato, salario, data_admissao, horario_expediente, status.  O usuário administrador do sistema pode realizar as operações de cadastrar, atualizar, consultar e desativar funcionario do sistema.  | RF02 | Mariana    |
| US03 | Gerenciar Aparelho | O sistema deve manter um cadastro de aparelho de um cliente. Um aparelho tem os atributos id, tipo, marca, modelo, numero_serie, cor, observações, cliente_id | RF03 | Jadson |
| US04 | Gerenciar Ordem_Serviço | Permite ao administrador abrir, consultar, atualizar, encerrar ordens de serviço | RF04 | Mariana |
| US05 | Manter Serviço | Permite ao usuário administrador gerenciar o catálogo de serviços oferecidos pela assistência técnica, incluindo cadastro, consulta, atualização e desativação de serviços, com seus respectivos valores padrão e tempo estimado de execução.| RF05 | Jadson |
| US06 | Registrar Serviço_Executado | Registra a execução de um serviço específico em uma ordem de serviço, com controle de tempo real, técnico responsável e cálculo automático de comissão.| RF06 | Mariana |
| US07 | Gerenciar Equipamento | Permite ao administrador cadastrar, consultar, atualizar, controlar estoque e desativar equipamentos/peças utilizados nos serviços. | RF07 | Jadson |
| US08 | Gerenciar Equipamento_Usado | Permite associar equipamentos a uma ordem de serviço.| RF08 | Mariana |
| US09 | Agendar Visita_Técnica | Permite ao administrador agendar visitas e ao técnico registrar a realização das visitas técnicas vinculadas a uma OS.| RF09 | Jadson |
| US10 |Gerenciar Conta_Receber | Gerencia automaticamente as contas a receber com valor_total da OS, data_emissão atual e data_vencimento calculada e permite registrar pagamentos (offline e online), incluindo marcar conta como paga. | RF10 | Mariana |
| US11 | Gerenciar Pagamento | Registra cada transação de pagamento realizada, permitindo que uma única conta a receber tenha múltiplos pagamentos (parcelado).| RF11 | Jadson |
| US12 | Gerar Relatório | Permite gerar um relatório de ordens de serviço filtrado por período de abertura, status e técnico responsável, com opção de exportação.| RF12 | Mariana |
| US13 | Controle de Garantia | Permite consultar e controlar o período de garantia das ordens de serviço finalizadas, com alerta para garantias próximas do vencimento ou já expiradas.| RF11| Jadson |
---
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

## US00 - Manter Usuário

**Descrição:**
Permite login, recuperação de senha e logout para todos os perfis de usuário.

**Requisitos:** RF00.1, RF00.2, RF00.3

**Prioridade:** Essencial
**Estimativa:** 8h

**Responsáveis:**
- Analista: Mariana
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
- Token contém perfil (cliente/tecnico/administrador)


## US01 - Manter Cliente

**Descrição:**  
Permite ao usuário administrador realizar todas as operações de gestão de clientes: cadastrar, atualizar, consultar e desativar clientes (PF e PJ).

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
- Listar todos os cliente

---

## US02 - Manter Funcionário

**Descrição:**  
Permite ao usuário administrador gerenciar funcionários, incluindo cadastro, atualização, consulta e desativação, com classificação em Técnico ou Administrativo.

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
- Listar todos os funcionários
---

## US03 - Gerenciar Aparelho

**Descrição:**
O sistema deve manter um cadastro de aparelho de um cliente. Um aparelho tem os atributos id, tipo, marca, modelo, numero_serie, cor, observações, cliente_id.

**Requisitos:** RF03.1, RF03.2, RF03.3, RF03.4

**Prioridade:** Essencial  
**Estimativa:**  6h

**Responsáveis:**  
- Analista: Jadson  
- Desenvolvedor: Jadson  
- Revisor: Mariana  
- Testador: Jadson  

**Testes de Aceitação:**
- Cadastrar um novo aparelho vinculado a um cliente_id existente
- Consultar aparelho por id, numero_serie, modelo ou cliente_id
- Atualizar informações como cor ou observações de um aparelho
- Tentar cadastrar um aparelho com um numero_serie já existente no sistema deve gerar um erro de duplicidade
- Excluir (desativar logicamente) um aparelho. Um aparelho com OS em andamento não pode ser desativado
- Listar todos os aparelhos de um cliente específico

---

## US04 - Gerenciar Ordem_Serviço 

**Descrição:** 
Permite ao administrador e técnico abrir, editar, consultar, atualizar o status da ordem de serviço conforme andamento e encerrar ordens de serviço.

**Requisitos:** RF04.1, RF04.2, RF04.3, RF04.4, RF04.5, RF04.6

**Prioridade:** Essencial  
**Estimativa:**  12h

**Responsáveis:**  
- Analista: Mariana  
- Desenvolvedor: Mariana  
- Revisor: Jadson  
- Testador: Mariana  

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
- Listar OS por cliente específico
- Listar OS por funcionário específico
- Listar OS por aparelhos de um cliente específico
- Listar OS por periodo
- Listar OS por status

---

## US05 - Manter Serviço

**Descrição:**  
Permite ao usuário administrador gerenciar o catálogo de serviços oferecidos pela assistência técnica, incluindo cadastro, consulta, atualização e desativação de serviços, com seus respectivos valores padrão e tempo estimado de execução.

**Requisitos:** RF05.1, RF05.2, RF05.3, RF05.4  

**Prioridade:** Essencial  
**Estimativa:** 4h  

**Responsáveis:**  
- Analista: Jadson  
- Desenvolvedor: Jadson  
- Revisor: Mariana  
- Testador: Jadson  

**Testes de Aceitação:**
- Cadastrar um novo serviço com nome, descrição, valor_padrao (R$), tempo_estimado (minutos) e status (ATIVO)
- Consultar serviços por id, nome ou filtro por status (ATIVO/INATIVO)
- Atualizar o valor_padrao e o tempo_estimado de um serviço existente
- Desativar (status = INATIVO) um serviço. Serviços vinculados a OS em aberto não podem ser desativados
- Tentar cadastrar um serviço com nome duplicado deve gerar um erro
- A listagem de serviços para uso em uma nova OS deve exibir apenas os serviços com status = ATIVO  

---

### US06 - Registrar Serviço_Executado

**Descrição:** 
Permite ao técnico registrar a execução de serviços individuais dentro de uma OS, com tempo real gasto e validação.

**Requisito Funcional Sugerido:** RF06.1,RF06.2, RF06.3, RF06.4, RF06.5, RF06.6, RF06.7, RF06.8, RF06.9, RF06.10, RF06.11

**Prioridade:** Importante
**Estimativa:** 6h

**Responsáveis:**  
- Analista: Mariana  
- Desenvolvedor: Mariana  
- Revisor: Jadson  
- Testador: Mariana  

**Testes de Aceitação:**
- Técnico inicia e para cronômetro para cada serviço
- Sistema registra tempo real gasto
- Múltiplos técnicos podem executar serviços diferentes na mesma OS
- Comissão calculada automaticamente baseada no serviço + técnico
- Relatório de produtividade por técnico/período

## US07 - Gerenciar Equipamento

**Descrição:**  
Permite cadastrar equipamentos, listar, consultar e desativar equipamentos.

**Requisitos:** RF07.1, RF07.2, RF07.3, RF07.4  

**Prioridade:** Essencial  
**Estimativa:** 6h  

**Responsáveis:**  
- Analista: Jadson  
- Desenvolvedor: Jadson  
- Revisor: Mariana  
- Testador: Jadson  

**Testes de Aceitação:**  
- Equipamento cadastrado com sucesso 
- Listar equipamentos
- Consultar equipamento por ID, código, tipo ou modelo
- Desativar equipamento 
- Código duplicado gera erro
- Equipamento vinculado a OS em aberto não pode ser desativado

---

## US08 - Gerenciar Equipamento_Usado

**Descrição:**  
Controla os equipamentos/peças utilizados em um serviço executado.

**Requisitos:** RF08.1, RF08.2, RF08.3, RF08.4  

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

## US09 - Agendar Visita_Técnica

**Descrição:**  
Permite ao administrador agendar visitas e ao técnico registrar a realização das visitas técnicas vinculadas a uma OS.

**Requisitos:** RF09.1, RF09.2  

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

## US10 - Gerenciar Conta_Receber

**Descrição:**  
Gerencia automaticamente as contas a receber com valor_total da OS, data_emissão atual e data_vencimento calculada.

**Requisitos:** RF10.1, RF10.2, RF10.3, RF10.4, RF10.5, RF10.6, RF10.7, RF10.8 

**Prioridade:** Essencial  
**Estimativa:** 8h  

**Responsáveis:**  
- Analista: Mariana  
- Desenvolvedor: Mariana  
- Revisor: Jadson  
- Testador: Mariana 

**Testes de Aceitação:**  
- Conta gerada automaticamente ao encerrar a OS  
- Campos: valor, data_emissão, data_vencimento (30 dias), status_pagamento
- Valor correto 
- Data_emissão = data atual
- Data_vencimento calculada corretamente
- OS sem valor_total válido impede encerramento 


---

## US11 - Gerenciar Pagamento
Permite registrar pagamentos online (cliente) e offline (administrador), incluindo marcar conta como paga e emitir comprovante.

**Requisitos:** RF11.1, RF11.2, RF11.3, RF11.4, RF11.5, RF11.6  

**Prioridade:** Essencial  
**Estimativa:** 6h  

**Responsáveis:**
- Analista: Jadson
- Desenvolvedor: Jadson
- Revisor: Mariana
- Testador: Jadson

**Testes de Aceitação:** 
- Cliente realiza pagamento online via gateway integrado
- Status alterado para PAGO com data_pagamento atual
- Conta já paga não pode ser alterada
- Conta vencida pode ser paga com multa
- Marcar conta como paga (status PAGO com data_pagamento atual)
- Conta com status PAGO não pode ser alterada novamente

---

## US12 - Gerar Relatório

**Descrição:**
Permite gerar um relatório de ordens de serviço filtrado por período de abertura, status e técnico responsável, com opção de exportação (PDF/CSV).

**Requisitos:** RF12.1, RF12.2, RF12.3, RF12.4

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

## US13 - Controle de Garantia 

**Descrição:**
Permite consultar e controlar o período de garantia das ordens de serviço finalizadas, com alerta para garantias próximas do vencimento ou já expiradas.

**Requisitos:** RF13.1, RF13.2, RF13.3

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

| ID    | Requisito Funcional                     | User Stories | Total |
| ------| --------------------------------------- | ------------ | ----- |
| RF00  | Manter Usuário                          | US00         |   1   | 
| RF01  | Manter Cliente                          | US01         |   1   |
| RF02  | Manter Funcionário                      | US02         |   1   |
| RF03  | Gerenciar Aparelho                      | US03         |   1   |
| RF04  | Gerenciar Ordem_Serviço                 | US04         |   1   |
| RF05  | Manter Serviço                          | US05         |   1   |
| RF06  | Registrar Serviço_Executado             | US06         |   1   | 
| RF07  | Gerenciar Equipamento                   | US07         |   1   |
| RF08  | Gerenciar Equipamento_Usado             | US08         |   1   |
| RF09  | Agendar Visita_Técnica                  | US09         |   1   |
| RF10  | Gerenciar Conta_Receber                 | US10         |   1   |
| RF11  | Gerenciar Pagamento                     | US11         |   1   |
| RF12  | Gerar Relatórios                        | US12         |   1   |
| RF13  | Controle de Garantia                    | US13         |   1   |


## 📊 Estatísticas

- **Total de Requisitos Funcionais:** 14
- **Total de User Stories:** 14
- **Média de US por RF:** 1:1
- **Total estimado de desenvolvimento:** 92 horas

## 🔄 Mapeamento US × Perfis de Usuário

| Perfil | User Stories |
|:---|:---|
| Cliente |	US03, US10, US11 |
| Técnico |	US03, US04,  US05, US06, US08, US09 |
| Administrativo | US00, US01, US02, US03, US04, US05, US06, US07, US08, US09, US10, US11, US12,US13 |

