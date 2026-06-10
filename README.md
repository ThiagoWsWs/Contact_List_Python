# 📒 Contact List Manager

A contact management system built with Python and MySQL.

This project was developed to practice database integration with Python, implementing a complete CRUD (Create, Read, Update, Delete) application through a terminal-based interface.

## 🚀 Features

* Add new contacts
* View all contacts
* Search contacts by name
* Edit existing contacts
* Delete contacts
* Colored terminal interface using Colorama
* MySQL database integration
* Secure credential management using environment variables (.env)

## 🛠️ Technologies Used

* Python 3
* MySQL
* mysql-connector-python
* Colorama
* python-dotenv
* Git & GitHub

## 📂 Project Structure

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

## ⚙️ Database Setup

Create the database and table in MySQL:

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

## 🔐 Environment Variables

Create a `.env` file in the project's root directory:

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=agenda_contatos
```

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/Contact_List.git
```

Navigate to the project directory:

```bash
cd Contact_List
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python main.py
```

## 🎯 Learning Objectives

This project was developed to practice:

* Python programming
* MySQL database management
* CRUD operations
* Project organization and structure
* Git and GitHub workflow
* Secure handling of credentials with environment variables

## 📈 Future Improvements

* Email validation
* Phone number validation
* Contact sorting and filtering
* Export contacts to CSV
* User authentication system
* Graphical User Interface (GUI)
* REST API integration

## 👨‍💻 Author

**Thiago Winicius da Silva**

GitHub: https://github.com/YOUR_USERNAME
