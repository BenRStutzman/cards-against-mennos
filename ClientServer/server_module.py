import sys
import time
import threading
from queue import Queue
from PodSixNet.Server import Server
from PodSixNet.Channel import Channel

def update_users(usernames, winner):
    f = open('user_list.txt', 'r+')
    users = {username: [int(num) for num in [games_played, games_won]] for username, games_played,
            games_won in [line.split() for line in f.read().splitlines()]}
    print(users)
    for username in usernames:
        games, wins = users.get(username, (0, 0))
        games += 1
        if username == winner:
            wins += 1
        users[username] = games, wins
    f.seek(0)
    for username, (games, wins) in users.items():
        f.write('%s %d %d\n' % (username, games, wins))
    f.close()
    return users

def open_server(host, port):
    # host is a string and port is an integer
    global server
    print("Server opened at " + host + ':' + str(port))
    return GameServer(localaddr = (host, port))

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

    def Network_response(self, data):
        self._server.responses.put((self.ID, data['response']))

class GameServer(Server):
    channelClass = ClientChannel

    def __init__(self, *args, **kwargs):
        Server.__init__(self, *args, **kwargs)
        self.players = {}
        self.responses = Queue()
        self.stop_threads = False
        self.loop = threading.Thread(target = self.keep_pumping)
        self.loop.daemon = True
        self.loop.start()

    def keep_pumping(self):
        while not self.stop_threads:
            self.Pump()

    def stop(self):
        self.stop_threads = True

    def Connected(self, channel, addr):
        self.AddPlayer(channel)

    def AddPlayer(self, player):
        self.players[player.ID] = player
        print("(Player %s has joined the game)" % player.ID)
        self.send_event("You are player #", details = str(player.ID), player_ID = player.ID)

    def DelPlayer(self, player):
        del self.players[player.ID]
        print("(Player %s has left the game)" % player.ID)

    def send_to_player(self, ID, event, details, time_lim, num_chars, from_all = False):
        if ID in self.players:
            self.players[ID].Send({'action': 'event', 'event': event,
                                    'details': details, 'time_lim': time_lim,
                                    'num_chars': num_chars})
            if not from_all:
                if details:
                    details = ": " + details
                print("'%s%s' sent to player %d" % (event, details, ID))
            return True
        else:
            return False

    def send_to_all(self, event, details, time_lim, num_chars, exclude = -1):
        for ID in self.players.copy():
            if ID != exclude:
                self.send_to_player(ID, event, details, time_lim, num_chars, from_all = True)
        if details:
            details = ": " + details
        print("'%s%s' sent to all players" % (event, details))

    def close(self):
        print("Server closed.")
        self.stop()
        sys.exit()

    def get_responses(self, num_needed = -1):
        if num_needed < 0:
            num_needed = len(self.players)
        response_list = []
        while self.responses.qsize() < num_needed:
            pass
        while not self.responses.empty():
            response_list.append(self.responses.get())
        return sorted(response_list)

    def send_event(self, event, details = '', player_ID = -1, time_lim = -1,
                    num_chars = -1):
        if player_ID == -1:
            self.send_to_all(event, details, time_lim, num_chars)
        else:
            self.send_to_player(player_ID, event, details, time_lim, num_chars)

    def clear_responses(self):
        self.responses.queue.clear() #clears all responses before this
        print("responses have been cleared")

    def send_score_totals(self, score_totals):
        #score_totals is a dictionary with {ID: [games_played, games_won]}
        for player, ID in self.players.items():
            games_played, games_won = [str(num) for num in  score_totals[ID]]
            self.send_event('Your score totals:', details = games_played +
            'games played, ' + games_won + ' games won')
