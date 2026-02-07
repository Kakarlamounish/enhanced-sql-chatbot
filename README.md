# 🤖 Enhanced SQL Chatbot (MySQL Edition)

A powerful, AI-powered SQL chatbot that allows you to interact with your MySQL database using natural language. Built with Streamlit, Groq AI, and LangChain, this application translates your questions into SQL queries and displays results in an intuitive, user-friendly interface.



## ✨ Features

- **🧠 Natural Language to SQL**: Ask questions in plain English and get accurate SQL queries
- **🔐 Secure Admin Authentication**: Protect your database with admin login functionality
- **🗂 Interactive Schema Explorer**: Browse your database schema with expandable table views
- **💬 Chat Interface**: Conversational UI with chat history for easy interaction
- **📊 Data Visualization**: View query results in beautiful, interactive tables
- **⬇️ Export Results**: Download query results as CSV files
- **🌙 Dark Theme**: Modern, eye-friendly dark interface
- **🛡️ Safety Features**: Built-in protection against dangerous SQL operations (DROP, DELETE, TRUNCATE, etc.)

## 🚀 Getting Started

## 📖 Usage

### 1. Admin Login

- Enter your admin username and password in the sidebar
- Click "Login" to authenticate

### 2. Connect to Database

- Fill in your MySQL connection details:
  - **MySQL User**: Your database username (default: `root`)
  - **Password**: Your database password
  - **Host**: Database host (default: `localhost`)
  - **Database**: Database name
- Click "Connect" to establish the connection

### 3. Explore Schema

- Once connected, browse your database schema in the sidebar
- Expand any table to view its columns and data types
- Click "View Sample" to see sample data from any table

### 4. Ask Questions

- Type your question in natural language at the bottom of the screen
- Examples:
  - "fetch all employees"
  - "how many employees and departments are there in the database"
  - "what is the budget for the projects"
  - "find employee with name Alice Johnson"
- The AI will generate SQL, execute it, and display results

### 5. Export Results

- After a successful query, click "Download CSV" to export the results

## 🏗️ Project Structure

```
enhanced-sql-chatbot/
│
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (create this)
├── .gitignore            # Git ignore rules
│
└── utils/
    ├── auth_utils.py      # Admin authentication utilities
    ├── db_utils.py        # Database connection and query utilities
    └── llm_utils.py       # Groq AI integration for SQL generation
```

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **Database**: MySQL (via SQLAlchemy)
- **AI/ML**: 
  - Groq API (Llama 3.3 70B model)
  - LangChain (for future enhancements)
- **Data Processing**: Pandas
- **Database ORM**: SQLAlchemy

## 🔧 Configuration

### Environment Variables

Create a `.env` file with the following:

```env
GROQ_API_KEY=your_groq_api_key_here
```

### Database Connection

The application supports:
- **MySQL**: Full support with connection parameters
- **SQLite**: Basic support for local databases

## 🛡️ Security Features

- Admin authentication before database access
- Protection against dangerous SQL operations:
  - `DROP` statements
  - `DELETE` statements
  - `TRUNCATE` statements
  - `ALTER` statements
  - `UPDATE` statements (read-only mode)
- Secure password input fields
- SQL injection protection through parameterized queries

## 📸 Screenshots

### Main Interface
- Dark-themed, modern UI
- Sidebar with database configuration and schema explorer
- Main chat area for natural language queries
- Interactive query suggestions
- 
### Query Results
- Generated SQL displayed in code blocks
- Results shown in interactive tables
- CSV export functionality
- Error handling with user-friendly messages




  <img width="1865" height="787" alt="image" src="https://github.com/user-attachments/assets/a655f254-5364-4953-9c8e-7ab2a0e6d1a0" />

  


<img width="1871" height="798" alt="image" src="https://github.com/user-attachments/assets/d8bd1dc6-9d63-4ee8-af33-cb95346e0cae" />





<img width="1891" height="820" alt="image" src="https://github.com/user-attachments/assets/9a9b2e71-0b98-4e60-92bd-647b27eff32a" />











## 📧 Contact
For questions or support, please open an issue on GitHub:
[![](https://img.shields.io)](https://github.com)


---

**Made with ❤️ using Streamlit, Groq AI, and LangChain**

