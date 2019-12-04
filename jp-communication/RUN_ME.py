import sys, os, threading, time
from app import read_and_reset

## THIS IS THE KEY FUNCTION
def exchange(message):
    # Sends "message" to the browser and waits for a response, then returns it
    f = open('py_to_js.txt', 'w')
    f.write(message)
    f.close()
    response = read_and_reset('js_to_py.txt')
    return response

def test_with_terminal():
    while True:
        response = exchange(input('message to send to browser: '))
        print('browser says:', response)

server = threading.Thread(target = os.system, args = {'flask run'})
server.start()

print("starting server...")
time.sleep(10)
print('server ready.')
input("Go to 127.0.0.1:5000 in your browser, then hit enter here")

test_with_terminal()
