# 🤖 Enhanced SQL Chatbot (MySQL Edition)

A powerful, AI-powered SQL chatbot that allows you to interact with your MySQL database using natural language. Built with Streamlit, Groq AI, and LangChain, this application translates your questions into SQL queries and displays results in an intuitive, user-friendly interface.

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-AI-FF6B6B?style=for-the-badge)

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

### Prerequisites

- Python 3.8 or higher
- MySQL database (or SQLite for local testing)
- Groq API key ([Get one here](https://console.groq.com/))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Kakarlamounish/enhanced-sql-chatbot.git
   cd enhanced-sql-chatbot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   
   Create a `.env` file in the root directory:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```
   
   Or using Python module:
   ```bash
   python -m streamlit run app.py
   ```

5. **Access the application**
   
   Open your browser and navigate to `http://localhost:8501`

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

### Query Results
- Generated SQL displayed in code blocks
- Results shown in interactive tables
- CSV export functionality
- Error handling with user-friendly messages

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- [Streamlit](https://streamlit.io/) for the amazing framework
- [Groq](https://groq.com/) for the fast AI inference
- [LangChain](https://www.langchain.com/) for AI orchestration tools
- [SQLAlchemy](https://www.sqlalchemy.org/) for database abstraction

## 📧 Contact

For questions or support, please open an issue on GitHub.

---

**Made with ❤️ using Streamlit, Groq AI, and LangChain**

