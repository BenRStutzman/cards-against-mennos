import sys, os, threading, time
from app import read_and_reset

## THIS IS THE KEY FUNCTION
def exchange(message, time_lim = 10):
    # Sends "message" to the browser and waits for a response, then returns it
    f = open('py_to_js.txt', 'w')
    f.write(message + '\n' + str(time_lim))
    f.close()
    return read_and_reset('js_to_py.txt')

def test_with_terminal():
    while True:
        response = exchange(input('message to send to browser: '))
        print('browser says:', response)

def setup_server():
    f = open('js_to_py.txt', 'w')
    f.close()
    f = open('py_to_js.txt', 'w')
    f.close()
    server = threading.Thread(target = os.system, args = {'flask run'})
    server.start()

    print("starting server...")
    input("\nWait until server details appear below, then"
            " go to 127.0.0.1:5000 in your browser and hit enter here.\n\n")

if __name__ == '__main__':
    setup_server()
