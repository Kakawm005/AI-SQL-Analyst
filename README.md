# 🤖 AISQLAnalyst

Um agente de Inteligência Artificial capaz de interpretar perguntas em linguagem natural e transformá-las em consultas SQL para buscar informações em um banco de dados.

O projeto foi desenvolvido para explorar a integração entre **LLMs, agentes de IA e bancos de dados**, permitindo que o usuário consulte informações sem precisar escrever SQL manualmente.

> **Exemplo:**
> “Quais são os produtos com preço maior que R$ 100?”
>
> O agente interpreta a pergunta, cria a consulta SQL adequada, executa no banco e retorna os resultados.

---

## 🚀 Objetivo

O **AISQLAnalyst** foi criado como um projeto prático para estudar e aplicar conceitos de:

* 🤖 Agentes de Inteligência Artificial
* 🧠 LLMs
* 🗃️ SQL e bancos de dados
* 🐍 Python
* 🔌 Integração entre IA e aplicações
* 💾 Memória persistente para agentes

A ideia principal é criar uma camada de interação em linguagem natural sobre um banco de dados.

---

## 🧠 Como funciona

O fluxo básico do sistema é:

```text
Usuário
   ↓
Pergunta em linguagem natural
   ↓
Agente de IA
   ↓
Interpretação da pergunta
   ↓
Geração da consulta SQL
   ↓
Banco SQLite
   ↓
Resultado
   ↓
Resposta do agente
```

### Exemplo

**Entrada:**

```text
Quais produtos custam mais de 500 reais?
```

**O agente pode gerar:**

```sql
SELECT *
FROM products
WHERE price > 500;
```

Depois da execução, os resultados são utilizados pelo agente para construir uma resposta compreensível para o usuário.

---

## 🛠️ Tecnologias

| Tecnologia        | Utilização                             |
| ----------------- | -------------------------------------- |
| 🐍 Python         | Linguagem principal                    |
| 🤖 Agno           | Criação e gerenciamento do agente      |
| 🧠 OpenAI         | Modelo de Inteligência Artificial      |
| 🗃️ SQLite        | Banco de dados                         |
| 🔐 python-dotenv  | Gerenciamento de variáveis de ambiente |
| 🧠 Agentic Memory | Memória persistente do agente          |

---

## 📁 Estrutura do projeto

```text
AISQLAnalyst/
│
├── agent/
│   └── ...
│
├── agent.py
├── createdatabase.py
│
├── db.sqlite
├── agent.db
│
├── .env
├── .gitignore
├── README.md
└── .venv/
```

### Principais arquivos

**`agent.py`**

Responsável pela criação e configuração do agente de IA, incluindo modelo, ferramentas, banco de memória e instruções.

**`createdatabase.py`**

Responsável pela criação e preparação do banco de dados utilizado pelo projeto.

**`db.sqlite`**

Banco de dados que contém os dados consultados pelo agente.

**`agent.db`**

Banco utilizado para persistência das informações relacionadas ao agente e sua memória.

---

## ⚙️ Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/SEU-USUARIO/AISQLAnalyst.git
```

Entre na pasta:

```bash
cd AISQLAnalyst
```

### 2. Crie um ambiente virtual

```bash
python -m venv .venv
```

No Windows:

```bash
.venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install agno openai python-dotenv
```

---

## 🔐 Configuração da API

Crie um arquivo `.env` na raiz do projeto:

```env
OPENAI_API_KEY=sua_chave_aqui
```

**Nunca coloque sua API Key diretamente no código ou publique o arquivo `.env` no GitHub.**

O `.env` deve estar no `.gitignore`:

```gitignore
.env
.venv/
__pycache__/
*.pyc
```

---

## ▶️ Executando o projeto

Depois de configurar o ambiente:

```bash
python agent.py
```

O agente poderá receber perguntas sobre os dados disponíveis no banco.

Exemplo:

```text
Quais são os produtos cadastrados?
```

ou:

```text
Mostre os produtos com preço acima de 100.
```

---

## 🔎 Banco de dados

Atualmente, o agente trabalha com informações armazenadas em um banco **SQLite**.

A principal tabela utilizada pelo projeto é:

```text
products
```

O agente foi configurado para realizar consultas específicas nessa tabela de acordo com a solicitação do usuário.

---

## 🧩 Arquitetura

O projeto utiliza três componentes principais:

### 1. LLM

Responsável por compreender a linguagem natural e determinar qual consulta precisa ser realizada.

### 2. Agente

O agente funciona como intermediário entre o usuário e o banco de dados.

Ele recebe a solicitação, utiliza a ferramenta de consulta SQL e interpreta os resultados.

### 3. Banco de dados

O SQLite armazena os dados que serão consultados.

Essa arquitetura permite transformar:

```text
Linguagem natural
        ↓
       IA
        ↓
       SQL
        ↓
    Database
        ↓
     Resultado
```

---

## 💡 O que aprendi desenvolvendo o projeto

Este projeto permitiu praticar conceitos importantes de desenvolvimento de software e Inteligência Artificial:

* Criação de agentes com Python
* Utilização de LLMs através de APIs
* Engenharia de prompts
* Geração de SQL utilizando IA
* Integração entre agentes e bancos de dados
* SQLite
* Variáveis de ambiente
* Memória persistente
* Desenvolvimento de ferramentas para agentes
* Estruturação de projetos Python

---

## 🔮 Próximos passos

Algumas melhorias planejadas para o projeto:

* [ ] Adicionar interface web
* [ ] Suporte para PostgreSQL e MySQL
* [ ] Permitir análise de múltiplas tabelas
* [ ] Implementar autenticação
* [ ] Adicionar validação e segurança das queries
* [ ] Exibir as consultas SQL geradas
* [ ] Criar gráficos automaticamente a partir dos resultados
* [ ] Adicionar histórico de consultas
* [ ] Criar API com FastAPI
* [ ] Adicionar testes automatizados
* [ ] Containerizar com Docker
* [ ] Criar dashboard para análise dos dados

---

## 🎯 Ideia do projeto

O objetivo do AISQLAnalyst não é simplesmente gerar SQL com IA.

A proposta é explorar como **agentes inteligentes podem funcionar como uma interface entre pessoas e bancos de dados**, permitindo que usuários façam perguntas utilizando linguagem natural em vez de precisarem conhecer SQL.

---

## 👨‍💻 Autor

**Kayque Silva Pimentel**

Estudante de Engenharia de Software e desenvolvedor interessado em **Python, Backend, Inteligência Artificial e desenvolvimento de agentes de IA**.

---

## 📄 Licença

Este projeto está disponível para fins de estudo e aprendizado.
