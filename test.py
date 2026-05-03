
import os
import subprocess
import random

# Hardcoded secret
password = "super_secret_123"

# Dangerous input
user_input = input("Enter something: ")

# Code execution
eval(user_input)
exec(user_input)

# Command injection
os.system(user_input)
subprocess.run(user_input, shell=True)

# SQL Injection
query = f"SELECT * FROM users WHERE name = '{user_input}'"
print(query)

# Weak randomness
token = random.random()

# Sensitive logging
print("Password is:", password)

# Path traversal
with open(user_input, "r") as f:
    data = f.read()
