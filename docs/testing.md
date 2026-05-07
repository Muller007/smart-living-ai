# Testing Checklist – Smart Living AI

## Core Tests

### Income Test
Input: "I sold 150"
Expected: Income recorded

---

### Expense Test
Input: "I spent 50"
Expected: Expense recorded

---

### Profit Test
Input: "profit"
Expected: Correct totals

---

## Edge Case Tests

### Unknown Input
Input: "hello"
Expected: Help message

---

### No Data
Input: "profit"
Expected: "No data yet"

---

### Invalid Input
Input: "I sold -100"
Expected: Error or ignore

---

### Multiple Transactions
Input: "I sold 100 and spent 50"
Expected: Ask for one at a time

---

## Stability Tests
- Send multiple messages quickly
- Check system doesn’t crash

---

## Real User Test
- Give to 1 real person
- Observe behavior
- Note confusion points