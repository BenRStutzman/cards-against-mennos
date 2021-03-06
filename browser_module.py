import sys, os, threading, time
from app import read_and_reset

def exchange(message, time_lim = 10):
    # Sends "message" to the browser and waits for a response, then returns the response
    # uses writing and reading from text files to make this happen
    open('js_to_py.txt', 'w').close()
    f = open('py_to_js.txt', 'w')
    f.write(message + '$$$$$$$' + str(time_lim)) #the delimeter is arbitrarily chosen as '$$$$$$$'
    f.close()
    return read_and_reset('js_to_py.txt')

def test_with_terminal():
    while True:
        response = exchange(input('message to send to browser: '))
        print('browser says:', response)

def setup_server():
    # clear the text files and start the server
    open('js_to_py.txt', 'w').close()
    open('py_to_js.txt', 'w').close()
    server = threading.Thread(target = os.system, args = {'flask run'})
    server.daemon = True
    server.start()

    print("\nWhen server details appear below,"
            " go to 127.0.0.1:5000 in your browser.\n")

if __name__ == '__main__':
    setup_server()
