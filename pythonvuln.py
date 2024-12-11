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

def unsafe_deserialization(serialized_data):
    # Vulnerabilidad 5: Unsafe Deserialization
    # Esta vulnerabilidad permite la ejecución remota de código
    # Un atacante puede craftar datos serializados maliciosos
    try:
        # Usando pickle, que es extremadamente peligroso
        obj = pickle.loads(serialized_data)
        
        # Otro ejemplo con marshal
        # obj = marshal.loads(serialized_data)
        
        return obj
    except Exception as e:
        print(f"Error en deserialización: {e}")

def main():
    # Ejemplo de uso de la vulnerabilidad de deserialización insegura
    # Este código es solo para demostración
    class MaliciousClass:
        def __reduce__(self):
            # Este método permite ejecutar código arbitrario durante la deserialización
            return (os.system, ('echo HACKED >> /tmp/pwned.txt',))

    # Serializar un objeto potencialmente malicioso
    malicious_payload = pickle.dumps(MaliciousClass())
    
    # Simular deserialización insegura
    unsafe_deserialization(malicious_payload)

    # Otras llamadas a funciones vulnerables para demostración
    vulnerable_sql_injection("admin' OR 1=1 --")
    command_injection("localhost; rm -rf /")
    print(weak_random_generation())

if __name__ == "__main__":
    main()
