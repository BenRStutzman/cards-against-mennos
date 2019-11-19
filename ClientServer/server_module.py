import sys
import time
import threading
from queue import Queue
from PodSixNet.Server import Server
from PodSixNet.Channel import Channel


class ClientChannel(Channel):
    """
    This is the server representation of a single connected client.
    """
    def __init__(self, *args, **kwargs):
        i = 0
        Channel.__init__(self, *args, **kwargs)
        while i in self._server.players:
            i += 1
        self.ID = i

    def Close(self):
        self._server.DelPlayer(self)

    def Network_event(self, data):
        self._server.events.put((self, data['event'], data['details']))

class GameServer(Server):
    channelClass = ClientChannel

    def __init__(self, *args, **kwargs):
        Server.__init__(self, *args, **kwargs)
        self.players = {}
        self.events = Queue()
        self.stop_threads = False
        self.loop = threading.Thread(target = self.keep_pumping)
        self.loop.start()
        print('Server launched')

    def keep_pumping(self):
        while not self.stop_threads:
            self.Pump()

    def stop(self):
        self.stop_threads = True

    def Connected(self, channel, addr):
        self.AddPlayer(channel)

    def AddPlayer(self, player):
        self.players[player.ID] = player
        print("Player %s has joined the game." % player.ID)

    def DelPlayer(self, player):
        del self.players[player.ID]
        print("Player %s has left the game." % player.ID)

    def send_to_player(self, ID, event, details, time_lim):
        if ID in self.players:
            self.players[ID].Send({'action': 'event', 'event': event,
                                    'details': details, 'time_lim': time_lim})
            return True
        else:
            return False

    def send_to_all(self, event, details, time_lim, exclude = ""):
        for ID in self.players.copy():
            if ID != exclude:
                self.send_to_player(ID, event, details, time_lim)
