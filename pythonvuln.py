# Proyecto: vulnerable_python_app.py
import base64
import sqlite3
import subprocess
import os

# Vulnerabilidad 1: Hardcoded Credentials
DATABASE_PASSWORD = "admin123"
AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

def vulnerable_sql_injection(username):
    # Vulnerabilidad 2: SQL Injection
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)

def command_injection(user_input):
    # Vulnerabilidad 3: Command Injection
    subprocess.run(f"ping {user_input}", shell=True)

def weak_random_generation():
    # Vulnerabilidad 4: Weak Random Generation
    return os.urandom(16).hex()

def sensitive_data_exposure():
    # Vulnerabilidad 5: Sensitive Data Exposure
    credentials = base64.b64encode(b"username:password").decode()
    return credentials

def main():
    vulnerable_sql_injection("admin' OR 1=1 --")
    command_injection("localhost; rm -rf /")
    print(weak_random_generation())
    print(sensitive_data_exposure())

if __name__ == "__main__":
    main()
