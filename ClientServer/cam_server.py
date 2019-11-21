from server_module import *

# Please see README for how to add game logic to this program

host = "10.6.26.177"
port = 1000
server = open_server(host, port)

num_players = 3

print("Waiting for players...")
while len(server.players) < num_players: #wait till you have enough players
    pass

server.send_event('Welcome to Cards Against Mennonites!')


# Do stuff to make the game happen
# (See README for what server functions are available)


# just an example of getting responses
server.send_event('What is your favorite letter?', time_lim = 10, num_chars = 1)
responses = server.get_responses()
for player, response in responses:
    print("Player %s chose '%s'" % (player, response))


server.send_event("Thanks for playing!")
server.close()
