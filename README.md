# AI Support Ticket Classifier

## Overview

AI Support Ticket Classifier is a lightweight backend application designed to demonstrate how AI-powered workflow automation can be integrated into real business operations.

The application converts unstructured customer support messages into structured operational data such as:

* ticket category
* urgency level
* summary
* recommended action

The project focuses on:

* backend API development
* workflow automation
* structured validation
* applied AI architecture
* clean software engineering practices

The system uses a local Large Language Model (LLM) through Ollama to semantically understand customer messages and generate structured operational outputs.

---

# Why AI/LLMs Are Useful Here

Traditional rule-based systems rely on manually written keyword logic such as:

```python
if "refund" in text:
    category = "Billing"
```

While this works for simple cases, real customer messages are often inconsistent, informal, or ambiguous.

For example:

```text
"Money got taken from my card twice and nobody answered support."
```

A rigid rule-based system may fail to correctly classify this message because it does not explicitly contain words like:

* refund
* billing
* payment

An LLM can instead understand the semantic meaning of the message and infer that the issue relates to billing and duplicate charges.

This allows AI systems to:

* understand natural language
* classify messy support tickets
* summarize customer issues
* recommend next actions
* reduce manual operational workload

In this architecture, the LLM acts as an intelligent language-understanding component within a larger backend workflow system.

---

# Example Workflow

## Input

```json
{
  "message": "My pizza came an hour late, the app crashed, and I got charged twice."
}
```

## Structured Output

```json
{
  "category": "Billing",
  "urgency": "High",
  "summary": "Customer experienced delayed delivery, app instability, and duplicate charge.",
  "recommended_action": "Escalate to billing and technical support teams."
}
```

---

# High-Level Architecture

```text
Customer Support Message
            ↓
FastAPI Backend API
            ↓
Prompt Construction
            ↓
Local LLM (Ollama)
            ↓
Structured JSON Response
            ↓
Pydantic Validation
            ↓
Operational API Output
```

The backend API receives unstructured customer text, sends a structured prompt to the LLM, validates the model output, and returns structured operational data that could later be integrated into downstream workflows such as routing, escalation, analytics, dashboards, or support tooling.

---

# Technologies Used

## Python

Primary programming language used for backend development and workflow processing.

Why:

* widely used in AI/ML engineering
* strong ecosystem for APIs and automation
* commonly used in applied AI systems

---

## FastAPI

FastAPI is the backend web framework used to build the API.

Why:

* lightweight and modern
* built-in request validation
* automatic API documentation
* strong support for type hints
* commonly used for AI and microservice backends

Responsibilities:

* exposing API endpoints
* handling HTTP requests
* returning JSON responses

---

## Ollama

Ollama is used to run a local Large Language Model (LLM).

Why:

* fully local and free
* supports open-source LLMs
* no cloud API dependency required
* enables semantic understanding of customer messages

Responsibilities:

* ticket classification
* semantic understanding
* summarization
* operational recommendation generation

Example models:

* llama3.2
* mistral
* deepseek

---

## Pydantic

Pydantic is used for structured data validation.

Why:

* ensures predictable request and response formats
* validates API inputs automatically
* helps prevent malformed AI outputs from entering workflows

Responsibilities:

* validating support ticket requests
* validating classification responses
* enforcing allowed categories and urgency levels

---

## Uvicorn

Uvicorn is the ASGI server used to run the FastAPI application locally.

Why:

* fast development server
* supports asynchronous Python applications

Responsibilities:

* serving the backend API
* enabling local development and testing

---

## Python-dotenv

Used to load environment variables from a `.env` file.

Why:

* separates configuration from source code
* simplifies local development configuration
* supports runtime settings and model configuration

Responsibilities:

* loading runtime configuration
* storing model settings
* managing local environment variables

---

# Project Structure

```text
ai-ticket-classifier/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── schemas.py
│   └── ai_service.py
│
├── requirements.txt
├── .env
└── README.md
```

---

# File Explanations

## `app/main.py`

Main FastAPI application entry point.

Responsibilities:

* creates the FastAPI application
* defines API endpoints
* receives requests
* returns structured responses

Endpoints:

* `GET /` → health check
* `POST /classify` → classify support tickets

This file acts as the API layer between the client and the AI workflow.

---

## `app/schemas.py`

Contains structured request and response models.

Responsibilities:

* defines valid request format
* defines valid response format
* validates structured data
* enforces allowed categories and urgency levels

This file ensures the workflow always returns predictable structured outputs.

---

## `app/ai_service.py`

Contains the AI classification logic.

Responsibilities:

* processes incoming ticket text
* builds prompts for the LLM
* sends requests to Ollama
* validates model outputs
* provides fallback behavior if the model fails

This file acts as the AI service layer and separates model logic from the API layer.

Key features:

* local LLM integration
* structured JSON prompting
* response validation
* fallback handling
* semantic classification

---

## `.env`

Stores environment variables and runtime configuration.

Usage:

* model selection
* Ollama API configuration
* runtime settings
* mock mode toggling

Example:

```env
USE_MOCK=false
OLLAMA_MODEL=llama3.2:3b
OLLAMA_URL=http://localhost:11434/api/generate
```

---

## `requirements.txt`

Contains Python dependencies required for the project.

Used for:

* environment setup
* dependency management
* reproducible installations

---

# How to Run the Project

## 1. Install Ollama

Download Ollama:

```text
https://ollama.com/download/mac
```

Install a model:

```bash
ollama pull llama3.2:3b
```

---

## 2. Create virtual environment

```bash
python3 -m venv venv
```

---

## 3. Activate virtual environment

```bash
source venv/bin/activate
```

---

## 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

---

## 5. Start Ollama

Make sure Ollama is running locally.

---

## 6. Start FastAPI server

```bash
python -m uvicorn app.main:app --reload
```

---

## 7. Open API documentation

Visit:

```text
http://127.0.0.1:8000/docs
```

---

# Example Request

```json
{
  "message": "My order never arrived and I was charged twice."
}
```

---

# Example Response

```json
{
  "category": "Billing",
  "urgency": "High",
  "summary": "Customer issue: My order never arrived and I was charged twice.",
  "recommended_action": "Route to billing support."
}
```

---

# Future Improvements

Potential future enhancements:

* confidence scoring
* retry/fallback handling
* database support
* dashboard UI
* logging and monitoring
* Docker deployment
* cloud deployment
* authentication and authorization
* workflow escalation logic
* vector search/RAG integration
* analytics pipelines

---

# Design Goals

The project was intentionally designed to emphasize:

* clean backend architecture
* practical AI workflow automation
* structured validation
* maintainability
* production-oriented AI integration patterns

rather than advanced machine learning research.

The primary goal is to demonstrate how AI systems can be integrated into operational business workflows in a reliable and structured way.
