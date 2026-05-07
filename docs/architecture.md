# System Architecture – Smart Living AI

## Overview
The system is a WhatsApp-based AI assistant that processes user messages into financial data and insights.

---

## Components

### 1. User (WhatsApp)
- Sends messages
- Receives responses

### 2. Twilio API
- Bridges WhatsApp and backend

### 3. Flask Backend (app.py)
- Main processing engine

### 4. Message Processor (utils.py)
- Interprets user messages

### 5. Database (SQLite)
- Stores transactions

---

## Data Flow

User → WhatsApp → Twilio → Flask → Processor → Database → Logic → Response → WhatsApp

---

## Key Design Principles
- Simplicity
- Reliability
- Low data usage
- Mobile-first (WhatsApp)

---

## Future Architecture
- Cloud hosting (AWS / Render)
- PostgreSQL database
- AI model integration
- Microservices architecture