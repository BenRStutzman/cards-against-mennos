# this is all background stuff and shouldn't have to be changed

from flask import Flask, jsonify, request, render_template
import time, os, threading, sys
import logging

#so it doesn't print every connection
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)

def read_and_reset(filename):
    while True:
        time.sleep(0.1)
        f = open(filename, 'r+')
        message = f.read().strip()
        if message:
            break
        f.close()
    f.truncate(0)
    f.close()
    return message

@app.route('/hello', methods=['GET', 'POST'])
def hello():

    # POST request
    if request.method == 'GET':
        instructions, time_lim = read_and_reset('py_to_js.txt').split('$$$$$$$')
        to_send = {'instructions': instructions, 'time_lim': time_lim}
        return jsonify(to_send)  # serialize and use JSON headers

    # GET request
    else:
        #print('Incoming..')
        #print("response:", end = ' ')
        js_to_py = request.get_json(force=True)['response']  # parse as JSON
        #print(js_to_py)
        f = open('js_to_py.txt', 'w+')
        f.write(js_to_py)
        f.close()
        return 'OK', 200

@app.route('/')
def test_page():
    # look inside `templates` and serve `index.html`
    return render_template('index.html')
