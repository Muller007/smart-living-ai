import re

def process_message(message):
    message = message.lower()

    # extract all numbers
    numbers = [float(n) for n in re.findall(r'\d+', message)]

    income = None
    expense = None

    # keywords
    income_keywords = ["sold", "made", "earned", "income", "received"]
    expense_keywords = ["spent", "bought", "used", "paid", "cost"]

    # detect income
    if any(word in message for word in income_keywords):
        if numbers:
            income = max(numbers)  # assume biggest number = income

    # detect expense
    if any(word in message for word in expense_keywords):
        if numbers:
            expense = min(numbers) if len(numbers) > 1 else numbers[0]

    # smart logic fix for mixed sentences
    if income and expense and income == expense:
        expense = None  # avoid duplicate mistake

    # generate reply
    if income and expense:
        profit = income - expense
        reply = f"📊 Recorded! Income: R{income}, Expense: R{expense}, Profit: R{profit}"
    elif income:
        reply = f"💰 Got it! Income of R{income} recorded."
    elif expense:
        reply = f"💸 Noted! Expense of R{expense} recorded."
    else:
        reply = "Try: 'I sold 100' or 'I spent 50 on stock'"

    return {
        "income": income,
        "expense": expense,
        "reply": reply
    }