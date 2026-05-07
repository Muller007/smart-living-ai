from flask import Flask, request
from database import engine, SessionLocal, Base
from models import Transaction
from ai_engine import process_message

# Create Flask app
app = Flask(__name__)

# Create database tables
Base.metadata.create_all(bind=engine)


@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        message = request.form.get("Body")
        phone = request.form.get("From")

        print(f"\n📩 Incoming message from {phone}: {message}")

        session = SessionLocal()

        # 🚀 YOUR LOCAL AI ENGINE (NO OPENAI)
        ai_result = process_message(message)

        print(f"🤖 Processed Output: {ai_result}")

        income = ai_result.get("income")
        expense = ai_result.get("expense")
        reply = ai_result.get("reply")

        # Store income
        if income is not None:
            session.add(Transaction(
                user_phone=phone,
                type="income",
                amount=float(income),
                description=message
            ))

        # Store expense
        if expense is not None:
            session.add(Transaction(
                user_phone=phone,
                type="expense",
                amount=float(expense),
                description=message
            ))

        session.commit()

        return f"<Response><Message>{reply}</Message></Response>"

    except Exception as e:
        print("❌ Error:", str(e))
        return "<Response><Message>Error occurred</Message></Response>"


if __name__ == "__main__":
    app.run(debug=True)