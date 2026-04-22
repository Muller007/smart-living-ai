

````markdown
# 🚀 Smart Living AI
### AI-Powered WhatsApp Assistant for Smarter Financial Decisions

---

## 🧠 Overview

Smart Living AI is a WhatsApp-based assistant designed to help small business owners and individuals track their finances and make smarter decisions using simple messages.

Instead of complex apps or spreadsheets, users can simply send messages like:

- "I sold 150"
- "I spent 50"
- "profit"

And instantly receive insights about their business.

---

## 🎯 Problem

Across Africa, millions of small and informal businesses:
- Do not track income and expenses properly  
- Make decisions based on guesswork  
- Lack access to simple financial tools  

Existing solutions are often:
- Too complex  
- Not accessible  
- Not designed for everyday users  

---

## 💡 Solution

Smart Living AI provides:

✅ Simple financial tracking via WhatsApp  
✅ Real-time profit calculation  
✅ Zero learning curve  
✅ No app installation required  

---

## ⚙️ How It Works

```text
User → WhatsApp → Twilio → Flask Backend → Database → Response → WhatsApp
````

1. User sends a message
2. System interprets it
3. Data is stored
4. Insights are generated
5. Response is sent instantly

---

## 🧱 Tech Stack

* **Backend:** Python (Flask)
* **Database:** SQLite (MVP)
* **ORM:** SQLAlchemy
* **Messaging API:** Twilio WhatsApp API
* **Tunneling:** ngrok

---

## 📊 Features (MVP)

* 📥 Record income
* 📤 Record expenses
* 📈 Calculate profit
* 💬 WhatsApp-based interaction

---

## 🧪 Example Usage

| User Input | System Response                       |
| ---------- | ------------------------------------- |
| I sold 150 | Income recorded ✅                     |
| I spent 50 | Expense recorded ✅                    |
| profit     | Income: 150, Expense: 50, Profit: 100 |

---

## 📁 Project Structure

```
smart-living-ai/
│── app.py
│── utils.py
│── models.py
│── database.py
│── requirements.txt
│
├── docs/
│   ├── api_docs.md
│   ├── architecture.md
│   ├── database_schema.md
│   ├── user_flow.md
│   ├── prd.md
│   ├── testing.md
│   ├── privacy_policy.md
│   ├── terms.md
```

---

## 🔧 Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/Muller007/smart-living-ai.git
cd smart-living-ai
```

---

### 2. Install dependencies

```
python -m pip install -r requirements.txt
```

---

### 3. Run the server

```
python app.py
```

---

### 4. Expose with ngrok

```
ngrok http 5000
```

---

### 5. Connect to WhatsApp (Twilio Sandbox)

* Paste ngrok URL + `/webhook` into Twilio
* Start sending messages from WhatsApp

---

## 🧠 Vision

To build an AI-powered system that helps people make smarter financial and life decisions using simple tools like WhatsApp.

---

## 🚀 Future Roadmap

* 🤖 AI-powered business insights
* 🎤 Voice input support
* 📊 Advanced analytics dashboard
* 🌍 Expansion across Africa

---

## 🏆 Why This Project Matters

This project focuses on:

* Accessibility over complexity
* Real-world impact
* Empowering underserved communities

---

## 👤 Founder

**Kwanele Mlalazi**

* BSc Computer Science 
* Focused on AI, systems, and real-world problem solving

---

## 📬 Contact

If you're interested in collaboration, partnerships, or feedback:

👉 Reach out via GitHub or connect professionally

---

## ⭐ Support

If you find this project valuable:

⭐ Star the repo
🍴 Fork it
📢 Share it

---

> “Building intelligent systems for real-world impact.”

````

---

