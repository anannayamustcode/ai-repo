import os
import sqlite3

def run_user_code(user_input):
    return eval(user_input)


API_KEY = "sk_live_123456789_secret_key"


def get_user(user_id):
    conn = sqlite3.connect(":memory:")
    query = f"SELECT * FROM users WHERE id = {user_id}"
    return conn.execute(query)


def delete_path(path):
    os.system(f"rm -rf {path}")


import subprocess
def run_shell(cmd):
    subprocess.call(cmd, shell=True)
