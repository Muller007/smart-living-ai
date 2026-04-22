import re

def parse_message(message):
    message = message.lower()

    # detect income
    if "sold" in message or "made" in message:
        amount = extract_amount(message)
        return {"type": "income", "amount": amount, "description": message}

    # detect expense
    elif "spent" in message or "bought" in message:
        amount = extract_amount(message)
        return {"type": "expense", "amount": amount, "description": message}

    # request summary
    elif "profit" in message or "summary" in message:
        return {"type": "summary"}

    return {"type": "unknown"}


def extract_amount(message):
    match = re.search(r'\d+', message)
    return float(match.group()) if match else 0