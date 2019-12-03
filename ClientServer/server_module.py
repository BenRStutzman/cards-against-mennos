import sys
import time
import threading
from queue import Queue
from PodSixNet.Server import Server
from PodSixNet.Channel import Channel

def update_scores(cur_players, winner_ID):
    f = open('user_list.txt', 'r+')

    # reading
    scores = {username: [int(num) for num in [games_played, games_won]] for username, games_played,
            games_won in [line.split() for line in f.read().splitlines()]}

    # updating
    for player in cur_players:
        games, wins = scores.get(player.username, (0, 0))
        games += 1
        if player.ID == winner_ID:
            wins += 1
        scores[player.username] = games, wins

    # writing
    f.seek(0)
    for username, (games, wins) in scores.items():
        f.write('%s %d %d\n' % (username, games, wins))
    f.close()
    return {player.ID: scores[player.username] for player in cur_players}

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
        self.username = 'anonymous'

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
        #self.send_event("You are player #", details = str(player.ID), player_ID = player.ID)

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
        addition = ' except player ' + str(exclude) if exclude >= 0 else ''
        print("'%s%s' sent to everyone%s" % (event, details, addition))

    def close(self):
        print("Server closed.")
        self.stop()
        sys.exit()

    def get_responses(self, num_needed = -1):
        if num_needed < 0:
            num_needed = len(self.players)
        responses = []
        while self.responses.qsize() < num_needed:
            pass
        while not self.responses.empty():
            responses.append(self.responses.get())
        responses = sorted(responses)
        for player_ID, response in responses:
            print("Player %s responded '%s'" % (player_ID, response))
        return responses

    def send_event(self, event, details = '', player_ID = -1, time_lim = -1,
                    num_chars = -1, exclude = -1):
        if player_ID == -1:
            self.send_to_all(event, details, time_lim, num_chars, exclude)
        else:
            self.send_to_player(player_ID, event, details, time_lim, num_chars)

    def clear_responses(self):
        self.responses.queue.clear() #clears all responses before this
        print("responses have been cleared")

    def send_scores(self, score_totals):
        #score_totals is a dictionary with {player_ID: [games_played, games_won]}
        for player_ID in self.players:
            games_played, games_won = score_totals[player_ID]
            plural1 = 's' if games_played > 1 else ''
            plural2 = 's' if games_won > 1 else ''
            details = str.format('%d game%s played, %d game%s won' %
                            (games_played, plural1, games_won, plural2))
            self.send_event('Your score totals', details = details,
                            player_ID = player_ID)
