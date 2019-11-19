from queue import Queue
import sys
import time
from PodSixNet.Connection import connection, ConnectionListener
import threading

class GameClient(ConnectionListener):

    def __init__(self, host, port):
        self.Connect((host, port))
        self.events = Queue()
        self.stop_threads = False
        self.loop = threading.Thread(target = self.keep_pumping)
        self.loop.start()
        print("You've joined the game.")

    def send(self, event, details):
        connection.Send({'action': 'event', 'event': event, 'details': details})

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
        print('Server disconnected')
        sys.exit()

    def Network_event(self, data):
        self.events.put((data['event'], data['details'], data['time_lim']))
