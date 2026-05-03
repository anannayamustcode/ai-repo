import os

# Hardcoded secret
password = "super_secret_123"

# Dangerous input usage
user_input = input("Enter something: ")

#  HIGH RISK — eval
eval(user_input)

#  HIGH RISK — exec
exec(user_input)

# MEDIUM — subprocess with shell=True
os.system("ls -la")

# MEDIUM — insecure random
import random
token = random.random()

# LOW — debug print
print("Debug:", password)

# Function with potential issue
def unsafe_function(data):
    query = f"SELECT * FROM users WHERE name = '{data}'"
    print(query)

unsafe_function(user_input)
