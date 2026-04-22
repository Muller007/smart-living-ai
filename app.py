from flask import Flask, request, jsonify
from database import engine, SessionLocal, Base
from models import Transaction
from utils import parse_message

app = Flask(__name__)

# Create tables
Base.metadata.create_all(bind=engine)


@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    # simulate WhatsApp structure
    message = data.get("message")
    phone = data.get("phone")

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

        return jsonify({
            "reply": f"{parsed['type']} of R{parsed['amount']} recorded ✅"
        })

    elif parsed["type"] == "summary":
        transactions = session.query(Transaction).filter_by(user_phone=phone).all()

        income = sum(t.amount for t in transactions if t.type == "income")
        expense = sum(t.amount for t in transactions if t.type == "expense")
        profit = income - expense

        return jsonify({
            "reply": f"📊 Income: R{income}, Expense: R{expense}, Profit: R{profit}"
        })

    return jsonify({"reply": "Sorry, I didn't understand. Try: 'I sold 100'"})


if __name__ == "__main__":
    app.run(debug=True)