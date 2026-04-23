from flask import Flask, request
from database import engine, SessionLocal, Base
from models import Transaction
from utils import parse_message

# ✅ CREATE APP FIRST
app = Flask(__name__)

# ✅ CREATE DATABASE TABLES
Base.metadata.create_all(bind=engine)


@app.route("/webhook", methods=["POST"])
def webhook():
    message = request.form.get("Body")
    phone = request.form.get("From")

    session = SessionLocal()
    parsed = parse_message(message)

    if parsed["type"] in ["income", "expense"]:
        transaction = Transaction(
            user_phone=phone,
            type=parsed["type"],
            amount=parsed["amount"],
            description=parsed["description"]
        )
        session.add(transaction)
        session.commit()

        reply = f"{parsed['type']} of R{parsed['amount']} recorded ✅"

    elif parsed["type"] == "summary":
        transactions = session.query(Transaction).filter_by(user_phone=phone).all()

        income = sum(t.amount for t in transactions if t.type == "income")
        expense = sum(t.amount for t in transactions if t.type == "expense")
        profit = income - expense

        reply = f"📊 Income: R{income}, Expense: R{expense}, Profit: R{profit}"

    else:
        reply = "Try: 'I sold 100' or 'I spent 50'"

    return f"<Response><Message>{reply}</Message></Response>"


if __name__ == "__main__":
    app.run(debug=True)