import sys
from time import sleep
from sys import stdin, exit

from PodSixNet.Connection import connection, ConnectionListener

# This example uses Python threads to manage async input from sys.stdin.
# This is so that I can receive input from the console whilst running the server.
# Don't ever do this - it's slow and ugly. (I'm doing it for simplicity's sake)
import threading

class Client(ConnectionListener):
    def __init__(self, host, port):
        self.Connect((host, port))
        # get a nickname from the user before starting
        #print("Enter your nickname: "),
        #connection.Send({"action": "nickname", "nickname": stdin.readline().rstrip("\n")})
        # launch our threaded input loop
        self.inp_thread = threading.Thread(target = self.InputLoop, args = ())
        self.inp_thread.start()

    def Loop(self):
        connection.Pump()
        self.Pump()

    def InputLoop(self):
        # horrid threaded input loop
        # continually reads from stdin and sends whatever is typed to the server
        try:
            while 1:
                connection.Send({"action": "message", "message": input()})
        except EOFError:
            return

    #######################################
    ### Network event/message callbacks ###
    #######################################

    def Network_players(self, data):
        if data['players']:
            print("Other players: " + ", ".join([p for p in data['players']]))
        else:
            print("You're the first one here.")

    def Network_message(self, data):
        print(data['who'] + ": " + data['message'])

    # built in stuff

    def Network_nickname(self, data):
        self.nickname = data["nickname"]
        print("Your name is " + self.nickname)

    def Network_new_player(self, data):
        print(data['new_player'] + " joined the game.")

    def Network_connected(self, data):
        print("You've joined the game (Press Ctr-C to exit).")

    def Network_error(self, data):
        print('error:', data['error'][1])
        connection.Close()

    def Network_disconnected(self, data):
        print('Server disconnected')
        exit()

if len(sys.argv) != 2:
    print("Usage:", sys.argv[0], "host:port")
    print("e.g.", sys.argv[0], "localhost:31425")
else:
    host, port = sys.argv[1].split(":")
    c = Client(host, int(port))
    try:
        while True:
            c.Loop()
            sleep(0.001)
    except KeyboardInterrupt:
        print("Goodbye!")
