# Doctor Appointment Multi-Agent (RAG + Agents)

A multi-agent Doctor Appointment system that combines an LLM (Groq Qwen), LangChain/LangGraph agents and a simple toolset to check doctor availability, book, cancel and reschedule appointments.
Includes a FastAPI backend (agent runner) and a Streamlit UI.

# What it does

- Accepts a user query (via UI or API) like: “Can you check and book a general dentist on 08-08-2024 at 20:00?”

- Supervisor agent routes the query to specialized agents:

- information_node — checks availability (tools use CSV data).

- booking_node — sets/cancels/reschedules appointments.

- Tools manipulate a local CSV (data/doctor_availability.csv) as a datastore for demo/testing.

- FastAPI exposes /execute endpoint to run the graph; Streamlit UI is a simple frontend.

# Project structure

```bash
.
├─ data/
│  └─ doctor_availability.csv
├─ data_models/
│  └─ models.py
├─ prompt_library/
│  └─ prompt.py
├─ toolkit/
│  └─ toolkits.py
├─ utils/
│  └─ llms.py
├─ agent.py
├─ main.py
├─ streamlit_ui.py
├─ setup.py
├─ requirements.txt
└─ README.md
```

# Prerequisites

  Python 3.10+

  Conda (recommended) or virtualenv

  Internet access (for Groq API)

  GROQ_API_KEY from Groq (do not commit to repo)

# Quickstart — run locally

## 1) Create the environment (example using conda):

```bash
# from repo root
conda create -p ./venv python=3.10 -y
conda activate ./venv
pip install -r requirements.txt

```

## 2) Add environment variables:

Create file `.env` in repo root (see `.env.example` below) and add your `GROQ_API_KEY`.

## 3) Start the API (run this first)

```bash
# run from project root
uvicorn main:app --reload --port 8003
```

## 4) Start Streamlit UI (in another terminal)

```bash
streamlit run streamlit_ui.py
```

## 5) Open:

  Streamlit UI:` http://localhost:8501`

  FastAPI docs: `http://127.0.0.1:8003/docs `
