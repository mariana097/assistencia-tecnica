# Documento de Arquitetura do Software

## 🧭 Visão Geral

O Sistema de Gestão de Assistência Técnica segue uma arquitetura em camadas, separando responsabilidades entre interface, lógica de negócio e persistência de dados.

```mermaid
flowchart LR
    Usuario --> Frontend
    Frontend --> Backend
    Backend --> Banco

    subgraph Frontend
        UI[Interface Web]
    end

    subgraph Backend
        API[API REST - FastAPI]
        Regras[Regras de Negócio]
    end

    subgraph Banco
        DB[(SQLite)]
    end
---

# Documento de Projeto Arquitetural do Software

# Arquitetura do Sistema - Assistência Técnica

## Diagrama da Arquitetura

```mermaid
flowchart TB
    subgraph CLIENTE["🖥️ CLIENTE (Navegador)"]
        direction TB
        HTML["📄 Páginas HTML<br/>(Login, Dashboard, Cliente, OS,<br/>Equipamento, Pagamento, Relatório, Garantia)"]
        JS["⚡ JavaScript ES6 + Bootstrap 5<br/>(Interatividade, validações, fetch API)"]
        HTML --> JS
    end

    subgraph BACKEND["⚙️ BACKEND - SERVIDOR (WSL2 / Ubuntu)"]
        direction TB
        
        UVICORN["🚀 Uvicorn Server (ASGI)<br/>Porta: 8000"]
        FASTAPI["⚡ FastAPI Application"]
        
        subgraph MIDDLEWARE["🔧 Middleware Layer"]
            M1["Static Files"] 
            M2["Auth Middleware"]
            M3["Log Request"] 
            M4["CORS"]
        end
        
        subgraph ROUTER["🗺️ Router Layer"]
            R1["Routes:<br/>/auth, /clientes, /funcionarios, /aparelhos,<br/>/os, /servicos, /equipamentos,<br/>/pagamentos, /relatorios"]
        end
        
        subgraph CONTROLLER["🎮 Controller Layer (Views)"]
            C1["Auth Views"] 
            C2["Cliente Views"]
            C3["OS Views"] 
            C4["Pagamento Views"]
            C5["Equipam. Views"] 
            C6["Serviço Views"]
            C7["Relatório Views"] 
            C8["Garantia Views"]
        end
        
        subgraph SERVICE["📦 Service Layer (Opcional)"]
            S1["Auth Service"] 
            S2["Cliente Service"]
            S3["OS Service"] 
            S4["Pagamento Service"]
        end
        
        subgraph MODEL["🗃️ Model Layer (SQLAlchemy ORM)"]
            M_MOD1["Usuario Model"]
            M_MOD2["Cliente Model"]
            M_MOD3["Funcionario Model"]
            M_MOD4["Aparelho Model"]
            M_MOD5["Servico Model"]
            M_MOD6["Equipamento Model"]
            M_MOD7["Conta_Receber Model"]
            M_MOD8["Visita_Tec Model"]
        end
        
        subgraph TEMPLATE["🎨 Template Layer (Jinja2)"]
            T1["base.html"]
            T2["auth/"]
            T3["clientes/"]
            T4["os/"]
            T5["pagamentos/"]
            T6["relatorios/"]
        end
        
        UVICORN --> FASTAPI
        FASTAPI --> MIDDLEWARE
        MIDDLEWARE --> ROUTER
        ROUTER --> CONTROLLER
        CONTROLLER --> SERVICE
        SERVICE --> MODEL
        MODEL --> TEMPLATE
    end

    subgraph DATABASE["💾 BANCO DE DADOS (SQLite)"]
        DB1["database.sqlite"]
        TABLES["📋 Tabelas:<br/>usuario, cliente, funcionario, aparelho,<br/>ordem_servico, servico, equipamento,<br/>conta_receber, visita_tecnica, notificacao"]
    end

    CLIENTE -- "🌐 HTTP / POST / GET / PUT" --> BACKEND
    BACKEND --> DATABASE
---

# Descrição dos Componentes

## 1. CLIENTE (Frontend - Navegador)

| Componente | Descrição |
|------------|-----------|
| **Páginas HTML** | Interfaces de usuário: Login, Dashboard, Clientes, Ordem de Serviço, Equipamentos, Pagamentos, Relatórios e Garantia |
| **JavaScript ES6 + Bootstrap 5** | Interatividade, validações frontend, chamadas fetch API à API backend |

---

## 2. BACKEND - SERVIDOR (WSL2 / Ubuntu)

| Camada | Componente | Descrição |
|--------|------------|-----------|
| **Servidor ASGI** | Uvicorn | Servidor web assíncrono na porta 8000 |
| **Framework** | FastAPI | Framework moderno para APIs REST com documentação automática |
| **Middleware** | Static Files, Auth, Log, CORS | Arquivos estáticos, autenticação, logs e CORS |
| **Router Layer** | Rotas organizadas | Endpoints: /auth, /clientes, /funcionarios, /aparelhos, /os, /servicos, /equipamentos, /pagamentos, /relatorios |
| **Controller Layer** | Views | Controlam fluxo das requisições e preparam respostas |
| **Service Layer** | Services (Opcional) | Lógica de negócio da aplicação |
| **Model Layer** | SQLAlchemy ORM | Mapeamento ORM: Usuario, Cliente, Funcionario, Aparelho, Servico, Equipamento, Conta_Receber, Visita_Tec |
| **Template Layer** | Jinja2 | Renderização de HTML dinâmico no servidor |

---

## 3. BANCO DE DADOS (SQLite)

| Componente | Descrição |
|------------|-----------|
| **database.sqlite** | Arquivo único com todos os dados da aplicação |
| **Tabelas** | usuario, cliente, funcionario, aparelho, ordem_servico, servico, equipamento, conta_receber, visita_tecnica, notificacao |

---

## Fluxo de Dados

1. **Cliente** acessa página HTML no navegador
2. **JavaScript** interage com usuário e faz requisições HTTP
3. **Uvicorn** recebe requisição e entrega ao FastAPI
4. **Middleware** processa autenticação, CORS e logs
5. **Router** direciona para o Controller adequado
6. **Controller** (opcionalmente) chama o Service
7. **Model** (SQLAlchemy) consulta/persiste dados no SQLite
8. **Resposta** (JSON ou HTML via Jinja2) retorna ao cliente



