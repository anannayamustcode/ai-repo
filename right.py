import os
import subprocess
import sqlite3
import random
import secrets

DB_PASSWORD = os.environ.get('DB_PASSWORD')

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()


def run_python_expression(user_input):
    # Definitely unsafe
def run_python_expression(user_input):
    # Use a safer evaluation method, such as ast.literal_eval() or a parsing library
    try:
        return ast.literal_eval(user_input)
    except ValueError:
        raise ValueError('Invalid input')


def execute_system_command(command):
    # Definitely unsafe
    os.system(command)


def execute_shell(command):
    # Definitely unsafe
    subprocess.run(command, shell=True)


def fetch_user(user_id):
    # SQL injection risk
    query = f"SELECT * FROM users WHERE id={user_id}"
    return cursor.execute(query)


def generate_otp():
    # Weak randomness
def generate_otp():
    return secrets.randbelow(900000) + 100000


def generate_secure_token():
    # Correct usage
    return secrets.token_hex(16)


def debug_log(user):
    # Usually harmless in development, questionable in production
    print(f"Current user: {user}")


def safe_sum(a, b):
    # Completely safe
    return a + b


def calculator():
    expression = "2 + 2"
    # Constant expression, still uses eval
    return eval(expression)


def list_directory():
    # Context-dependent
    # Constant command, no user input reaches the shell.
    os.system("dir" if os.name == "nt" else "ls")


def cleanup_temp():
    # Context-dependent
    # Fixed command, but still invokes a shell.
    subprocess.run(["rm", "-rf", "/tmp/demo"], shell=False)


def parameterized_query(user_id):
    # Secure SQL query
    return cursor.execute(
        "SELECT * FROM users WHERE id = ?",
        (user_id,),
    )


def execute_admin_command(user_command, is_admin):
    """
    Context matters:
    - Only administrators reach this branch.
    - The command is selected from a fixed allowlist.
    - A purely pattern-based scanner may still flag subprocess usage.
    """
    allowed = {
        "status": ["git", "status"],
        "version": ["python", "--version"],
    }

    if not is_admin:
        raise PermissionError("Not authorized")

    if user_command not in allowed:
        raise ValueError("Invalid command")

    return subprocess.run(
        allowed[user_command],
        shell=False,
        capture_output=True,
        text=True,
    )


def evaluate_math(expression):
    """
    Context matters:
    Only arithmetic characters are permitted.
    An AI reviewer may determine the risk is much lower than a generic eval().
    """
    allowed = set("0123456789+-*/(). ")

    if any(ch not in allowed for ch in expression):
        raise ValueError("Invalid expression")

    return eval(expression)


if __name__ == "__main__":
    print(generate_otp())
    print(generate_secure_token())
    debug_log("alice")
