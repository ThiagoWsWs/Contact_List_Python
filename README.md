# Contact_List_Python
Sistema de gerenciamento de contatos desenvolvido em Python com MySQL, utilizando CRUD completo, Colorama para interface de terminal e variáveis de ambiente para segurança das credenciais.


# 📒 Agenda de Contatos

Sistema de gerenciamento de contatos desenvolvido em Python e MySQL.

O projeto foi criado com o objetivo de praticar integração entre Python e banco de dados relacional, implementando um CRUD completo (Create, Read, Update e Delete) através de uma interface em terminal.

## 🚀 Funcionalidades

* Adicionar contatos
* Listar contatos
* Buscar contatos por nome
* Editar contatos
* Excluir contatos
* Interface colorida utilizando Colorama
* Conexão com banco de dados MySQL
* Utilização de variáveis de ambiente (.env) para proteção de credenciais

## 🛠️ Tecnologias Utilizadas

* Python 3
* MySQL
* mysql-connector-python
* Colorama
* Python-dotenv
* Git e GitHub

## 📂 Estrutura do Projeto

```text
Contact_List/
│
├── .env
├── .gitignore
├── contato.py
├── database.py
├── main.py
├── requirements.txt
└── README.md
```

## ⚙️ Configuração do Banco de Dados

Crie o banco de dados no MySQL:

```sql
CREATE DATABASE agenda_contatos;

USE agenda_contatos;

CREATE TABLE contatos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    telefone VARCHAR(20),
    email VARCHAR(100)
);
```

## 🔐 Configuração das Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=sua_senha
DB_NAME=agenda_contatos
```

## 📦 Instalação

Clone o repositório:

```bash
git clone https://github.com/SEU_USUARIO/Contact_List.git
```

Entre na pasta do projeto:

```bash
cd Contact_List
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute o sistema:

```bash
python main.py
```

## 🎯 Objetivo

Este projeto foi desenvolvido para praticar:

* Programação em Python
* Manipulação de banco de dados MySQL
* Organização de projetos
* Uso de Git e GitHub
* Boas práticas de segurança com variáveis de ambiente

## 👨‍💻 Autor

Thiago Winicius da Silva
