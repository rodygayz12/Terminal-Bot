import os
import re

id_pattern = re.compile(r'^.\d+$')


token = os.environ.get("TOKEN","6861294909:AAEf5aupZPVgBeWmfM864AWcLSoRyutDrnY")
app_id = int(os.environ.get("APP_ID","21503867"))
app_hash = os.environ.get("API_HASH","e0e50d95e1319072731fb0a4a585e9d5")
allowed = [int(user) if id_pattern.search(user) else user for user in os.environ.get('AUTH_USERS', '6221136155').split()]

help_text = """
Hello I'm Terminal Bot which will Execute your Commands.

With this bot you can execute system commands on your server.

**if you not owner of this bot You can not use me because I'm private...
So you run one of these for yourself [here](https://github.com/moshe-coh/Terminal-Bot)**

**My Commands For Owner Only:**

🔹 /st - speed test
🔹 /ip - ip details
🔹 /stats - disk space
🔹 /cd - change working dir
🔹 /my_files - file manager
🔹 And All System Commands...

"""
