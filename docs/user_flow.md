# User Flow – Smart Living AI

## Main Flow

1. User sends message on WhatsApp
   Example: "I sold 150"

2. Message sent to Twilio

3. Twilio forwards to backend

4. Backend processes message

5. Transaction stored in database

6. Response generated

7. Message sent back to user

---

## User Actions

### Record Income
User → "I sold 150"
System → "Income recorded"

---

### Record Expense
User → "I spent 50"
System → "Expense recorded"

---

### Check Profit
User → "profit"
System → "Income: X, Expense: Y, Profit: Z"

---

## Error Flow

User → "hello"
System → "Send: 'I sold 100' or 'I spent 50'"

---

## Goal
User should:
- Not think
- Not learn anything new
- Just message naturally