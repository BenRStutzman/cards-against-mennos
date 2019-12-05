import sys, os, threading, time

## THIS IS THE KEY FUNCTION
def exchange(message):
    # Sends "message" to the browser and waits for a response, then returns it
    f = open('py_to_js.txt', 'w')
    f.write(message)
    f.close()
    response = read_and_reset('js_to_py.txt')
    return response

def read_and_reset(filename):
    while True:
        f = open(filename, 'r+')
        message = f.readline().strip()
        if message:
            break
        f.close()
    f.truncate(0)
    f.close()
    return message

def test_with_terminal():
    while True:
        response = exchange(input('message to send to browser: '))
        print('browser says:', response)

f = open('js_to_py.txt', 'w')
f.close()
f = open('py_to_js.txt', 'w')
f.close()
server = threading.Thread(target = os.system, args = {'flask run'})
server.start()

print("starting server...")
input("\nWait until server details appear below, then"
        " go to 127.0.0.1:5000 in your browser and hit enter here.\n\n")

test_with_terminal()
