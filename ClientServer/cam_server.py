from server_module import *
import random

# Please see README for how to add game logic to this program


## Pregame stuff

## Server stuff
#host = "10.6.28.148" #Dan's Computer
host = "10.6.26.177" #Ben's Computer
port = 1000
server = open_server(host, port)

num_players = 3

print("Waiting for players...")
while len(server.players) < num_players: #wait till you have enough players
    pass

responses = server.get_responses()
for player_ID, username in responses.items():
    server.players[player_ID].username = username
server.send_event('Welcome to Cards Against Mennonites!')
server.send_event('Players', details = ', '.join(
                [player.username for player in server.players.values()]))


# Do stuff to make the game happen

# (See README for what server functions are available)

# just an example of getting responses
server.send_event('What is your favorite letter?', time_lim = 10, num_chars = 1)
responses = server.get_responses()

winner_ID, winner_response = random.choice(responses)
print("Player %d wins with '%s'" % (winner_ID, winner_response))
server.send_event(server.players[winner_ID].username + ' wins!', exclude = winner_ID)
server.send_event('You win!', player_ID = winner_ID)
scores = update_scores(server.players.values(), winner_ID)
server.send_scores(scores)
server.send_event("Thanks for playing!")
server.close()
