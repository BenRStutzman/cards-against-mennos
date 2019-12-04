import sys, os, threading, time

def run_server():
    os.system('flask run')

server = threading.Thread(target = run_server)
server.start()
print("starting server...")

time.sleep(10)
print('server ready.')
input("Go to 127.0.0.1:5000 in your browser, then hit enter here")

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

test_with_terminal()
