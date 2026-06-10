# Verba 📖

Verba is an intelligent Document Summarizer API. It allows users to upload text documents, stores them in a MySQL database, and uses LangChain with OpenAI's GPT models to automatically generate concise summaries of the content.

## Features
- **Document Upload**: Fast and secure file uploading via FastAPI.
- **Automated Summarization**: Powered by LangChain and OpenAI's `gpt-3.5-turbo` using a scalable `map_reduce` chain.
- **Persistent Storage**: Raw content and generated summaries are reliably stored using SQLAlchemy and MySQL.
- **RESTful Architecture**: Clean, modular API design with built-in interactive Swagger documentation.

## Tech Stack
- **Backend Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **Database**: MySQL, SQLAlchemy (ORM)
- **AI/LLM**: [LangChain](https://python.langchain.com/), OpenAI
- **Server**: Uvicorn

## Prerequisites
- Python 3.8+
- MySQL Server installed and running locally (or remotely)
- An active OpenAI API Key

## Setup & Installation

1. **Navigate to the project directory**:
   ```bash
   cd verba
   ```

2. **Create a virtual environment and activate it**:
   ```bash
   python -m venv venv
   
   # On macOS/Linux:
   source venv/bin/activate  
   
   # On Windows: 
   venv\Scripts\activate
   ```

3. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Configuration**:
   Create a `.env` file in the root directory and add your credentials:
   ```env
   DATABASE_URL=mysql+pymysql://<your_mysql_user>:<your_mysql_password>@localhost:3306/verba_db
   OPENAI_API_KEY=your_openai_api_key_here
   ```

5. **Database Initialization**:
   Ensure you have created a database named `verba_db` in your MySQL server before running the application. The SQLAlchemy engine will automatically generate the tables for you on startup.

## Running the Application

Start the FastAPI development server using Uvicorn:

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

## API Documentation

FastAPI automatically generates interactive API documentation. Once the server is running, you can test the upload and retrieval endpoints directly from your browser:
- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
