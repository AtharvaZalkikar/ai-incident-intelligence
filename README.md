# AI Incident Investigation Platform

An AI-powered incident investigation platform that transforms raw infrastructure logs into actionable insights using FastAPI, React, SQLAlchemy, and OpenAI.

The platform automatically groups related logs into incidents, generates AI-powered summaries, and enables engineers to investigate incidents through a context-aware AI Copilot.

![Python](https://img.shields.io/badge/Python-3.13-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.116-green)
![React](https://img.shields.io/badge/React-19-61DAFB)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-black)
![License](https://img.shields.io/badge/License-MIT-green)

## Overview

Infrastructure teams often deal with thousands of log entries during an outage. Manually identifying related events, determining the primary failure reason, and understanding the impact can be time-consuming.

This project automates that workflow by processing log files, grouping related events into incidents, generating AI-powered summaries, and providing an interactive AI Copilot that answers natural language questions about each incident.

The result is a streamlined investigation experience that helps engineers understand incidents faster.

## Project Highlights

- 🤖 AI-powered incident investigation using OpenAI GPT-4o-mini
- 📊 Automatic incident detection from infrastructure logs
- 🧠 Context-aware AI Copilot for natural language investigation
- 💾 Persistent Incident Store built with SQLAlchemy and SQLite
- ⚛️ Modern React dashboard with an interactive investigation workspace
- 🏗️ Clean service-layer architecture following separation of concerns

## Features

### 📂 Log Ingestion

- Upload infrastructure log files in CSV format.
- Automatically store and process raw log data using SQLite.

### 🚨 Intelligent Incident Detection

- Group related log events into incidents based on configurable time windows and node identifiers.
- Automatically calculate failure distribution and incident statistics.

### 🤖 AI-Powered Incident Analysis

- Generate concise AI summaries for every detected incident.
- Use structured incident context to explain the primary failure reason.

### 🧠 AI Investigation Copilot

- Ask natural language questions about any incident.
- Receive context-aware answers using the selected incident's data.
- Recommend possible next troubleshooting steps.

### 💾 Persistent Incident Store

- Store processed incidents separately from raw logs.
- Reuse processed incident data without re-running analysis.

### 🎨 Interactive Dashboard

- Browse incidents through a clean React interface.
- View incident summaries and investigate issues using the integrated AI Copilot.

## Architecture

```text
                CSV Upload
                     │
                     ▼
              Raw Log Storage
                     │
                     ▼
          Incident Detection Engine
                     │
                     ▼
        Persistent Incident Store
             │                │
             ▼                ▼
      AI Summary         React Dashboard
             │                │
             └──────┬─────────┘
                    ▼
            AI Investigation Copilot
                    │
                    ▼
              OpenAI GPT-4o-mini
```

## Tech Stack

### Backend

- Python
- FastAPI
- SQLAlchemy
- SQLite

### Frontend

- React
- Tailwind CSS
- Axios

### Artificial Intelligence

- OpenAI GPT-4o-mini
- OpenAI Embeddings
- Prompt Engineering
- Similarity Search

### Development Tools

- Git
- GitHub
- Visual Studio Code

## Project Structure

```text
ai-incident-intelligence/
│
├── app/
│   ├── models/          # SQLAlchemy database models
│   ├── routers/         # FastAPI API endpoints
│   ├── services/        # Business logic and AI services
│   ├── database.py      # Database configuration
│   └── main.py          # FastAPI application entry point
│
├── frontend/
│   ├── components/      # Reusable React components
│   ├── pages/           # Application pages
│   ├── services/        # API communication
│   └── App.jsx
│
├── logs.db              # SQLite database
└── README.md
```


## How It Works

1. The user uploads an infrastructure log file (CSV).
2. The backend stores the raw logs in a SQLite database.
3. Related log entries are grouped into incidents using configurable time and node-based rules.
4. Each incident is analyzed to calculate failure distribution and incident statistics.
5. OpenAI generates an automated AI summary for every incident.
6. Processed incidents are stored in a persistent Incident Store.
7. The React dashboard displays all detected incidents.
8. Users can select an incident and ask natural language questions through the AI Copilot.
9. The AI Copilot retrieves the selected incident, builds a context-aware prompt, and generates intelligent responses using OpenAI GPT-4o-mini.

## Getting Started

### Prerequisites

- Python 3.13+
- Node.js 18+
- OpenAI API Key

### Backend Setup

```bash
git clone https://github.com/AtharvaZalkikar/ai-incident-intelligence.git

cd ai-incident-intelligence

python -m venv venv

# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

The backend will be available at:

```text
http://localhost:8000
```

---

### Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

The frontend will be available at:

```text
http://localhost:5173
```

---

### Configure Environment Variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key
```

## Future Improvements

- Integrate a dedicated vector database (ChromaDB/Pinecone) for scalable similarity search.
- Stream AI responses for a ChatGPT-like experience.
- Add user authentication and role-based access.
- Support multiple investigation sessions.
- Visualize incident trends and analytics.
- Containerize the application using Docker.
- Deploy to a cloud platform (AWS/Azure/GCP).


## Key Learnings

Building this project strengthened my understanding of:

- Layered backend architecture using FastAPI.
- Service-oriented design and separation of concerns.
- Prompt engineering for context-aware AI applications.
- React state management and component composition.
- REST API design and frontend-backend integration.
- Persistent data modeling with SQLAlchemy.
- Git workflows using feature branches and pull requests.


## License

This project is licensed under the MIT License.