import sys
import time
import random
from PodSixNet.Server import Server
from PodSixNet.Channel import Channel

first_names = ['Levi', 'Matthias', 'Irene', 'Annie', 'Mary', 'David', 'Daniel',
                'Jeanie', 'Methuselah', 'Nebuchadnezzar', 'Jedediah', 'John',
                'Eli', 'Noah', 'Samuel', 'Sarah', 'Rebecca', 'Anna', 'Susanna',
                'Hannah', 'Susan', 'Elizabeth', 'Rachael', 'Moses']
last_names = ['Yoder', 'Stoltzfus', 'Martin', 'Reimer', 'Berg',
                'Friesen', 'Longachre', 'Lehman', 'Miller', 'Weaver', 'Weber',
                'Horst', 'Hurst', 'Kauffman', 'Hostetler', 'Good', 'Shenk',
                'Brubaker', 'Landis', 'Zehr', 'Garber', 'Roth', 'Mast', 'Wenger',
                'Bontrager', 'Burkholder', 'Peachey', 'Shrock', 'Zimmerman']

class ClientChannel(Channel):
    """
    This is the server representation of a single connected client.
    """
    def __init__(self, *args, **kwargs):
        self.nickname = (first_names.pop(random.randint(0, len(first_names) - 1)) +
        " " + last_names.pop(random.randint(0, len(last_names) - 1)) + '-' +
        last_names.pop(random.randint(0, len(last_names) - 1)))
        Channel.__init__(self, *args, **kwargs)

    def Close(self):
        self._server.DelPlayer(self)

    ##################################
    ### Network specific callbacks ###
    ##################################

    def Network_message(self, data):
        self._server.SendToAll({"action": "message", "message": data['message'], "who": self.nickname})

    def Network_nickname(self, data):
        self.nickname = data['nickname']
        self._server.SendPlayers()

class GameServer(Server):
    channelClass = ClientChannel

    def __init__(self, *args, **kwargs):
        Server.__init__(self, *args, **kwargs)
        self.players = {}
        print('Server launched')

    def Connected(self, channel, addr):
        self.AddPlayer(channel)

    def AddPlayer(self, player):
        print(player.nickname + " joined the game.")
        self.players[player] = True
        player.Send({"action": "nickname", "nickname": player.nickname})
        self.SendToAll({"action": "new_player", "new_player": player.nickname},
            exclude = player)
        player.Send({"action": "players", "players":
            [p.nickname for p in self.players if p != player]})

    def DelPlayer(self, player):
        print(player.nickname + " left the game.")
        del self.players[player]
        self.SendPlayers()

    def SendPlayers(self):
        self.SendToAll({"action": "players", "players": [p.nickname for p in self.players]})

    def SendToAll(self, data, exclude = ""):
        [p.Send(data) for p in self.players if p != exclude]

    def Launch(self):
        while True:
            self.Pump()
            time.sleep(0.0001)


host = input("Enter this computer's IP address: ")
port = input("Enter the port # you'd like to use (1000 is fine): ")
server = GameServer(localaddr=(host, int(port)))
server.Launch()

'''
# get command line argument of server, port
if len(sys.argv) != 2:
    print("Usage:", sys.argv[0], "host:port")
    print("e.g.", sys.argv[0], "localhost:31425")
else:
    host, port = sys.argv[1].split(":")
    s = GameServer(localaddr=(host, int(port)))
    s.Launch()
'''
