# API Documentation – Smart Living AI

## Base URL
http://127.0.0.1:5000

---

## Endpoint: POST /webhook

### Description
Receives messages from WhatsApp (via Twilio) and processes business transactions.

---

## Request Format

### Headers
Content-Type: application/json (local testing)

### Body (Local Testing)
{
  "phone": "0821234567",
  "message": "I sold 150"
}

---

### Body (Twilio Format)
- Body: message text
- From: user phone number

---

## Response Format

{
  "reply": "income of R150 recorded"
}

---

## Supported Commands

| Input Example       | Action              |
|--------------------|---------------------|
| I sold 150         | Record income       |
| I spent 50         | Record expense      |
| profit             | Show summary        |

---

## Errors

| Scenario              | Response                          |
|----------------------|----------------------------------|
| Unknown message      | Help instruction                 |
| No data for profit   | "No data yet"                    |

---

## Future Endpoints (Planned)
- GET /user-summary
- POST /voice-input
- GET /insights