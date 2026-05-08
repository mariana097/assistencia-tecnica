# Modelo de Dados

## 📊 Diagrama de Classes usando Mermaid

```mermaid
classDiagram
    %% Entidades Base
    class USUARIO {
        -int id
        -string email
        -string senha
        -string status
        +autenticar(email, senha): bool
        +recuperarSenha(email): bool
        +logout(): void
        +alterarSenha(novaSenha): bool
        +alterarEmail(novoEmail): bool
    }
    
    class CLIENTE {
        -int id
        -string nome
        -string endereco
        -string contato
        +solicitarOrdemServico(): int
        +visualizarMinhasContas(): List~ContaReceber~
        +visualizarMeusAparelhos(): List~Aparelho~
        +visualizarMinhasOS(): List~OrdemServico~
        +selecionarContasParaPagamento(contasIds): float
        +realizarPagamentoOnline(contasIds, formaPagamento): bool
        +obterComprovantePagamento(contaId): PDF
    }
    
    class CLIENTE_PF {
        -string cpf
        -date data_nascimento
    }
    
    class CLIENTE_PJ {
        -string cnpj
        -string razao_social
        -string nome_fantasia
    }
    
    class FUNCIONARIO {
        -int id
        -string nome
        -string cpf
        -string contato
        -float salario
        -date data_admissao
        -string horario_expediente
        -string status_funcionario
        +registrarPonto(): void
    }
    
    class TECNICO {
        - int id
        -string especialidade
        -string certificacoes
        -int nivel_experiencia
        -float comissao_percentual
        +iniciarExecucaoServico(servicoExecutadoId): void
        +pausarExecucaoServico(servicoExecutadoId): void
        +retomarExecucaoServico(servicoExecutadoId): void
        +finalizarExecucaoServico(servicoExecutadoId): void
        +calcularComissao(): float
        +registrarVisita(visitaId, resultado): void
        +atualizarStatusOS(osId, novoStatus): void
    }
    
    class ADMINISTRADOR {
        - int id
        -string cargo
        -string setor
        -float bonus_fixo
        +gerenciarFuncionarios(): void
        +gerenciarClientes(): void
        +gerenciarAparelhos(): void
        +gerenciarServicos(): void
        +gerenciarEquipamentos(): void
        +registrarPagamentoOffline(contaId, formaPagamento): void
        +cancelarConta(contaId): void        
        +gerarRelatorioOS(filtros): Relatorio
        +agendarVisitaTecnica(osId, dataAgendamento): int
    }
    
    %% Entidades de Negócio
    class APARELHO {
        -int id
        -string tipo
        -string marca
        -string modelo
        -string numero_serie
        -string cor
        -string observacoes
        -int cliente_id
        -string status
        +getHistoricoOS(): List~OrdemServico~
        +atualizarObservacoes(texto): void
    }
    
    class ORDEM_SERVICO {
        -int id
        -date data_abertura
        -date data_encerramento
        -string descricao_problema
        -string status
        -float valor_total
        -int cliente_id
        -int tecnico_id
        -int aparelho_id
        +calcularValorTotal(): float
        +alterarStatus(novoStatus): void
        +adicionarServico(servicoId, quantidade): void
        +removerServico(servicoExecutadoId): bool
        +adicionarEquipamentoUsado(equipamentoId, quantidade): void
        +imprimirRelatorio(): PDF
    }
    
    class SERVICO {
        -int id
        -string nome
        -string descricao
        -float valor_padrao
        -int tempo_estimado
        -string status
        +aplicarDesconto(percentual): float
        +calcularTempoTotal(): int
    }
    
    class SERVICO_EXECUTADO {
        -int id
        -int garantia_dias
        -float valor_cobrado
        -string observacoes
        -int os_id
        -int servico_id
        -int tecnico_id
        -datetime data_inicio
        -datetime data_fim
        -time tempo_gasto
        -string status_execucao
        -float comissao_calculada
        +calcularGarantia(): date
        +calcularTempoGasto(): time
        +calcularComissao(): float
        +verificarGarantiaAtiva(): bool
    }
    
    class EQUIPAMENTO {
        -int id
        -string codigo
        -string tipo
        -string marca
        -string modelo
        -int quantidade_estoque
        -string status
        -string numero_serie
        -date data_aquisicao
        -float valor_compra
        +diminuirEstoque(quantidade): bool
        +verificarDisponibilidade(quantidade): bool
        +reporEstoque(quantidade): void
    }
    
    class EQUIPAMENTO_USADO {
        -int id
        -float horas_utilizadas
        -string observacoes
        -int servico_executado_id
        -int quantidade
        -int equipamento_id        
        +calcularCustoUso(): float
    }
    
    class VISITA_TECNICA {
        -int id
        -datetime data_agendamento
        -datetime data_realizacao
        -string resultado
        -int os_id
        -int tecnico_id
        -string status
        +registrarVisita(): void
        +reagendar(novaData): void
        +cancelar(): void
    }
    
    %% Entidades Financeiras
    class CONTA_RECEBER {
        -int id
        -float valor_original
        -float multa
        -float juros
        -float valor_total
        -date data_emissao
        -date data_vencimento
        -date data_pagamento
        -string status_pagamento
        -string forma_pagamento
        -string transacao_id
        -string qr_code_pix
        -string boleto_codigo
        -int os_id
        +calcularTotalComJuros(): float
        +marcarComoPago(dataPagamento): void
        +gerarBoleto(): string
        +gerarQRCodePix(): string
        +aplicarMulta(dias_atraso): void
        +validarPagamento(transacao_id): bool
    }
    
    class PAGAMENTO {
        -int id
        -float valor_pago
        -date data_pagamento
        -string forma_pagamento
        -string transacao_id
        -string status_transacao
        -string comprovante_url
        -int conta_receber_id
        +processarPagamento(): bool
        +confirmarPagamento(): void
        +estornarPagamento(): bool
        +emitirComprovante(): PDF
    }
    
    %% Entidades de Suporte
    class NOTIFICACAO {
        -int id
        -int usuario_id
        -string tipo
        -string titulo
        -string mensagem
        -datetime data_envio
        -datetime data_leitura
        -string status
        -string link_referencia
        +enviar(): void
        +marcarComoLida(): void
    }
    
    class AUDITORIA_LOG {
        -int id
        -int usuario_id
        -string tabela_afetada
        -int registro_id
        -string acao
        -json dados_antigos
        -json dados_novos
        -datetime data_hora
        -string ip_origem
        +registrar(): void
        +consultarLogs(filtros): List
    }
    
    %% Relacionamentos de Herança
    USUARIO <|-- CLIENTE
    USUARIO <|-- FUNCIONARIO
    CLIENTE <|-- CLIENTE_PF
    CLIENTE <|-- CLIENTE_PJ
    FUNCIONARIO <|-- TECNICO
    FUNCIONARIO <|-- ADMINISTRADOR
    
    %% Relacionamentos de Associação
    CLIENTE "1" -- "0..*" APARELHO : possui
    CLIENTE "1" -- "0..*" ORDEM_SERVICO : solicita
    CLIENTE "1" -- "0..*" CONTA_RECEBER : possui 
    CLIENTE "1" -- "0..*" NOTIFICACAO : recebe   
    APARELHO "1" -- "0..*" ORDEM_SERVICO : registrado_em    
    TECNICO "1" -- "0..*" ORDEM_SERVICO : responsavel_por
    TECNICO "1" -- "0..*" SERVICO_EXECUTADO : executa
    TECNICO "1" -- "0..*" VISITA_TECNICA : realiza    
    ADMINISTRADOR "1" -- "0..*" AUDITORIA_LOG : registra 
    ORDEM_SERVICO "1" -- "1" CONTA_RECEBER : gera
    ORDEM_SERVICO "1" -- "0..*" VISITA_TECNICA : gera
    ORDEM_SERVICO "1" -- "1..*" SERVICO_EXECUTADO : contem    
    SERVICO "1" -- "0..*" SERVICO_EXECUTADO : executado_em    
    SERVICO_EXECUTADO "1" -- "0..*" EQUIPAMENTO_USADO : utiliza    
    EQUIPAMENTO "1" -- "0..*" EQUIPAMENTO_USADO : usado_em    
    CONTA_RECEBER "1" -- "0..1" PAGAMENTO : tem    
    USUARIO "1" -- "0..*" NOTIFICACAO : recebe
    USUARIO "1" -- "0..*" AUDITORIA_LOG : gera

```

### Descrição das Entidades

Entidade                          |	Descrição   |
---------                         | ----------- |
Usuário	   | Entidade base abstrata para representar informações gerais de acesso ao sistema: id, email, senha, status. Possui o método +autenticar(email, senha), +recuperarSenha(email), +logout(),+alterarSenha(novaSenha),   +alterarEmail(novoEmail) para validação de credenciais. |
Cliente	   | Entidade que representa um cliente do sistema, estendendo USUARIO. Contém informações cadastrais: nome, endereco, contato. Possui o método +solicitarOrdemServico(), +visualizarMinhasContas(), +visualizarMeusAparelhos(), +visualizarMinhasOS(),+selecionarContasParaPagamento(contasIds), +realizarPagamentoOnline(contasIds, formaPagamento, +obterComprovantePagamento(contaId). |
Cliente CPF	| Especialização de CLIENTE para pessoa física. Adiciona os atributos cpf e data_nascimento. |
Cliente CNPJ	| Especialização de CLIENTE para pessoa jurídica. Adiciona os atributos cnpj, razao_social e nome_fantasia. |
Funcionário	 | Especialização de funcionário para técnico. Contém dados como nome, cpf, contato, salario, data_admissao, horario_expediente e status. Possui o método +registrarPonto() para controle de jornada. |
Técnico | Especialização de FUNCIONARIO para técnicos especializados. Adiciona especialidade, certificacoes, nivel_experiencia e comissao_percentual. Possui os métodos +iniciarExecucaoServico(servicoExecutadoId), +pausarExecucaoServico(servicoExecutadoId), +retomarExecucaoServico(servicoExecutadoId), +finalizarExecucaoServico(servicoExecutadoId), +registrarVisita(visitaId, resultado), +atualizarStatusOS(osId, novoStatus) e +calcularComissao() para gestão de serviços e remuneração variável.|
Administrador | Especialização de FUNCIONARIO para administradores do sistema. Adiciona cargo, setor e bonus_fixo. Possui o método +gerenciarFuncionarios(), +gerenciarClientes(), +gerenciarAparelhos(), +gerenciarServicos(), +gerenciarEquipamentos(), +registrarPagamentoOffline(contaId, formaPagamento), +cancelarConta(contaId), +gerarRelatorioOS(filtros),+agendarVisitaTecnica(osId, dataAgendamento)|
Aparelho | Entidade que representa os aparelhos dos clientes que serão reparados. Contém informações técnicas: tipo, marca, modelo, numero_serie, cor, observacoes e cliente_id e status. Possui os métodos +getHistoricoOS() para consultar todas as ordens de serviço do aparelho e +atualizarObservacoes() para manutenção do registro. |
Ordem_Serviço | Entidade central que representa uma ordem de serviço aberta para reparo. Contém id, data_abertura, data_encerramento, descricao_problema, status, valor_total, cliente_id, tecnico_id e aparelho_id. Possui métodos para +calcularValorTotal(), +alterarStatus(novoStatus), +adicionarServico(servicoId, quantidade), +removerServico(servicoExecutadoId), +adicionarEquipamentoUsado(equipamentoId, quantidade) e +imprimirRelatorio(). |
Serviço | Entidade que representa um tipo de serviço oferecido pela assistência (ex: limpeza, troca de tela, reparo de placa). Contém nome, descricao, valor_padrao, tempo_estimado e status. Possui métodos para +aplicarDesconto(percentual) e +calcularTempoTotal(). |
Serviço_executado | Entidade associativa que registra a execução de um serviço específico em uma ordem de serviço. Contém garantia_dias,valor_cobrado (que pode ser diferente do valor padrão), observacoes, os_id, servico_id, tecnico_id, data_inicio, data_fim, tempo_gasto, status_execucao, comissao_calculada. Possui o método +calcularGarantia(), +calcularTempoGasto(),+calcularComissao() e +verificarGarantiaAtiva() para formalizar a realização do serviço. |
Equipamento	| Entidade que representa insumos, ferramentas ou peças do estoque da assistência. Contém codigo, tipo, marca, modelo, quantidade_estoque, status, numero_serie, data_aquisicao e valor_compra. Possui métodos para +diminuirEstoque(), +verificarDisponibilidade() e +reporEstoque() para controle de inventário. |
Equipamento_usado | Entidade associativa que registra quais equipamentos/peças foram consumidos ou utilizados em cada serviço executado. Contém horas_utilizadas, observacoes, servico_executado_id, equipamento_id e quantidade. Possui o método +calcularCustoUso() para apurar o custo dos insumos aplicados. |
Visita_Técnica | Entidade que representa visitas realizadas por técnicos na residência do cliente. Contém data_agendamento, data_realizacao, resultado, os_id e tecnico_id e status. Possui métodos para +registrarVisita(), +reagendar() e +cancelar() para gestão do atendimento externo. |
Conta_Receber	| Entidade que representa as obrigações financeiras geradas pelas ordens de serviço. Contém valor_original, multa, juros, valor_total, data_emissao, data_vencimento, data_pagamento, status_pagamento, forma_pagamento, transacao_id, -string qr_code_pix, string boleto_codigo e os_id. Possui métodos para +calcularTotalComJuros(), +marcarComoPago(), +gerarQRCodePix(), +gerarBoleto(), +aplicarMulta() e +validarPagamento() para gestão financeira completa. |
Pagamento | Representa o ato do pagamento em si (transação, comprovante, processamento). Uma CONTA_RECEBER pode gerar um PAGAMENTO. Contém valor_pago, data_pagamento, forma_pagamento, transacao_id, status_transacao, comprovante_url. Possui métodos para       +processarPagamento(), +confirmarPagamento(), +estornarPagamento(), +emitirComprovante().|
| Notificaçao | Entidade que representa as notificações enviadas pelo sistema aos usuários sobre eventos importantes. Contém usuario_id (destinatário), tipo (GARANTIA_EXPIRANDO, CONTA_VENCENDO, OS_ATUALIZADA, VISITA_AGENDADA, PAGAMENTO_CONFIRMADO), titulo, mensagem, data_envio, data_leitura, status (ENVIADO, LIDO, FALHOU) e link_referencia. Possui métodos para +enviar() (dispara a notificação) e +marcarComoLida() (registra leitura pelo usuário).|
| Auditoria_log | Entidade que registra todas as ações dos usuários no sistema para fins de rastreabilidade, conformidade e segurança. Contém usuario_id (quem executou a ação), tabela_afetada (nome da tabela modificada), registro_id (ID do registro afetado), acao (INSERT, UPDATE, DELETE, STATUS_CHANGE), dados_antigos (JSON com estado anterior), dados_novos (JSON com novo estado), data_hora (timestamp da ação) e ip_origem (endereço IP da requisição). Possui métodos para +registrar() (insere o log automaticamente) e +consultarLogs(filtros) (permite consulta filtrada). Os logs são imutáveis e não podem ser alterados ou excluídos.|

---

## Diagrama Entidade-Relacionamento

```mermaid
erDiagram
    %% Entidades Base
    USUARIO {
        int id PK
        string email
        string senha
        string status
    }
    
    CLIENTE {
        int id PK
        string nome
        string endereco
        string contato
    }
    
    CLIENTE_PF {
        int id PK
        string cpf
        date data_nascimento
    }
    
    CLIENTE_PJ {
        int id PK
        string cnpj
        string razao_social
        string nome_fantasia
    }
    
    FUNCIONARIO {
        int id PK
        string nome
        string cpf
        string contato
        float salario
        date data_admissao
        string horario_expediente
        string status_funcionario
    }
    
    TECNICO {
        int id PK
        string especialidade
        string certificacoes
        int nivel_experiencia
        float comissao_percentual
    }
    
    ADMINISTRADOR {
        int id PK
        string cargo
        string setor
        float bonus_fixo
    }
    
    %% Entidades de Negócio
    APARELHO {
        int id PK
        string tipo
        string marca
        string modelo
        string numero_serie
        string cor
        string observacoes
        int cliente_id FK
        string status
    }
    
    ORDEM_SERVICO {
        int id PK
        date data_abertura
        date data_encerramento
        string descricao_problema
        string status
        float valor_total
        int cliente_id FK
        int tecnico_id FK
        int aparelho_id FK
    }
    
    SERVICO {
        int id PK
        string nome
        string descricao
        float valor_padrao
        int tempo_estimado
        string status
    }
    
    SERVICO_EXECUTADO {
        int id PK
        int garantia_dias
        float valor_cobrado
        string observacoes
        int os_id FK
        int servico_id FK
        int tecnico_id FK
        datetime data_inicio
        datetime data_fim
        time tempo_gasto
        string status_execucao
        float comissao_calculada
    }
    
    EQUIPAMENTO {
        int id PK
        string codigo
        string tipo
        string marca
        string modelo
        int quantidade_estoque
        string status
        string numero_serie
        date data_aquisicao
        float valor_compra
    }
    
    EQUIPAMENTO_USADO {
        int id PK
        float horas_utilizadas
        string observacoes
        int quantidade
        int servico_executado_id FK
        int equipamento_id FK
    }
    
    VISITA_TECNICA {
        int id PK
        datetime data_agendamento
        datetime data_realizacao
        string resultado
        int os_id FK
        int tecnico_id FK
        string status
    }
    
    %% Entidades Financeiras
    CONTA_RECEBER {
        int id PK
        float valor_original
        float multa
        float juros
        float valor_total
        date data_emissao
        date data_vencimento
        date data_pagamento
        string status_pagamento
        string forma_pagamento
        string transacao_id
        string qr_code_pix
        string boleto_codigo
        int os_id FK
    }
    
    PAGAMENTO {
        int id PK
        float valor_pago
        datetime data_pagamento
        string forma_pagamento
        string transacao_id
        string status_transacao
        string comprovante_url
        int conta_receber_id FK
    }
    
    %% Entidades de Suporte
    NOTIFICACAO {
        int id PK
        int usuario_id FK
        string tipo
        string titulo
        string mensagem
        datetime data_envio
        datetime data_leitura
        string status
        string link_referencia
    }
    
    AUDITORIA_LOG {
        int id PK
        int usuario_id FK
        string tabela_afetada
        int registro_id
        string acao
        json dados_antigos
        json dados_novos
        datetime data_hora
        string ip_origem
    }
    
    %% Relacionamentos de Herança (Generalização/Especialização)
    USUARIO ||--|| CLIENTE : "é um"
    USUARIO ||--|| FUNCIONARIO : "é um"
    CLIENTE ||--|| CLIENTE_PF : "é um"
    CLIENTE ||--|| CLIENTE_PJ : "é um"
    FUNCIONARIO ||--|| TECNICO : "é um"
    FUNCIONARIO ||--|| ADMINISTRADOR : "é um"
    
    %% Relacionamentos de Associação
    CLIENTE ||--o{ APARELHO : "possui"
    CLIENTE ||--o{ ORDEM_SERVICO : "solicita"
    CLIENTE ||--o{ CONTA_RECEBER : "possui"
    CLIENTE ||--o{ NOTIFICACAO : "recebe"
    
    APARELHO ||--o{ ORDEM_SERVICO : "registrado_em"
    
    TECNICO ||--o{ ORDEM_SERVICO : "responsavel_por"
    TECNICO ||--o{ SERVICO_EXECUTADO : "executa"
    TECNICO ||--o{ VISITA_TECNICA : "realiza"
    
    ADMINISTRADOR ||--o{ AUDITORIA_LOG : "registra"
    
    ORDEM_SERVICO ||--o{ VISITA_TECNICA : "gera"
    ORDEM_SERVICO ||--|| CONTA_RECEBER : "gera"
    ORDEM_SERVICO ||--o{ SERVICO_EXECUTADO : "contem"
    
    SERVICO ||--o{ SERVICO_EXECUTADO : "executado_em"
    
    SERVICO_EXECUTADO ||--o{ EQUIPAMENTO_USADO : "utiliza"
    
    EQUIPAMENTO ||--o{ EQUIPAMENTO_USADO : "usado_em"
    
    CONTA_RECEBER ||--o{ PAGAMENTO : "tem"
    
    USUARIO ||--o{ NOTIFICACAO : "recebe"
    USUARIO ||--o{ AUDITORIA_LOG : "gera"
```

### Dicionário de Dados

|   Tabela   | USUARIO |
| ---------- | ----------- |
| Descrição  | Armazena as credenciais de autenticação dos usuários do sistema. |
| Observação | É uma entidade abstrata/base para autenticação. Um usuário pode ser cliente e/ou funcionário, conforme as regras de negócio. |

|  Nome         | Descrição                        | Tipo de Dado | Tamanho | Restrições de Domínio |
| ------------- | -------------------------------- | ------------ | ------- | --------------------- |
| id | Identificador único | SERIAL | --- | PK / Identity |
| e-mail | e-mail para login  | VARCHAR | 150 | Unique / Not Null |
| senha  | Senha criptografada | VARCHAR | 255 | Not Null |
| status | Situação do usuário no sistema | VARCHAR | 20 | NOT NULL / DEFAULT 'ATIVO' / CHECK (status IN ('ATIVO', 'INATIVO', 'BLOQUEADO', 'PENDENTE_VERIFICACAO')) |

---

|   Tabela   | CLIENTE |
| ---------- | ----------- |
| Descrição  | Armazena as informações gerais dos clientes da assistência técnica. |
| Observação | Clientes podem ser Pessoa Física (PF) ou Pessoa Jurídica (PJ). |

|  Nome         | Descrição                        | Tipo de Dado | Tamanho | Restrições de Domínio |
| ------------- | -------------------------------- | ------------ | ------- | --------------------- |
| id | Identificador único(FK para USUARIO) | INT | --- | PK / FK (USUARIO.id) |
| nome | Nome completo do cliente (PF) ou razão social (PJ) | VARCHAR | 150 | Not Null |
| endereco  | Endereço completo do cliente | VARCHAR | 200 | --- |
| contato | Telefone para contato | VARCHAR | 20 | --- |


|   Tabela   | CLIENTE_PF |
| ---------- | ----------- |
| Descrição  | Armazena informações específicas de clientes do tipo Pessoa Física. |
| Observação | Todo cliente PF deve ter um registro correspondente na tabela Cliente.|

|  Nome         | Descrição                        | Tipo de Dado | Tamanho | Restrições de Domínio |
| ------------- | -------------------------------- | ------------ | ------- | --------------------- |
| id | Identificador único(FK para CLIENTE) | INT | --- | PK / FK |
| cpf | Cadastro de Pessoa Física | VARCHAR | 14 | Unique / Not Null |
| data_nascimento  | Data de nascimento do cliente | DATE | --- | Not Null |


|   Tabela   | CLIENTE_PJ |
| ---------- | ----------- |
| Descrição  | Armazena informações específicas de clientes do tipo Pessoa Jurítica. |
| Observação | Todo cliente PJ deve ter um registro correspondente na tabela Cliente.|

|  Nome         | Descrição                        | Tipo de Dado | Tamanho | Restrições de Domínio |
| ------------- | -------------------------------- | ------------ | ------- | --------------------- |
| id | Identificador único(FK para CLIENTE) | INT | --- | PK / FK |
| cnpj | Cadastro Nacional da Pessoa Jurídica | VARCHAR | 18 | Unique / Not Null |
| razao_social  | Razão social da empresa | VARCHAR | 150 | Not Null |
| nome_fantasia | Nome fantasia da empresa | VARCHAR | 100 | --- |

---

|   Tabela   | FUNCIONARIO |
| ---------- | ----------- |
| Descrição  | Armazena as informações gerais dos funcionários da assistência técnica. |
| Observação | Funcionários podem ser técnico ou administrativo. |

|  Nome         | Descrição                        | Tipo de Dado | Tamanho | Restrições de Domínio |
| ------------- | -------------------------------- | ------------ | ------- | --------------------- |
| id | Identificador único(FK para USUARIO) | INT | --- | PK / FK (USUARIO.id) |
| nome | Nome completo do Funcionário  | VARCHAR | 150 | Not Null |
| cpf |	Cadastro de Pessoa Física |	VARCHAR | 14 | Unique / Not Null |
| contato | Telefone para contato | VARCHAR | 20 | --- |
| salario |	Salário base do funcionário | DECIMAL(10,2) | --- |	NOT NULL / CHECK (salario >= 0) |
| data_admissao	| Data de contratação |	DATE | --- | Not Null |
| horario_expediente | Horário de trabalho | VARCHAR | 50 |	--- |
| status |	Situação do funcionário	| VARCHAR |	10	| CHECK (status IN ('ATIVO','FERIAS','AFASTADO','DESATIVADO')) / DEFAULT 'ATIVO' |


|   Tabela   | TECNICO |
| ---------- | ----------- |
| Descrição  | Responsável pela execução de Ordens de Serviço e Visitas Técnicas. Armazena dados específicos como especialidade, certificações, nível de experiência e comissão percentual. |
| Observação | Especialização da tabela FUNCIONARIO. A identificação do tipo é feita pela existência do registro nesta tabela (via LEFT JOIN). |

|  Nome         | Descrição                        | Tipo de Dado | Tamanho | Restrições de Domínio |
| ------------- | -------------------------------- | ------------ | ------- | --------------------- |
| id | Identificador único(FK para FUNCIONARIO) | INT | --- | PK / FK |
| especialidade | Área de atuação principal | VARCHAR | 100 | Not Null |
| certificacoes  | Certificações técnicas (formato JSON ou texto) | TEXT| --- | --- |
| nivel_experiencia | Nível hierárquico (1-5) | INT | --- | CHECK (nivel_experiencia BETWEEN 1 AND 5) |
|comissao_percentual | Percentual de comissão sobre serviços | DECIMAL(5,2) | --- |	DEFAULT 0.00, CHECK (comissao_percentual >= 0) |


|   Tabela   | ADMINISTRADOR |
| ---------- | ----------- |
| Descrição  | Responsável pela gestão, emissão de contas, cadastro de clientes etc. |
| Observação | Especialização da tabela FUNCIONARIO. A identificação do tipo é feita pela existência do registro nesta tabela (via LEFT JOIN). |

|  Nome         | Descrição                        | Tipo de Dado | Tamanho | Restrições de Domínio |
| ------------- | -------------------------------- | ------------ | ------- | --------------------- |
| id | Identificador único(FK para FUNCIONARIO) | INT | --- | PK / FK |
| cargo | Cargo administrativo | VARCHAR | 80 | Not Null |
| setor | Setor de atuação (ex: Financeiro, RH, Operações) | VARCHAR | 80 | --- |
|bonus_fixo | Bônus mensal fixo | DECIMAL(10,2) | --- |	DEFAULT 0.00 / CHECK (bonus_fixo >= 0) |

---

|   Tabela   | APARELHO |
| ---------- | ----------- |
| Descrição  | Representa os aparelhos dos clientes que precisam de manutenção ou serão reparados. |
| Observação | Um cliente pode possuir vários aparelhos. O aparelho é vinculado a uma ou mais Ordens de Serviço ao longo do tempo. |

|  Nome         | Descrição                        | Tipo de Dado | Tamanho | Restrições de Domínio |
| ------------- | -------------------------------- | ------------ | ------- | --------------------- |
| id | Identificador único | SERIAL / INT | --- | PK / Identity |
| tipo  | Tipo/categoria do aparelho (celular, notebook, tablet, etc.) | VARCHAR | 30 | NOT NULL |
| marca | Marca do aparelho | VARCHAR | 20 |	--- |
| modelo | Modelo do aparelho | VARCHAR | 20 | --- |
| numero_serie | numero_serie | VARCHAR | 50 | UNIQUE |
| cor | Cor do aparelho | VARCHAR |	30 | --- |
| observacoes |	Observações adicionais sobre o aparelho | TEXT | --- | --- |
| cliente_id | Referência ao cliente proprietário |	INT	| --- |	FK (CLIENTE.id) / NOT NULL |
| status | Situação do aparelho | VARCHAR | 20 | DEFAULT 'ATIVO' / CHECK (status IN ('ATIVO', 'INATIVO')) |

---

|   Tabela   | ORDEM_SERVICO |
| ---------- | ----------- |
| Descrição  | Núcleo do sistema. Registra cada solicitação de serviço, seu status, valor total, datas de abertura e encerramento, além de vincular cliente solicitante e técnico responsável. |
| Observação | Uma OS é aberta para cada atendimento solicitado. Ao ser finalizada, gera automaticamente uma CONTA_RECEBER. |

|  Nome         | Descrição                        | Tipo de Dado | Tamanho | Restrições de Domínio |
| ------------- | -------------------------------- | ------------ | ------- | --------------------- |
| id | Identificador único da OS | SERIAL / INT | --- | PK / Identity |
| data_abertura | Data de criação da Ordem de Serviço  | DATE | --- | NOT NULL / DEFAULT CURRENT_DATE |
| data_encerramento  | Data de conclusão do serviço | DATE | --- | --- |
| descricao_problema | Descrição detalhada do problema relatado pelo cliente | TEXT | --- |	NOT NULL |
| status | Situação atual da Ordem de Serviço |	VARCHAR | 20 | CHECK (status IN ('ABERTA', 'EM_ANDAMENTO', 'AGUARDANDO_PECA', 'FINALIZADA', 'CANCELADA')) / DEFAULT 'ABERTA' |
| valor_total |	Valor total do serviço (mão de obra + equipamentos) | DECIMAL(10,2) | --- |	DEFAULT 0.00 / CHECK (valor_total >= 0) |
| cliente_id | Referência ao cliente solicitante | INT | --- | FK para CLIENTE(id) / NOT NULL |
| tecnico_id | Referência ao técnico responsável | INT | --- | FK para TECNICO(id) |
| aparelho_id |	Referência ao aparelho consertado |	INT	| --- |	FK (APARELHO.id) / NOT NULL |

---

|   Tabela   |  SERVICO  |
| ---------- | ----------- |
| Descrição	| Catálogo de serviços oferecidos pela assistência técnica. |
| Observação | O valor padrão pode ser ajustado no momento da execução via tabela SERVICO_EXECUTADO. |

|  Nome         | Descrição                        | Tipo de Dado | Tamanho | Restrições de Domínio |
| ------------- | -------------------------------- | ------------ | ------- | --------------------- |
| id | Identificador único do serviço |	SERIAL / INT | --- | PK / Identity |
| nome | Nome do serviço | VARCHAR | 100 | NOT NULL / UNIQUE |
| descricao | Descrição detalhada do serviço | TEXT	| --- |	--- |
| valor_padrao | Valor padrão do serviço | DECIMAL(10,2) | --- | NOT NULL / CHECK (valor_padrao >= 0) |
| tempo_estimado | Tempo estimado em minutos para execução | INT | --- | CHECK (tempo_estimado > 0) |
| status | Situação do serviço no catálogo | VARCHAR | 20 | DEFAULT 'ATIVO' / CHECK (status IN ('ATIVO', 'INATIVO')) |

---

|   Tabela   | SERVICO_EXECUTADO |
| ---------- | ----------- |
| Descrição | Registra a execução de um serviço específico em uma Ordem de Serviço.|
| Observação |	Permite registrar valor cobrado diferente do valor padrão (desconto ou acréscimo), além de observações específicas da execução.|

|  Nome         | Descrição                        | Tipo de Dado | Tamanho | Restrições de Domínio |
| ------------- | -------------------------------- | ------------ | ------- | --------------------- |
| id | Identificador único | SERIAL / INT |	--- | PK / Identity |
| garantia_dias | Dias de garantia do serviço prestado | INT | --- |  DEFAULT 90 |
| valor_cobrado | Valor efetivamente cobrado pelo serviço |	DECIMAL(10,2) |	--- | NOT NULL / CHECK (valor_cobrado >= 0) |
| observacoes |	Observações sobre a execução do serviço | TEXT| --- | --- |
| ordem_servico_id | Referência à Ordem de Serviço | INT | --- | FK (ORDEM_SERVICO.id) / NOT NULL |
| servico_id | Referência ao serviço executado | INT | --- | FK (SERVICO.id) / NOT NULL |
| tecnico_id | Técnico que executou o serviço | INT | --- | FK (TECNICO.id) |
| data_inicio | Data e hora de início da execução | DATETIME | --- | --- |
| data_fim | Data e hora de término da execução | DATETIME | --- |---|
| tempo_gasto | Tempo total gasto na execução | TIME | --- |---|
| status_execucao | Status da execução do serviço | VARCHAR | 20 | DEFAULT 'PENDENTE' / CHECK (status_execucao IN ('PENDENTE', 'EM_EXECUCAO', 'PAUSADO', 'CONCLUIDO')) |
| comissao_calculada | Valor da comissão gerada para o técnico | DECIMAL(10,2) | --- | DEFAULT 0.00 |

---

|   Tabela   | EQUIPAMENTO |
| ---------- | ----------- |
| Descrição  | Representa insumos, peças de reposição e ferramentas do estoque da assistência técnica. |
| Observação | Um equipamento pode ser utilizado em múltiplas Ordens de Serviço, e uma OS pode utilizar múltiplos equipamentos (relacionamento N:N).|

|  Nome         | Descrição                        | Tipo de Dado | Tamanho | Restrições de Domínio |
| ------------- | -------------------------------- | ------------ | ------- | --------------------- |
| id | Identificador único da equipamento | SERIAL / INT | --- | PK / Identity |
| codigo | Código de identificação do equipamento  | VARCHAR | 20 | UNIQUE / NOT NULL |
| tipo  | Tipo/categoria do equipamento | VARCHAR | 20 | NOT NULL |
| marca | Marca do equipamento | VARCHAR | 20 |	--- |
| modelo | Modelo do equipamento | VARCHAR | 20 | --- |
| quantidade | Quantidade disponível em estoque | INT | --- | DEFAULT 0 / CHECK (quantidade >= 0) |
| status | Situação do equipamento | VARCHAR | 10 | CHECK (status IN ('ATIVO','DESATIVADO')) / DEFAULT 'ATIVO' |
| numero_serie | Número de série (para itens únicos) | VARCHAR | 50 | UNIQUE |
| data_aquisicao |	Data de compra do equipamento |	DATE | --- | --- |
| valor_compra | Valor de compra do equipamento	| DECIMAL(10,2) | --- |	CHECK (valor_compra >= 0) |

---

|   Tabela   | EQUIPAMENTO_USADO
| ---------- | ----------- |
| Descrição | Registra quais equipamentos/peças foram consumidos ou utilizados em cada serviço executado.|
| Observação | Esta tabela controla o consumo de insumos e permite calcular o custo real do serviço.|

|  Nome         | Descrição                        | Tipo de Dado | Tamanho | Restrições de Domínio |
| ------------- | -------------------------------- | ------------ | ------- | --------------------- |
| id | Identificador único | SERIAL / INT |	---	| PK / Identity |
| horas_utilizadas | Horas de utilização (para equipamentos alugados/hora) | DECIMAL(8,2) |	---	| DEFAULT 0 / CHECK (horas_utilizadas >= 0)|
| observacoes |	Observações sobre a utilização | TEXT |	--- | --- |
| quantidade | Quantidade de equipamento utilizados | INT |	--- | DEFAULT 1 / CHECK (quantidade > 0)|
| servico_executado_id | Referência ao serviço executado | INT | --- | FK (SERVICO_EXECUTADO.id) / NOT NULL|
| equipamento_id | Referência ao equipamento utilizado | INT | --- | FK (EQUIPAMENTO.id) / NOT NULL|

---

|   Tabela   | VISITA_TECNICA |
| ---------- | ----------- |
| Descrição  | Vinculada a uma OS, registra agendamentos e realizações de atendimentos presenciais. |
| Observação | A visita só pode ser atribuída a um técnico válido. Permite reagendamento e cancelamento. |

|  Nome         | Descrição                        | Tipo de Dado | Tamanho | Restrições de Domínio |
| ------------- | -------------------------------- | ------------ | ------- | --------------------- |
| id | Identificador único da visita | SERIAL / INT | --- | PK / Identity |
| data_agendamento | Data agendada para a visita técnica  | DATETIME | --- | NOT NULL |
| data_realizacao  | Data em que a visita foi efetivamente realizada | DATETIME | --- | --- |
| resultado | Descrição do resultado da visita técnica | TEXT | --- | --- |
| os_id | Referência à Ordem de Serviço | INT | --- | FK para ORDEM_SERVICO(id) / NOT NULL |
| tecnico_id | Referência ao técnico responsável | INT | --- | FK para TECNICO(id)/ NOT NULL |
| status | Situação da visita | VARCHAR | 20 | DEFAULT 'AGENDADA' / CHECK (status IN ('AGENDADA', 'REALIZADA', 'CANCELADA')) |

---

|   Tabela   | CONTA_RECEBER |
| ---------- | ----------- |
| Descrição  | Gerada automaticamente ao encerrar uma OS, registra o valor a ser pago pelo cliente e controla o status do pagamento. |
| Observação | O status muda de PENDENTE para PAGO quando o pagamento é registrado. Multa e juros são aplicados automaticamente em caso de atraso.|

|  Nome         | Descrição                        | Tipo de Dado | Tamanho | Restrições de Domínio |
| ------------- | -------------------------------- | ------------ | ------- | --------------------- |
| id | Identificador único do pagamento | SERIAL / INT | --- | PK / Identity |
| valor_original | Valor original da OS (sem multa/juros)  | DECIMAL(10,2) | --- | NOT NULL / CHECK (valor_original > 0) |
| multa | Multa fixa sobre valor_original (se vencido) | DECIMAL(10,2) | --- | DEFAULT 0.00 / CHECK (multa >= 0) |
| juros | Juros ao dia de atraso | DECIMAL(10,2) | --- | DEFAULT 0.00 / CHECK (juros >= 0) |
| valor_total |	Valor total (original + multa + juros) | DECIMAL(10,2) | --- |	NOT NULL / CHECK (valor_total >= 0)|
| data_emissao  | Data de emissão da conta | DATE | --- | NOT NULL / DEFAULT CURRENT_DATE |
| data_vencimento  | Data de vencimento da conta | DATE | --- | NOT NULL |
| data_pagamento  | Data em que a conta foi paga | DATE | --- | --- |
| status_pagamento | Situação atual do pagamento | VARCHAR | 10 | CHECK (status_pagamento IN ('PENDENTE', 'PAGO', 'VENCIDO', 'CANCELADO')) / DEFAULT 'PENDENTE' |
| forma_pagamento | Forma de pagamento utilizada | VARCHAR | 20 | CHECK (forma_pagamento IN ('CARTAO','BOLETO','PIX','DINHEIRO')) |
| transancao_id | ID da transação no gateway de pagamento | VARCHAR | 100 | --- |
| qr_code_pix | QR Code PIX para pagamento | TEXT | --- | |
| boleto_codigo | Código de barras do boleto | VARCHAR | 100 | |
| os_id | Referência à Ordem de Serviço | INT | --- | FK para ORDEM_SERVICO(id) / NOT NULL |

---

|   Tabela   | PAGAMENTO |
| ---------- | ----------- |
| Descrição  | Registra cada transação de pagamento realizada, permitindo que uma única conta a receber tenha múltiplos pagamentos (parcelado). |
| Observação | Um pagamento sempre está vinculado a uma CONTA_RECEBER. Uma conta pode ter vários pagamentos (ex: parcelado). |

|  Nome         | Descrição                        | Tipo de Dado | Tamanho | Restrições de Domínio |
| ------------- | -------------------------------- | ------------ | ------- | --------------------- |
| id | Identificador único | SERIAL / INT | --- | PK / Identity |
| valor_pago |  Valor efetivamente pago |	DECIMAL(10,2) |	---	| NOT NULL / CHECK (valor_pago > 0)|
| data_pagamento |	Data e hora do pagamento |	DATETIME |	---	 | NOT NULL|
| forma_pagamento |	Forma de pagamento utilizada |	VARCHAR	| 20 | NOT NULL / CHECK (forma_pagamento IN ('CARTAO', 'BOLETO', 'PIX', 'DINHEIRO', 'TRANSFERENCIA'))|
| transacao_id | ID da transação no gateway | VARCHAR |	100	| --- |
| status_transacao | Status da transação | VARCHAR | 20	| DEFAULT 'PENDENTE' / CHECK (status_transacao IN ('PENDENTE', 'CONFIRMADO', 'FALHOU', 'ESTORNADO'))|
| comprovante_url |	URL do comprovante em PDF |	VARCHAR | 255 |	--- |
| conta_receber_id | Referência à conta paga | INT |---| FK (CONTA_RECEBER.id) / NOT NULL|

---

|   Tabela   | NOTIFICACAO |
| ---------- | ----------- |
| Descrição  | Armazena notificações enviadas aos usuários sobre eventos importantes (garantia expirando, conta vencendo, OS atualizada, etc.) |
| Observação | As notificações são geradas automaticamente pelo sistema com base em regras de negócio (ex: garantia próxima do vencimento). |

| Nome | Descrição | Tipo de Dado | Tamanho | Restrições de Domínio |
|------|-----------|-------------|---------|----------------------|
| id | Identificador único da notificação | SERIAL/INT | --- | PK / Identity |
| usuario_id | Usuário destinatário da notificação | INT | --- | FK (USUARIO.id) / NOT NULL |
| tipo | Tipo da notificação | VARCHAR | 30 | NOT NULL / CHECK (tipo IN ('GARANTIA_EXPIRANDO', 'CONTA_VENCENDO', 'OS_ATUALIZADA', 'VISITA_AGENDADA', 'PAGAMENTO_CONFIRMADO')) |
| titulo | Título da notificação | VARCHAR | 100 | NOT NULL |
| mensagem | Mensagem da notificação | TEXT | --- | NOT NULL |
| data_envio | Data e hora do envio | DATETIME | --- | DEFAULT CURRENT_TIMESTAMP |
| data_leitura | Data e hora da leitura | DATETIME | --- |---|
| status | Status da notificação | VARCHAR | 20 | DEFAULT 'ENVIADO' / CHECK (status IN ('ENVIADO', 'LIDO', 'FALHOU')) |
| link_referencia | Link para página relacionada | VARCHAR | 255 | --- |

---

|   Tabela   | AUDITORIA_LOG |
| ---------- | ----------- |
| Descrição  | Registra todas as ações de usuários no sistema para fins de auditoria, rastreabilidade e conformidade. |
| Observação | Os logs são imutáveis (não podem ser alterados ou excluídos) e servem para identificar responsabilidades em caso de inconsistências. |

| Nome | Descrição | Tipo de Dado | Tamanho | Restrições de Domínio |
|------|-----------|-------------|---------|----------------------|
| id | Identificador único do log | SERIAL/INT | --- | PK / Identity |
| usuario_id | Usuário que realizou a ação | INT | --- | FK (USUARIO.id) / NOT NULL |
| tabela_afetada | Nome da tabela alterada | VARCHAR | 50 | NOT NULL |
| registro_id | ID do registro afetado | INT | --- | NOT NULL |
| acao | Tipo de ação realizada | VARCHAR | 20 | NOT NULL / CHECK (acao IN ('INSERT', 'UPDATE', 'DELETE', 'STATUS_CHANGE')) |
| dados_antigos | Dados antes da alteração (formato JSON) | JSON | --- |---|
| dados_novos | Dados depois da alteração (formato JSON) | JSON | --- |---|
| data_hora | Data e hora da ação | DATETIME | --- | DEFAULT CURRENT_TIMESTAMP |
| ip_origem | IP de origem da requisição | VARCHAR | 45 | NOT NULL |

---