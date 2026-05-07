# Database Schema – Smart Living AI

## Table: transactions

| Field        | Type      | Description                     |
|--------------|----------|---------------------------------|
| id           | Integer  | Primary key                     |
| user_phone   | String   | User identifier                 |
| type         | String   | income / expense                |
| amount       | Float    | Transaction amount              |
| description  | String   | Original message                |
| date         | DateTime | Timestamp                       |

---

## Relationships
- One user → many transactions

---

## Future Tables

### Users
- id
- phone
- business_type

### Customers
- name
- last_purchase
- frequency

---

## Notes
- SQLite used for MVP
- Will migrate to PostgreSQL for scaling