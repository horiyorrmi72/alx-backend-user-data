# 🔐 Personal Data Handling Project

This project demonstrates secure handling of sensitive user data using Python and MySQL. It emphasizes best practices such as password hashing, redacted logging, and secure database access.

---

## 🚀 Features

### 1. **🔑 Password Hashing**
**Module**: `encrypt_password.py`  
Securely handles password storage using [bcrypt](https://pypi.org/project/bcrypt/).

- `hash_password(password: str) -> bytes`  
  Generates a salted hash for a given password.

- `is_valid(hashed_password: bytes, password: str) -> bool`  
  Verifies if a plain-text password matches its hashed version.

---

### 2. **🕵️ Secure Logging with Redaction**
**Module**: `filtered_logger.py`  
Implements privacy-focused logging with automatic redaction of PII fields.

- Redacts sensitive user information (`name`, `email`, `phone`, `ssn`, `password`) in logs.
- Custom `RedactingFormatter` ensures consistent and secure log formatting.
- Connects to a MySQL database and logs user data in a sanitized format.

---

### 3. **🗄️ Database Schema**
**File**: `main.sql`  
Initializes a sample MySQL database (`my_db`) with a `users` table for testing.

- Defines fields like `name`, `email`, `phone`, `ssn`, `password`, `ip`, `last_login`, and `user_agent`.
- Populates the table with mock user data including PII.

---

## ⚙️ Environment Configuration

`filtered_logger.py` uses environment variables for secure, dynamic database access:

| Variable                     | Description           | Default        |
|-----------------------------|-----------------------|----------------|
| `PERSONAL_DATA_DB_USERNAME` | MySQL username        | `root`         |
| `PERSONAL_DATA_DB_PASSWORD` | MySQL password        | *(empty)*      |
| `PERSONAL_DATA_DB_HOST`     | MySQL host address    | `localhost`    |
| `PERSONAL_DATA_DB_NAME`     | Target database name  | *(empty)*      |

---

## 🛠️ How to Use

### 1. **Set Up the Database**
Run the SQL script to initialize the database and insert sample data:
```bash
mysql -u <username> -p < main.sql
 ```

### 2. **Set environment variables and run the logger script:**
Run the SQL script to initialize the database and insert sample data:
```bash
PERSONAL_DATA_DB_USERNAME=root \
PERSONAL_DATA_DB_PASSWORD=root \
PERSONAL_DATA_DB_HOST=localhost \
PERSONAL_DATA_DB_NAME=my_db \
./filtered_logger.py
```
### Expected sanitized output (example):
``` bash
[HOLBERTON] user_data INFO 2025-05-01 13:37:59: name=***; email=***; phone=***; ssn=***; password=***; ip=...; last_login=...; user_agent=...;

```

## 📚 Understanding the Code
#!/usr/bin/env python3: Ensures the script runs with Python 3.

Docstrings describe the purpose and functionality of each function.

Regex patterns are used to detect and redact sensitive fields in log messages.


