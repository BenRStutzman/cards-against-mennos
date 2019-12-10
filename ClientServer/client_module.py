'''
Back-end functions for the connection between client and server
These are used by cam_client.py
'''

from queue import Queue
import sys
import time
from PodSixNet.Connection import connection, ConnectionListener
import threading
import msvcrt

class GameClient(ConnectionListener):

    def __init__(self, host, port):
        self.Connect((host, port))
        self.events = Queue()
        self.stop_threads = False
        self.loop = threading.Thread(target = self.keep_pumping)
        self.loop.daemon = True
        self.loop.start()
        print("You've joined the game.")

    def send(self, response):
        connection.Send({'action': 'response', 'response': response})

    def stop(self):
        self.stop_threads = True

    def keep_pumping(self):
        while not self.stop_threads:
            connection.Pump()
            self.Pump()

    def Network_error(self, data):
        print('error:', data['error'][1])
        connection.Close()

    def Network_disconnected(self, data):
        self.events.put(('server closed', '', -1, -1))

    def Network_event(self, data):
        self.events.put((data['event'], data['details'], data['time_lim'],
                        data['num_chars']))

def timed_input(prompt, time_lim, num_chars = 1):
    while msvcrt.kbhit():
        msvcrt.getch()
    start_time = time.time()
    print(prompt)
    response = ''

    while time.time() - start_time < time_lim:
        if msvcrt.kbhit():
            char = msvcrt.getwch()
            print(char)
            response += char
            if len(response) == num_chars:
                return response
    else:
        print('Too late!')
        return 'no response'
